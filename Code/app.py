from flask import Flask, render_template, request

app = Flask('__name__')

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/conteudo1")
def conteudo1():
    return render_template("conteudo1.html")


@app.route("/teste-definicoes")
def teste1():
    return render_template("teste-definicoes.html")


@app.route("/conteudo2")
def conteudo2():
    return render_template("conteudo2.html")

@app.route("/teste-responsabilidade_e_papeis")
def teste2():
   return render_template("teste-responsabilidade.html")


@app.route("/conteudo3")
def conteudo3():
    return render_template("conteudo3.html")


@app.route("/teste-eventos_do_scrum")
def teste3():
   return render_template("teste-eventos.html")


@app.route("/conteudo4")
def conteudo4():
    return render_template("conteudo4.html")


@app.route("/teste-artefatos_do_scrum")
def teste4():
   return render_template("teste-artefatos.html")


# @app.route("/examefinal")
# def examefinal():
#    return render_template("examefinal.html")

@app.route("/examefinal", methods=['GET','POST'])
def teste():
    if request.method == 'POST':
        questoes = '''qt1 qt2 qt3 qt4 qt5 qt6 qt7 qt8 qt9 qt10 qt11 qt12'''.split()
        acertos = 0
        for c in questoes:
            checkbox_value = request.form.get(c)
            if checkbox_value == None:
                return render_template("examefinal.html")
            if checkbox_value == 'true':
                acertos+=1
        if acertos >= 10:
            return f'Parabéns - Você acertou {acertos} questões'
        else:
            return f'Volte a estudar - Você acertou {acertos} questões'
    return render_template("examefinal.html")

#@app.route("/baseteste")
#def teste2():
#    return render_template("testebase.html")