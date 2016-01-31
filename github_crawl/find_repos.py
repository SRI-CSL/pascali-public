import sys
import os
import json
import urllib2
import pprint
import base64
import getpass

base_url = "https://api.github.com"
username = "X"
password = "X"

def get_json(request_string):
	request = urllib2.Request(request_string)
	base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
	request.add_header("Authorization", "Basic %s" % base64string)   	
	return json.load(urllib2.urlopen(request))

def main():	
	language = "Java"

	find_repos_url = "https://api.github.com/search/repositories?q=language:{}&sort=stars&order=desc".format(language)
	json = get_json(find_repos_url)
	print json
	for repo in json["items"]:
		name = repo["full_name"]
		stars = repo["stargazers_count"]
		url = repo["html_url"]
		print ("Repo: {}, Stars: {}, URL: {}".format(name, stars, url))

if __name__ == '__main__':
	global username
	global password
	username = raw_input("Github username: ")
	password = getpass.getpass("Github password: ")
	main()