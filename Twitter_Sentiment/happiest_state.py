# Pierrot Musumbu Dibwe
# Happinesst analyzer collecting tweets from twenty lines obtained from the API
# and returning the name and the score of the state with the highest score

from __future__ import division
import sys
import json

list_of_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    # Construct a dict of  words sentiments
    scores = {}
    for input_line in sent_file:
        term, score = input_line.split("\t") 
        scores[term] = int(score)

    # Collect words from tweets
    collected_tweets = []
    for input_line in tweet_file:
        tweets = json.loads(input_line)

        # Select valid words
        if 'word' in tweets.keys() and 'place' in tweets.keys() and tweets['place'] != None:
            term = tweets['word'].replace("\n", "").encode('utf-8').strip()
            country = tweets['place']['country_code']
            state = tweets['place']['full_name'].encode('utf-8').strip()[-2::1]

            # Select only tweets from USA
            if country == 'US' and state in list_of_states:
                collected_tweets.append((term, state))
    
    ''' Compute the sentiment of each tweet according to the AFINN dictionary 
        localize the place where the tweet originated classify the tweets by 
        state of origine and compute the total sentiment by state and select 
        the sate with the higest positive tweet score as the happiest state'''
    
    state_sentiment = {code:[0, 1] for code in list_of_states} # 1st is sum, 2nd is count
    for (tweet, state) in collected_tweets:
        sentiment = 0.0
        for word in tweet.split():
            if word in scores:
                sentiment += scores[word]
        state_sentiment[state][0] += sentiment
        state_sentiment[state][1] += 1
        
    state_score = {code:state_sentiment[code][0] / state_sentiment[code][1] for code in list_of_states}
    print(sorted(state_score, key = state_score.get)[-1])
        

if __name__ == '__main__':
    main()