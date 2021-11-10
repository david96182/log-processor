class LogLine:
    ip = ''
    Time = ''
    req = ''
    status = ''
    ubytes = ''
    ref = ''
    user_agent = ''
    http_res = ''

    def __init__(self, ip, Time, req, status,
                 ubytes, ref, user_agent, http_res):
        self.ip = ip
        self.Time = Time
        self.req = req
        self.status = status
        self.ubytes = ubytes
        self.re = ref
        self.user_agent = user_agent
        self.http_res = http_res

    def getIP(self):
        return self.ip

    def setIP(self, IP):
        self.ip = IP

    def getTime(self):
        return self.Time

    def setTime(self, Time):
        self.Time = Time

    def getReq(self):
        return self.req

    def setReq(self, Req):
        self.req = Req

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getBytes(self):
        return self.ubytes

    def setBytes(self, uBytes):
        self.ubytes = uBytes

    def getReferer(self):
        return self.ref

    def setReferer(self, ref):
        self.ref = ref

    def getUserAgent(self):
        return self.user_agent

    def setUserAgent(self, User_Agent):
        self.user_agent = User_Agent

    def getHttpRes(self):
        return self.http_res

    def setHttpRes(self, http):
        self.http_res = http

    def __str__(self):
        print(self.ip, self.Time, self.req, self.status, self.ubytes, self.ref, self.user_agent, self.http_res)
