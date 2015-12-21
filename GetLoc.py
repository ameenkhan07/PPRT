
import json
import fileinput

from geopy.geocoders import Nominatim
geolocator = Nominatim()


outfile = file("balti2.json","w")



listy = ['Maryland', 'District of Columbia']

def json_dump(file_obj,tweet):
    twit = json.dumps(tweet)
    file_obj.write(twit + '\n')
    

def local_tweets(tweet,file_obj,state_pri,state_sec,country):    
    global U_count
    if country  == "United States of America":
        
        for word in listy:
            if state_pri == word  or state_sec == word:
                print state_sec,state_pri,country
                json_dump(file_obj,tweet)
                U_count = U_count + 1

for line in fileinput.input("baltimore.json"):
    
    T_count = T_count + 1
    tweet = json.loads(line)
    if tweet["coordinates"] is not None:
        
        longitude = str(tweet["coordinates"]["coordinates"][0]) 
        latitude = str(tweet["coordinates"]["coordinates"][1])
        
        location_pair =latitude + " , " + longitude 
        L_count = L_count + 1
        
        try:
            address, (latitude, longitude) = geolocator.reverse(location_pair, language='en')                   
            address = address.split(",")
            
            local_tweets(tweet,outfile,address[-2].lstrip(),address[-3].lstrip(),address[-1].lstrip())
        except:
            pass
    
    elif tweet["user"]["location"]:
        
        L_count = L_count + 1
            
        try:
            address, (latitude, longitude) = geolocator.geocode(tweet["user"]["location"],timeout=None)
            address = address.split(",")
            
            local_tweets(tweet,outfile,address[-2].lstrip(),address[-3].lstrip(),address[-1].lstrip())
        except:
            pass
    else:
        N_count = N_count + 1
        json_dump(outfile,tweet)
        

fileinput.close()
