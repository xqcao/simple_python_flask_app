from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    return render_template('index.html',title="this is main page")

messages=[
    {'name':'adam','message':'hello wolrd'},
    {'name':'cat','message':'miao miao'},
    {'name':'dog','message':'wang wang!'}
]
@app.route('/todo',methods=['POST'])
def tosave():
    uname = request.form['uname']
    message = request.form['umsg']
    messages.append({'name':uname,"message":message})
    return render_template('success.html',messages=messages)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)