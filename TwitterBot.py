import tweepy
#For the GUI use tkinter, a standard GUI library for Python 
from Tkinter import *

# store your credentials in variables 
consumer_key = 'consumer key'
consumer_secret = 'consumer secrets'
access_token = 'access token'
access_token_secret = 'access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#activating the api of this case, each time the consumer 
# wants to access to the users data from that service 
# provider, the consumer includes the access token with
#  the API request to the service provider
api = tweepy.API(auth)


# In order to verify authentication, you could simply print 
# your username and location to the console
user = api.me()
print(user.name)
print(user.location)


for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

print("Followed everyone that is following " + user.name)

# To initialize tkinter, create a Tk root widget, 
# which is a window with a title bar 

root = Tk()

# For the interface, we will use 7 labels
#  We will also need a submit button so that when clicked,
#  we can call our getData function.

# Creating our first label widget: Search
label1 = Label( root, text="Search")
E1 = Entry(root, bd =5)

#Creating label widget 2 : number of tweets
label2 = Label( root, text="Number of Tweets")
E2 = Entry(root, bd =5)

#Creating label widget 3 : response
label3 = Label( root, text="Response")
E3 = Entry(root, bd =5)

#Creating label widget 4 : reply
label4 = Label( root, text="Reply?")
E4 = Entry(root, bd =5)

#Creating label widget 5 : retweet
label5 = Label( root, text="Retweet?")
E5 = Entry(root, bd =5)

#Creating label widget 6 : favorite
label6 = Label( root, text="Favorite?")
E6 = Entry(root, bd =5)

#Creating label widget 7 : follow
label7 = Label( root, text="Follow?")
E7 = Entry(root, bd =5)

# when submit button is clicked, nothing happens. 
# so We have to collect the data.
# we have to get the text input into the labels

def getE1():
    return E1.get()

def getE2():
    return E2.get()

def getE3():
    return E3.get()


def getE4():
    return E4.get()

def getE5():
    return E5.get()

def getE6():
    return E6.get()

def getE7():
    return E7.get()


# Now we are ready to code the main function. From now on, all code is in this function:

def mainFunction():
    getE1()
    search = getE1()
    
    getE2()
    numberOfTweets = getE2()
    numberOfTweets = int(numberOfTweets)
    
    getE3()
    phrase = getE3()
    
    getE4()
    reply = getE4()
    
    getE5()
    retweet = getE5()
    
    getE6()
    favorite = getE6()

    getE7()
    follow = getE7()

    if reply == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Reply
                print('\nTweet by: @' + tweet.user.screen_name)
                print('ID: @' + str(tweet.user.id))
                tweetId = tweet.user.id
                username = tweet.user.screen_name
                api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
                print ("Replied with " + phrase)
                
            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break


    if retweet == "yes": 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Retweet
                tweet.retweet()
                print('Retweeted the tweet')   

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if favorite == "yes": 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Favorite
                tweet.favorite()
                print('Favorited the tweet')   

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if follow == "yes": 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Follow
                tweet.user.follow()
                print('Followed the user')
                
            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break       
            
# We need a submit button so that when clicked, we can call our main function
submit = Button(root, text ="Submit", command = mainFunction)



# So that the computer knows to keep the GUI on the screen, 
# we need to pack our labels and then loop the root display.
# The pack method tells Tk to fit the size of the window to the given text
label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()
label5.pack()
E5.pack()
label6.pack()
E6.pack()
label7.pack()
E7.pack()
submit.pack(side =BOTTOM)
#creating aloop for this running program 
root.mainloop()
