from flask import Flask, render_template

app = Flask('__name__')

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/conteudo1")
def conteudo1():
    return render_template("conteudo1.html")


#@app.route("/teste-1/")
#def teste1():
 #   return render_template(".html")


@app.route("/conteudo2")
def conteudo2():
    return render_template("conteudo2.html")

#@app.route("/teste-2/")
#def main():
#    return render_template(".html")


@app.route("/conteudo3")
def conteudo3():
    return render_template("conteudo3.html")


#@app.route("/teste-3/")
#def main():
  #  return render_template(".html")


@app.route("/conteudo4")
def conteudo4():
    return render_template("conteudo4.html")


#@app.route("/teste-4/")
#def main():
#    return render_template(".html")
