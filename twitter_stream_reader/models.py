
class Message:
    """
    Message represents a tweet from Twitter user
    """
    def __init__(self, message_id, creation_timestamp, message_text, message_author):
        self.message_id = message_id
        self.creation_timestamp = creation_timestamp
        self.message_text = message_text
        self.message_author = message_author

class Author:
    """
    Author represents a Twitter user
    """
    def __init__(self, user_id, creation_timestamp, user_name, screen_name):
        self.user_id = user_id
        self.creation_timestamp = creation_timestamp
        self.user_name = user_name
        self.screen_name = screen_name
    
    def __str__(self):
        return f"{self.user_id} : {self.user_name}: {self.screen_name}, {self.creation_timestamp}"