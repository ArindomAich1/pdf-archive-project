from os import environ
from archive import create_app

config_env = environ.get("CONFIG_ENV")
app = create_app(config_env)

if __name__ == "__main__":
    app.run()