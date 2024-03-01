# from flask import Flask
from flask import current_app as app
from .connector.conexao import CONEXAO as C, conectar
from .mensagens import mensagem
from .mensagens.mensagem_popup import apresenta_caixa_mensagens

import os.path as path

# app = Flask(__name__)

def init_bd():
    """
        Início da módulo/libraria de base de dados
    """
    # Acresentar os caminhos da pasta c_bd, do css, do js e da DataTable
    caminho = "/" + path.relpath(app.static_folder)
    apresenta_caixa_mensagens(texto_mensagem=caminho)
    if not app.config['C_BD_PASTA_CSS']: app.config['C_BD_PASTA_CSS'] = caminho + "/c_bd/css"
    if not app.config['C_BD_PASTA_JS']: app.config['C_BD_PASTA_JS'] = caminho + "/c_bd/js"
    if not app.config['C_BD_PASTA_DATATABLES']: app.config['C_BD_PASTA_DATATABLES'] = caminho + "/c_bd/DataTables"
    if not app.config['C_BD_PASTA_BOOTSTRAP']: app.config['C_BD_PASTA_BOOTSTRAP'] = caminho + "/c_bd/bootstrap532"
    
    nova_bd = BASE_DADOS
    nova_bd.con = conectar()
    return nova_bd

class BASE_DADOS:
    app = None
    con : C = None
    comandos = []
    # mensagens = []

    def __init__(self):
        self.app = app

    def __exit__(self):
        if self.con.conexao.is_connected():
            self.con.conexao.close()

    def __limpa_infos__ (self):
        b = self.__init__()
        self = b

