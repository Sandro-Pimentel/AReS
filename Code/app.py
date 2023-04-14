from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/capitulo-1/")
def cap1():
    return render_template("capitulo1.html")


#@app.route("/teste-1/")
#def teste1():
 #   return render_template(".html")


@app.route("/capitulo-2/")
def cap2():
    return render_template("capitulo2.html")

#@app.route("/teste-2/")
#def main():
#    return render_template(".html")


@app.route("/capitulo-3/")
def main():
    return render_template("capitulo3.html")


#@app.route("/teste-3/")
#def main():
  #  return render_template(".html")


@app.route("/capitulo-4/")
def main():
    return render_template("capitulo4.html")


#@app.route("/teste-4/")
#def main():
#    return render_template(".html")







