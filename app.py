from flask import Flask

from search.api import api

app = Flask(__name__)

app.register_blueprint(api, url_prefix='/api/search')

if __name__ == '__main__':
    app.run()
