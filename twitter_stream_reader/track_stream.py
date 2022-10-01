import time
import json
import requests
from requests_oauthlib import OAuth1
import urllib3

from twitter_stream_reader.models import Author, Message


class Stream:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, **kwargs):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.running = False
        self.session = requests.Session()
        # Initialise messages, author and author_message_map
        self.messages = []
        self.authors = []
        self.author_message_map = {}

    def track_keywords(self, keywords):
        auth = OAuth1(self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)
        method = "POST"
        endpoint = "statuses/filter"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        url = f"https://stream.twitter.com/1.1/{endpoint}.json"
        body = {"track": ','.join(map(str, keywords))}
        self._get_tracked_messages_from_stream(method, url, auth, headers, body)

    def _get_tracked_messages_from_stream(self, method, url, auth, headers, body):
        self.running = True
        current_epoch_ts = int(time.time())
        try:
            while self.running:
                try:
                    with self.session.request(
                        method, url, headers=headers, data=body, stream=True, auth=auth,
                        verify=True, timeout=30
                    ) as resp:
                        if resp.status_code == 200:
                            # in production, we would use log here
                            print("Stream connected")
                            for line in resp.iter_lines():
                                if line:
                                    self._handle_line_data(line)
                                else:
                                    print("Problem in getting line data")
                                time_lapsed = int(time.time())-current_epoch_ts
                                print("time lapsed since connection openend :: ", time_lapsed)
                                # we need to collect 100 messages or for 30 seconds whichever happens first
                                if not self.running or len(self.messages) >= 100 or time_lapsed >= 30:
                                    self.running = False
                                    return
                            if resp.raw.closed:
                                print("Stream connection closed by Twitter")
                        else:
                            print(f"Stream encountered HTTP error: {resp.status_code}")
                            if not self.running:
                                break
                            print(f"HTTP error response text: {resp.text}")
                except Exception as ex:
                    print(ex)
        except Exception as ex:
            print(ex)

    def _handle_line_data(self, line):
        tweet_data = json.loads(line)
        if "disconnect" in tweet_data:
            self.is_running = False
            return
        message_id, message_creation_ts, message_text = tweet_data["id_str"], tweet_data["timestamp_ms"], tweet_data["text"]
        user_id, user_name, screen_name = tweet_data["user"]["id_str"], tweet_data["user"]["name"], tweet_data["user"]["screen_name"] 
        user_creation_ts = int(time.mktime(time.strptime(tweet_data["user"]["created_at"], "%a %b %d %H:%M:%S +0000 %Y")))
        author = Author(user_id, user_creation_ts, user_name, screen_name)
        message = Message(message_id, message_creation_ts, message_text, author)
        self.authors.append(author)
        self.messages.append(message)
        if author in self.author_message_map:
            self.author_message_map[author].append(message)
        else:
            self.author_message_map[author] = [message]
