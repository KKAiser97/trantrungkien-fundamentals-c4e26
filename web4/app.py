from flask import Flask, render_template, request
import food
from db import food_collection, user_collection
app = Flask(__name__)

@app.route("/food_list")
def food_list():
    #get food
    all_food=food.get_food({})
    #render:food+html
    #return
    return render_template("food_list.html",all_food=all_food)
@app.route("/food_list/<id>")
def food_detail(id):
    f=food.get_by_id(id)
    return render_template("food_detail.html", f=f)
@app.route("/add_food", methods=["GET","POST"])
def add_food():
    if request.method=="GET":
        return render_template("food_form.html")
    elif request.method=="POST":
        form=request.form
        n=form["name"]
        p=form["price"]
        food.add_food(n,p)
        return "New food added"
@app.route("/user/add", methods=["GET","POST"])
def add_user():
    if request.method=="GET":
        return render_template("add_user.html")
    elif request.method=="POST":
        form=request.form
        u=form["username"]
        p=form["password"]
        new_user={
            "username":u,
            "password":p
        }
        user_collection.insert_one(new_user)
        return "New user added"
        
@app.route("/user", methods=["GET","POST"])
def user():
    if request.method=="GET":
        return render_template("user.html")
    elif request.method=="POST":
        form=request.form
        us=form["username"]
        pas=form["password"] 
        user={
            "username":us,
            "password":pas
        }
        a=user_collection.find_one(user["username"])
        if a ==None:
            return "This user doesn't exist. Please register a new account."
        
            

if __name__ == '__main__':
    app.run(debug=True) 

