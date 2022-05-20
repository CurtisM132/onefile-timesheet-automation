import json


class JSONFormDetails:
    jsonData = None

    def load_json_details(self):
        with open('details.json') as json_file:
            self.jsonData = json.load(json_file)

    def get_username(self):
        try:
            return self.jsonData["username"]
        except KeyError:
            return ""

    def get_password(self):
        try:
            return self.jsonData["password"]
        except KeyError:
            return ""
    
    def get_timesheet_description(self):
        try:
            return self.jsonData["timesheetDescription"]
        except KeyError:
            timesheetDescription = "Study Day"
            print("No Timesheet Description, using default of {0}".format(timesheetDescription))
            return timesheetDescription

    def get_timesheet_category(self):
        try:
            return self.jsonData["timesheetCategory"]
        except KeyError:
            timesheetCategory = "Assignment preparation & writing"
            print("No Timesheet Category, using default of {0}".format(timesheetCategory))
            return timesheetCategory
            
    def get_chrome_binary_path(self):
        try:
            return self.jsonData["chromeBrowserBinaryPath"]
        except KeyError:
            path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            print("Chrome binary path, using default of {0}".format(path))
            return path