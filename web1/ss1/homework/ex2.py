from flask import Flask
app = Flask(__name__)

@app.route("/user/<username>")
def user(username):
    users = {"huy" :{
			"name" : "Nguyen Quang Huy",
			"age" : 29
       },
       "tuananh" : {
			"name" : "Huynh Tuan Anh",
			"age" : 22
       }
}
    for i in users:
        if username==i:
            return str(users[username])
        else:
            return "User not found"

if __name__ == '__main__':
  app.run(debug=True) 