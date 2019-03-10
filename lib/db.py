import pymysql
from config import config


def get_conn():
    conn=pymysql.connect(host=config.db_host,
                         port=config.db_port,
                         user=config.db_user,
                         password=config.db_password,
                         db=config.db,
                         charset='utf8')
    return conn

def db_query(sql):
    config.logging.debug(sql)  #todo 使用logging方法
    conn=get_conn()
    cur=conn.cursor()
    cur.execute(sql)
    r=cur.fetchall()
    config.logging.debug(r)  #todo使用loging方法
    cur.close()
    conn.close()
    return r

def db_change(sql):
    config.logging.debug(sql)  #todo 使用loging方法
    conn=get_conn()
    cur=conn.cursor()
    try:   #如果修改的时候出错了 要回滚回来
        cur.execute(sql)
        conn.commit() #提交修改
    except Exception as e:
        config.logging.error(repr(e))  #打印错误信息 todo logging
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# r=db_query("select * from user where name='liuliu2'")

def check_user(name):
    result=db_query("select * from user where name='%s'" % name)
    if result:
        return True
    else:
        return False

def delete_user(name):
    db_change("delete from user where name= '{}' ".format(name))

if __name__== '__main__':
    print(check_user("liuliu2"))