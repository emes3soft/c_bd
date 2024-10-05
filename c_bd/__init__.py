from flask import current_app as fapp
from .basedados import init_bd


class APP_CBD:
    def __init__(self, dados_ligacao : dict = None):
        self.basedados = init_bd() if dados_ligacao is None else init_bd(dados_ligacao)
        
    def atualiza_conexao(self, dados_ligacao : dict = None):
        self.basedados = init_bd(dados_ligacao)
        
