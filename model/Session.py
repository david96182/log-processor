class Session:
    # 1. Total of requests X    --------
    totalreq = 0
    # 2. Total of pages requested  X  ----------
    totalpages = 0
    # 3. Duration of the session in seconds  X  -----------
    sessionlenght = 0
    # 4. Total bytes sent to the client in the session  X ---------
    totalbytes = 0
    # 7. Average time per page in seconds  X ---------------
    timeperpage = 0
    # 8. Percentage of http requets with code 2xx   X  ------------
    percof2xx = 0
    # 8. Percentage of http requets with code 3xx   X  ----------
    percof3xx = 0
    # 8. Percentage of http requets with code 4xx   X   -----------
    percof4xx = 0
    # 8. Percentage of http requets with code 5xx    X --------
    percof5xx = 0
    # 9. Percentage of http request with method GET   X  --------
    percofget = 0
    # 9. Percentage of http request with method POST  X  ---------
    percofpost = 0
    # 9. Percentage of http request with method PUT   X  -------
    percofput = 0
    # 9. Percentage of http request with method DELETE  X -------
    percofdelete = 0
    # 9. Percentage of http request with method PATCH   X ------
    percofpatch = 0
    # 11. 14 Percentage of requests of Image png ico gig jpg jpeg ...  X -------
    percofimgreq = 0
    # 11. 14 Percentage of requests of Javascript or Css  X  --------
    percofjscssreq = 0
    # 11. 14 Percentage of requests of Others Files pdf txt zip rar ....  X  --------
    percofofilereq = 0
    # 12 Standar deviation between two consecutive requests  X -------------
    standev2req = 0
    # 13. Total of requests using the previous http method   X  --------------
    prevhttpm = 0
    # 17. Browsing speed  X --------
    brospeed = 0
    # 21. Percentage of requests with empty referer   X --------
    perofempref = 0

    def __init__(self):
        self.totalreq = 0
        self.totalpages = 0
        self.sessionlenght = 0
        self.totalbytes = 0
        self.timeperpage = 0
        self.percof2xx = 0
        self.percof3xx = 0
        self.percof4xx = 0
        self.percof5xx = 0
        self.percofget = 0
        self.percofpost = 0
        self.percofput = 0
        self.percofdelete = 0
        self.percofpatch = 0
        self.percofimgreq = 0
        self.percofjscssreq = 0
        self.percofofilereq = 0
        self.standev2req = 0
        self.prevhttpm = 0
        self.brospeed = 0
        self.perofempref = 0

    def getTotalReq(self):
        return self.totalreq

    def setTotalreq(self, t):
        self.totalreq = t

    def getTotalpages(self):
        return self.totalpages

    def setTotalpages(self, t):
        self.totalpages = t

    def getSessionLenght(self):
        return self.sessionlenght

    def setSessionllenght(self, s):
        self.sessionlenght = s

    def getTotalBytes(self):
        return self.totalbytes

    def setTotalBytes(self, t):
        self.totalbytes = t

    def gettimeperpage(self):
        return self.timeperpage

    def settimeperpage(self, timeperpage):
        self.timeperpage = timeperpage

    def getpercof2xx(self):
        return self.percof2xx

    def setpercof2xx(self, percof2xx):
        self.percof2xx = percof2xx

    def getpercof3xx(self):
        return self.percof3xx

    def setpercof3xx(self, percof3xx):
        self.percof3xx = percof3xx

    def getpercof4xx(self):
        return self.percof4xx

    def setpercof4xx(self, percof4xx):
        self.percof4xx = percof4xx

    def getpercof5xx(self):
        return self.percof5xx

    def setpercof5xx(self, percof5xx):
        self.percof5xx = percof5xx

    def getpercofget(self):
        return self.percofget

    def setpercofget(self, percofget):
        self.percofget = percofget

    def getpercofpost(self):
        return self.percofpost

    def setpercofpost(self, percofpost):
        self.percofpost = percofpost

    def getpercofput(self):
        return self.percofput

    def setpercofput(self, percofput):
        self.percofput = percofput

    def getpercofdelete(self):
        return self.percofdelete

    def setpercofdelete(self, percofdelete):
        self.percofdelete = percofdelete

    def getpercofpatch(self):
        return self.percofpatch

    def setpercofpatch(self, percofpatch):
        self.percofpatch = percofpatch

    def getpercofimgreq(self):
        return self.percofimgreq

    def setpercofimgreq(self, percofimgreq):
        self.percofimgreq = percofimgreq

    def getpercofjscssreq(self):
        return self.percofjscssreq

    def setpercofjscssreq(self, percofjscssreq):
        self.percofjscssreq = percofjscssreq

    def getpercofofilereq(self):
        return self.percofofilereq

    def setpercofofilereq(self, percofofilereq):
        self.percofofilereq = percofofilereq

    def getstandev2req(self):
        return self.standev2req

    def setstandev2req(self, standev2req):
        self.standev2req = standev2req

    def getprevhttpm(self):
        return self.prevhttpm

    def setprevhttpm(self, prevhttpm):
        self.prevhttpm = prevhttpm

    def getbrospeed(self):
        return self.brospeed

    def setbrospeed(self, brospeed):
        self.brospeed = brospeed

    def getperofempref(self):
        return self.perofempref

    def setperofempref(self, perofempref):
        self.perofempref = perofempref

    def __str__(self):
        print(self.totalreq,self.totalpages,self.sessionlenght,
            self.totalbytes,self.timeperpage,self.percof2xx,
            self.percof3xx,self.percof4xx,self.percof5xx,
            self.percofget,self.percofpost,self.percofput,
            self.percofdelete,self.percofpatch,self.percofimgreq,
            self.percofjscssreq,self.percofofilereq,self.standev2req,
            self.prevhttpm,self.brospeed,self.perofempref)
