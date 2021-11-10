from model.Session import Session
import uuid
import statistics
from db.postgres import saveLogs, saveSession

img = ['.ico', '.png', '.gif', '.jpg', '.jpeg', '.bmp']
cssjs = ['.js', '.css']
ofiles = ['.txt', '.zip', 'pdf', 'rar']


def proccessLogsperSession(conn, userid, reqs):
    for req in reqs:
        session = Session()
        sessionid = uuid.uuid4().hex

        session.setTotalreq(len(req))
        session.setSessionllenght((req[len(req) - 1].getTime() - req[0].getTime()).total_seconds())

        totalpages = 0
        totalbytes = 0

        # amount of requests with files js ...
        amtjs = 0
        amtimg = 0
        amtfiles = 0

        httpmethods = {'GET': 0, 'POST': 0, 'PUT': 0, 'DELETE': 0, 'PATCH': 0}
        amtempref = 0
        httpresp = {'2xx': 0, '3xx': 0, '4xx': 0, '5xx': 0}
        timebtwpages = []
        httpprevmeth = ''
        amthttpprevmeth = 0
        for r in req:
            if r.getHttpRes() == httpprevmeth:
                amthttpprevmeth += 1
            else:
                httpprevmeth = r.getHttpRes()

            timebtwpages.append(r.getTime())

            totalbytes += int(r.getBytes())

            if r.getReferer() == '':
                amtempref += 1

            if any(map(r.getReq().__contains__, cssjs)):
                amtjs += 1
            elif any(map(r.getReq().__contains__, cssjs)):
                amtimg += 1
            elif any(map(r.getReq().__contains__, ofiles)):
                amtfiles += 1
            else:
                totalpages += 1

            if r.getHttpRes() in httpmethods:
                httpmethods[r.getHttpRes()] += 1

            if r.getStatus().startswith('2'):
                httpresp['2xx'] += 1
            elif r.getStatus().startswith('3'):
                httpresp['3xx'] += 1
            elif r.getStatus().startswith('4'):
                httpresp['4xx'] += 1
            elif r.getStatus().startswith('5'):
                httpresp['5xx'] += 1

        session.setTotalpages(totalpages)
        session.setTotalBytes(totalbytes)
        res = []
        if len(timebtwpages) <= 1:
            session.settimeperpage(0)
        else:
            for t in range(len(timebtwpages) - 1):
                res.append((timebtwpages[t + 1] - timebtwpages[t]).total_seconds())
            avgr = 0
            for tim in res:
                avgr += tim
            session.settimeperpage(avgr / len(timebtwpages))

        session.setpercof2xx(100 * float(httpresp['2xx']) / float(session.getTotalReq()))
        session.setpercof3xx(100 * float(httpresp['3xx']) / float(session.getTotalReq()))
        session.setpercof4xx(100 * float(httpresp['4xx']) / float(session.getTotalReq()))
        session.setpercof5xx(100 * float(httpresp['5xx']) / float(session.getTotalReq()))

        session.setpercofget(100 * float(httpmethods['GET']) / float(session.getTotalReq()))
        session.setpercofpost(100 * float(httpmethods['POST']) / float(session.getTotalReq()))
        session.setpercofput(100 * float(httpmethods['PUT']) / float(session.getTotalReq()))
        session.setpercofdelete(100 * float(httpmethods['DELETE']) / float(session.getTotalReq()))
        session.setpercofpatch(100 * float(httpmethods['PATCH']) / float(session.getTotalReq()))

        session.setpercofimgreq(100 * float(amtimg) / float(session.getTotalReq()))
        session.setpercofjscssreq(100 * float(amtjs) / float(session.getTotalReq()))
        session.setpercofofilereq(100 * float(amtfiles) / float(session.getTotalReq()))

        session.setprevhttpm(amthttpprevmeth)
        # requests / second.BS = Sl / Sd
        if session.getSessionLenght() > 0:
            session.setbrospeed(session.getTotalReq() / session.getSessionLenght())

        session.setperofempref(100 * float(amtempref) / float(session.getTotalReq()))
        if len(res) > 1:
            session.setstandev2req(statistics.stdev(res))

        saveSession(conn, userid, sessionid, session)
        saveLogs(conn, req, sessionid)