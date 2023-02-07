import asyncio
from flask import Flask, request

from controller import Controller
from services.list import ListService

loop = asyncio.get_event_loop()
app = Flask(__name__)

controller = Controller()


@app.route("/")
def home():
    return controller.home()

@app.route("/list", methods=["GET", "POST"])
def list_page(org):
    a = request.data
    return f"showing {org}"

@app.route("/list", methods=["GET", "POST"])
def list():
    if request.method == "GET":
        return controller.get_list()
    if request.method == "POST":
        return controller.get_filtered_list(request.json)
    return f""

@app.route("/notify")
def notify(org):
    return f"notifying {org}"


if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
