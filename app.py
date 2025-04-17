from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/interview')
def interview():
    return render_template("interview.html")

@app.route('/tools')
def tools():
    return render_template("tools.html")

@app.route('/scenarios')
def scenarios():
    return render_template("scenarios.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/resources')
def resources():
    return render_template("resources.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if _name_ == '_main_':
    app.run(host="0.0.0.0", port=5000)