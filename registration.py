from flask import Flask,render_template,request
app = Flask(__name__)

#Index page najnennen coding
print('hii')
@app.route("/registration")
def welcome_page():
    return render_template('userinfo.html')

@app.route("/save/",methods=["POST"])
def save_user_info():
    print('METHOD TYPE', request.method)
    print('GET METHOD TYPE', request.args)  #
    print('POST METHOD TYPE', request.form)  # post
    firstname = request.form['fname']
    lastname =  request.form['lname']
    gender = request.form['gender']
    address = request.form['address']
    skills = request.form.getlist['skills']
    courses = request.form.getlist['courses']
    print('--------------------------------')
    print('FirstName : ', firstname)
    print('Lastname : ', lastname)
    print('Gender : ', gender)
    print('Address : ', address)
    print('Skills : ', skills)
    print('Courses : ', courses)
    print('--------------------------------')
    return render_template('userinfo.html')






if __name__ == '__main__':
    app.run(debug=True,port=1828)