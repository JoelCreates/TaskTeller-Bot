# Overview
TaskTeller Bot is a versatile Discord bot designed to assist students and groups in managing their homework and event schedules efficiently. Harnessing the power of Python and the apscheduler.schedulers.asyncio library, this bot serves as an interactive reminder system, ensuring that no assignment or important date is missed.

# Key Features
- **Homework Reminder**: Users can set reminders for homework or tasks. The bot uses scheduled jobs to notify users at predetermined times, ensuring efficient time management.
- **Cron-Style Scheduling**: Utilises CronTrigger from the apscheduler.schedulers.asyncio library, enabling precise scheduling. For example, CronTrigger(day_of_week="mon", hour="10", minute="00") schedules a reminder every Monday at 10:00 AM.
- **Flexible Task Configuration**: The bot allows adding "jobs" with customisable arguments. Users can select specific functions to execute at set times, catering to diverse scheduling needs.
- **Music Integration**: Apart from reminders, the bot enhances the user experience by interfacing with music playback features, adding an element of leisure to the functional environment.

# Technologies
- **Python**: The core language used for developing the bot, known for its readability and versatility.
- **APScheduler**: An advanced Python library that enables scheduling jobs in a cron-like fashion, integral to the bot's reminder system.
- **Discord API**: Utilizes Discord's robust API for seamless integration and interaction within Discord servers.

# Instructions
The TaskTeller Bot uses the scheduler.add_job function from the apscheduler.schedulers.asyncio library for scheduling tasks. This function is integral to setting up reminders and executing specific functions at predetermined times. Below is a detailed breakdown of how to use this function effectively in the TaskTeller Bot.

## scheduler.add_job Function
- **Purpose**: This method schedules a new job in APScheduler, specifying which task (function) to execute and when to execute it.

## Configuration Arguments
1. First Argument - hwreminder:

- Role: The function to be executed when the job runs.
- Context: In this case, hwreminder is a placeholder function in the bot's code. This is responsible for executing the user reminder actions, like sending a reminder message on Discord. This can be changed to whatever function the user requires.

2. Second Argument - CronTrigger(...):
- Function: It sets the specific timing for the execution of the hwreminder function.
- Format: Similar to Unix/Linux cron jobs, allowing highly flexible scheduling.

## CronTrigger Settings
- day_of_week="DAY": Designates the day of the week for the job to run. Replace "DAY" with the desired day (e.g., "mon", "tue"). Use "*" for every day.
- hour="10": Sets the hour (in 24-hour format) for the job. 10 signifies the job will run at 10:00 AM.
- minute="00": Determines the minute of the hour for the job's execution. 00 indicates the start of the hour.
- second="00": Specifies the exact second within the minute for the job to trigger. 00 means the trigger occurs right as the minute begins.

## Example
When configured as follows:
```
scheduler.add_job(hwreminder, CronTrigger(day_of_week="mon", hour="10", minute="00", second="00"))
```
This setting ensures that the hwreminder function is executed every Monday at 10:00 AM precisely.

# Future Enhancements
- Setting up schedule through command: Plans to implement a schedule command, thus making it easier for the user to instead command the bot to make a reminder rather than making new functions on Python.

# Contribution
Interested in contributing? Great! Feel free to fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.
