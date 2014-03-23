import web
import urllib
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def __init__(self):
        self.storeKey = ('REMOTE_ADDR', 'REMOTE_PORT', 'REQUEST_URI', 'REQUEST_METHOD')

    def GET(self, name):
        headerLines = []
        for k, v in web.ctx.env.iteritems():
            if k.startswith('HTTP') or k in self.storeKey:
                headerLines.append('%s: %s' %(k,v))
        resultBody = '<html><body>'
        for line in sorted(headerLines):
            resultBody = resultBody + line + '</br>'
        resultBody = resultBody + '<pre>' + str(self.getIpInfo()) + '</pre></body></html>'
        return resultBody

    def getIpInfo(self):
        clientIp = ''
        if 'HTTP_X_REAL_IP' in  web.ctx.env:
            clientIp = web.ctx.env.get('HTTP_X_REAL_IP', '')
        else:
            clientIp = web.ctx.env.get('REMOTE_ADDR', '')
        return urllib.urlopen('http://ipinfo.io/%s/json' % clientIp).read()
if __name__ == "__main__":
    app.run()
