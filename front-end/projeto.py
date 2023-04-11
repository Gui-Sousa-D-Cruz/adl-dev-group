from flask import Flask, render_template

#chamada para iniciar o site
#criar a 1ª página do site
#route -> Caminho que vem depois do domínio, exemplo: alaimalmeida.com.br/projeto
app = Flask(__name__)

@app.route('/')
def home():  # função -> O que você quer exibir naquela página
    return render_template('home.html')

@app.route("/sistemas")
def sistemas():
    return render_template("sistemas.html")

@app.route("/cad_sistema")
def cad_sistema():
    return render_template("cad_sistema.html")

@app.route("/cad_perfil")
def cad_perfil():
    return render_template("cad_perfil.html")

@app.route("/cad_matriz_sod")
def cad_matriz_sod():
    return render_template("cad_matriz_sod.html")

@app.route("/cad_perfil_usuario")
def cad_perfil_usuario():
    return render_template("cad_perfil_usuario.html")

@app.route("/consul_sistema")
def consul_sistema():
    return render_template("consul_sistema.html")

@app.route("/consul_perfil")
def consul_perfil():
    return render_template("consul_perfil.html")

@app.route("/consul_matriz_sod")
def consul_matriz_sod():
    return render_template("consul_matriz_sod.html")

@app.route("/consul_perfil_usuario")
def consul_perfil_usuario():
    return render_template("consul_perfil_usuario.html")


# chamada para colocar o site no ar e rodar automaticamente a cada alteração
if __name__ == '__main__':
    app.run(debug=True)