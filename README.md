# Whatsapp Chat Analyser


## Table of Content
  * [Demo](#demo)
  * [Problem Statement](#problem-statement)
  * [Approach](#approach)
  * [Technologies Used](#technologies-used)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Bugs & Logs](#bugs--logs)
  * [Contributors](#contributors)

## Demo
Link: [https://whatsapp-chat-analyser01.herokuapp.com/](https://whatsapp-chat-analyser01.herokuapp.com/)

![whatsapp](https://user-images.githubusercontent.com/76767335/171602095-c494946d-4934-4bfd-90bb-bc0587772b17.gif)


## Problem Statement
WhatsApp-Analyzer  is  a  statistical  analysis  tool  for WhatsApp  chats.  Working  on  the  chat  files  that  can  be exported  from  WhatsApp  it  generates  various  plots showing,  for  example,  which  another  participant  a  user responds  to  the  most.  We  propose  to  employ  dataset manipulation techniques to have a better understanding of WhatsApp chat present in our phones. 

## Approach
Data Exploration : Exploring dataset using pandas, numpy.

Feature Engineering : Removed missing values and created new features as per insights.

Text Preprocessing : Apply Text Preprocessing techinques to clean data.

Pickle File : Created pickle file as per need.

Building web app : Building web app using python.

User Interface & deployment :  Created an UI that shows the output.
                          After that I have deployed project on heroku.
## Technologies Used
 
   1. Python 
   2. Pandas
   3. Numpy
   4. Steamlit
   5. WordCloud
   6. Regular Expression(re)

## Installation
Click here to install [python](https://www.python.org/downloads/). To install the required packages and libraries, run this pip command in the project directory after cloning the repository:
```bash
git clone https://github.com/Shankar297/Whatsapp-Chat-Analyser.git
```

```bash
pip install -r requirements.txt
```
If pip is not already installed, Follow this [link](https://pip.pypa.io/en/stable/installation/)

## Deployement on Heroku
Create a virtual app on Heroku website. You can either connect your github profile or download cli to manually deploy this project.
Follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Bugs & Logs

1. If you find a bug, kindly open an issue and it will be addressed as early as possible.
2. Under localhost, logging is performed for all the actions and its stored onto logs.txt file
3. When the app is deployed on heroku, logs can be viewed on  heroku dashboard or CLI.

## Contributors
  [Shankar Wagh](https://github.com/Shankar297)
