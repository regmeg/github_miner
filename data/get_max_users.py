import json,urllib
import urllib2, base64
import re
#import html2text

#max = not more than 30 000 000

#num_digits = 8

base_url = 'https://api.github.com/users?since='

dig_arr = []

max_digits=0

def send_req(url):
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	json_response=json.loads(response.read())
	return_val = True if len(json_response) > 0 else False
	return return_val


def find_max_digits(max_boundary):
	for i in range (0, max_boundary):
		url = base_url + format(1<<i, 'b')
		print ("finding max digits for " + url)
		exists = send_req(url)
		print ("exists: " + str(exists))
		if exists:
			max_dig = i
		else:
			break
	return max_dig + 1
'''
def get_max(pos, dig_arr):
	print('starting pos' + str(pos) )
	for i in range(10, 0)



for category in categories:
	cat = category.replace(' ', '+').replace('&','%26')
	url = start_url + '&category='+cat
	recurse_links(url)

print("Max user id")
print(len(complete_json['results']))
'''
max_digits = find_max_digits(10)
print("Max digit is: " + str(max_digits))
print("Done")