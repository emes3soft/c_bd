
from . import cria_chamada_ficheiros, teste_pasta_static, apresenta_caixa_mensagens, app
from .connector.conexao import CONEXAO as C, conectar


def init_bd(criar_chamada_ficheiros: bool = False):
    """
        Início da módulo/libraria de base de dados
    """
    if not app:
        apresenta_caixa_mensagens(texto_mensagem="Aplicação flask não iniciada")
        return False

    # Para criar chamada dos ficheiros css e js na masterpage
    cria_chamada_ficheiros()

    # Teste da pasta c_bd dentro da pasta static do projeto
    teste_pasta_static()
    
    nova_bd = BASE_DADOS(app, conectar())
    return nova_bd

class BASE_DADOS:
    app = None
    con : C = None
    comandos = []
    # mensagens = []

    def __init__(self, aplicacao, conexao, comandos=[]):
        self.app = aplicacao
        self.con = conexao
        self.comandos = comandos

    def __exit__(self):
        self.__limpa_infos__()
        if self.con.conexao.is_connected():
            self.con.conexao.close()

    def __limpa_infos__ (self):
        b = self.__init__()
        self = b
