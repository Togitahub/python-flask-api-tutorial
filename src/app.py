from flask import Flask, abort, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False},
]


@app.route("/todos", methods=["GET"])
def show_todos():
    return jsonify(todos)


@app.route("/todos", methods=["POST"])
def add_new_todo():
    request_body = request.json
    if request_body.get("label") == None:
        return jsonify('Bad Request: Label Requerido'), 400
    if request_body.get("done") == None:
        request_body["done"] = False
    todos.append(request_body)
    return jsonify(todos)


@app.route("/todos/<int:position>", methods=["DELETE"])
def delete_todo(position):
    if position < len(todos) and position >= 0:
        del todos[position]
        return jsonify(todos)
    else:
        return jsonify('Not Found: El ID a eliminar no se pudo encontrar'), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3245, debug=True)
