import requests
from bs4 import BeautifulSoup
import youtube_dl
import os
import time

DEFAULT_PATH = 'D:/keenan'

class Logger(object):
	def __init__(self, csv, title):
		self.csv = csv
		self.title = title

	def debug(self, msg):
		print(csv + '-' + title + '-----' + msg)

	def warning(self, msg):
		print(csv + '-' + title + '-----' + msg)

	def error(self, msg):
		print(csv + '-' + title + '-----' + msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def create_out_tmpl(title, csv_name, part=None):
	if part == None:
		title = title[:title.rfind('-')-1]
	else:
		title = title[:title.rfind('-')-1] + '-' + part
	hierarchy = get_folder_hierarchy(csv_name)
	path = os.path.join(DEFAULT_PATH, *hierarchy, title + '.%(ext)s')
	return path

def get_folder_hierarchy(csv_name):
	csv_name = csv_name[:csv_name.index('.')]
	hierarchy = csv_name.split('_')
	return hierarchy

headers = {
	'Cookie': '_ga=GA1.2.1131684750.1547509642; intercom-id-c2xdup6c=7b58df99-ecad-4473-9f84-47c2448df697; _fbp=fb.1.1549492863831.458568248; wordpress_test_cookie=WP+Cookie+check; _gid=GA1.2.617485332.1552098858; wordpress_logged_in_4b3d08e309852ea3c6d29dfbcc1541a1=bpham%7C1553308816%7CATu34eUTGGYFkGoQu6EQ2fKWheWT3wcMmAlsVsqpdVz%7Ce1178924467af823143c6542a6e75463d2faf948034e54b99a0ae2c913be8f2c; intercom-session-c2xdup6c=YnpYbkJQNklVby9ERmZtLzNxSTZ4YkpFQU5LVEhmNWpscXppdjV5dnlERThST2dsTk81Uk9IOGZOdlFRTjRsVC0tdUpaNUUwYldUWEVST1k1bFVIYVllQT09--d99cd9111765b2cbb6523b519eb4f5cabc0c3bc2'.
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
	'Referer': 'https://keenanonline.com/'
}

# MAX_RETRIES = 20
# session = requests.Session()
# adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
# session.mount('https://', adapter)
# session.mount('http://', adapter)

proxies = {
    "http": 'http://35.196.186.229:80'
}

directory = os.path.join("D:\\","keenan")
for root,dirs,files in os.walk(directory):
	for file in files:
		if file.endswith(".csv"):
			f = open(file, 'r')
			hierarchy = get_folder_hierarchy(file)
			folder_dir = os.path.join(DEFAULT_PATH, *hierarchy)

			# os.makedirs(folder_dir)

			for url in f:
				print(url)
				r = requests.get(url, headers=headers, proxies=proxies)
				time.sleep(20)
				print(r)
				# time.sleep(5)
			# 	soup = BeautifulSoup(r.text, 'html.parser')
			# 	videos = soup.find_all('iframe')
			# 	part = 1
				# for video in videos:
				# 	video_url=video['src']
				# 	video_url=video_url[:video_url.index('?')]
				# 	title = soup.title.string

				# 	ydl_opts = {
				# 		'logger': Logger(file, title),
				# 		'progress_hooks': [my_hook],
				# 		'outtmpl': create_out_tmpl(title, file, part)
				# 	}
				# 	youtube_dl.utils.std_headers['Referer'] = url
				# 	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				# 		ydl.download([video_url])
				# 	part = part + 1
			f.close()
			# source = os.path.join("D:\\","keenan", file)
			# target = os.path.join("D:\\","keenan", "done", file)
			# os.rename(source, target)

# url='https://keenanonline.com/closed-guard-how-to-do-an-armbar/'
# url='https://keenanonline.com/submissions-other-the-forgotten-choke-the-brabo-choke/'

# r = requests.get(url, headers=headers)
# soup = BeautifulSoup(r.text, 'html.parser')
# video_url=soup.iframe['src']
# video_url=video_url[:video_url.index('?')]
# title = soup.title.string

# print(video_url)
# print(title)

# ydl_opts = {
# 	'logger': Logger(),
#     'progress_hooks': [my_hook],
#     'outtmpl': create_out_tmpl(title, 'openguard_retention.csv')
# }
# youtube_dl.utils.std_headers['Referer'] = url
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([video_url])