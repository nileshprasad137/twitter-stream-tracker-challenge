# twitter-stream-tracker-challenge
Track Twitter Stream v1.1 using Pin based OAuth and without any twitter library.

## Task

Write code that will cover the functionality listed below:

- Connect to the
  [Twitter Streaming API V1](https://developer.twitter.com/en/docs/twitter-api/v1).
- Filter messages that track on "bieber".
- Retrieve the incoming messages for 30 seconds or up to 100 messages, whichever comes
  first.
- For each message, we will need the following:
  - The message ID
  - The creation date of the message as epoch value
  - The text of the message
  - The author of the message
- For each author, we will need the following:
  - The user ID
  - The creation date of the user as epoch value
  - The name of the user
  - The screen name of the user
- Your application should return the messages grouped by user (users sorted
  chronologically, ascending).
- The messages per user should also be sorted chronologically, ascending.
- Print this information to a tab-separated file, with a header containing the
  column names.

## Notes

- Please, create your own modules, and **do not use off-the-shelf Twitter libraries**.
  You can, of course, use available or native HTTP/RESTful API modules, as well as
  modules for handling the authentication/OAuth calls. If you are not sure if you can
  use a certain module, please contact us.
- You will need to provide the _Consumer Key_ and _Consumer Secret_ and follow through
  the OAuth process (get temporary token, retrieve access URL, authorise application,
  enter PIN for authenticated token). You can find more information on how-to do that
  [here](https://developer.twitter.com/en/docs/authentication/oauth-1-0a).

## Solution Notes / Learnings:
- First part of the challenge was to understand OAuth1. OAuth1 is complex and I had to spend some time to understand how OAuth1 works and how pin-based OAuth works in twitter authentication (See [this](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/pin-based-oauth))
- Next part of the challenge was to connect to a streaming API. Connecting to twitter stream API is conceptually, downloading an infinitely long file over HTTP. See [this](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/connecting) for understanding how this works. Since, I  was not allowed to use off the shelf libraries, I spent some time understanding these twitter docs. You can make a long HTTP call in Python using `requests` module (use `stream=True`) [see this](https://requests.readthedocs.io/en/latest/user/advanced/#body-content-workflow). You can read [Tweepy](https://www.tweepy.org/) library to understand how this will be performed in best way possible.
- Another and most interesting part of the challenge was to listen to twitter stream for specific amount of time AND only upto certain number of results. Doing a long HTTP Call using requests module is a blocking IO call and so I had to ensure this has to be done in a separate daemon thread which will get killed after 30s max. If there are > 100 results for tracking a keyword, listening to a stream gets shut down gracefully.



