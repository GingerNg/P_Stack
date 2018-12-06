# coding=utf-8

'''
http://blog.csdn.net/u010651137/article/details/53322194
https://www.cnblogs.com/520sojustdoit/p/4506916.html
'''

import pyhs2

with pyhs2.connect(host='X.X.X.X',
                   port=10000,
                   authMechanism="PLAIN",
                   user='root',
                   password='************',
                   database='default') as conn:
    with conn.cursor() as cur:
        # Show datastorage
        print (cur.getDatabases())

        # Execute query
        cur.execute("select * from student")

        # Return column info from query
        print (cur.getSchema())

        # Fetch table results
        for i in cur.fetch():
            print (i)