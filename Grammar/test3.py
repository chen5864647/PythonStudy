import requests
from bs4 import BeautifulSoup

url = "http://www.xbiquge.la/26/26154/"
re = requests.get(url, auth=('user', 'pass'))
re_status = re.status_code
re_enc = re.encoding
re_tex = re.text
# re_jso = re.json()

print()