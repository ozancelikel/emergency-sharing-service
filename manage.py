import asyncio
import os

from flask import Flask, request, make_response, jsonify

from controller import Controller

loop = asyncio.get_event_loop()
app = Flask(__name__)

app.config.from_prefixed_env()
# TODO: fix here
es_ip = "localhost"
es_port = 9200
es_index = "earthquake"

controller = Controller(es_ip, es_port, es_index)


@app.route("/list", methods=["GET", "POST"])
def list_():
    if request.method == "GET":
        # TODO: add page number and size
        return make_response(jsonify(controller.get_list()), 200)
    if request.method == "POST":
        # TODO: add filter
        return make_response(jsonify(controller.get_filtered_list(request.json), 200))
    return f""


@app.route("/notify")
def notify(org):
    return f"notifying {org}"


@app.route("/add", methods=["POST"])
def add_new():
    return controller.add_new(request.json)


@app.route("/test_pagination", methods=["GET", "POST"])
def test_pagination():
    # TODO: pagination should be done in here
    if request.method == "POST":
        return controller.get_page(request.json)
    return controller.get_page(0)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, use_reloader=False)
