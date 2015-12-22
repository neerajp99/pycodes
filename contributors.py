#!/usr/bin/env python

"""
Python script to get the list of all contributors 
in a github repository
"""

import requests
import sys

if len(sys.argv) < 3:
	print "Enter desired username and repo name"
	exit(1)

baseURL = "https://api.github.com/repos/"

# https://api.github.com/repos/fossasia/gci15.fossasia.org/contributors

username = sys.argv[1]
repo = sys.argv[2]

finalURL = baseURL + username + "/" + repo + "/contributors"
req = requests.get(finalURL)

jsonData = req.json()

i = 1
for data in jsonData:
	print i, data["login"]
	i = i + 1