import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen("https://apod.nasa.gov/apod/ap060719.html")
except urllib.error.URLError:
    print("Deu erro!")
else:
    print("Tudo certo!")
    print(site.read())