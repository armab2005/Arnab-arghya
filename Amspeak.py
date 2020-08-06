#A python based project
#============Let us start ========================
from textblob import TextBlob 
text=input('Please submit your feelings here ')
sentiment=TextBlob(text). sentiment.polarity
print (sentiment)
#=========If negative he/she is sad and if positive he /she is Happy=========
