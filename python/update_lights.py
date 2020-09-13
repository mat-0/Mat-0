import urllib.request
import urllib.parse
import os

# personal details
url = os.getenv('IFTTT_URL')

# Processing
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))