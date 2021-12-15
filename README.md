## OneFile Timesheet Automation Script

Automates a OneFile Timesheet, by default, on today's date

Python script that utilises Selenium with a Chrome webdriver

### Prerequisites
* Chrome (version 96.0.xx.xx) installed in the default location
  - Note: You can download a different Chrome webdriver (https://chromedriver.chromium.org/downloads) that corresponds to your Chrome version

### Usage
Open the detail.json file and complete the entries with your data

Note: The _timesheetDescription_ and _timesheetCategory_ keys are optional


**Create timesheet (date set to today)** - _python OneFileTimesheetAutomation.py_

**Create timesheet (parse in DD/MM/YYYY date)** - _python OneFileTimesheetAutomation.py 15/12/2021_
