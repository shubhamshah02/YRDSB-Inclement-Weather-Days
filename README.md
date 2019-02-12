# YRDSB Inclement Weather Days

This bot runs a constant stream of the @YRDSB Twitter page using the Twitter API and the Tweepy module and uses Discord Webhooks to post on a server. This project is fully open sourced.

## Getting Started

This bot will need to run 24/7 on a system with Python 3 or higher. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them. 

```You will need to apply for a Twitter Developers API key to get the Consumer Key, Consumer Secret, Access Token and the Access Token Secret. You can do that [here](https://developer.twitter.com/en/apply-for-access).```

```
Tweepy - For accessing Twitter API (pip install tweepy)
JSON - For reading API responses (pip install json)
dhooks - For forwarding content via Embed to Discord (pip install dhooks)
```

### Installing

A step by step series of examples that tell you how to get this bot running on your system.

Open the yrdsbbot.py file and fill the empty variables with your Twitter Developer authentications.

```
![Image of yrdsbbot.py](https://i.imgur.com/TawEUH0.png)
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

