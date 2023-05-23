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

@app.route("/exame1")
def exame1():
    return render_template("exame1.html")

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

@app.route("/exame2")
def exame2():
    return render_template("exame2.html")

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

@app.route("/exame3")
def exame3():
    return render_template("exame3.html")

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

@app.route("/exame4")
def exame4():
    return render_template("exame4.html")

@app.route("/probacklog")
def probacklog():
    return render_template("probacklog.html")

@app.route("/avaliacao", methods = ['GET', 'POST'])
def avaliacao():
    if request.method == 'POST':
        lista = ['dg1','dg2','dg3','de1','de2','de3']

        count, media1, media2 = 0, 0, 0
        for c in lista:
            nota = int(request.form.get(c))
            if count < 3:
                media1+= nota
            else:
                media2+= nota
            count+=1
        media1/=3
        media2/=3
        return render_template("avaliacao.html", media1 = media1, media2 = media2)

    return render_template("avaliacao.html")

@app.route("/fracasso")
def fracasso():
    return render_template("fracasso.html")

@app.route("/sucesso")
def sucesso():
    return render_template("sucesso.html")

@app.route("/kanban")
def kanban():
    return render_template("kanban.html")

@app.route("/planpok")
def planpok():   
    return render_template("planpok.html")

@app.route("/exame1", methods=['GET','POST'])
def teste1():
    if request.method == 'POST':
        questoes = '''qt1 qt2 qt3 qt4 qt5 qt6 qt7 qt8'''.split()
        acertos = 0
        for c in questoes:
            checkbox_value = request.form.get(c)
            if checkbox_value == None:
                return render_template("exame1.html")
            if checkbox_value == 'true':
                acertos+=1 
        if acertos >= 6:
            return render_template("sucesso.html", acertos=acertos)
        else:
            return render_template("fracasso.html", acertos=acertos)
    return render_template("exame1.html")

@app.route("/exame2", methods=['GET','POST'])
def teste2():
    if request.method == 'POST':
        questoes = '''qt1 qt2 qt3 qt4 qt5 qt6 qt7 qt8'''.split()
        acertos = 0
        for c in questoes:
            checkbox_value = request.form.get(c)
            if checkbox_value == None:
                return render_template("exame2.html")
            if checkbox_value == 'true':
                acertos+=1 
        if acertos >= 6:
            return render_template("sucesso.html", acertos=acertos)
        else:
            return render_template("fracasso.html", acertos=acertos)
    return render_template("exame2.html")

@app.route("/exame3", methods=['GET','POST'])
def teste3():
    if request.method == 'POST':
        questoes = '''qt1 qt2 qt3 qt4 qt5 qt6 qt7 qt8'''.split()
        acertos = 0
        for c in questoes:
            checkbox_value = request.form.get(c)
            if checkbox_value == None:
                return render_template("exame3.html")
            if checkbox_value == 'true':
                acertos+=1 
        if acertos >= 6:
            return render_template("sucesso.html", acertos=acertos)
        else:
            return render_template("fracasso.html", acertos=acertos)
    return render_template("exame3.html")

@app.route("/exame4", methods=['GET','POST'])
def teste4():
    if request.method == 'POST':
        questoes = '''qt1 qt2 qt3 qt4 qt5 qt6 qt7 qt82'''.split()
        acertos = 0
        for c in questoes:
            checkbox_value = request.form.get(c)
            if checkbox_value == None:
                return render_template("exame4.html")
            if checkbox_value == 'true':
                acertos+=1 
        if acertos >= 6:
            return render_template("sucesso.html", acertos=acertos)
        else:
            return render_template("fracasso.html", acertos=acertos)
    return render_template("exame4.html")

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

