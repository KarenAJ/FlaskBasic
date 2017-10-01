#!/usr/bin/python
from flask import Flask,request,render_template

app = Flask(__name__)
# @ indicates decorator
@app.route('/')
def index(): #name of page route
    #   return 'this is the homepage'
    return 'method used %s'%request.method

@app.route('/bacon',methods=['GET','POST'])
def bacon(): #name of page route
    #return '<h2>fish is tasty</h2>'
    if request.method=='POST':
        return 'method used is POST'
    else:
        return 'method used is GET'


@app.route('/tuna')
def tuna(): #name of page route
    return '<h2>fish is tasty</h2>'

@app.route('/profile')
@app.route('/profile/<username>')
def profile(username=None): #name of page route
    return render_template("username.html",username=username)

@app.route('/post/<int:post_id>')
def show_post(post_id): #name of page route
    return 'post %s' %post_id

@app.route('/shopping')
def shopping(): #name of page route
    food=['cheese','bread','butter']
    return render_template("shopping.html",food=food)


if __name__=="__main__":
    app.run(debug=True)
