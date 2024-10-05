from .constantes import PAGINA_WEB as wp

def erros(erro = None):
    txt_erro = ["Desconhecido", "Reporte o erro ao desenvolvedor do projeto Emes3Soft através do formulário incluído na página principal"]
    
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

    return wp.format(erro, txt_erro[0], txt_erro[1])

def sem_acesso():
    return wp.format(650, "Acesso não permitido", "O utilizador não tem acesso ao endereço introduzido!")

def sem_app():
    return wp.format(640, "Aplicação Flask", "Aplicação flask não iniciada")