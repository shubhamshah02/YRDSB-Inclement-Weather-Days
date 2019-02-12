from tweepy import StreamListener
from tweepy import Stream
from dhooks import Webhook, Embed
import tweepy
import json

#Get Twitter Developers API Key
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

webhooks = ['Type Discord Webhook URL']

def is_part(some_string, target):
    return target in some_string
	
print("Discord Webhook Bot is online!")

class StdOutListener(StreamListener):

    def on_data(self, data):
        # process stream data here
        d = json.loads(data)
        try:
            if d['in_reply_to_user_id'] is None:
                a = ['weather', 'environment canada', 'extremely cold temperatures', 'cold temperatures', 'temperature', 'extreme weather conditions', 'inclement weather']
                message = (str(d['text'])).lower()
                
                a_match = [True for match in a if match in message]

                if True in a_match:
                  inclementdetection = True
                else:
                  inclementdetection = False
                  
                if inclementdetection == True:
                    message = str(d['text'])
                    try:
                        if len(d['entities']['media'][0]['type']) > 0:
                            message = message.replace(d['entities']['media'][0]['url'], '')
                    except:
                        pass
                    if (d['text'])[:2] != "RT":
                        embed = Embed(
                            description=":warning: [" + message + "](" + "https://twitter.com/YRDSB/status/" + d['id_str'] + ")",
                            color=0xEB2922,
                            timestamp='now'
                            )

                        embed.set_author(name='York Region DSB @YRDSB', url='https://twitter.com/YRDSB', icon_url="https://pbs.twimg.com/profile_images/1046763671274156033/jDQiSFxV_200x200.jpg")
                        embed.set_footer(text='Made by Spike | Powered by Twitter', icon_url = "https://images-ext-1.discordapp.net/external/bXJWV2Y_F3XSra_kEqIYXAAsI3m1meckfLhYuWzxIfI/https/abs.twimg.com/icons/apple-touch-icon-192x192.png")
                        try:
                            embed.set_image(d['entities']['media'][0]['media_url'])
                        except:
                            pass
                        for x in webhooks:
                            hook = Webhook(x)
							hook.send(embed=embed)
        except:
            pass
         
    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    listener = StdOutListener()
    twitterStream = Stream(auth, listener)
    twitterStream.filter(follow=['593188821'])