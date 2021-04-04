from flask import *
from farmerce.forms import CreateVendorForm
from pymongo import MongoClient

password = 'KxM8sn4PRljHpmBK'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

cluster = MongoClient("mongodb+srv://sid:"+password+"@farmerce.2s4c2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster.farmerce

@app.route('/', methods=['GET', 'POST'])
def create_vendor():
    form = CreateVendorForm()

    if request.method == 'POST':
        print(form.name.data)
        print(form.description.data)
        print(form.price.data)

        post = {'name': form.name.data, 'description': form.description.data, 'is_organic': form.organic.data,
                'farming_method': form.methods.data, 'is_chemical': form.chemical.data, 'usda': form.usda.data,
                'contact': form.contact.data}

        collection = db.vendors
        collection.insert_one(post)
        return redirect(url_for('index'))
    return render_template('new_vendor.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)


