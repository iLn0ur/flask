import os
from dotenv import load_dotenv
from blog.enums import EnvType

load_dotenv()
ENV = os.getenv('FLASK_ENV', default=EnvType.production)

