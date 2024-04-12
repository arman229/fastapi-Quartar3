from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config(".env")
except FileNotFoundError:
    print('Error: The .env file does not exist')
except Exception as e:
    print("Error:", e)
DATA_BASE_URL = config("DATA_BASE_URL", cast=Secret)

TEST_DATA_BASE_URL = config("TEST_DATA_BASE_URL", cast=Secret)
