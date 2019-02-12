# YRDSB Inclement Weather Days

This bot runs a constant stream of the [@YRDSB Twitter](https://twitter.com/YRDSB?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor) page using the Twitter API and the Tweepy module and uses Discord Webhooks to post on a server. This project is fully open sourced.

## Getting Started

This bot will need to run 24/7 on a system with Python 3 or higher. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them. 

You will need to apply for a Twitter Developers API key to get the Consumer Key, Consumer Secret, Access Token and the Access Token Secret. You can do that [here](https://developer.twitter.com/en/apply-for-access).

```
Tweepy - For accessing Twitter API (pip install tweepy)
JSON - For reading API responses (pip install json)
dhooks - For forwarding content via Embed to Discord (pip install dhooks)
```

### Installing

A step by step series of examples that tell you how to get this bot running on your system.

Open the yrdsbbot.py file and fill the empty variables with your Twitter Developer authentications.

![Image of yrdsbbot.py](https://i.imgur.com/TawEUH0.png)

Open Discord and choose a channel where you want these messages to be posted. Click settings and create a new Webhook. Name the webhook, give it a profile picture and copy the URL and add it to the webhooks list on yrdsbbot.py.

![Discord Webhooks](https://support.discordapp.com/hc/article_attachments/360007455811/1_.jpg)

Get the Twitter User ID of the user you want to track. In this case, YRDSB's Twitter ID is 593188821. To find this User ID, click [here](http://gettwitterid.com/)

![Find Twitter User ID](https://i.imgur.com/UfE6R4q.png)

## Deployment

Save all changes and run the bot via a command-line program on your operating system. (For example, py yrdsbbot.py and the bot should print Discord Webhook Bot is online! when its ready)

## Built With

* [Twitter](https://twitter.com/?lang=en) - Popular Social Media Platform
* [Tweepy](http://www.tweepy.org/) - Python module to access the Twitter API
* [dhooks](https://github.com/kyb3r/dhooks) - Used to send embed data to Discord via Webhooks

## Authors

* **Shubham Shah** - *Full development* - [SpikePlayz](https://github.com/SpikePlayz)

## Acknowledgments

* Hat tip to anyone whose code was used. Thx <3
* Inspiration (There's nothing like this available and the YRDSB website needs an upgrade)

