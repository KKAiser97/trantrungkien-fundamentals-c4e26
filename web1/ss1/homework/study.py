from flask import Flask
from flask import redirect
app=Flask(__name__)
@app.route("/about-me")
def info():
    info={"name":"Kien",
          "work":"student",
          "hobbies":"['books','game','shoes']",
          "crush":"['Rosé','Yuqi']"}
    return str(info)
@app.route("/school")
def school():
    return redirect("http://techkids.vn")
if __name__ == '__main__':
  app.run(debug=True)



