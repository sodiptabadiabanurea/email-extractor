import sys
from module import extract as ext


def handle_protocol(site):
    if not site.startswith("http"):
       return "{}{}".format("https://",site)
    return site

if __name__=="__main__":
   print (ext.banner)
   try:
       find = ext.extract(handle_protocol(sys.argv[1]))
       print (find.emails())
   except IndexError:
       sys.exit("  usage: main.py <site>\n")

