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
