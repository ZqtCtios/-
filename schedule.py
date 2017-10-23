import pymysql
from course import course
db = pymysql.connect(
    "localhost",
    "root",
    "zqt1997",
    "kebiao",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()

weeks = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天']


class schedule:
    data = {'day': '', 'num': '', 'cid': '', 'time': '', 'long': ''}
    day = []
    week = []
    homework = True
    homework_dir = './homeworks'
    num = 0

    def init_data(self):
        while True:
            self.num += 1
            c = self.add_course(self.num)
            if self.save_to_db(c) != True:
                print('添加失败，有冲突课程')
            else:
                yes = str(input('继续添加？y/n'))
                if yes.lower() == 'y':
                    pass
                else:
                    break

    def save_to_db(self, c):
        return True

    def add_course(self, cid):
        c = course(cid)
        c.getdata()
        c.save()
        return c

    def load(self):
        pass

    def alter(self):
        pass

    def set_dir(self):
        pass

    def make_dir(self):
        pass

    def show_today(self):
        pass

    def show_all(self):
        pass

    def show_homework(self, course=0):
        pass
