from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

import os

app = Flask(__name__)


@app.route('/')
def render_homepage():
    return render_template('home.html')


@app.route('/farmer')
def render_farmerpage():
    return render_template('individualfarmer.html')


@app.route('/detectdisease')
def render_diseasedetectpage():
    return render_template('diseasedetection.html')


data = [{'_id': '6069e79986d2956895f96ab5', 'id': 'eeef4bff822d4c07b77b94c31ec2ad85', 'name': 'dsfas', 'description': 'asdfasd', 'is_organic': 'Yes', 'farming_method': 'Unsustainable', 'is_chemical': 'No', 'usda': 'Yes', 'contact': 'asdfasdf', 'price': '$', 'produce': 'fasdfasdf'}, {'_id': '6069e8ebd4910b8d2794b615', 'id': '4518a1c9283d4d42bd253940fe0239ec', 'name': 'test', 'description': 'test', 'is_organic': 'Somewhat', 'farming_method': 'Unsustainable', 'is_chemical': 'No', 'usda': 'Yes', 'contact': 'test', 'price': '$$', 'produce': 'test'}, {'_id': '6069eb78d4910b8d2794b61a', 'id': 'f3df3e00f6344e59af98cf45edf22d90', 'name': 'test', 'description': 'test', 'is_organic': 'Somewhat', 'farming_method': 'Unsustainable', 'is_chemical': 'No', 'usda': 'Yes', 'contact': 'test', 'price': '$$', 'produce': 'test'}, {'_id': '6069e79986d2956895f96ab5', 'id': 'eeef4bff822d4c07b77b94c31ec2ad85', 'name': 'dsfas', 'description': 'asdfasd', 'is_organic': 'Yes', 'farming_method': 'Unsustainable', 'is_chemical': 'No', 'usda': 'Yes', 'contact': 'asdfasdf', 'price': '$', 'produce': 'fasdfasdf'}, {'_id': '6069e8ebd4910b8d2794b615', 'id': '4518a1c9283d4d42bd253940fe0239ec', 'name': 'test', 'description': 'test', 'is_organic': 'Somewhat', 'farming_method': 'Unsustainable', 'is_chemical': 'No', 'usda': 'Yes', 'contact': 'test', 'price': '$$', 'produce': 'test'}, {'_id': '6069e79986d2956895f96ab5', 'id': 'eeef4bff822d4c07b77b94c31ec2ad85', 'name': 'dsfas', 'description': 'asdfasd', 'is_organic': 'Yes', 'farming_method': 'Unsustainable', 'is_chemical': 'No', 'usda': 'Yes', 'contact': 'asdfasdf', 'price': '$', 'produce': 'fasdfasdf'}, {'_id': '6069e8ebd4910b8d2794b615', 'id': '4518a1c9283d4d42bd253940fe0239ec', 'name': 'test', 'description': 'test', 'is_organic': 'Somewhat', 'farming_method': 'Unsustainable', 'is_chemical': 'No', 'usda': 'Yes', 'contact': 'test', 'price': '$$', 'produce': 'test'}, {
    '_id': '6069e79986d2956895f96ab5', 'id': 'eeef4bff822d4c07b77b94c31ec2ad85', 'name': 'dsfas', 'description': 'asdfasd', 'is_organic': 'Yes', 'farming_method': 'Unsustainable', 'is_chemical': 'No', 'usda': 'Yes', 'contact': 'asdfasdf', 'price': '$', 'produce': 'fasdfasdf'}, {'_id': '6069e8ebd4910b8d2794b615', 'id': '4518a1c9283d4d42bd253940fe0239ec', 'name': 'test', 'description': 'test', 'is_organic': 'Somewhat', 'farming_method': 'Unsustainable', 'is_chemical': 'No', 'usda': 'Yes', 'contact': 'test', 'price': '$$', 'produce': 'test'}, {'_id': '6069eb78d4910b8d2794b61a', 'id': 'f3df3e00f6344e59af98cf45edf22d90', 'name': 'test', 'description': 'test', 'is_organic': 'Somewhat', 'farming_method': 'Unsustainable', 'is_chemical': 'No', 'usda': 'Yes', 'contact': 'test', 'price': '$$', 'produce': 'test'}, {'_id': '6069e79986d2956895f96ab5', 'id': 'eeef4bff822d4c07b77b94c31ec2ad85', 'name': 'dsfas', 'description': 'asdfasd', 'is_organic': 'Yes', 'farming_method': 'Unsustainable', 'is_chemical': 'No', 'usda': 'Yes', 'contact': 'asdfasdf', 'price': '$', 'produce': 'fasdfasdf'}, {'_id': '6069e8ebd4910b8d2794b615', 'id': '4518a1c9283d4d42bd253940fe0239ec', 'name': 'test', 'description': 'test', 'is_organic': 'Somewhat', 'farming_method': 'Unsustainable', 'is_chemical': 'No', 'usda': 'Yes', 'contact': 'test', 'price': '$$', 'produce': 'test'}, {'_id': '6069e79986d2956895f96ab5', 'id': 'eeef4bff822d4c07b77b94c31ec2ad85', 'name': 'dsfas', 'description': 'asdfasd', 'is_organic': 'Yes', 'farming_method': 'Unsustainable', 'is_chemical': 'No', 'usda': 'Yes', 'contact': 'asdfasdf', 'price': '$', 'produce': 'fasdfasdf'}, {'_id': '6069e8ebd4910b8d2794b615', 'id': '4518a1c9283d4d42bd253940fe0239ec', 'name': 'test', 'description': 'test', 'is_organic': 'Somewhat', 'farming_method': 'Unsustainable', 'is_chemical': 'No', 'usda': 'Yes', 'contact': 'test', 'price': '$$', 'produce': 'test'}]


@app.route('/gallery')
def render_gallery():
    # collection = db.vendors
    # data = list(collection.find())
    # print(data)
    return render_template('galleryscreen.html', data=data)


app.config["IMAGE_UPLOADS"] = "/mnt/c/wsl/projects/pythonise/tutorials/flask_series/app/app/static/img/uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 * 1024


def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


def allowed_image_filesize(filesize):

    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            if "filesize" in request.cookies:

                if not allowed_image_filesize(request.cookies["filesize"]):
                    print("Filesize exceeded maximum limit")
                    return redirect(request.url)

                image = request.files["image"]

                if image.filename == "":
                    print("No filename")
                    return redirect(request.url)

                if allowed_image(image.filename):
                    filename = secure_filename(image.filename)

                    image.save(os.path.join(
                        app.config["IMAGE_UPLOADS"], filename))

                    print("Image saved")

                    return redirect(request.url)

                else:
                    print("That file extension is not allowed")
                    return redirect(request.url)

    return render_template("upload_image.html")


if __name__ == '__main__':
    app.run(debug=True)
