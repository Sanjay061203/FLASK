from flask import Flask,redirect,render_template,request,url_for
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
#name = sanjay rocky,email = sanjay43650@gmail.com
@app.route('/getdata',methods=['GET'])
def getdata():
    name = request.args.get('name')
    email = request.args.get('email')
    return f'name = {name},email = {email}'

@app.route('/getDatafromPOST',methods=['POST'])
def getDatafromPOST():
    data = request.get_json()
    name = data['name']
    email = data['email']
    return f'name = {name},email = {email}'

@app.route('/postData',methods=['POST'])
def postData():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    if name is None or len(name)<5:
        return render_template('index.html',error='name is required and length should be greater than 5')
    if email is None:
        return render_template('index.html',error='email is invalid')
    if password is None or len(password)<4:
        return render_template('index.html',error='password is wrong')

    return render_template('index.html',success='data is valid')

@app.route('/updatedata/<email>',methods=['Put'])
def updatedata(email):
    data = request.get_json()
    email1 = data['email']
    print(email1)
    return f'email = {email}'


@app.route('/deletedata/<email>',methods=['DELETE'])
def deletedata(email):
    return f'email = {email} is deleted'

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == "GET":
        name = request.args.get('name')
        email = request.args.get('email')
    if request.method == "POST":
        data = request.get_json()
        name = data['name']
        email = data['email']
    return f'the name is {name} and mail is {email}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)