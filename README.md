## IQOPTION ML TRADER

this app is developed to use machine learning and trade in IOPTION

NN to predict 1 minute Binary Options

this code is based on Lorenzo Argentieri's code from IQ OPTION BOT<br>
I found this code on internet and I'm trying to put it to works<br>

- https://github.com/ModeMan12345/iq_option_BOT <br>

I don't even know how it works but I'm updating the code to put it to work<br>
and To learn machine learning.

IT'S NOT WORKS PROPERLY YET, BECAUSE API IS OUTDATED
I'M WORKING ON IT

PLEASE, NO COMPLAINTS
JUST HELP ME

## NOTE

Do not be selfish use the code and share your improvements with the community

## Summary
- [Contribute with Community](#contribe)
- [What I could do?](#whaticoulddo)
- [PYTHON VERSION 2.7](#pythonversion)
- [How to start](#howtostart)
- [TODO](#todo)
- [Other bots](#otherbots)

<div id='contribe'/>

## Contribute with Community

Do fork<br>
do your changes<br>
do merge request with an explanation to be easy to understand why and what you have changed<br>
Be happy !!!

Please send me suggestions ... feedbacks are welcome

<div id='whaticoulddo'/>

## What I could do?

- update libraries
- create requirements.txt
- How to install
- Now it is open graphic interface

<div id='pythonversion'/>

### PYTHON VERSION 2.7

iqoption current version:
https://github.com/n1nj4z33/iqoptionapi

<div id='howtostart'/>

## How to start

I'm using anaconda with python 2 to reduce time installing things

```
conda create -n myenviqoption
conda activate myenviqoption
pip install -r requirements.txt
pip install --upgrade git+https://github.com/n1nj4z33/iqoptionapi.git@master

```

rename userdata-sample.py to userdata.py

to get the real account id and demo run code below and look to amount of each object

```
python getBalanceId.py
```

update user data in this file than run:

```
python main.py
```

<div id='todo'/>

## TODO

- Update iqoption api to newest version:<br>
  https://github.com/Lu-Yi-Hsun/iqoptionapi<br>
  pip install -U git+git://github.com/Lu-Yi-Hsun/iqoptionapi.git
- add pylint
- update python version to 3
- add editorconfig
- add unit test
- after it start working convert it to webapp with flash and React.js or Vue.js

<div id='otherbots'/>

### Other bots I found

#### Python

- https://github.com/arun-mansa/tradingbot
- https://github.com/zoome0215/predictBO
- https://github.com/AlexCollin/IQOption-Bot-Trade-System
- https://github.com/thinkguru/thinkgurumt2iq

#### c #

- https://github.com/MongkonEiadon/Ai-Option

#### node

- https://github.com/quex46/iqoption
- https://github.com/ongspxm/iqo2
