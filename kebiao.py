import json

course = {'cname': '',
          'cfrom': '',
          'cto=0': '',
          'weekkind': '',
          'teacher': '',
          'classroom': ''}
course_data = {'num': '', 'courses': {}}
week_data = {}
data = {'week_data': week_data, 'course_data': course_data}


def make_json():
    path = 'course_data.json'
    f = open(path, 'w+')
    js = json.dumps(data, indent=4, separators=(',', ': '))
    f.write(js)
    f.close()


def init(num):
    course_data['num'] = num
    for i in range(course_data['num']):
        course_data['courses'][i + 1] = course.copy()
    make_json()


if __name__ == '__main__':
    init(4)
