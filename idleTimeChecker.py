import os
import json
from datetime import datetime

import rumps
from datetime import datetime

def check_idle():
    idle_time = get_idle_duration()
    # clear_terminal()
    total_idle = save_idle_time(idle_time)
    print_idle_information(total_idle, get_current_date())


def print_idle_information(total_idle, date):
    formatted = format_seconds(total_idle)
    print(f"Idle duration at {date}: {formatted}")


def save_idle_time(idle_time):
    formatted_date = get_current_date()
    histories = load_history()
    if formatted_date in histories:
        idle_history = histories[formatted_date]
        if "total_idle" not in idle_history:
            idle_history["total_idle"] = 0
        if "last_idle" not in idle_history:
            idle_history["last_idle"] = idle_time
        if idle_history["last_idle"] > idle_time:
            idle_history["total_idle"] += idle_history["last_idle"]
            idle_history["last_idle"] = 0
        else:
            idle_history["last_idle"] = idle_time
        histories[formatted_date] = idle_history
    else:
        histories[formatted_date] = {"last_idle": idle_time, "total_idle": idle_time}
    save_history(histories)
    idle_history = histories[formatted_date]
    total_idle = idle_history["last_idle"] + idle_history["total_idle"]
    return total_idle


def get_current_date():
    current_time = datetime.now()
    return current_time.strftime("%Y/%m/%d")


def get_idle_duration():
    cmd = "ioreg -c IOHIDSystem | perl -ane 'if (/Idle/) {$idle=(pop @F)/1000000000; print $idle}'"
    result = os.popen(cmd)
    str = result.read()
    return int(str.split(".")[0])


def format_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    formatted_time = ""
    if hours > 0:
        formatted_time += f"{hours}h "
    if minutes > 0:
        formatted_time += f"{minutes}m "
    formatted_time += f"{seconds}s"

    return formatted_time


def save_history(data):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    logfile_path = os.path.join(script_dir, "idle-history.json")
    with open(logfile_path, "w") as json_file:
        json.dump(data, json_file)


def load_history():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    logfile_path = os.path.join(script_dir, "idle-history.json")
    try:
        with open(logfile_path, "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}


def get_total_idle():
    histories = load_history()
    current_date = get_current_date()
    if current_date in histories:
        idle_history = histories[current_date]
        return idle_history["total_idle"] + idle_history["last_idle"]
    else:
        return 0


def clear_terminal():
    print("\033c", end="")


class IdleTimeChecker(rumps.App):
    def __init__(self):
        super(IdleTimeChecker, self).__init__("Idle time")

    def update_menubar(self):
        self.title = "Today's idle: " + format_seconds(get_total_idle())

    @rumps.timer(10) # checks idletime every 10 seconds
    def check_idle_time(self, _):
        now = datetime.now()
        # Check if the current time is between 8 am and 5 pm
        if 8 <= now.hour < 17:
            check_idle()
            self.update_menubar()
        else:
            self.title = "Total todays idle: " + format_seconds(get_total_idle())


if __name__ == "__main__":
    IdleTimeChecker().run()
