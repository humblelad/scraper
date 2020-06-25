import re
import urllib2

a=1

for i in range(0,310):
    no = "id" #my id. SECRET :)
    zero=str(a)
    o=zero.zfill(3)
    no=no+o
    a=a+1

    request = urllib2.Request("https://example.com?regregno="+str(no)+"&submit1=Submit", headers={"Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "http://thewebsite.com",
    "Connection": "keep-alive" })
    contents = urllib2.urlopen(request).read()

  
    results = re.findall('(thing)',contents)   #enter the the thig to search in thing
    print("test "+no)
    for i in results:
        print i
