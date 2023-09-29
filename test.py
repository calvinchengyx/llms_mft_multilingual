def function_to_remove_tweet_entities(tweet):
    tweet = re.sub(r"@\w+", "", tweet)  # Remove mentions
    tweet = re.sub(r"#\w+", "", tweet)  # Remove hashtags
    tweet = re.sub(r"http\S+", "", tweet)  # Remove links
    tweet = re.sub(r"pic.twitter.com\S+", "", tweet)  # Remove pic.twitter.com links
    return tweet


    