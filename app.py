from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("public/index.html")


app.config["IMAGE_UPLOADS"] = "D:\\MY\\My_Projects\\video-upload-flask-app\\data"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":

        if request.files:
            image = request.files["image"]

            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image))

            print(image)

            return redirect(request.url)

    return render_template("public/index.html")


if __name__ == '__main__':
    app.run(debug=type)
