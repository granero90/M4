
from conf.config import consumer_secret, consumer_key, secret, token
from lib.streaming import TwitterStreamReader
from lib.utiles import save_json
import tweepy


def main():

    # Realizar la autenticacion en la API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token, secret)
    api = tweepy.API(auth)

    # Crear el streamer
    twitter_stream = TwitterStreamReader(28800)
    reader = tweepy.Stream(api.auth, twitter_stream)

    hastags = ['#Blockchain','#Bitcoin','#Stocks','#Cryptomoneda','#Coinbase', '#Ethereum']
    # Leer los tweets y recuperar la lista
    reader.filter(track=hastags)
    tweets = twitter_stream.get_tweets()

    json_file = 'data/_UEMC_M4.json'
    # Guardarlos en un archivo JSON
    save_json(tweets, json_file)


if __name__ == '__main__':
    main()