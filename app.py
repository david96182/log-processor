# # nginx.conf
# http {
#   ...
#   log_format combined '$remote_addr - $remote_user [$time_local] '
#                       '"$request" $status $body_bytes_sent '
#                       '"$http_referer" "$http_user_agent"';
#   ...
# }
#  EXAMPLE LOG LINE:
#  127.0.0.1 - - [18/Oct/2021:13:26:42 -0400] "GET / HTTP/1.1" 304 0 "-"
# "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
#
#  MODEL:
#  IP ; ( - ) ; remote_user ; time_local ; request ; status(HTTP response code) ; body_bytes_sent ; http_referer ; user agent
#
#
from util.util import getAppProperties
from db.postgres import createPostgresDBConnection

from logproc.logproc import proccessLogsperSession
from db.postgres import existUser, saveUser
from model.LogLine import LogLine
import re
import datetime
from progressbar import *

def main():
    # Session timeout
    sessionTimeout = datetime.timedelta(minutes=30)
    ipDict = {}

    props = getAppProperties("app.properties", "=")

    db_user = props.get("db_user")
    db_password = props.get("db_password")
    db_host = props.get("db_host")
    db_name = props.get("db_name")
    db_port = props.get("db_port")
    log_location = props.get("log_location")

    regex = props.get("regex")
    conn = createPostgresDBConnection(db_user, db_password, db_host, db_port, db_name)

    if conn is not None:
        logs = None
        try:
            logs = open(log_location, mode='r')
        except:
            print("Error reading logs")
            print("Error in log patch configuration, check app.properties")

        if logs is not None:
            fileRowCount = 0
            for line in logs:
                # evaluate if the line has a match with the regex and save it
                fileRowCount = fileRowCount + 1
                result = re.search(regex, line)

                # if a line doesnt match with the regex ignore it and print the line
                if result is None:
                    print("No match found for row {}".format(fileRowCount))
                    print(line)
                    continue

                # create a time with datetime from a String from log line
                timestr = result.group(3).split()
                time = datetime.datetime.strptime(timestr[0], "%d/%b/%Y:%H:%M:%S")

                # create a logline object
                logLine = LogLine(result.group(1), time, result.group(5), result.group(7), result.group(8),
                                  result.group(9), result.group(10), result.group(4))

                if logLine.getIP() not in ipDict:
                    ipDict[logLine.getIP()] = {logLine.getUserAgent(): {1: time, 2: [[logLine]]}}
                else:
                    if logLine.getUserAgent() not in ipDict[logLine.getIP()]:
                        ipDict[logLine.getIP()][logLine.getUserAgent()] = {1: time, 2: [[logLine]]}
                    else:
                        lasttime = ipDict[logLine.getIP()][logLine.getUserAgent()][1]
                        ipDict[logLine.getIP()][logLine.getUserAgent()][1] = time
                        if time - lasttime < sessionTimeout:
                            arrsize = len(ipDict[logLine.getIP()][logLine.getUserAgent()][2])
                            ipDict[logLine.getIP()][logLine.getUserAgent()][2][arrsize - 1].append(logLine)
                        else:
                            ipDict[logLine.getIP()][logLine.getUserAgent()][2].append([logLine])
        logs.close()
        for ip, val in ipDict.items():
            for userag, v in val.items():
                reqs = v[2]
                userid = existUser(conn, ip, userag)

                if userid is None:
                    userid = saveUser(conn, ip, userag)
                proccessLogsperSession(conn, userid, reqs)
        print('Log processing complete')


if __name__ == '__main__':
    main()
