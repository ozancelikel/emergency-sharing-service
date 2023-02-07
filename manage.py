import asyncio
from flask import Flask

from controller import Controller

loop = asyncio.get_event_loop()
app = Flask(__name__)

controller = Controller()

@app.route("/")
def home():
    return controller.home()

@app.route("/ekipler/<org>")
def equip(org):
    return f"showing {org}"

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)