from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("public/index.html")


app.config["IMAGE_UPLOADS"] = "D:\\MY\\My_Projects\\video-upload-flask-app\\data"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]


def allowed_image(filename):

    # We only want files with a . in the filename
    if not "." in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":

        if request.files:
            image = request.files["image"]

            if image.filename == "":
                print("No filename")
                return redirect(request.url)

            filename = secure_filename(image.filename)

            image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

            print(image)

            return redirect(request.url)

    return render_template("public/index.html")


if __name__ == '__main__':
    app.run(debug=type)
