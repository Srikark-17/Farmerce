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

    if request.method == 'POST':
        print(form.name.data)
        print(form.description.data)
        print(form.price.data)

        post = {'id': uuid.uuid4().hex, 'name': form.name.data, 'description': form.description.data, 'is_organic': form.organic.data,
                'farming_method': form.methods.data, 'is_chemical': form.chemical.data, 'usda': form.usda.data,
                'contact': form.contact.data, 'price': form.price.data, 'produce': form.produce.data}

        collection = db.vendors
        collection.insert_one(post)
        return redirect(url_for('index'))

    return render_template('new_vendor.html', form=form)

@app.route('/view')
def view():
    return 'to be implemented'

@app.route('/view/<id>')
def view_vendor(id):
    return 'to be implemented '

if __name__ == "__main__":
    app.run(debug=True)


