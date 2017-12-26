from lib.utiles import formato_tweet
import logging
import tweepy
import time


class TwitterStreamReader(tweepy.StreamListener):
    """
    http://tweepy.readthedocs.io/en/v3.5.0
    """

    def __init__(self, limit=60):
        # Activar logging
        logging.basicConfig(level=logging.INFO)

        # Cargar la superclase
        super(TwitterStreamReader, self).__init__()

        # Preparar el contenedor y contador
        self.tweets = []
        self.counter = 0

        # Establecer limite
        self.limit = limit
        self.initial = time.time()

        # Empezar el Streamer
        now = time.strftime('%Y %m %d %H:%M:%S')
        print('Initiating the Streamer at {}'.format(now))

    def on_status(self, status):
        # Mantener la escucha hasta que lleguemos al limite
        if (time.time() - self.initial) < self.limit:

            # Obtener el json
            tweet = status._json

            # Limpiar el tweet
            cleaned_tweet = formato_tweet(tweet)

            # Log into the console the tweet and counter
            logging.info('#{}: {} '.format(self.counter, tweet['text']))

            # Agregar el tweet y actualizar el contador
            self.tweets.append(cleaned_tweet)
            self.counter += 1
        else:
            # Si hemos acabado, devolvemos falso
            num_tweets = len(self.tweets)
            now = time.strftime('%Y %m %d %H:%M:%S')
            print('Job finished at {} . \n'
                  'Tweets captured : {}'.format(now, num_tweets))
            return False

    def on_error(self, status_code):
        print("Error :{}".format(status_code))

    def get_tweets(self):
        # Metodo simple para deolver el contenedor
        return self.tweets