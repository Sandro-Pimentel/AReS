from flask import Flask, render_template, request

app = Flask('__name__')

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/conteudo1")
def conteudo1():
    return render_template("conteudo1.html")

@app.route("/conteudo2")
def conteudo2():
    return render_template("conteudo2.html")

@app.route("/conteudo3")
def conteudo3():
    return render_template("conteudo3.html")

@app.route("/conteudo4")
def conteudo4():
    return render_template("conteudo4.html")

# @app.route("/examefinal")
# def examefinal():
#    return render_template("examefinal.html")

@app.route("/fracasso")
def fracasso():
    return render_template("fracasso.html")

@app.route("/sucesso")
def sucesso():
    return render_template("sucesso.html")

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
            return render_template("sucesso.html", acertos=acertos)
        else:
            return render_template("fracasso.html", acertos=acertos)
    return render_template("examefinal.html")

