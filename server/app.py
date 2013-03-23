import web
from api import ApiRoot

urls = (
    '/api', ApiRoot
)
app = web.application(urls, globals(), autoreload=False)

if __name__ == "__main__":
    app.run()
