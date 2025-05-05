from flask import Flask, request, jsonify

app = Flask(__name__)
context_data = {}

@app.route("/context", methods=["POST"])
def update_context():
    global context_data
    context_data = request.json
    return jsonify({"status": "context updated", "context": context_data})

@app.route("/context", methods=["GET"])
def get_context():
    return jsonify(context_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
