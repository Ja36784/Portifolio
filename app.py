from flask import Flask, render_template, redirect, request, flash
# envia email e capta a msg 
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
load_dotenv()
# variavel app que recebe o objeto Flask
app = Flask(__name__)

#criptografa transições externas do projeto
app.secret_key = "Ja30104015*"

#dicionario do config flask
mail_settings = {
    #
    "MAIL_SERVER": "smtp.gmail.com",
    # porta do email
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    #segurança
    "MAIL_USE_SSL": False,
    #nosso email
    "MAIL_USERNAME": os.getenv("EMAIL"),
    #nossa senha
    "MAIL_PASSWORD": os.getenv("SENHA")
}

#colocando configuração do email_settings dentro do app.config
app.config.update(mail_settings)

#instancia o objeto mail que vai enviar o email e recebe o app qu foi criado no flask(app = Flask(__name__))
mail = Mail(app)    

#organizar as informações do formulario HTML
class Contato:
    #inicializando as variaveis (objeto )que tem no HTML na sequencia
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

#rota principal
@app.route("/")
# fução index
def index():
    # renderiza template no index.html
    return render_template("index.html")

#rota de envio recebendo os metodos, Post do formulario para o servidor e o servidor fazer o envio do email
@app.route("/send", methods=["GET", "POST"])

#função de envio de email
def send():
    # só envia o email se requisição for igual a Post
    if request.method =="POST":
        #cria um formulario contato(objeto) que vai receber o objeto contato(classe)
        formContato = Contato(
            # manda requisição para a rota, enviando pelo post e o que tem dentro dos campos form do HTML(name), na mesma ordem
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )

        #mensagem
        msg = Message(
            # assunto
            subject = f'{formContato.nome} te enviou uma mensagem',
            # enviando
            sender = app.config.get("MAIL_USERNAME"),
            # recebido composto por array
            recipients=["jose.azarias78@gmail.com", app.config.get("MAIL_USERNAME")],
            # corpo do email
            body=f'''

            {formContato.nome} com o e-mail {formContato.email}, te enviou a seguinte mensagem:

            {formContato.mensagem}

            '''
        )
        # objeto mail com metodo send para enviar (msg), atraves do mail instanciado(mail = Mail(app))
        mail.send(msg)
        # depois do envio, retorna a mensagem enviada
        flash("Mensagem enviada com sucesso!")
    # retorna o redirecionamento da funcao def send() para rota principal atraves do ("/")
    return redirect("/")
#só roda o programa se name for igual a main
if __name__ == "__main__":
    #atualiza app sem precisar dar f5
    app.run(debug=True)
    