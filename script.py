import requests
from bs4 import BeautifulSoup

headers = {}
headers['Cookie']='_ga=GA1.2.1131684750.1547509642; intercom-id-c2xdup6c=7b58df99-ecad-4473-9f84-47c2448df697; _fbp=fb.1.1549492863831.458568248; _gid=GA1.2.1349588973.1551285743; wordpress_test_cookie=WP+Cookie+check; wordpress_logged_in_4b3d08e309852ea3c6d29dfbcc1541a1=bpham%7C1551458576%7CTIW6MDkPaFdmbVRCImkamrnaaIa8XHUSG93Vd8fAehQ%7Cc1b19e9551e1aff0c4c73bddc815c03c273d75110d4cbe16e8a3ff78124ad3e1; intercom-session-c2xdup6c=ajM4MmIrK1VBUmxYdUV4VEZnZnJ0OXdEMHZCWEVyWWZVc0xORUtSdzE1REIwa1l4K2JtUnVVaTBMTWhLWWhiVi0telc2dnlqQjF3d2ptZGZrNXhQYzl2UT09--8e2701d30bc6b48453cfd3786ef245cecd25ee2a'
headers['user-agent']='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
url='https://keenanonline.com/guard-retention-stiff-arm-guard-retention/'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
video_url=soup.iframe['src']
video_url=video_url[:video_url.index('?')]
title = soup.title.string

print(r)