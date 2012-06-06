import shelve
import re

def get_average(tweet_dict):
	return sum(tweet_dict.itervalues())/len(tweet_dict)

analysis_dict = {}
money_re = re.compile('pay \$([^ ]*) ')

shelf = shelve.open('hbotweets.dat')


for tweet in shelf['tweets']:
	if 'RT' not in tweet['text'] and 'pay $' in tweet['text']:
		money_text = money_re.findall(tweet['text'])
		try:
			money = float(money_text[0])
			if money < 100:
				analysis_dict[tweet['id']] = money 
		except ValueError:
			continue


print 'original points:'
print len(shelf['tweets'])
print 'Data points:'
print len(analysis_dict)
print 'Average:'
print get_average(analysis_dict)
