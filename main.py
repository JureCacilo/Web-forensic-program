#!/usr/bin/env python
import os
import jinja2
import webapp2
from forenzicni_program import crim_characteristics, hair_color, facial_shape, eye_color, gender, race


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))




class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")
    
    def post(self):
        dna_code = self.request.get("DNA-code")
        criminal = {}
        # find criminal facial shape
        criminal["hair-color"] = crim_characteristics(hair_color, "hair color", dna_code)

        #find the criminal facial shape
        criminal["face-shape"] = crim_characteristics(facial_shape, "face shape", dna_code)

        #find the criminal eye color
        criminal["eye-color"] =  crim_characteristics(eye_color, "eye color", dna_code)

        # find the criminal gender
        criminal["gender"] = crim_characteristics(gender, "gender", dna_code)

        # find the criminal race
        criminal["race"] = crim_characteristics(race, "race", dna_code)

        params = {"criminal": criminal}
        return self.render_template("hello.html", params = params)
        



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
