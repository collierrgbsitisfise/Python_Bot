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
import dataVariableFile as datafile
"""End Local import"""
# end import


def send_message(api, user_id, message, **kwargs):
    data_dict = {
        'user_id': user_id,
        'message': message,
    }
    data_dict.update(**kwargs)
    return api.messages.send(**data_dict)
# end

# funtiond send message


def send_a_message(user_id, api, message_text):
    res = send_message(api, user_id=user_id, message=message_text)
    return res
# end

# return json respons format using id


def get_solution(python_list, user_id , api):
    solution = ''
    for user in python_list:
        for link in user:
            if(str(user[link]) == str(user_id)):
                solution = solution + str(user['attachments']) + "\n" + "*************************************" + "\n"
                print(user['attachments'][0]['photo']['src_xbig'])
    return solution
# end

def get_comments_from_post(user_id,post_id,api):
    respons = api.wall.getComments(owner_id = user_id , post_id = post_id , sort = 'asc', count = 100)
    json_fomrmat = json.dumps(respons, sort_keys=True, indent=4)
    list = json.loads(json_fomrmat)
    python_list = list[1:]
    print(python_list)
    print('**********************************')    
#end

# save inf in file(2 - mods)
def save_solution_in_file(FILE_NAME, mod, INFO):
    """mod can be 1) add -> add info  2) add_and_del"""
    if mod == 'add':
        f = open(str(FILE_NAME), 'a')
        f.write(INFO)
        f.close()
    else:
        f = open(str(FILE_NAME), 'w')
        f.write(INFO)
        f.close()
# end

# find text of post using isLiked method by id


def get_solution_text(info, api, user_id):
    text = ''
    for attachments in info:
        time.sleep(0.3)
        print(attachments['id'])
        result = api.likes.isLiked(
            owner_id='-61219960', type='post', user_id=user_id, item_id=str(attachments['id']))
        if result == 1:
            text = attachments[
                'text'] + " [ " + str(time.ctime(attachments['date']))+" ] " + "\n\n"

    return text
# end

# find most repeted words in filr


def find_most_rep_words(FILE_NAME, num_of_words):
    fhand = open(FILE_NAME)
    counts = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    lst = list()
    for key, val in counts.items():
        if len(str(key)) > 3:
            lst.append((val, key))

    lst.sort(reverse=True)
    result = list()
    for val, key in lst[:num_of_words]:
        print(str(key) + " : " + str(val))
        result.append((key, val))
    return result
# end


def get_wall_posts_from_group(user_id, api, person_id):
    try:
        #respons = api.wall.get(owner_id = user_id , count = 100)
        #json_fomrmat = json.dumps(respons, sort_keys=True, indent=4)
        # print(json_fomrmat)
        #list = json.loads(json_fomrmat)
        #info = list[1:]
        # return info
        respons = 'some_string_more_then_10_len'
        off = 0
        while len(respons) > 10:
            respons = api.wall.get(owner_id=user_id, count=100, offset=off)
            json_fomrmat = json.dumps(respons, sort_keys=True, indent=4)
            list = json.loads(json_fomrmat)
            list_with_id = list
            #print(str(list_with_id) + "\n\n")
            info = list[1:]
            off = off + 100
            # solution = get_solution_text(info, api, person_id) #For publics as KP
            print(list[0])
            solution = get_solution_text(info, api , person_id)
            solution = str(solution)
            save_solution_in_file('file.txt', 'add', solution)
        print(off * 100)
        print("******************************")
    except ez:
        print('problems with acces ' + str(ex))
# end


def json_in_list(data):
    json_fomrmat = json.dumps(data, sort_keys=True, indent=4)
    list_format = json.loads(json_fomrmat)
    return list_format[1:]
# end


def get_id_messages(list_data):
    list_of_ids = []
    for ids in list_data:
        list_of_ids.append(ids['uid'])
    return list_of_ids
# end


def get_id_and_text_messages(list_data):
    list_of_ids_text = []
    for ids in list_data:
        list_of_ids_text.append((ids['uid'], ids['body']))
    return list_of_ids_text
# end


def del_messages(list_of_ids, api):
    for i in list_of_ids:
        try:
            api.messages.deleteDialog(uid=str(i))
            print('deleted')
        except:
            print('some problems')
# end


def echo_send_message(list_of_val, api):
    if len(list_of_val) > 0:
        for i in list_of_val:
            message = send_a_message_by_caomnd(str(i[1]), str(i[0]), api)
            print(message)
            send_a_message(
                str(i[0]), api, str(message) + "\n\n" + datafile.SAY_HELLO)
            print(str(i[0]))
            # api.messages.markAsRead(i[0])
    else:
        print('NO New Messages')
# end


def random_video(msg):
    link = urllib.parse.urlencode({"search_query": msg})
    content = urllib.request.urlopen("https://www.youtube.com/results?" + link)
    search_results = re.findall(
        'href=\"\/watch\?v=(.*?)\"', content.read().decode())
    if len(search_results) > 0:
        # Первые 10 результатов
        search_results = search_results[0:9:1]
        choice_f = random.choice(search_results)
        yt_link = "https://www.youtube.com/watch?v="+choice_f
        return yt_link
# end


def random_img(msg):
    ss = requests.Session()
    r = ss.get('https://yandex.ua/images/search?text='+msg)
    p = 'div.class\=\"serp-item.*?url\"\:\"(.*?)\"'
    response = r.text
    w = re.findall(p, response)
    if len(w) > 0:
        # Первые 30 фото
        w = w[0:29:1]
        choice_f = random.choice(w)
        return choice_f
    else:
        return 'NO FHOTO by this word'
# end


def get_boobs(api):
    isphoto = False
    boobs = None
    result = 'Nothink'
    while isphoto == False:
        time.sleep(0.5)
        respons = api.wall.get(
            owner_id=-94842501, offset=random.randint(1, 1985), count=1)
        json_fomrmat = json.dumps(respons, sort_keys=True, indent=4)
        list_f = json.loads(json_fomrmat)
        boobs = list_f[1:]
        if len(boobs) == 0:
            continue
        if 'attachments' in boobs[0]:
            if 'photo' in boobs[0]['attachments'][0]:
                print(boobs[0]['attachments'])
                result = 'photo'+str(boobs[0]['attachments'][0]['photo']['owner_id'])+'_'+str(
                    boobs[0]['attachments'][0]['photo']['pid'])
                isphoto = True
    print(result)
    return result
# end


def send_a_message_by_caomnd(command, ids, api):
    # chek if message begin with !!!
    if command[0:3] == '!!!':
        f = open('important.txt', 'a')
        time = now = datetime.datetime.now()
        link = "vk.com/id" + ids
        f.write(str(command) + "\n" + str(time) + "   " + link)
        f.write("\n\n\n")
        f.close()
        return "Ваше cообщение было cохраненно"
    elif command == datafile.commands[0]:
        respons = datafile.respouns_for_hello[
            random.randint(0, len(datafile.respouns_for_hello) - 1)]
        return respons
    elif command == datafile.commands[1]:
        respons = random.choice(datafile.respons_for_shedule)
    elif command == datafile.commands[2]:
        respons = random.choice(datafile.respons_for_home_work)
    elif command == datafile.commands[3]:
        respons = get_boobs(api)
        api.messages.send(uid=ids, attachment=respons)
        return "boobs(.)(.)"
    elif command == datafile.commands[4]:
        pass
    elif command == datafile.commands[5]:
        search = random.choice(datafile.search_word_photo)
        respons = random_img(search)
        return respons
    elif command == datafile.commands[6]:
        search = random.choice(datafile.search_word_video)
        respons = random_video(search)
        return respons
    else:
        respons = datafile.err_comands[
            random.randint(0, len(datafile.err_comands) - 1)]
        return respons
# end
