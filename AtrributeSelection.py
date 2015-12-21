

import json
import fileinput

unwanted_tweet_stuff = ['contributors','truncated','is_quote_status','source','in_reply_to_screen_name','in_reply_to_user_id'
                        'in_reply_to_user_id_str','in_reply_to_status_id_str']
wanted_user_stuff = ['id','verified','followers_count','protected','statuses_count','description','friends_count','name',
					  'favourites_count','created_at','listed_count','following']

outfile = open("BAL-4.0.json","w")

for line in fileinput.input("BAL-3.0.json"):
    try:
        tweet = json.loads(line)
    except:
        continue
    for key in unwanted_tweet_stuff:
    	tweet.pop(key,None)

    for key in tweet["user"].keys():
    	if key not in wanted_user_stuff:
         tweet["user"].pop(key,None)	
    
    twit = json.dumps(tweet)
    outfile.write(twit + '\n')
