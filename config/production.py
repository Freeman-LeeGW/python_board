from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x11J\x90\xf8\x00\xd8\x07\x0b\xe3^\xe7\x9f\xa8YK\xf7'
