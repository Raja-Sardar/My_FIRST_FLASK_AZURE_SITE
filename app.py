from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="GET":
        return render_template("index.html")
    
    else:
        name = request.form.get("name")
        age = request.form.get("age")
        country = request.form.get("country")
        return render_template("reply.html", name=name, age = age, country = country)
    

if __name__=="__main__":
    app.run(debug=True)