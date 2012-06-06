Data Analysis for the #takemymoneyHBO trend on Twitter
=====================================================

I was curious about what the average amount of money 
people would be willing to pay for a standalone
HBOGO streaming service, so I wrote two small Python
scripts that use the Twitter search API to retrieve
the 1500 most recent tweets, store them in a Python
shelf, and then analyse them to determine the average
amount. 

There are limitations to this approach, since there are
certainly more than 1500 tweets with this hashtag. I
made the following decisions about how I handled the data:

*  RTs were ignored, because I'm interested in each person's
   personal opinion.
*  I looked for the phrase 'pay $' in the tweet, and extracted
   the number following the '$'. If there was no number following,
   the tweet was ignored (e.g. some people tweeted statements 
   like 'I would pay $$$'.
*  Money amounts >$50 were ignore, since some people tweeted
   statements like 'I would pay $1000000'. 

Currently the script only returns the average amount and the 
number of data points available of the 1500 downloaded (after
RTs, etc are removed).


Results
=======

Wednesday 5:10AM GMT/UTC +0:00 - *$12.06*, from 1063 data points.

Wednesday 5:24AM GMT/UTC +0:00 - *$12.30*, from 1071 data points. 

Remix This
==========
These (very simple) scripts are released under the CC-BY license,
so download them, run them yourself, and modify them to extract 
more interesting data - e.g. draw graphs. 

