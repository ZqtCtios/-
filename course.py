import pymysql
db = pymysql.connect(
    "localhost",
    "root",
    "zqt1997",
    "kebiao",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()

# 课属性：节数，名字，周数，老师，教室，本周作业


class course:
    def __init__(
            self,
            cid=0,
            cname='',
            cfrom=0,
            cto=0,
            weekkind=0,
            teacher='',
            classroom=''
            ):
        self.cname = cname
        self.cfrom = cfrom
        self.cto = cto
        self.weekkind = weekkind
        self.teacher = teacher
        self.classroom = classroom
        self.cid = cid

    def getdata(self):
        self.cname = input('输入课程名称：')
        while True:
            self.cfrom = input('从第几节课开始（数字）：')
            if self.cfrom.isdigit():
                break
            else:
                print('请输入纯数字')

        while True:
            self.cto = input('到第几节课开始（数字）：')
            if self.cfrom.isdigit():
                break
            else:
                print('请输入纯数字')

        while True:
            self.weekkind = input('上课模式（1-单周，2-双周，3-全周）')
            if self.cfrom.isdigit():
                break
            else:
                print('请输入纯数字')

        self.teacher = input('老师姓名：')
        self.classroom = input('教室:')

    def save(self):
        sql = 'insert into course values(%s,%s,%s,%s,%s,%s,%s)'
        data = [
            self.cid,
            self.cname,
            self.cfrom,
            self.cto,
            self.weekkind,
            self.teacher,
            self.classroom]
        cursor.execute(sql, data)
        db.commit()
