from flask import Flask, render_template, request

app = Flask('__name__')

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/definicoes")
def definicoes():
    return render_template("definicoes.html")

@app.route("/pilares")
def pilares():
    return render_template("pilares.html")

@app.route("/papeis")
def papeis():
    return render_template("papeis.html")

@app.route("/po")
def po():
    return render_template("po.html")

@app.route("/sm")
def sm():
    return render_template("sm.html")

@app.route("/dt")
def dt():
    return render_template("dt.html")

@app.route("/eventos")
def eventos():
    return render_template("eventos.html")

@app.route("/sprintplan")
def sprintplan():
    return render_template("sprintplan.html")

@app.route("/daily")
def daily():
    return render_template("daily.html")

@app.route("/sprev")
def sprev():
    return render_template("sprintrev.html")


@app.route("/spret")
def spret():
    return render_template("sprintret.html")


@app.route("/replame")
def replame():
    return render_template("relplamee.html")

@app.route("/dorxdod")
def dorxdod():
    return render_template("dorxdod.html")

@app.route("/sprintback")
def sprintback():
    return render_template("sprintback.html")

@app.route("/productinc")
def productinc():
    return render_template("productinc.html")
    
@app.route("/burndown")
def burndown():
    return render_template("burndown.html")

@app.route("/productbacklog")
def probacklog():
    return render_template("probacklog.html")

@app.route("/avaliacao")
def avaliacao():
    return render_template("avaliacao.html")

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

@app.route("/mvp")
def mvp():
    return render_template("mvp.html")

@app.route("/softskills")
def softskills():
    return render_template("softskills.html")
