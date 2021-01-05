import requests
import re,sys
from .urls import geturl

banner = """
                     (_) |           | |                | |
  ___ _ __ ___   __ _ _| |   _____  _| |_ _ __ __ _  ___| |_ ___  _ _
 / _ \ '_ ` _ \ / _` | | |  / _ \ \/ / __| '__/ _` |/ __| __/ _ \| '__|
 | __/ | | | | | (_| | | |  | __/>  <| |_| | | (_| | (__| || (_) | |
 \___|_| |_| |_|\__,_|_|_|   \___/_/\_\\__|_|  \__,_|\___|\__\___/|_|

  @aksiologikode"""

class extract:
    pattern = "[\w\d._]+@[\w\d._]+"

    def __init__(self,site):
        self.site = site

    def validator(self,y):
        self.list = []
        for email in y:
            if email not in self.list:
               self.list.append(email)
            pass
        return self.list

    def getemail(self,url):
        self.req = requests.get(url).text
        self.result = re.findall(r"{}".format(self.pattern),self.req)
        self.emails = []
        if len(self.result) >= 0:
           for email in self.result:
               self.emails.append(email)
           self.bingo = self.validator(self.emails)
           return self.bingo

    def emails(self):
        self.other_page = geturl(self.site).all()
        self.object = []
        for self.url in self.validator(self.other_page):
            print (f"   [*] {self.url}")
            self.object.append(self.getemail(self.url))
        return self.validator(self.object)
