import requests
import time

URL = "http://10.0.0.20/body"
clear="http://10.0.0.20/clear"
text='Wubba lubba dub dub'
r = requests.get(url=URL,params={'text':text}, timeout=60)
time.sleep(2)
#reply=requests.get(url=clear)

data = r.text
print(data)
