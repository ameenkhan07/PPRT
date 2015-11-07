
import json
import fileinput


outfile = open("balti_data.json","w")

#Paste only English tweets in the output file  
for line in fileinput.input("deduped.json"):
    tweet = json.loads(line)
    if tweet["lang"] == 'en':
        json.dump(tweet,outfile)

