import urllib.request
import urllib.parse
import os
import time
# personal details
url = os.getenv('IFTTT_URL')
# Processing
a = urllib.request.urlopen(url)
print(a.read().decode('utf-8'))
time.sleep(45)
b = urllib.request.urlopen(url)
print(b.read().decode('utf-8'))