from . import fapp
from multipledispatch import dispatch
from .mensagens.mensagem import cria_mensagem
from .mensagens.mensagem_popup import apresenta_caixa_mensagens
import inspect as i

def criar_ligacao(dados_ligacao : dict = None):
    """
        Cria uma ligação com os dados:\n
            . importados da variável no config da app CFG_CLASS_BD\n
            . criados através da classe LIGACAO
    """

    l = None
    if fapp.config.get(LIGACAO.nome_variavel_configuracao):
        l = LIGACAO.DADOS_LIGACAO(fapp.config[LIGACAO.nome_variavel_configuracao]).devolve_dicionario()
    elif not dados_ligacao:
        from .criptografia import desencriptar_ficheiro, FICHEIROS
        from flask import json

        texto_devolucao=desencriptar_ficheiro(FICHEIROS["base_dados"])

        if isinstance(texto_devolucao, bool):
            return l

        txt = json.loads(texto_devolucao.replace("'", '"').replace("False","false").replace("True","True"))
        
        if isinstance(txt, dict):
            l = LIGACAO.DADOS_LIGACAO(txt).devolve_dicionario()
    elif isinstance(dados_ligacao, dict):
        l = LIGACAO.DADOS_LIGACAO(dados_ligacao).devolve_dicionario()

    return l

class LIGACAO:
    nome_variavel_configuracao = "CBD_DADOS_LIGACAO"

    class DADOS_LIGACAO:
        server = "localhost"
        port = "3306"
        user = None
        password = None
        database = None
        auto_commit = False

        @dispatch(str, str, str, str, str, bool)
        def __init__(self, servidor : str = "127.0.0.1", porta : str = "3306", basedados : str = None, 
            utilizador : str = None, palavrapasse : str = None, auto_atualizar : bool = False):

            self.host = servidor
            self.port = porta
            self.database = basedados
            self.user = utilizador
            self.password = palavrapasse
            self.autocommit = auto_atualizar


        @dispatch(dict)
        def __init__(self, dicionario_dados : dict = {}):

            self.host = dicionario_dados["host"]
            self.port = dicionario_dados["port"]
            self.database = dicionario_dados["database"]
            self.user = dicionario_dados["user"]
            self.password = dicionario_dados["password"]
            self.autocommit = dicionario_dados["autocommit"]

        
        def devolve_dicionario(self):
            return vars(self)