import datetime

from flask import Flask
import pymysql
import traceback

app = Flask(__name__)

def get_db():
    """
    链接数据库
    :return: 连接，游标
    """
    # 配置数据库连接参数
    db_host = 'localhost'
    db_user = 'root'
    db_password = 'iopiopiop'
    db_name = 'GamePlatform'

    # 创建数据库连接
    db = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name, autocommit = True)
    # 创建游标
    cursor = db.cursor()  # 执行完毕返回的结果集默认以元组显示
    return db, cursor


def close_db(db, cursor):
    """
    关闭链接
    :param db:
    :param cursor:
    :return:
    """
    if cursor:
        cursor.close()
    if db:
        db.close()


def query(sql, *args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询到的结果，((),(),)的形式
    """
    db, cursor = get_db()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_db(db, cursor)
    return res


def exec_(sql):
    cursor = None
    db = None
    try:
        db, cursor = get_db()
        cursor.execute(sql)
        db.commit()  # 提交事务 update delete insert操作
    except:
        traceback.print_exc()
    finally:
        close_db(db, cursor)

def commit_():
    db, cursor = get_db()
    db.commit()  # 提交事务 update delete insert操作


def main():
    # classroom = 'A111'
    # sql = "INSERT INTO `CourseTime`.`study` (`study_course_no`, `study_student_no`, `study_teacher_no`, `study_begintime`, `study_endtime`, `study_beginweek`, `study_endweek`, `study_room`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')"%(
    #         '1', '2112190111', '1', '8:10', '9:35', '2023/09/11', '2024/01/01', 'A408')
    # sql = "INSERT INTO `CourseTime`.`study` (`study_course_no`, `study_student_no`, `study_teacher_no`, `study_begintime`, `study_endtime`, `study_beginweek`, `study_endweek`, `study_room`) VALUES ('4','2112190111','4','18:30:00','20:50:00','2023-09-11','2024/1/1','b幢410');"  # mysql查询语句
    # res = exec_(sql)
    sql = "SELECT study_beginweek, study_no FROM CourseTime.study"
    res = query(sql)
    print(res)

if __name__ == '__main__':
    main()

@app.route('/')
def test_db_connection():
    try:
        sql = "SELECT teacher_no FROM teacher"
        res = query(sql)
        for row in res:
            print(row)
        return 'MySQL Database version: {}'.format(res)
    except pymysql.Error as e:
        return 'Error connecting to MySQL: {}'.format(e)

# if __name__ == '__main__':
#     app.run(debug=True)