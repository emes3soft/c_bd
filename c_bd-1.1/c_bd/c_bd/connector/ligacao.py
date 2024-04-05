from .constantes import LIGACAO as L
from ..mensagens.mensagem import cria_mensagem
from ..mensagens.mensagem_popup import apresenta_caixa_mensagens
import inspect as i

def criar_ligacao(dados_ligacao : L.DADOS_LIGACAO = None):
    """
        Cria uma ligação com os dados:\n
            . importados da variável no config da app CFG_CLASS_BD\n
            . criados através da classe LIGACAO
    """
    l = None
    if L.app.config.get(L.nome_variavel_configuracao):
        l = LIGACAO(L.app.config[L.nome_variavel_configuracao])
    elif not dados_ligacao:
        l = None
    else:
        l = LIGACAO(dados_ligacao)
    return l

class LIGACAO:
    dicionario = None

    def __init__(self, ligacao : L.DADOS_LIGACAO = None):
        if L.app.config.get(L.nome_variavel_configuracao):
            self.dicionario = L.app.config[L.nome_variavel_configuracao]
        else:
            self.dicionario = self.valores_dicionario(ligacao)

    def valores_dicionario(self, valores : L.DADOS_LIGACAO):
        return {
            "host" : valores["servidor"],
            "port" : valores["porta"],
            "user": valores["utilizador"],
            "password": valores["palavra_passe"],
            "database": valores["base_dados"],
            "autocommit": valores["auto_atualizacao"]
        }