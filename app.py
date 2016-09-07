#_*_ coding : utf-8 _*_
#!/usr/bin/env python

# import necessary libraryes for work
from __future__ import unicode_literals
import pprint
from urllib.parse import parse_qs
import webbrowser
import pickle
from datetime import datetime, timedelta
import vk
import time
import json
"""Local import"""
import authorisation as auth
import Functions as func
import dataVariableFile
import random
"""End of local import"""

# end import


def main():
    api = auth.authorization_by_link()
    """
    func.get_wall_posts_from_group(dataVariableFile.GROUP_ID, api , dataVariableFile.ID_PERSON)
    func.find_most_rep_words('file.txt' , 20) """
    while True:
        try:
            #func.send_a_message(['163863990'], api, qust)
            respons = api.messages.get(filters=1)
            time.sleep(10)
            list_format = func.json_in_list(respons)
            list_for_send = func.get_id_and_text_messages(list_format)
            func.echo_send_message(list_for_send, api)
        except vk.exceptions.VkAPIError:
        	print('ERROR')
    """
    Delete ALL Messages
    ids = func.get_id_messages(list_format)
    for i in range(1,10):
    	func.del_messages(ids , api)
    """
# end

if __name__ == '__main__':
    main()
