import csv

def write_messages_to_tsv(author_message_map, authors):
    """
    Messages should be grouped by user (users sorted chronologically, ascending).
    The messages per user should also be sorted chronologically, ascending.
    Print this information to a tab-separated file, with a header containing the column names.
    """
    authors.sort(key=lambda author: author.creation_timestamp)
    with open('output.tsv', 'w') as creating_new_csv_file:
        pass
    with open('output.tsv', 'a', newline='') as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        tsv_output.writerow(["AuthorID", "MessageID", "Message Date", "Message Text", "Author Name", "Author Screen Name", "Author Timestamp"])
        for author in authors:
            author_message_map[author].sort(key=lambda message: message.creation_timestamp)
            for message in author_message_map[author]:
                tsv_output.writerow(
                    [
                        author.user_id, message.message_id, message.creation_timestamp, message.message_text, author.user_name, author.screen_name, author.creation_timestamp
                    ]
                )
