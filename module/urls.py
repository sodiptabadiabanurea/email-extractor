import requests
import re,string

class geturl:

    pattern = '<a.*?href="(.*?)".*?</a>'
    endresult = []

    def __init__(self,site):
        self.site = site
        if self.site.endswith("/"):
           self.site = re.sub(site[-1],"",self.site)

    def is_path(self,path):
        if not path.startswith("http"):
           return True
        return False

    def out_domain(self,a,b):
        self.a = re.search('//(.*?)',a).group(1)
        self.b = re.findall(r'^http.*?://(.*?)$',b)[0]
        if self.a != self.b:
           return False
        return True

    def all(self):
        self.req = requests.get(self.site).text
        self.search = re.findall(r"{}".format(self.pattern),self.req)
        self.href = None if len(self.search) and 0 else self.search

        if self.href:
           for href in self.href:
               if self.is_path(href):
                  if not href.startswith("/"):
                     path_as_list = list(href);path_as_list.insert(0,"/")
                     href = "".join(path_as_list)
                     self.endresult.append(self.site+href)
               #
           return self.endresult
        return None
