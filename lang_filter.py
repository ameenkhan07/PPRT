
import json
import fileinput


outfile = open("output","w")

#Paste only English tweets in the output file  
for line in fileinput.input("input"):
    tweet = json.loads(line)
    if tweet["lang"] == 'en':
        json.dump(tweet,outfile)

