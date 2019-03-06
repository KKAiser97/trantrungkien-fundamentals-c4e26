from flask import Flask, render_template, request
app = Flask(__name__)

bikes=[]
@app.route("/new_bike", methods=["GET","POST"])
def add_bike():
    if request.method=="GET":
        return render_template("bike_form.html")
    elif request.method=="POST":
        form=request.form
        m=form["Model"]
        d=form["Daily fee"]
        i=form["Image"]
        y=form["Year"]
        new_bike={
            "Model":m,
            "Daily fee":d,
            "Image":i,
            "Year":y
        }
        bikes.append(new_bike)
        return "New bike added"

if __name__ == '__main__':
  app.run(debug=True) 





