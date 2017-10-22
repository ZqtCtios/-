import pymysql
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

    def init_data(self):
        pass

    def load(self):
        pass

    def alter(self):
        pass

    def make_dir(self):
        pass

    def show_today(self):
        pass

    def show_all(self):
        pass

    def show_homework(self, course=0):
        pass
