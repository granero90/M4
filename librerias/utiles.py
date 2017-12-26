import json, re, os

def save_json(json_dict, output_file):
    """
    Funcion que exporta el contenido de un bloque json en un archivo
    """
    if not os.path.exists('data'):
        os.makedirs('data')
        
    with open(output_file, 'w') as file:
        json.dump(json_dict, file)


def clean_emojis(tweet):
    """
    La solucion para eliminar los emojis ha sido obtenida a partir de este
    hilo de StackOverFlow : https://stackoverflow.com/a/33417311/3356476
    :param tweet:
    :return:
    """
    # Patron para reconocer y eliminar emojis
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               "]+", flags=re.UNICODE)

    return emoji_pattern.sub(r'', tweet)


def formato_tweet(in_tweet):
    """
    Extraemos info necesario
    """

    # Crear diccionario
    tweet = dict()

    # Obtener informacion del usuario
    tweet['usuario'] = in_tweet['user']['screen_name']
    tweet['localizacion'] = in_tweet['user']['location']
    tweet['seguidores'] = in_tweet['user']['followers_count']

    # Obtener texto del tweet y eliminar emojis
    t_date = in_tweet['created_at']
    tweet['creado'] = t_date
    tweet_text = in_tweet['text']
    clean_tweet = clean_emojis(tweet_text)
    tweet['texto'] = clean_tweet
    tweet['fuentes'] = in_tweet['source']
    tweet['contador_caracteres'] = len(clean_tweet)
    tweet['contador_palabras'] = len(clean_tweet.split())

    # Devolver tweet limpio
    return tweet
