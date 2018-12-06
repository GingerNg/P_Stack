# ­*­ coding: utf­8 ­*­
"""
@author: ginger
@file: lock_demo.py
@time: 2018/5/10 11:28
@source: http://www.jb51.net/article/51947.htm
"""
#
import logging, time
import pymysql as MySQLdb


class Glock:
    def __init__(self, db):
        self.db = db

    def _execute(self, sql):
        cursor = self.db.cursor()
        try:
            ret = None
            cursor.execute(sql)
            if cursor.rowcount != 1:
                logging.error("Multiple rows returned in mysql lock function.")
                ret = None
            else:
                ret = cursor.fetchone()
            cursor.close()
            return ret
        except Exception as ex:
            logging.error("Execute sql \"%s\" failed! Exception: %s", sql, str(ex))
            cursor.close()
            return None

    def lock(self, lockstr, timeout):
        sql = "SELECT GET_LOCK('%s', %s)" % (lockstr, timeout)
        ret = self._execute(sql)

        if ret[0] == 0:
            logging.debug("Another client has previously locked '%s'.", lockstr)
            return False
        elif ret[0] == 1:
            logging.debug("The lock '%s' was obtained successfully.", lockstr)
            return True
        else:
            logging.error("Error occurred!")
            return None

    def unlock(self, lockstr):
        sql = "SELECT RELEASE_LOCK('%s')" % (lockstr)
        ret = self._execute(sql)
        if ret[0] == 0:
            logging.debug("The lock '%s' the lock is not released(the lock was not established by this thread).",
                          lockstr)
            return False
        elif ret[0] == 1:
            logging.debug("The lock '%s' the lock was released.", lockstr)
            return True
        else:
            logging.error("The lock '%s' did not exist.", lockstr)
            return None


# Init logging
def init_logging():
    sh = logging.StreamHandler()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s -%(module)s:%(filename)s-L%(lineno)d-%(levelname)s: %(message)s')
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    logging.info("Current log level is : %s", logging.getLevelName(logger.getEffectiveLevel()))


def main():
    init_logging()
    db = MySQLdb.connect(host='XXX', user='root', passwd='XXX')
    lock_name = 'queue'

    l = Glock(db)

    ret = l.lock(lock_name, 10)
    if ret != True:
        logging.error("Can't get lock! exit!")
        quit()
    time.sleep(10)
    logging.info("You can do some synchronization work across processes!")
    ##TODO
    ## you can do something in here ##
    time.sleep(10000)
    l.unlock(lock_name)


if __name__ == "__main__":
    main()