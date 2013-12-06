import sys
import urllib
import urllib2
from xml.dom import minidom
from config import config

PMS_IP = config['PMS_IP']
PMS_PORT = config['PMS_PORT']

SAB_URL = config['SAB_URL']
SAB_API = config['SAB_API']

PMS_URL = 'http://%s:%s/status/sessions' % (PMS_IP, PMS_PORT)
SAB_URL = 'http://%s/sabnzbd/api?mode=config&name=speedlimit&apikey=%s&value=' % (SAB_URL, SAB_API)



def get_active_streams(url):
	dom = minidom.parse(urllib.urlopen(url))
	total = dom.getElementsByTagName('MediaContainer')
	for i in total:
		return int(i.attributes['size'].value)
		
active = get_active_streams(PMS_URL)

if active < 1:
	speed = config['NONE']
	url = SAB_URL+speed
	req = urllib2.Request(url)
	result = urllib2.urlopen(req)
elif active < 3:
	speed = config['UNDER_THREE']
	url = SAB_URL+speed
	req = urllib2.Request(url)
	result = urllib2.urlopen(req)
elif active < 5:
	speed = config['UNDER_FIVE']
	url = SAB_URL+speed
	req = urllib2.Request(url)
	result = urllib2.urlopen(req)
elif active < 7:
	speed = config['UNDER_SEVEN']
	url = SAB_URL+speed
	req = urllib2.Request(url)
	result = urllib2.urlopen(req)