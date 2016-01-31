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

total_java_repos = 0
total_java_repos_with_travis = 0

def get_json(request_string):
	request = urllib2.Request(request_string)
	base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
	request.add_header("Authorization", "Basic %s" % base64string)   	
	return json.load(urllib2.urlopen(request))

def scan_readme(content_url):
	readme_url = content_url.replace("{+path}", "README.md")
	json_data = get_json(readme_url)

	if "message" in json_data and json_data["message"]=="Not Found":
		print ("No README in {}".format(repo_data['name']))
		return
	readme_data = base64.b64decode(json_data['content'])

	print readme_data
	if "https://travis-ci.org" in readme_data:
		print("Has a travis badge")


def has_file(content_url, file_name):
	travis_url = content_url.replace("{+path}", file_name)
	try:
		json_data = get_json(travis_url)

		if "message" in json_data and json_data["message"]=="Not Found":
			return False
	except urllib2.HTTPError:
		return False
	return True


def scan_repo(repo_data):
	global total_java_repos
	global total_java_repos_with_travis
	content_url = repo_data["contents_url"]
	has_travis = has_file(content_url, ".travis.yml")
	total_java_repos += 1
	if has_travis == True:
		total_java_repos_with_travis += 1
	print("{}: {}\t has travis:{}".format(repo_data['name'], repo_data['clone_url'], has_travis))


def scan_repos_of_org(org_name, prog_lang):
	curl_string = "{}/orgs/{}/repos".format(base_url, org_name)
	try:
		json_data = get_json(curl_string)
		if "message" in json_data and json_data["message"]=="Not Found":
			print ("No repos found for {}".format(org_name))
			return 

		print ("  total repos for {}: {}".format(org_name, len(json_data)))
		for repo in json_data:
			if repo["private"] == False and repo["language"] == prog_lang:			
				scan_repo(repo)
	except urllib2.HTTPError as err:
		print(err)
		return 

def read_github_orgs(file_name):
	orgs = list()
	with open(file_name) as f:
		for org in f.readlines():
			orgs.append(org.rstrip())
	return orgs

def main():	
	org_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "org_list.txt")
	print ("Reading orgs from {}".format(org_file))
	interesting_orgs = read_github_orgs(org_file)
	language = "Java"
	for org_name in interesting_orgs:
		scan_repos_of_org(org_name, language)
	print ("Total repos for {}: {}".format(language, total_java_repos))
	print ("Total repos with Travis: {}".format(total_java_repos_with_travis))

if __name__ == '__main__':
	global username
	global password
	username = raw_input("Github username: ")
	password = getpass.getpass("Github password: ")
	main()

