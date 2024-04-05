from flask import render_template, current_app as app
from .constantes import PAGINA_WEB as wp

@app.route('/<erro>', methods=['GET'])
def raiz(erro = None):
    txt_erro = ["Desconhecido", "Reporte o erro ao desenvolvedor do projeto Emes3Soft através do formulário"]
    
    if erro:
        erro = int(erro)
        if isinstance(erro, int):
            match erro:
                case 404:
                    txt_erro = ["Página não encontrada", "O endereço introduzido não existe! Verifique a ligação!"]
                case 500:
                    txt_erro = ["Acesso ilegítimo", "O endereço introduzido não permite o seu acesso!"]
                case 600:
                    txt_erro = ["Problema de sistema", "O sistema encontrou um erro que faz com que o sistema não possa funcionar corretamente! Contacte o administrador do sistema através do email: administrador@emes3soft.pt"]
                case 610:
                    txt_erro = ["Ligação indisponível", "A ligação para mudança de palavra-passe não está disponível! Possivelmente existe algum erro na ligação, a ligação já foi utilizada ou deixou de estar disponível por ultrapassar o tempo limite."]
                case _:
                    txt_erro = ["Erro não identificado", "Envie um descrição do erro para o email administrador@emes3soft.pt"]

    return render_template("erros.html", cod=erro, titulo="ERRO", err_titulo=txt_erro[0], err_descricao=txt_erro[1])

@app.route("/sem_acesso")
def sem_acesso():
    return render_template('sem_acesso.html', titulo="ERRO")

@app.route("/sem_app")
def sem_acesso():
    return wp.format(640, "Aplicação Flask", "Aplicação flask não iniciada")