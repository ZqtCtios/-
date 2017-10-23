
# 课表属性：节数分别上课时间，星期提示，上课提示，显示计算
# 控制系统：装载，常规显示提醒，查询，修改，用户化
# 数据库：

# 课程Class


import json
course = {'cid': '',
          'cname': '',
          'cfrom': '',
          'cto=0': '',
          'weekkind': '',
          'teacher': '',
          'classroom': ''}
course_data={}

def make_json():
    path='course_data.json'
    f=open(path,'w+')
    js=json.dumps(course_data, sort_keys=True, indent=4, separators=(',', ': '))
    f.write(js)
    f.close()
    
def init(num):
    for i in range(num):
        course_data[i+1]=course.copy()
        
    
if __name__ == '__main__':
    init(10)
    make_json()
