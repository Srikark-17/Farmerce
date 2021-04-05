from flask import *
from farmerce.forms import CreateVendorForm
from pymongo import MongoClient
import uuid
from werkzeug.utils import secure_filename
import os

password = 'KxM8sn4PRljHpmBK'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config["IMAGE_UPLOADS"] = os.getcwd()
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 * 1024

cluster = MongoClient("mongodb+srv://sid:"+password+"@farmerce.2s4c2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster.farmerce


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/new_vendor', methods=['GET', 'POST'])
def create_vendor():
    form = CreateVendorForm()
    collection = db.vendors

    if request.method == 'POST':
        print(form.name.data)
        print(form.description.data)
        print(form.pic.data)

        post = {'id': uuid.uuid4().hex, 'name': form.name.data, 'description': form.description.data,
                'is_organic': form.organic.data, 'farming_method': form.methods.data,
                'is_chemical': form.chemical.data, 'usda': form.usda.data, 'contact': form.contact.data,
                'price': form.price.data, 'produce': form.produce.data, 'pic': form.pic.data}

        collection.insert_one(post)

        return redirect(url_for('index'))

    return render_template('new_vendor.html', form=form)

@app.route('/view')
def view():
    collection = db.vendors
    data = reversed(list(collection.find()))
    return render_template('gallery.html', data=data)

@app.route('/view/<id>')
def view_vendor(id):
    collection = db.vendors
    data = list(collection.find())
    vendor = {}
    for x in data:
        if x['id'] == id:
            vendor = x
    return render_template('viewvendor.html', vendor=vendor)


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
        print(request.files)
        if request.files:

            if "filesize" in request.cookies:
                print(request.cookies['filesize'])
                if not allowed_image_filesize(request.cookies["filesize"]):
                    print("Filesize exceeded maximum limit")
                    return redirect(request.url)

                image = request.files["image"]

                if image.filename == "":
                    print("No filename")
                    return redirect(request.url)

                if allowed_image(image.filename):
                    filename = secure_filename(image.filename)

                    image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

                    print("Image saved")

                    return redirect(request.url)

                else:
                    print("That file extension is not allowed")
                    return redirect(request.url)

    return render_template("upload_image.html")


@app.route('/detectdisease')
def render_diseasedetectpage():
    return render_template('diseasedetection.html')

@app.route('/result')
def new():
    return render_template('new.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)


