from flask import Flask,render_template,jsonify

app = Flask(__name__)

STUDENTS=[
    {
        'id':1,
        'title':'master',
        'location':'Hangzhou,China',
        'name':'Young'
    },
    {
        'id':2,
        'title':'master',
        'location':'Hangzhou,China',
        'name':'QIQI'
    },
    {
        'id':3,
        'title':'master',
        'location':'Hangzhou,China',
        'name':'Elaine'
    },
    {
        'id':4,
        'location':'Hangzhou,China',
        'name':'NIUNIU'
    },
]






@app.route("/")
def hello_world():
    return render_template('home.html',
                           students=STUDENTS,
                           school='ZJUT')


@app.route("/api/students")
def list_students():
    return jsonify(STUDENTS)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)