#!/usr/bin/python3

# autopep8 --in-place --aggressive --aggressive .\kebiao.py
import json
import sys
import getopt
import os
from datetime import *
import time
from math import *

course = {'cname': '',
          'cfrom': '',
          'cto=0': '',
          'weekkind': '',
          'week_num': '',
          'week_from': '',
          'week_to': '',
          'teacher': '',
          'classroom': ''}
courses = {}
course_data = {'num': '', 'courses': courses}
time = {}
week_data = {'long': '', 'time': time}
data = {
    'week_data': week_data,
    'course_data': course_data,
    'homeWk_dir': 'homework',
    'date_from': '',
    'week': ''}
week_table = {}
today_table = {}
week_ch = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天']


def init(num):
    show_msg()
    course_data['num'] = num
    for i in range(course_data['num']):
        courses[i + 1] = course.copy()
    for i in range(1, 11):
        time[i] = ''
    path = 'data.json'
    print('数据初始化成功')
    print('数据文件为data.json')
    f = open(path, 'w+')
    js = json.dumps(data, indent=4, separators=(',', ': '))
    f.write(js)
    f.close()


def load_data():
    f = open('data.json', 'r', encoding='utf-8')
    js = f.read()
    data = json.loads(js)
    return data


def show_msg():
    print()


def showhelp():
    print('-------用法-------')
    print()
    print()
    print()
    print()
    print()
    print()


def init_homework():
    data = load_data()
    path = data['homeWk_dir']
    c_list = []
    courses = data['course_data']['courses']
    for i in courses.keys():
        c_list.append(courses[i]['cname'])
    c_list = list(set(c_list))
    if not os.path.isdir(path):
        os.mkdir(path)
    for x in c_list:
        x_path = path + '\\' + x
        os.mkdir(x_path)
        f = open(x_path + '\\作业.txt', 'w+')
        f.close()

    print('初始化作业文件夹')


def show_all():
    print('=======================================================================')
    print("| 时间 | {0[0]} | {0[1]} | {0[2]} | {0[3]} | {0[4]} | {0[5]} | {0[6]} |".format(
        week_ch))


def work(data):
    week_num_s = data['week']
    date_s = datetime.strptime(data['date_from'], '%Y-%m-%d')
    day_of_week = 6 - date_s.weekday()
    date_n = datetime.now() - date_s
    n = date_n.days - day_of_week
    week_now = n // 7 + int(week_num_s) + 1
    week_day = datetime.now().weekday()
    for i in range(1, 11):
        today_table[i] = ''
    for i in range(1, 8):
        week_table[i] = today_table.copy()
    print(week_table)
    c = data['course_data']['courses']
    for x in c.keys():
        course = c[x]
        weekkind = course['weekkind']
        if ((week_now //
             2 == 1) and (weekkind in ['1', '3'])) or ((week_now //
                                                        2 == 0) and (weekkind in ['2', '3'])):
            week_from = course['week_from']
            week_to = course['week_to']
            if week_now > week_to or week_now < week_from:
                continue
            x = int(course['week_num'])
            y = int(course['cfrom'])
            week_table[x][y] = course
            week_table[x][y + 1] = course
        else:
            continue
    print(week_table)


def show_today():
    print('show_today')


def error():
    print('-----没有这样的用法------')
    showhelp()


def show_homework():
    print('show_homework')


def main(argv):

    try:
        opts, args = getopt.getopt(argv, 'hi:s:', ['help', 'init=', 'show='])
    except getopt.GetoptError:
        error()
    if len(opts) > 1:
        error()
    opt = opts[0][0]
    arg = opts[0][1]
    if opt in ('-h', '--help'):
        showhelp()
    elif opt in ('-i', '--init'):
        if arg.isdigit():
            init(int(arg))
        elif arg == 'homework':
            init_homework()
        else:
            error()
    elif opt in ('-s', '--show'):
        if arg.lower() == 'today':
            show_today()
        elif arg.lower() == 'all':
            show_all()
        elif arg.lower() == 'homework':
            show_homework()
        else:
            error()


if __name__ == '__main__':
    # main(sys.argv[1:])
    data = load_data()
    work(data)
