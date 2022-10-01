from twitter_stream_reader.auth import get_access_token
from twitter_stream_reader.track_stream import Stream
from twitter_stream_reader.file_writer import write_messages_to_tsv

def main():
    consumer_key = input('Enter your consumer key: ')
    consumer_secret = input('Enter your consumer secret: ')
    keywords = input('Enter space separated keywords to track: ').split(" ")
    access_token, access_token_secret = get_access_token(consumer_key, consumer_secret)
    twitter_stream_tracker = Stream(
        consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )
    twitter_stream_tracker.track_keywords(keywords)
    write_messages_to_tsv(
        twitter_stream_tracker.author_message_map, twitter_stream_tracker.authors
    )


if __name__ == "__main__":
    main()