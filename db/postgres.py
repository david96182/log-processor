import psycopg2
import uuid


def createPostgresDBConnection(db_user, db_password, db_host, db_port, db_name):
    # Connect as user db_user with password db_password to the db_name database running on this computer.
    print("...trying to connect to postgres db")
    connection = None
    try:
        connection = psycopg2.connect(user=db_user, password=db_password,
                                      host=db_host, port=db_port, database=db_name)
        # Print PostgreSQL Connection properties
        print("...database connection successful... details below")
        print(connection.get_dsn_parameters(), "\n")
    except (Exception, psycopg2.Error) as error:
        print("Error in insert operation", error)
        print("Error in database configuration, check app.properties")

    return connection


def commitOperation(connection):
    if connection:
        connection.commit()


def closeDBConnection(connection):
    if connection:
        connection.close()
        print("PostgreSQL connection is closed")


def getDBCursor(connection):
    if connection:
        return connection.cursor()


def saveLogs(connection, logList, sessionid):
    sql = """INSERT INTO requests (time,req,status,bytes,referer,http_method,sessionid,requestid)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

    for log in logList:
        reqid = uuid.uuid4().hex
        try:
            connection.cursor().execute(sql, (log.getTime(), log.getReq(), log.getStatus(), log.getBytes(),
                                              log.getReferer(), log.getHttpRes(), sessionid, reqid))
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error in insert operation", error)


def existUser(connection, ip, useragent):
    sql_getuser_query = """select userid from users where ip = %s and useragent = %s"""
    user = None
    try:
        cursor = connection.cursor()
        cursor.execute(sql_getuser_query, (ip, useragent))
        user = cursor.fetchone()
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error in select operation", error)

    return user


def saveUser(connection, ip, useragent):
    sql = """INSERT INTO users(userid,ip,useragent) VALUES(%s,%s,%s)"""
    userid = uuid.uuid4().hex

    try:
        cursor = connection.cursor()
        cursor.execute(sql, (userid, ip, useragent))
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        userid = None
        print("Error in insert operation", error)

    return userid


def saveSession(connection, userid, sessionid, session):
    sql = """INSERT INTO sessions (sessionid,userid,totalreq, totalpages, sessionlenght, 
                                    totalbytes, timeperpage, percof2xx, percof3xx, percof4xx, percof5xx,
                                    percofget, percofpost, percofput, percofdelete, percofpatch, percofimgreq,
                                    percofjscssreq, percofofilereq, standev2req, prevhttpm, brospeed, perofempref)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    try:
        connection.cursor().execute(sql, (
            sessionid, userid, session.getTotalReq(), session.getTotalpages(), session.getSessionLenght(),
            session.getTotalBytes(), session.gettimeperpage(), session.getpercof2xx(), session.getpercof3xx(),
            session.getpercof4xx(), session.getpercof5xx(), session.getpercofget(),
            session.getpercofpost(), session.getpercofput(), session.getpercofdelete(),
            session.getpercofpatch(), session.getpercofimgreq(), session.getpercofjscssreq(),
            session.getpercofofilereq(), session.getstandev2req(), session.getprevhttpm(),
            session.getbrospeed(), session.getperofempref()))
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error in insert operation", error)
