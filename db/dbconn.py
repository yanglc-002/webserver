#!/usr/bin/env python3
# _*_ coding:utf8 _*_
# __author__ = yanglc


import pymysql




results_list = []


def mysqldb_connect(db_host,db_port,db_user,db_passwd,db_name,db_exeute):

        conn = pymysql.connect(host=db_host,
                               port=db_port,
                               user=db_user,
                               passwd=db_passwd,
                               db=db_name
                               )

        cursor = conn.cursor()
        cursor.execute(db_exeute)
        data = cursor.fetchall()
        # data = cursor.fetchall()
        # data = cursor.fetchone()
        # for i  in data:
        list1=list(data)


        results_list.append(list1)
        conn.commit()
        cursor.close()
        conn.close()
        # results_list.clear()



def mysqldb_operation(db_exeute):
     mysqldb_connect("192.168.190.34",3306,"root","MyNewPass4!","mysitedb",db_exeute)



if __name__ == "__main__":
   mysqldb_operation("SELECT *  from cmdb_user")
   print(results_list[0])
   # dict1 = dict(results_list[0])
   #    # print(dict1)