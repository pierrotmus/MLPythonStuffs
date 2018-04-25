# Pierrot Musumbu Dibwe
# Twitter sentiment analyzer collecting tweets from twenty lines obtained from the API
# and returning the score

import sys
import json

# Make a diction by parsing file and returnin a {word: sentiment}
def sentiment_score(sent_file):
    
    with open(sent_file) as file_content:
        return {line.split('\t')[0]: int(line.split('\t')[1]) for line in file_content}

# Check the score of the tweet in AFINN-11.txt and return it or return 0
def tweet_afinn_score(tweet, scores):
    
    return sum(scores.get(word, 0) for word in tweet.split())

# Evaluate the scores of all the tweets in the file
def all_tweets_score(tweet_file, scores):
    
    with open(tweet_file) as file_content:
        tweets = (json.loads(line).get('text', '') for line in file_content)
        return [tweet_afinn_score(tweet, scores) for tweet in tweets]

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    scores = sentiment_score(sent_file=sent_file)
    sys.stdout.writelines('{0}.0\n'.format(score)
                          for score in all_tweets_score(tweet_file=tweet_file, scores=scores))

if __name__ == '__main__':
    main()
