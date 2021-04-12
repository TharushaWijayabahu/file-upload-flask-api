from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("public/index.html")


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    return render_template("public/upload_image.html")


if __name__ == '__main__':
    app.run()
