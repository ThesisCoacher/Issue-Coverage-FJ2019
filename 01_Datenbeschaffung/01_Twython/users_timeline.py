# Zuerst muessen wir Twython importieren.
from twython import Twython
# Authentifizierung mit Twitter. Hier speichern wir die Tokens erst in Variablen ab, die dann uebergeben werden.
APP_KEY = 'xyz'
APP_SECRET = 'xyz'
# Senden der Authentifizierung
twitter = Twython(APP_KEY, APP_SECRET)
# Ueberpruefung, ob wir wirklich authentifiziert wurden
try:
    user_timeline = twitter.get_user_timeline(screen_name='Arne85420832')
except TwythonError as e:
    print (e)
print (user_timeline)
