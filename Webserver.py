from flask import Flask,render_template

app = Flask("Mi primera web en python") 

@app.route("/")
def Hola_mundo():
    return render_template("index.html")

@app.route("/ejemplo")
def ejemplo_ruta():
    return "Hola wey que pedo gallo"

if __name__ == "__main__":
    app.run(debug=True,host= "0.0.0.0", port = 5000)