from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_homepage():
    return render_template('home.html')


@app.route('/farmer')
def render_farmerpage():
    return render_template('individualfarmer.html')


if __name__ == '__main__':
    app.run(debug=True)
