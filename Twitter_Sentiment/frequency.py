# Pierrot Musumbu Dibwe
# Tweet word frequency counter collecting words from tweets obtained from the API
# and returning the  word and the frequency

import sys
import json

twitterData = sys.argv[1] #output.txt

def main():
    
    ''' Create a disctionary of words compute theirs frequencies '''
    collected_tweets = tweet_dict(twitterData)
    list_of_words = []
    words_frequency = {}
    # Identify punctuactions and make a list of punctuations.
    punctuactions = '?:!.,;"!@\''
    punctuations_list = []
    for char in punctuactions:
        
        punctuations_list.append(char)
    
    for index in range(len(collected_tweets)):
        
        if collected_tweets[index].has_key("text"):
            
            words_in_tweet = collected_tweets[index]["text"].split()
            for word in words_in_tweet:
                
                word = word.rstrip(punctuactions)
                list_of_words.append(word)# create list of total terms
                

    for word in list_of_words:
        
	if word in words_frequency:
		words_frequency[word] = words_frequency[word]+1
		
	else:
		words_frequency[word] = 1
		
    total_number = len(words_frequency)

    for word in words_frequency:
        
        words_frequency[word] = "%.4f" %(float(words_frequency[word])/total_number)
        print(word.encode("utf-8") + "  " + words_frequency[word])

def tweet_dict(twitterData):  
    
    twitter_list_dict = []
    twitterfile = open(twitterData)
    
    for line in twitterfile:
        twitter_list_dict.append(json.loads(line))
    return twitter_list_dict

   
if __name__ == '__main__':
    main()