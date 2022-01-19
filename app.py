# Importing the libraries

import os
from textblob import TextBlob
import nltk
from newspaper import Article
import analyser
import storeResponses

## Getting current file's absolute location

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

## Getting the article

# url = "https://shouvikbajpayee.pythonanywhere.com"
url = input("Enter valid URL: ")
article = Article(url)

## Doing some NLP work

article.download()
article.parse()
# The below line installs "punkt" in your system if "punkt" is not installed in your machine
nltk.download("punkt")
article.nlp()

## Get the summary of the Article

text = article.summary
# print(text)

## Create a TextBlob Object

obj = TextBlob(text)

sentiment = obj.sentiment.polarity  # this returns a value between (-1 , +1)
# print(sentiment)

print(analyser.analyse(sentiment))

## Store the responses in a file

resp = storeResponses.store(APP_ROOT, url, text, sentiment)
print(resp["message"])
