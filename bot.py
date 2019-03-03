import os
import random
import tweepy
import creds # hidden and ignored by git

  
# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(creds.consumer_key, creds.consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(creds.access_token, creds.access_token_secret) 
api = tweepy.API(auth) 
  



def rline (filename):
	with open(filename) as f:
		lines = f.readlines()
		random_int = random.randint(0,len(lines)-1)
		b = lines[random_int]
		v = b.strip()
		return v
    	
    	
twit = rline ("users.txt")
malware = rline("malware.txt")
C = rline("countries.txt")
noun = rline("nouns.txt")
animal = rline("animals.txt")

msg = "."+twit+" is rumoured to be creating / distributing "+malware+" & working as a proxy of the "+C+" APT group known as "+noun.capitalize()+" "+animal+" "
print (msg)
api.update_status(status=msg)
