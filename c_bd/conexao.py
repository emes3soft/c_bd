from . import fapp
from .ligacao import LIGACAO as L, criar_ligacao
from .mensagens import constantes as MC
from .mensagens.mensagem import cria_mensagem, CM, MENSAGENS as M
from .mensagens.mensagem_popup import apresenta_caixa_mensagens

import mysql.connector as m
import inspect as i

def conectar(ligacao : L = None):
    """
        Conetar à base de dados segundo uma configuração\n
        . ignorar a variável configuracao - vai buscar os dados ao config da app e à variável CFG_CLASSE_BD (recomendado)\n
        . ao instroduzir os dados de configuração, tem de criar um dicionário com as variáveis obrigatórias database, user e password
    """

    c = CONEXAO()

    if isinstance(ligacao, dict):
        c.ligacao = ligacao
    else:
        c.ligacao = criar_ligacao()

    if not fapp:
        c.conetado = False
        cria_mensagem(1004, f"{i.currentframe().f_code.co_filename.split('\\')[-1]} - {i.currentframe().f_code.co_name}")
        return False
        
    if not c.ligacao:
        cria_mensagem(1002, f"{i.currentframe().f_code.co_filename.split('\\')[-1]} - {i.currentframe().f_code.co_name}")
        return False

    try:
        c.conexao = m.connect(**c.ligacao)

        if not c.conexao.is_connected():
            c.conetado = False
            cria_mensagem(1000, f"{i.currentframe()} - {c.__class__.__name__}")
        else:
            c.conetado = True
            c.cursor = c.conexao.cursor(dictionary=True) if c.nome_campos else c.conexao.cursor()

    except m.Error as err:
        c.conetado = False
        cod_msg = str(err.errno)
        nova_msg = M(tipo_mensagem=MC.TIPOS.erro,
            codigo_mensagem=cod_msg, titulo_mensagem=f"{i.currentframe()} - {c.__class__.__name__}",
            texto_mensagem=err.msg)
        cria_mensagem(nova_msg)

    return c

class CONEXAO:
    ligacao : L = None
    autocommit : bool = False
    conetado : bool = False
    conexao : object = None
    cursor : object = None
    nome_campos : bool = True

    def __init__(self, nomes_campos : bool = True):
        self.ligacao = None
        self.conetado = False
        self.conexao  = None
        self.cursor = None
        self.nomes_campos = nomes_campos

def limpar_conexao():
    c = CONEXAO()
    return c