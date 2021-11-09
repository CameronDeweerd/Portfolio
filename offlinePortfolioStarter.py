from flask import Flask
webApp = Flask(__name__)

from portfolio.views import portfolio
webApp.register_blueprint(portfolio)

if __name__ == '__main__':
    webApp.run(debug=True)
