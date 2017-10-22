
# 课表属性：节数分别上课时间，星期提示，上课提示，显示计算
# 控制系统：装载，常规显示提醒，查询，修改，用户化
# 数据库：

# 课程Class
import pymysql

from schedule import schedule
db = pymysql.connect(
    "localhost",
    "root",
    "zqt1997",
    "kebiao",
    use_unicode=True,
    charset="utf8")
cursor = db.cursor()


if __name__ == '__main__':
    s = schedule()
    s.add_course()
