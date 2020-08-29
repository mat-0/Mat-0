# importing the module
import tweepy 

# personal details 
consumer_key = ${{ secrets.TW_ACCESS_SECRET }}
consumer_secret = ${{ secrets.TW_ACCESS_TOKEN }}
access_token = ${{ secrets.TW_CONSUMER_KEY }}
access_token_secret = ${{ secrets.TW_CONSUMER_SECRET }}

# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 

api = tweepy.API(auth) 

# update the status 
api.update_status(status ="Up The Chels!") 
