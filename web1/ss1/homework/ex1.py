from flask import Flask
app = Flask(__name__)

@app.route("/BMI/<int:w>/<int:cm>")
def bmi(w,cm):
    h=cm/100
    bmi=w/(h*h)
    return str(bmi)
    if bmi<16:
        return "Severely underweight"
    elif bmi<18.5:
        return "Underweight"
    elif bmi<25:
        return "Normal"
    elif bmi<30:
        return "Overweigh"
    else:
        return "Obese"

if __name__ == '__main__':
  app.run(debug=True)
