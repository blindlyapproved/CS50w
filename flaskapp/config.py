
class Config(object):
    DEBUG = False
    TESTING = False

    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"

    UPLOADS = "/home/username/app/app/static/images/uploads"

    CLIENT_IMAGES = "/Users/luuk/cs50w/flaskapp/app/static/client/img"
    CLIENT_CSV = "/Users/luuk/cs50w/flaskapp/app/static/client/csv"
    CLIENT_REPORT = "/Users/luuk/cs50w/flaskapp/app/static/client/reports"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"

    UPLOADS = "/home/username/projects/flask_test/app/app/static/images/uploads"
    IMAGE_UPLOADS = "/Users/luuk/cs50w/flaskapp/app/static/uploads"
    ALLOWED_IMAGE_EXTENSIONS = ["PNG", "JPG", "JPEG", "GIF"]


class TestingConfig(Config):
    TESTING = True

    DB_NAME = "testing-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"

    UPLOADS = "/home/username/projects/flask_test/app/app/static/images/uploads"
