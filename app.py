from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "ok", "message": "Flask CI/CD running without local tools!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
