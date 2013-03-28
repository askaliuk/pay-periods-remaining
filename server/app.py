import web
from api import ApiRoot

urls = (
    '/.*', ApiRoot
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = True
    app.run()
