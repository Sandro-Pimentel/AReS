from flask import Flask, render_template

app = Flask('__name__')

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/conteudo1")
def conteudo1():
    return render_template("conteudo1.html")


#@app.route("/teste-definições")
#def teste1():
#    return render_template("teste-definiçoes.html")


@app.route("/conteudo2")
def conteudo2():
    return render_template("conteudo2.html")

#@app.route("/teste-responsabilidade_e_papeis")
#def teste2():
#    return render_template("teste-responsabilidade.html")


@app.route("/conteudo3")
def conteudo3():
    return render_template("conteudo3.html")


#@app.route("/teste-eventos_do_scrum")
#def teste3():
#    return render_template("teste-eventos.html")


@app.route("/conteudo4")
def conteudo4():
    return render_template("conteudo4.html")


#@app.route("/teste-artefatos_do_scrum")
#def teste4():
#    return render_template("teste-artefatos.html")


#@app.route("/teste-final")
#def testefinal():
#    return render_template("testefinal.html")

#@app.route("/testebase")
#def teste():
#    return render_template("baseteste.html")

#@app.route("/baseteste")
#def teste2():
#    return render_template("testebase.html")