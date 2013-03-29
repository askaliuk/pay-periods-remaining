import logic
import web
try:
    import simplejson as json
except ImportError:
    import json
import mimerender

mimerender = mimerender.WebPyMimeRender()
render_json = lambda **args: json.dumps(args)


class ApiRoot:

    @mimerender(json=render_json)
    def GET(self, param):
        try:
            method = getattr(self, param)
            if callable(method):
                return method()
            else:
                raise web.webapi.notfound()
        except AttributeError:
            raise web.webapi.notfound()

    def pay_peroids_remaining(self):
        return {'pay_peroids_remaining': logic.pay_peroids_remaining()}
