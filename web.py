from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pointpark():
    return 'Point Park is almost out for the semester'

if __name__ == '__main__':
    app.run(debug=True)