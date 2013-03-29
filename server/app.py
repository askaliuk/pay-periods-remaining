import web
from api import ApiRoot

urls = (
    '/api/(.+)', ApiRoot
)


def create_application():
    return web.application(urls, globals(), autoreload=True)


if __name__ == "__main__":
    web.config.debug = True
    app = create_application()
    app.run()
