# [START imports]
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

# [START main_page]
class MainPage(webapp2.RequestHandler):

    def get(self):

        streams = filter(None, self.request.path.split('/'))
        uniq_streams = []

        for s in streams:
            if s not in uniq_streams:
                uniq_streams.append(s)

        template_values = {
            'project' : 'multiLIVEhouse',
            'streams' : streams,
            'unique_streams' : uniq_streams,
            'nstreams' : len(streams),
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
# [END main_page]

app = webapp2.WSGIApplication([
    ('/.*', MainPage),
], debug=True)
