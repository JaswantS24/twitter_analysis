#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Hello World program in Python
    
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from matplotlib import pyplot as plt
import numpy as np

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'g7PQBR3Rb3W7TDhgpIXeV9NHx'
        consumer_secret = 'CK9qnyPkUqSae7bhQ7KxlxqZmCEoTwxKOcFOPiSKlBFgHQzwlS'
        access_token = '3252742549-jOKldJhe8WbtSJyyJLQFH7rrQKFnxlmFTFGhgrW'
        access_token_secret = 'nNnjwVArszV3CvPDX5TRNM9oGolemKpnxxSRRCLqS3HVg'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\//\+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    uname = input("Enter Twitter user Name : ")
    print("****************************************************")
    tweets = api.get_tweets(query = uname, count = 200)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neutweets=[tweet for tweet in tweets if tweet['sentiment']=='neutral']
    # picking positive tweets from tweets
    p=format(100*len(ptweets)/len(tweets))
    # picking negative tweets from tweets
    n=format(100*len(ntweets)/len(tweets))
    #picking neutral tweets from tweets
    neu=format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets))
    print("****************************************************")
    #Plotting a piechart
    tweet_label=['positive','negative','neutral']
    tweet_percent=[p,n,neu]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(tweet_percent, labels = tweet_label,autopct='%1.0f%%')
    plt.show()
    print("****************************************************")
    
    # percentage of positive tweets
    print("Positive tweets percentage:",p,"%")

    # percentage of negative tweets
    print("Negative tweets percentage:",n,"%")

    # percentage of neutral tweets
    print("Neutral tweets percentage:",neu,"%")

    # printing few positive tweets
    print("****************************************************")
    print("Positive tweets:")
    print("****************************************************")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing few negative tweets
    print("****************************************************")
    print("Negative tweets:")
    print("****************************************************")
    for tweet in ntweets[:10]:
        print(tweet['text'])

     # printing few neutral tweets
    print("****************************************************")
    print("Neutral tweets:")
    print("****************************************************")
    for tweet in neutweets[:10]:
        print(tweet['text'])    
if __name__ == "__main__":
    # calling main function
    main()


# In[5]:


# Hello World program in Python
    
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from matplotlib import pyplot as plt
import numpy as np

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'g7PQBR3Rb3W7TDhgpIXeV9NHx'
        consumer_secret = 'CK9qnyPkUqSae7bhQ7KxlxqZmCEoTwxKOcFOPiSKlBFgHQzwlS'
        access_token = '3252742549-jOKldJhe8WbtSJyyJLQFH7rrQKFnxlmFTFGhgrW'
        access_token_secret = 'nNnjwVArszV3CvPDX5TRNM9oGolemKpnxxSRRCLqS3HVg'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\//\+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    uname = input("Enter Twitter user Name : ")
    print("****************************************************")
    tweets = api.get_tweets(query = uname, count = 200)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neutweets=[tweet for tweet in tweets if tweet['sentiment']=='neutral']
    # picking positive tweets from tweets
    p=format(100*len(ptweets)/len(tweets))
    # picking negative tweets from tweets
    n=format(100*len(ntweets)/len(tweets))
    #picking neutral tweets from tweets
    neu=format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets))
    print("****************************************************")
    #Plotting a piechart
    tweet_label=['positive','negative','neutral']
    tweet_percent=[p,n,neu]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(tweet_percent, labels = tweet_label,autopct='%1.0f%%')
    plt.show()
    print("****************************************************")
    
    # percentage of positive tweets
    print("Positive tweets percentage:",p,"%")

    # percentage of negative tweets
    print("Negative tweets percentage:",n,"%")

    # percentage of neutral tweets
    print("Neutral tweets percentage:",neu,"%")

    # printing few positive tweets
    print("****************************************************")
    print("Positive tweets:")
    print("****************************************************")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing few negative tweets
    print("****************************************************")
    print("Negative tweets:")
    print("****************************************************")
    for tweet in ntweets[:10]:
        print(tweet['text'])

     # printing few neutral tweets
    print("****************************************************")
    print("Neutral tweets:")
    print("****************************************************")
    for tweet in neutweets[:10]:
        print(tweet['text'])    
if __name__ == "__main__":
    # calling main function
    main()


# In[6]:


# Hello World program in Python
    
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from matplotlib import pyplot as plt
import numpy as np

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'g7PQBR3Rb3W7TDhgpIXeV9NHx'
        consumer_secret = 'CK9qnyPkUqSae7bhQ7KxlxqZmCEoTwxKOcFOPiSKlBFgHQzwlS'
        access_token = '3252742549-jOKldJhe8WbtSJyyJLQFH7rrQKFnxlmFTFGhgrW'
        access_token_secret = 'nNnjwVArszV3CvPDX5TRNM9oGolemKpnxxSRRCLqS3HVg'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\//\+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    uname = input("Enter Twitter user Name : ")
    print("****************************************************")
    tweets = api.get_tweets(query = uname, count = 200)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neutweets=[tweet for tweet in tweets if tweet['sentiment']=='neutral']
    # picking positive tweets from tweets
    p=format(100*len(ptweets)/len(tweets))
    # picking negative tweets from tweets
    n=format(100*len(ntweets)/len(tweets))
    #picking neutral tweets from tweets
    neu=format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets))
    print("****************************************************")
    #Plotting a piechart
    tweet_label=['positive','negative','neutral']
    tweet_percent=[p,n,neu]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(tweet_percent, labels = tweet_label,autopct='%1.0f%%')
    plt.show()
    print("****************************************************")
    
    # percentage of positive tweets
    print("Positive tweets percentage:",p,"%")

    # percentage of negative tweets
    print("Negative tweets percentage:",n,"%")

    # percentage of neutral tweets
    print("Neutral tweets percentage:",neu,"%")

    # printing few positive tweets
    print("****************************************************")
    print("Positive tweets:")
    print("****************************************************")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing few negative tweets
    print("****************************************************")
    print("Negative tweets:")
    print("****************************************************")
    for tweet in ntweets[:10]:
        print(tweet['text'])

     # printing few neutral tweets
    print("****************************************************")
    print("Neutral tweets:")
    print("****************************************************")
    for tweet in neutweets[:10]:
        print(tweet['text'])    
if __name__ == "__main__":
    # calling main function
    main()


# In[7]:


# Hello World program in Python
    
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from matplotlib import pyplot as plt
import numpy as np

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'g7PQBR3Rb3W7TDhgpIXeV9NHx'
        consumer_secret = 'CK9qnyPkUqSae7bhQ7KxlxqZmCEoTwxKOcFOPiSKlBFgHQzwlS'
        access_token = '3252742549-jOKldJhe8WbtSJyyJLQFH7rrQKFnxlmFTFGhgrW'
        access_token_secret = 'nNnjwVArszV3CvPDX5TRNM9oGolemKpnxxSRRCLqS3HVg'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\//\+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    uname = input("Enter Twitter user Name : ")
    print("****************************************************")
    tweets = api.get_tweets(query = uname, count = 200)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neutweets=[tweet for tweet in tweets if tweet['sentiment']=='neutral']
    # picking positive tweets from tweets
    p=format(100*len(ptweets)/len(tweets))
    # picking negative tweets from tweets
    n=format(100*len(ntweets)/len(tweets))
    #picking neutral tweets from tweets
    neu=format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets))
    print("****************************************************")
    #Plotting a piechart
    tweet_label=['positive','negative','neutral']
    tweet_percent=[p,n,neu]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(tweet_percent, labels = tweet_label,autopct='%1.0f%%')
    plt.show()
    print("****************************************************")
    
    # percentage of positive tweets
    print("Positive tweets percentage:",p,"%")

    # percentage of negative tweets
    print("Negative tweets percentage:",n,"%")

    # percentage of neutral tweets
    print("Neutral tweets percentage:",neu,"%")

    # printing few positive tweets
    print("****************************************************")
    print("Positive tweets:")
    print("****************************************************")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing few negative tweets
    print("****************************************************")
    print("Negative tweets:")
    print("****************************************************")
    for tweet in ntweets[:10]:
        print(tweet['text'])

     # printing few neutral tweets
    print("****************************************************")
    print("Neutral tweets:")
    print("****************************************************")
    for tweet in neutweets[:10]:
        print(tweet['text'])    
if __name__ == "__main__":
    # calling main function
    main()


# In[8]:


# Hello World program in Python
    
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from matplotlib import pyplot as plt
import numpy as np

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'g7PQBR3Rb3W7TDhgpIXeV9NHx'
        consumer_secret = 'CK9qnyPkUqSae7bhQ7KxlxqZmCEoTwxKOcFOPiSKlBFgHQzwlS'
        access_token = '3252742549-jOKldJhe8WbtSJyyJLQFH7rrQKFnxlmFTFGhgrW'
        access_token_secret = 'nNnjwVArszV3CvPDX5TRNM9oGolemKpnxxSRRCLqS3HVg'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\//\+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    uname = input("Enter Twitter user Name : ")
    print("****************************************************")
    tweets = api.get_tweets(query = uname, count = 200)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neutweets=[tweet for tweet in tweets if tweet['sentiment']=='neutral']
    # picking positive tweets from tweets
    p=format(100*len(ptweets)/len(tweets))
    # picking negative tweets from tweets
    n=format(100*len(ntweets)/len(tweets))
    #picking neutral tweets from tweets
    neu=format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets))
    print("****************************************************")
    #Plotting a piechart
    tweet_label=['positive','negative','neutral']
    tweet_percent=[p,n,neu]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(tweet_percent, labels = tweet_label,autopct='%1.0f%%')
    plt.show()
    print("****************************************************")
    
    # percentage of positive tweets
    print("Positive tweets percentage:",p,"%")

    # percentage of negative tweets
    print("Negative tweets percentage:",n,"%")

    # percentage of neutral tweets
    print("Neutral tweets percentage:",neu,"%")

    # printing few positive tweets
    print("****************************************************")
    print("Positive tweets:")
    print("****************************************************")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing few negative tweets
    print("****************************************************")
    print("Negative tweets:")
    print("****************************************************")
    for tweet in ntweets[:10]:
        print(tweet['text'])

     # printing few neutral tweets
    print("****************************************************")
    print("Neutral tweets:")
    print("****************************************************")
    for tweet in neutweets[:10]:
        print(tweet['text'])    
if __name__ == "__main__":
    # calling main function
    main()


# In[9]:


# Hello World program in Python
    
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from matplotlib import pyplot as plt
import numpy as np

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'g7PQBR3Rb3W7TDhgpIXeV9NHx'
        consumer_secret = 'CK9qnyPkUqSae7bhQ7KxlxqZmCEoTwxKOcFOPiSKlBFgHQzwlS'
        access_token = '3252742549-jOKldJhe8WbtSJyyJLQFH7rrQKFnxlmFTFGhgrW'
        access_token_secret = 'nNnjwVArszV3CvPDX5TRNM9oGolemKpnxxSRRCLqS3HVg'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\//\+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    uname = input("Enter Twitter user Name : ")
    print("****************************************************")
    tweets = api.get_tweets(query = uname, count = 200)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neutweets=[tweet for tweet in tweets if tweet['sentiment']=='neutral']
    # picking positive tweets from tweets
    p=format(100*len(ptweets)/len(tweets))
    # picking negative tweets from tweets
    n=format(100*len(ntweets)/len(tweets))
    #picking neutral tweets from tweets
    neu=format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets))
    print("****************************************************")
    #Plotting a piechart
    tweet_label=['positive','negative','neutral']
    tweet_percent=[p,n,neu]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(tweet_percent, labels = tweet_label,autopct='%1.0f%%')
    plt.show()
    print("****************************************************")
    
    # percentage of positive tweets
    print("Positive tweets percentage:",p,"%")

    # percentage of negative tweets
    print("Negative tweets percentage:",n,"%")

    # percentage of neutral tweets
    print("Neutral tweets percentage:",neu,"%")

    # printing few positive tweets
    print("****************************************************")
    print("Positive tweets:")
    print("****************************************************")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing few negative tweets
    print("****************************************************")
    print("Negative tweets:")
    print("****************************************************")
    for tweet in ntweets[:10]:
        print(tweet['text'])

     # printing few neutral tweets
    print("****************************************************")
    print("Neutral tweets:")
    print("****************************************************")
    for tweet in neutweets[:10]:
        print(tweet['text'])    
if __name__ == "__main__":
    # calling main function
    main()


# In[10]:


# Hello World program in Python
    
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from matplotlib import pyplot as plt
import numpy as np

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'g7PQBR3Rb3W7TDhgpIXeV9NHx'
        consumer_secret = 'CK9qnyPkUqSae7bhQ7KxlxqZmCEoTwxKOcFOPiSKlBFgHQzwlS'
        access_token = '3252742549-jOKldJhe8WbtSJyyJLQFH7rrQKFnxlmFTFGhgrW'
        access_token_secret = 'nNnjwVArszV3CvPDX5TRNM9oGolemKpnxxSRRCLqS3HVg'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\//\+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    uname = input("Enter Twitter user Name : ")
    print("****************************************************")
    tweets = api.get_tweets(query = uname, count = 200)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neutweets=[tweet for tweet in tweets if tweet['sentiment']=='neutral']
    # picking positive tweets from tweets
    p=format(100*len(ptweets)/len(tweets))
    # picking negative tweets from tweets
    n=format(100*len(ntweets)/len(tweets))
    #picking neutral tweets from tweets
    neu=format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets))
    print("****************************************************")
    #Plotting a piechart
    tweet_label=['positive','negative','neutral']
    tweet_percent=[p,n,neu]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(tweet_percent, labels = tweet_label,autopct='%1.0f%%')
    plt.show()
    print("****************************************************")
    
    # percentage of positive tweets
    print("Positive tweets percentage:",p,"%")

    # percentage of negative tweets
    print("Negative tweets percentage:",n,"%")

    # percentage of neutral tweets
    print("Neutral tweets percentage:",neu,"%")

    # printing few positive tweets
    print("****************************************************")
    print("Positive tweets:")
    print("****************************************************")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing few negative tweets
    print("****************************************************")
    print("Negative tweets:")
    print("****************************************************")
    for tweet in ntweets[:10]:
        print(tweet['text'])

     # printing few neutral tweets
    print("****************************************************")
    print("Neutral tweets:")
    print("****************************************************")
    for tweet in neutweets[:10]:
        print(tweet['text'])    
if __name__ == "__main__":
    # calling main function
    main()


# In[11]:


# Hello World program in Python
    
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from matplotlib import pyplot as plt
import numpy as np

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'g7PQBR3Rb3W7TDhgpIXeV9NHx'
        consumer_secret = 'CK9qnyPkUqSae7bhQ7KxlxqZmCEoTwxKOcFOPiSKlBFgHQzwlS'
        access_token = '3252742549-jOKldJhe8WbtSJyyJLQFH7rrQKFnxlmFTFGhgrW'
        access_token_secret = 'nNnjwVArszV3CvPDX5TRNM9oGolemKpnxxSRRCLqS3HVg'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\//\+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    uname = input("Enter Twitter user Name : ")
    print("****************************************************")
    tweets = api.get_tweets(query = uname, count = 200)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neutweets=[tweet for tweet in tweets if tweet['sentiment']=='neutral']
    # picking positive tweets from tweets
    p=format(100*len(ptweets)/len(tweets))
    # picking negative tweets from tweets
    n=format(100*len(ntweets)/len(tweets))
    #picking neutral tweets from tweets
    neu=format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets))
    print("****************************************************")
    #Plotting a piechart
    tweet_label=['positive','negative','neutral']
    tweet_percent=[p,n,neu]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(tweet_percent, labels = tweet_label,autopct='%1.0f%%')
    plt.show()
    print("****************************************************")
    
    # percentage of positive tweets
    print("Positive tweets percentage:",p,"%")

    # percentage of negative tweets
    print("Negative tweets percentage:",n,"%")

    # percentage of neutral tweets
    print("Neutral tweets percentage:",neu,"%")

    # printing few positive tweets
    print("****************************************************")
    print("Positive tweets:")
    print("****************************************************")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing few negative tweets
    print("****************************************************")
    print("Negative tweets:")
    print("****************************************************")
    for tweet in ntweets[:10]:
        print(tweet['text'])

     # printing few neutral tweets
    print("****************************************************")
    print("Neutral tweets:")
    print("****************************************************")
    for tweet in neutweets[:10]:
        print(tweet['text'])    
if __name__ == "__main__":
    # calling main function
    main()


# In[12]:


# Hello World program in Python
    
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from matplotlib import pyplot as plt
import numpy as np

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'g7PQBR3Rb3W7TDhgpIXeV9NHx'
        consumer_secret = 'CK9qnyPkUqSae7bhQ7KxlxqZmCEoTwxKOcFOPiSKlBFgHQzwlS'
        access_token = '3252742549-jOKldJhe8WbtSJyyJLQFH7rrQKFnxlmFTFGhgrW'
        access_token_secret = 'nNnjwVArszV3CvPDX5TRNM9oGolemKpnxxSRRCLqS3HVg'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\//\+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    uname = input("Enter Twitter user Name : ")
    print("****************************************************")
    tweets = api.get_tweets(query = uname, count = 200)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neutweets=[tweet for tweet in tweets if tweet['sentiment']=='neutral']
    # picking positive tweets from tweets
    p=format(100*len(ptweets)/len(tweets))
    # picking negative tweets from tweets
    n=format(100*len(ntweets)/len(tweets))
    #picking neutral tweets from tweets
    neu=format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets))
    print("****************************************************")
    #Plotting a piechart
    tweet_label=['positive','negative','neutral']
    tweet_percent=[p,n,neu]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(tweet_percent, labels = tweet_label,autopct='%1.0f%%')
    plt.show()
    print("****************************************************")
    
    # percentage of positive tweets
    print("Positive tweets percentage:",p,"%")

    # percentage of negative tweets
    print("Negative tweets percentage:",n,"%")

    # percentage of neutral tweets
    print("Neutral tweets percentage:",neu,"%")

    # printing few positive tweets
    print("****************************************************")
    print("Positive tweets:")
    print("****************************************************")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing few negative tweets
    print("****************************************************")
    print("Negative tweets:")
    print("****************************************************")
    for tweet in ntweets[:10]:
        print(tweet['text'])

     # printing few neutral tweets
    print("****************************************************")
    print("Neutral tweets:")
    print("****************************************************")
    for tweet in neutweets[:10]:
        print(tweet['text'])    
if __name__ == "__main__":
    # calling main function
    main()


# In[14]:


# Hello World program in Python
    
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from matplotlib import pyplot as plt
import numpy as np

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'g7PQBR3Rb3W7TDhgpIXeV9NHx'
        consumer_secret = 'CK9qnyPkUqSae7bhQ7KxlxqZmCEoTwxKOcFOPiSKlBFgHQzwlS'
        access_token = '3252742549-jOKldJhe8WbtSJyyJLQFH7rrQKFnxlmFTFGhgrW'
        access_token_secret = 'nNnjwVArszV3CvPDX5TRNM9oGolemKpnxxSRRCLqS3HVg'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\//\+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    uname = input("Enter Twitter user Name : ")
    print("****************************************************")
    tweets = api.get_tweets(query = uname, count = 200)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neutweets=[tweet for tweet in tweets if tweet['sentiment']=='neutral']
    # picking positive tweets from tweets
    p=format(100*len(ptweets)/len(tweets))
    # picking negative tweets from tweets
    n=format(100*len(ntweets)/len(tweets))
    #picking neutral tweets from tweets
    neu=format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets))
    print("****************************************************")
    #Plotting a piechart
    tweet_label=['positive','negative','neutral']
    tweet_percent=[p,n,neu]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(tweet_percent, labels = tweet_label,autopct='%1.0f%%')
    plt.show()
    print("****************************************************")
    
    # percentage of positive tweets
    print("Positive tweets percentage:",p,"%")

    # percentage of negative tweets
    print("Negative tweets percentage:",n,"%")

    # percentage of neutral tweets
    print("Neutral tweets percentage:",neu,"%")

    # printing few positive tweets
    print("****************************************************")
    print("Positive tweets:")
    print("****************************************************")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing few negative tweets
    print("****************************************************")
    print("Negative tweets:")
    print("****************************************************")
    for tweet in ntweets[:10]:
        print(tweet['text'])

     # printing few neutral tweets
    print("****************************************************")
    print("Neutral tweets:")
    print("****************************************************")
    for tweet in neutweets[:10]:
        print(tweet['text'])    
if __name__ == "__main__":
    # calling main function
    main()


# In[15]:


# Hello World program in Python
    
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from matplotlib import pyplot as plt
import numpy as np

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'g7PQBR3Rb3W7TDhgpIXeV9NHx'
        consumer_secret = 'CK9qnyPkUqSae7bhQ7KxlxqZmCEoTwxKOcFOPiSKlBFgHQzwlS'
        access_token = '3252742549-jOKldJhe8WbtSJyyJLQFH7rrQKFnxlmFTFGhgrW'
        access_token_secret = 'nNnjwVArszV3CvPDX5TRNM9oGolemKpnxxSRRCLqS3HVg'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\//\+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    uname = input("Enter Twitter user Name : ")
    print("****************************************************")
    tweets = api.get_tweets(query = uname, count = 200)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neutweets=[tweet for tweet in tweets if tweet['sentiment']=='neutral']
    # picking positive tweets from tweets
    p=format(100*len(ptweets)/len(tweets))
    # picking negative tweets from tweets
    n=format(100*len(ntweets)/len(tweets))
    #picking neutral tweets from tweets
    neu=format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets))
    print("****************************************************")
    #Plotting a piechart
    tweet_label=['positive','negative','neutral']
    tweet_percent=[p,n,neu]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(tweet_percent, labels = tweet_label,autopct='%1.0f%%')
    plt.show()
    print("****************************************************")
    
    # percentage of positive tweets
    print("Positive tweets percentage:",p,"%")

    # percentage of negative tweets
    print("Negative tweets percentage:",n,"%")

    # percentage of neutral tweets
    print("Neutral tweets percentage:",neu,"%")

    # printing few positive tweets
    print("****************************************************")
    print("Positive tweets:")
    print("****************************************************")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing few negative tweets
    print("****************************************************")
    print("Negative tweets:")
    print("****************************************************")
    for tweet in ntweets[:10]:
        print(tweet['text'])

     # printing few neutral tweets
    print("****************************************************")
    print("Neutral tweets:")
    print("****************************************************")
    for tweet in neutweets[:10]:
        print(tweet['text'])    
if __name__ == "__main__":
    # calling main function
    main()
    


# In[16]:


# Hello World program in Python
    
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from matplotlib import pyplot as plt
import numpy as np

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'g7PQBR3Rb3W7TDhgpIXeV9NHx'
        consumer_secret = 'CK9qnyPkUqSae7bhQ7KxlxqZmCEoTwxKOcFOPiSKlBFgHQzwlS'
        access_token = '3252742549-jOKldJhe8WbtSJyyJLQFH7rrQKFnxlmFTFGhgrW'
        access_token_secret = 'nNnjwVArszV3CvPDX5TRNM9oGolemKpnxxSRRCLqS3HVg'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\//\+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    uname = input("Enter Twitter user Name : ")
    print("****************************************************")
    tweets = api.get_tweets(query = uname, count = 200)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neutweets=[tweet for tweet in tweets if tweet['sentiment']=='neutral']
    # picking positive tweets from tweets
    p=format(100*len(ptweets)/len(tweets))
    # picking negative tweets from tweets
    n=format(100*len(ntweets)/len(tweets))
    #picking neutral tweets from tweets
    neu=format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets))
    print("****************************************************")
    #Plotting a piechart
    tweet_label=['positive','negative','neutral']
    tweet_percent=[p,n,neu]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(tweet_percent, labels = tweet_label,autopct='%1.0f%%')
    plt.show()
    print("****************************************************")
    
    # percentage of positive tweets
    print("Positive tweets percentage:",p,"%")

    # percentage of negative tweets
    print("Negative tweets percentage:",n,"%")

    # percentage of neutral tweets
    print("Neutral tweets percentage:",neu,"%")

    # printing few positive tweets
    print("****************************************************")
    print("Positive tweets:")
    print("****************************************************")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing few negative tweets
    print("****************************************************")
    print("Negative tweets:")
    print("****************************************************")
    for tweet in ntweets[:10]:
        print(tweet['text'])

     # printing few neutral tweets
    print("****************************************************")
    print("Neutral tweets:")
    print("****************************************************")
    for tweet in neutweets[:10]:
        print(tweet['text'])    
if __name__ == "__main__":
    # calling main function
    main()


# In[17]:


# Hello World program in Python
    
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from matplotlib import pyplot as plt
import numpy as np

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'g7PQBR3Rb3W7TDhgpIXeV9NHx'
        consumer_secret = 'CK9qnyPkUqSae7bhQ7KxlxqZmCEoTwxKOcFOPiSKlBFgHQzwlS'
        access_token = '3252742549-jOKldJhe8WbtSJyyJLQFH7rrQKFnxlmFTFGhgrW'
        access_token_secret = 'nNnjwVArszV3CvPDX5TRNM9oGolemKpnxxSRRCLqS3HVg'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\//\+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    uname = input("Enter Twitter user Name : ")
    print("****************************************************")
    tweets = api.get_tweets(query = uname, count = 200)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neutweets=[tweet for tweet in tweets if tweet['sentiment']=='neutral']
    # picking positive tweets from tweets
    p=format(100*len(ptweets)/len(tweets))
    # picking negative tweets from tweets
    n=format(100*len(ntweets)/len(tweets))
    #picking neutral tweets from tweets
    neu=format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets))
    print("****************************************************")
    #Plotting a piechart
    tweet_label=['positive','negative','neutral']
    tweet_percent=[p,n,neu]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(tweet_percent, labels = tweet_label,autopct='%1.0f%%')
    plt.show()
    print("****************************************************")
    
    # percentage of positive tweets
    print("Positive tweets percentage:",p,"%")

    # percentage of negative tweets
    print("Negative tweets percentage:",n,"%")

    # percentage of neutral tweets
    print("Neutral tweets percentage:",neu,"%")

    # printing few positive tweets
    print("****************************************************")
    print("Positive tweets:")
    print("****************************************************")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing few negative tweets
    print("****************************************************")
    print("Negative tweets:")
    print("****************************************************")
    for tweet in ntweets[:10]:
        print(tweet['text'])

     # printing few neutral tweets
    print("****************************************************")
    print("Neutral tweets:")
    print("****************************************************")
    for tweet in neutweets[:10]:
        print(tweet['text'])    
if __name__ == "__main__":
    # calling main function
    main()


# In[ ]:




