
"""
Created on Sat Aug 22 13:39:10 2015

@author: beingcooper
"""

from urllib2 import urlopen
import json
import csv
import time

fl = open("Baltimore_tweets.csv","w")
wr = csv.writer(fl)

def is_blank(cont):
    st = cont.find("[")
    en = cont.rfind("]")

    if st + 1 == en :
        return 1
    return 0


def get_json(url):
    html_cont = urlopen(url).read()
    time.sleep(1)

    if is_blank(html_cont):
        return 0

    json_st = html_cont.find("[")
    json_end = html_cont.rfind("]")
    html_cont = html_cont[json_st : json_end +1]
    return json.loads(html_cont)


def get_url(offset,mintime):
    url = ("http://otter.topsy.com/search.js?callback=jQuery18309681285265833139_1440320936553&"
           "q=baltimore+OR+freddie+gray"
           "&type=tweet&offset="+str(offset)+"&perpage=100&mintime="+str(mintime)+"&"
           "maxtime=1430092836&sort_method=-date&call_timestamp=1440320937774"
           "&apikey=09C43A9B270A470B8EB8F2946A9369F3&_=1440320938936")
    return url


if __name__ == "__main__":

    keywords = "baltimore OR freddie gray"
    #start_time = 1428818420    # 12-04-2015 06:00
    end_time = 1430092836      # 26-04-2015 23:59
    start_time = 1429152154

    offset = 00
    offset_list = []

    while offset < 1000:
        offset_list.append(offset)
        offset+=100


    min_time = start_time
    date = start_time

    big_row_len = 0
    big_row=[]

    while(min_time < end_time):

     print min_time,"->",end_time

     for offset in offset_list:
         #print offset
         time.sleep(1)
         url = get_url(offset,min_time)
         data = get_json(url)

         if data == 0:
             break

         for i in range(len(data)):
             id_url = data[i]["url"]
             index = id_url.rfind("/")
             tweet_id = id_url[index + 1:]
             new_date = data[i]["firstpost_date"]

             tweet_id_set=[]
             tweet_id_set.append(tweet_id.encode("utf-8"))
             tweet_id_set.append(new_date)
             #print tweet_id_set
             wr.writerows([tweet_id_set])
             big_row.append(tweet_id_set)
             #print tweet_id_set 
             new_tweet_id_set_len = len(big_row)
     if new_tweet_id_set_len == big_row_len :
         break
     big_row_len = new_tweet_id_set_len

     if new_date == date :
        new_date = new_date + 1
        date = new_date
        min_time = new_date
     else :
        min_time = new_date
        date = new_date