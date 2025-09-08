import os
from flask import Flask, Response

app = Flask(__name__)

@app.get("/")
def hello():
    label = os.environ.get("VAR", "-1")
    return Response(f"Hello World from SJSU-{label}", mimetype="text/plain")

if __name__ == "__main__":
    # Bind to all interfaces for VM access, on port 8080
    app.run(host="0.0.0.0", port=8080)
