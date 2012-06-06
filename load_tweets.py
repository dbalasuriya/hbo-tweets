import json
import shelve
import requests

'''
Loads the most recent 1500 tweets matching the search result
#takemymoneyHBO and stores them in a python shelf.
'''

shelf = shelve.open('hbotweets.dat')

shelf['tweets'] = []

for page in xrange(1,16):
	query_params = {'q':'#takemymoneyHBO','result_type':'recent','rpp':'100','page':page}
	r = requests.get('http://search.twitter.com/search.json',params=query_params)

	tweets = json.loads(r.text)['results']

	shelf['tweets'] += tweets

shelf.sync()

