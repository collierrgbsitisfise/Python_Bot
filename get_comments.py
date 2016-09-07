from __future__ import unicode_literals
import pprint
from urllib.parse import parse_qs
import webbrowser
import pickle
from datetime import datetime, timedelta
import vk
import time
import json
import random
import requests
import json
import urllib.request
import urllib.parse
import urllib
import urllib.request
import re
import sys
import os
import platform
import datetime
"""Local import"""
import dataVariableFile
import authorisation as auth
import Functions as func
"""End local import"""

def get_post(api , owner_id):
	respons = 'some_string_more_then_10_len'
	off = 0
	info = []
	list_id = []
	while len(respons) > 10:
		time.sleep(1.5)
		respons = api.wall.get(owner_id=owner_id, count=100, offset=off)
		json_fomrmat = json.dumps(respons, sort_keys=True, indent=4)
		list = json.loads(json_fomrmat)
		info += list[1:]
		off = off + 100
	for user in info:
		list_id.append(user['id'])
	return list_id
#end

def get_comments(api , list_id , owner_id):
	for ids in list_id:
		off = 0
		respons = "opopopopopopopopop"
		coments_from_post = []
		while len(respons) > 5:
			time.sleep(3)
			respons = api.wall.getComments(sort = 'asc' , owner_id = owner_id , post_id = ids)
			json_fomrmat = json.dumps(respons , sort_keys = True , indent = 4)
			list = json.loads(json_fomrmat)
			coments_from_post += list[1:]
			off = off + 100 
		
		for comment in coments_from_post:
			print(comment)
			print("****************************")
			if comment['from_id'] == '116216246':
				text = str(comment['text'])
				func.save_solution_in_file('file.txt', 'add', text)

def main():
	api = auth.authorization_by_link()
	ids_list = get_post(api , dataVariableFile.GROUP_ID)
	respons = api.wall.getComments(sort = 'asc' , owner_id = dataVariableFile.GROUP_ID , post_id = ids_list[456])
	print(respons)
	#get_comments(api , ids_list , dataVariableFile.GROUP_ID) 
if __name__ == '__main__':
	main()