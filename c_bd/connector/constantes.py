from flask import current_app as app

class LIGACAO:
    app = app
    nome_variavel_configuracao = "CFG_CLASS_BD"

    class DADOS_LIGACAO:
        servidor = "localhost"
        porta = "3306"
        utilizador = None
        palavra_passe = None
        base_dados = None
        auto_atualizacao = False
