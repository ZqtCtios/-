#!/usr/bin/python

import json
import sys
import getopt
course = {'cname': '',
          'cfrom': '',
          'cto=0': '',
          'weekkind': '',
          'week': '',
          'teacher': '',
          'classroom': ''}
courses = {}
course_data = {'num': '', 'courses': courses}
time = {}
week_data = {'long': '', 'time': time}
data = {'week_data': week_data, 'course_data': course_data}


def init(num):
    show_msg()
    course_data['num'] = num
    for i in range(course_data['num']):
        courses[i + 1] = course.copy()
    for i in range(1, 11):
        time[i] = ''
    path = 'data.json'
    print('数据文件为data.json')
    f = open(path, 'w+')
    js = json.dumps(data, indent=4, separators=(',', ': '))
    f.write(js)
    f.close()


def load_data():
    f = open('data.json', 'r')
    js = f.read()
    data = json.loads(js)
    return data


def show_msg():
    print()


def showhelp():
    print('help')


def init_homework():
    data = load_data()
    c_list=[]
    courses = data['course_data']['courses']
    for i in courses.keys():
        c_list.append(courses[i]['cname'])
    c_list=list(set(c_list))
    for x in c_list:
        
        
        
    print('init_homework')


def show_all():
    print('show_all')


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
    main(sys.argv[1:])
