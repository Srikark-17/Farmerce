from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_homepage():
    return render_template('home.html')


@app.route('/farmer')
def render_farmerpage():
    return render_template('individualfarmer.html')


@app.route('/farmer')
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


if __name__ == '__main__':
    app.run(debug=True)
