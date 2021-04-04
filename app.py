from flask import *
from farmerce.forms import CreateVendorForm
from pymongo import MongoClient
import uuid

password = 'KxM8sn4PRljHpmBK'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

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

if __name__ == "__main__":
    app.run(debug=True)


