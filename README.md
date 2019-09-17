# <p align="center">Chatbot_Rasa

<p align="center">A Chatbot Based on Rasa_NLU in the platform of telegram using the <a href="https://core.telegram.org/bots/api">Telegram Bot API</a>.

  * [Introduction.](#introduction)
  * [Getting started.](#getting-started)
    * [pyTelegramBotAPI](#pyTelegramBotAPI)
    * [Rasa](#rasa)
      * [Quick Installation](#quick-installation)
      * [Building from Source](#building-from-source)
      * [Dependencies for spaCy](#dependencies-for-spacy)
      * [Rasa_NLU](#rasa_nlu)
  * [Usage](#usage)
  * [Declaration](#declaration)
    * [API Import](#api-import)
    * [Rasa Construction](#rasa-Construction)
  * [Examples for some demos](#examples-for-some-demos)
  * [Reference](#reference)
  * [Epilogue](#epilogue)

## Introduction
  This chatbot was aimed at being a multi-function communication online chatbot, currently the function of weather part is realized.
  You can find the chatbot on telegram directely by searching for "Whisper" on the search bar. <br /> **Remember the chatbot will only operate smartly when this program is running!**

## Getting-started
  To get started, you need to install the packages including but not limited to the following ones:
  
### pyTelegramBotAPI
This API was tested with Python 3.6.7 on my PC.
There are two ways to install the library:

* Installation using pip (a Python package manager)*:

```
$ pip install pyTelegramBotAPI
```
* Installation from source (requires git):

```
$ git clone https://github.com/eternnoir/pyTelegramBotAPI.git
$ cd pyTelegramBotAPI
$ python setup.py install
```
### Rasa
#### Quick Installation
You can install both Rasa and Rasa X using pip (requires Python 3.5.4 or higher).
```
$ pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple
```
#### Building from Source
If you want to use the development version of Rasa, you can get it from GitHub:
```
$ git clone https://github.com/RasaHQ/rasa.git
$ cd rasa
$ pip install -r requirements.txt
$ pip install -e .
```

#### Dependencies for spaCy
You can install it with the following commands:
```
$ pip install rasa[spacy]
$ python -m spacy download en_core_web_md
$ python -m spacy link en_core_web_md en
```

#### Rasa_NLU
If you have some problem with Rasa_NLU, you can install it with the following command:
```
pip install rasa-nlu
```
If the above steps can solve your problem, please go to the official website of <a href="https://rasa.com/docs/rasa/user-guide/installation/#">Rasa</a> for help

## Usage
If you have finished all the configuration of your environment, technically you can just run the bot.py (on the root directory).</br> 
With the program running, you can go to the telegram, using your own account, to chat with this cute chatbot :)</br>
(You'd better talk to the robot after the fitting work is done)
</br>
</br>PS: If you are in some special countries like China, you need to use proxy for both telegram and project. Once the it reports the SSLError, the most likely reason is you are blocked by the GFW.

## Declaration
### API Import
* Currently, the `Open Weather Map API` and `pyTelegramBotAPI` are what I used.</br> 
*`Open Weather Map API` is a really convenient API for getting weather and weather forecasts for multiple cities. You can search the weather in various cities by entering the name of the place, and the results will be returned very quickly.</br> 
*`pyTelegramBotAPI` is a simple, but extensible Python implementation for the Telegram Bot API, which makes webhook unneccesarry since it can receive update each time you send a message

### Rasa Construction
* `rasa-nlu` & `rasa-core` have been constructed both. The version of `rasa-nlu` is 0.15.1, the version of `rasa-core` is 0.14.5.

* The configuration of rasa-core is completed mostly, including stories, domains, actions and so on. However, I didn't use rasa-core for holding conversations and deciding what to do next, for the limited size of our training data. </br> Instead, I write the session management directly in `bot.py` with the assist of pyTelegramBotAPI. 

* `rasa-nlu` & `rasa-core` are integreted under the same directory called `rasa`.

## Examples for some demos
* **Command weather inquiring**</br>
![](https://github.com/cbai066/Chatbot_Rasa/blob/master/img/Command%20weather%20inquiring.png)

* **Current weather data**</br>
![](https://github.com/cbai066/Chatbot_Rasa/blob/master/img/Current%20weather%20data.png)

* **Negative message recognition**</br>
![](https://github.com/cbai066/Chatbot_Rasa/blob/master/img/Negative%20message%20judgement.png)

* **Forecast weather data**</br>
![](https://github.com/cbai066/Chatbot_Rasa/blob/master/img/Forecast%20weather%20data.png)

* **Random reply generation**</br>
![](https://github.com/cbai066/Chatbot_Rasa/blob/master/img/Random%20reply%20generation.png)

## Reference
* A tutorial video on YouTube: <a href="Building a chatbot with Rasa NLU and Rasa Core">Building a chatbot with Rasa NLU and Rasa Core</a> 
* User Guide for <a href="https://github.com/eternnoir/pyTelegramBotAPI#using-web-hooks">pyTelegramBotAPI</a>
* Tutorial on the <a href="https://rasa.com/docs/rasa/user-guide/installation/#">Rasa</a> website
* <a href="https://rapidapi.com/community/api/open-weather-map?endpoint=53aa6043e4b00287471a2b66">Open Weather Map API</a> Documentation
* <a href="https://core.telegram.org/bots/api">Telegram Bot API</a>

## Epilogue
For any issues you can text me or comment below



