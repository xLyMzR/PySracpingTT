import pandas as pd
import snscrape.modules.twitter as sntwitter
import xlwt


tweets_list1 = []
tweet_list2 = []
maxDia = 30
flag = True
dia = 1

for i, tweet in enumerate(sntwitter.TwitterSearchScraper('politíca near:"São Paulo" since:2022-08-01').get_items()):
    if i > 200:
        break
    tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    tweet_list2.append([tweet.content])

df = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Tweet', 'Username'])
df.to_csv('result_politica.csv', index=None, sep=',')
#df.to_excel('resuult_politica.xls')


class Texto:

    def __init__(self, text, tipo):
        self.tipo = tipo
        self.text = text


for tweet in tweet_list2:

    primeiro = Texto(tweet, 0)
    print(f"{primeiro.tipo} \n texto {primeiro.text} \n")
