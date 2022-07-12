import os
SECRET_KEY = os.urandom(32)

# Enable debug mode.
DEBUG = True

PROPAGATE_EXCEPTIONS = True

# Database configuration
SQLALCHEMY_DATABASE_URI ="mysql+pymysql://root:@localhost:3310/alba?host=localhost"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False
ERROR_404_HELP = False


