from flask import Flask, render_template, request
app = Flask(__name__)

items=[
    {"name":"com rang",
    "price":25000},
    {"name":"pho bo",
    "price":30000},
    {"name":"xoi",
    "price":20000}  
]
@app.route("/")
def menu():
    return render_template("menu.html", item_list=items, user="Kien")
@app.route("/food/<int:i>")
def food(i):
    return render_template("food_detail.html", item=items[i])
@app.route("/add_food", methods=["GET","POST"])
def add_food():
    if request.method=="GET":
        return render_template("food_form.html")
    elif request.method=="POST":
        form=request.form
        f=form["food"]
        p=form["price"]
        new_item={
            "name":f,
            "price":p
        }
        items.append(new_item)
        return f+": "+str(p)

if __name__ == '__main__':
  app.run(debug=True) 



