import os
from dotenv import load_dotenv
from blog.enums import EnvType

load_dotenv()
ENV = os.getenv('FLASK_ENV', default=EnvType.production)
FLASK_ADMIN_SWATCH = 'cosmo'
OPENAPI_URL_PREFIX = '/api/swagger'
OPENAPI_SWAGGER_UI_PATH = '/'
OPENAPI_SWAGGER_UI_VERSION = '3.22.0'
