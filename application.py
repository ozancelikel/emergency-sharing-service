from flask import Flask
from controller import Controller


class FlaskApplication(Flask):
    def __init__(self, name, ip, port):
        super().__init__(name)
        self.ip = ip
        self.port = port
    
    def start(self):
        self.run(
            host=self.ip,
            port=self.port
        )
    
    def add_rule(self, rule):
        self.add_url_rule(
            rule=rule,
            view_func=Controller.home,
            methods=["GET"]
        )


def create_app() -> FlaskApplication:
    app = __create_app
    app.add_url_rule(
        "/",
    )
    return app


def __create_app(ip, port) -> FlaskApplication:
    app = FlaskApplication(__name__, ip, port)
    return app
