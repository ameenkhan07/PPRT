#To copy all the English language tweets in a new JSON file

import json
import fileinput


outfile = open("output_file","w")

#Paste only English tweets in the output file  
if __name__ == "__main__":
	for line in fileinput.input("input_file"):
	    tweet = json.loads(line)
	    if tweet["lang"] == 'en':
	        twit = json.dumps(tweet)
	        outfile.write(twit + '\n')

