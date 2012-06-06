import shelve
import re

'''
Opens the python shelf created by load_tweets.py
and removes the money data from each tweet, verifying
that each tweet is not a RT, contains 'pay $x' in it,
and is not a repeated data point. Amounts over $50 are
ignored, because some tweets contain statements like
'I would pay $100000'. 

RTs are ignored because we want each person's individual
opinion. 
'''


money_re = re.compile('pay \$([^ ]*) ')

def get_average(tweet_dict):
	return sum(tweet_dict.itervalues())/len(tweet_dict)

analysis_dict = {}
shelf = shelve.open('hbotweets.dat')

for tweet in shelf['tweets']:
	# check the tweet is not a RT, and contains 'pay $'
	if 'RT' not in tweet['text'] and 'pay $' in tweet['text']:
		money_text = money_re.findall(tweet['text'])
		# try to extract the money amount, but discard
		# any failures, since some tweets contain 
		# statements like 'I would pay $$$$'
		try:
			# we read the first money amount in the 
			# tweet; there should only be one. 
			money = float(money_text[0])

			# disregard any money amounts > $50
			if money < 50:
				# a dictionary is used to store the tweets
				# with the tweet_id as a key, avoiding any
				# duplicates in the search/loading process
				analysis_dict[tweet['id']] = money 

		except ValueError:
			continue


print 'Data points:'
print len(analysis_dict)
print 'Average:'
print get_average(analysis_dict)
