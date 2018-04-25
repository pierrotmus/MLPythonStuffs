# Pierrot Musumbu Dibwe
# Tweet terms analyzer collecting words from tweets obtained from the API
# and returning the  word and the score

from __future__ import division
import sys
import json


def scores_extraction(sent_file):
    with open(sent_file) as file_content:
        return {line.split('\t')[0]: int(line.split('\t')[1]) for line in file_content}


def tweet_afinn_score(tweet, scores):
    return sum(scores.get(word, 0) for word in tweet)


def new_word_score(tweet_file, scores):
    with open(tweet_file) as file_content:
        tweets = (json.loads(line).get('text', '').split() for line in file_content)
        return {word: tweet_afinn_score(tweet, scores) / len(tweet)
                for tweet in tweets if tweet
                for word in tweet if word not in scores}

def main():
    
    scores = scores_extraction(sent_file=sys.argv[1])
    sys.stdout.writelines('{0} {1}\n'.format(word.encode('utf-8'), score)
                          for word, score in new_word_score(
                              tweet_file=sys.argv[2],scores=scores).items())

if __name__ == '__main__':
    main()