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
            print("No Username")
            return ""

    def get_password(self):
        try:
            return self.jsonData["password"]
        except KeyError:
            print("No Password")
            return ""
    
    def get_title(self):
        try:
            return self.jsonData["title"]
        except KeyError:
            title = "Study Day"
            print("No Title, using default of {0}".format(title))
            return title

    def get_description(self):
        try:
            return self.jsonData["description"]
        except KeyError:
            description = "Study Day"
            print("No Description, using default of {0}".format(description))
            return description

    def get_category(self):
        try:
            return self.jsonData["category"]
        except KeyError:
            category = "Assignment preparation & writing"
            print("No Category, using default of {0}".format(category))
            return category
            
    def get_chrome_binary_path(self):
        try:
            return self.jsonData["chromeBrowserBinaryPath"]
        except KeyError:
            path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            print("No Chrome binary path, using default of {0}".format(path))
            return path