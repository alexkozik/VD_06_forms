from flask import render_template, request, redirect, url_for
from hw import hw

users = []

@hw.route("/", methods =["GET","POST"])
# @app.route('/', classmethod = ['GET','POST'])

def index():
    if request.method == "POST":
        name = request.form.get("name")
        city = request.form.get("city")
        hobby = request.form.get("hobby")
        age = request.form.get("age")
        if name and city and hobby and age:
            users.append({'name': name, 'city': city, 'hobby': hobby, 'age': age})
            return redirect(url_for('index'))
    return render_template('user_ncat_col.html', users = users)
