# Idle Time Monitor
<img width="442" alt="image" src="https://github.com/Humayung/idle-time-monitor/assets/35966084/e7852658-b522-461e-b1f8-1c0be1984544">
## Introduction

The Idle Time Monitor is a simple script designed to help users track their idle time activities on macOS. By monitoring and logging idle time data, users can gain insights into their productivity habits and identify opportunities for improvement.

## Installation

To install the Idle Time Monitor, follow these steps:

1. Clone the repository to your local machine:
```
git clone https://github.com/your-username/idle-time-monitor.git
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

5. Run the script:
```
python idle_time_monitor.py
```


## Usage

Once the script is running, it will automatically monitor your idle time activities. Idle time is defined as a period during which there is no mouse movement or keyboard activity detected. You can view your today's idle time on the menu bar icon on your macOS system, or by opening the `idle-history.json` file.

## Features

- Automatic monitoring and logging of idle time activities
- Daily saving of idle time logs in JSON format
- Display of idle time logs on the macOS menu bar

## Configuration Options

The Idle Time Monitor offers the following configuration options:

- Customizable logging interval
- User-defined output directory for saving log files (TODO)
- Adjustable threshold for identifying idle time periods (TODO)
