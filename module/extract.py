import re
import sys
import requests
import concurrent.futures as cf
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

    #
    def filter(self,email):
        for dn in open("dn.txt","r").readlines():
            dn = dn.split("\n")
            if email in dn:
               return 

    def emails(self):
        self.other_page = geturl(self.site).all()
        self.result_sementara = []
        for self.url in self.validator(self.other_page):
            print (f"  [*] {self.url}")
            self.result_sementara.append(self.getemail(self.url))

        self.object = []
        with cf.ThreadPoolExecutor(max_workers=5) as cft:
             output = [cft.submit(self.filter,email) for email in self.result_sementara[0]]
             for y in output:
                 if y:
                    print (y.result())
                    self.object.append(y.result())

        return self.validator(self.object)
