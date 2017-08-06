import cherrypy
import random
import string

@cherrypy.expose
class StringGeneratorWebService(object):
	
	def POST(self, length=8):
		some_string = ''.join(random.sample(string.hexdigits,int(length)))
		cherrypy.session['mystring']=some_string
		return some_string

	@cherrypy.tools.accept(media='text/plain')
	def GET(self):
		return cherrypy.session['mystring']

	def PUT(self,another_string):
		cherrypy.session['mystring'] = another_string

	def DELETE(self):
		cherrypy.session.pop('mystring', None)

if __name__=='__main__':
	conf = {
		'/':{
		    'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on': True,
			'tools.response_headers.on': True,
			'tools.response_headers.headers': [('Content-Type','text/plain')]
		}
	}
	cherrypy.quickstart(StringGeneratorWebService(),'/',conf)