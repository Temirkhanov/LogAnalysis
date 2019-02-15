# !/usr/bin/env python
# Author: Ruslan Temirkhanov
# Date: 12/12/2018

import psycopg2

DBNAME = "news"

try:
    def executeQ(query):
        db = psycopg2.connect(dbname=DBNAME)
        cursor = db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        db.close()
        return results

    posts = "select * from TOP_ARTICLES limit 3;"

    authors = "select a.name, SUM(ta.count) as view_count \
            from authors as a \
            inner join articles as ar on a.id = ar.author \
            inner join TOP_ARTICLES as ta on ar.title = ta.title \
            group by a.name order by view_count desc;"

    errors = "select to_char(rc.date, 'Month dd, yyyy') as date, \
                    SUM(100.0*ec.count/rc.count) as proc \
            from (select date(time), count(id) from log group by date) as rc \
            inner join (select date(time), count(id) \
               from log where status = '404 NOT FOUND' group by date) as ec \
                    on rc.date = ec.date \
            group by rc.date having SUM(100.0*ec.count/rc.count) > 1.0;"

    result = executeQ(posts)
    print "Most popular three articles of all time:"
    for item in result:
        print "   \"{}\" - {} views".format(item[0], item[1])
    print "\n"

    result = executeQ(authors)
    print "Most popular article authors of all time:"
    for item in result:
        print "   {} - {} views".format(item[0], item[1])
    print "\n"

    result = executeQ(errors)
    print "Days with more than 1% of requests lead to errors:"
    for item in result:
        print "   {} - {:.1f}% errors".format(item[0], item[1])
except psycopg2.Error as e:
    print e.pgerror
