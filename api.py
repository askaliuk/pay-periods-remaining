import web
import logic
try:
    import simplejson as json
except ImportError:
    import json
import mimerender

mimerender = mimerender.WebPyMimeRender()

render_json = lambda **args: json.dumps(args)

urls = (
    '/', 'Root'
)
app = web.application(urls, globals(), autoreload=False)


class Root:

    @mimerender(json=render_json)
    def GET(self):
        return {'pay_peroids_remaining': logic.pay_peroids_remaining()}

if __name__ == "__main__":
    app.run()
