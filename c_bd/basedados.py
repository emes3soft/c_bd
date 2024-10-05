from . import fapp
from .constantes import PASTAS, FICHEIROS_NECESSARIOS
from .conexao import CONEXAO as C, conectar
from .mensagens.mensagem import cria_mensagem
from .mensagens.mensagem_popup import apresenta_caixa_mensagens
from .ligacao import LIGACAO

import inspect as i
from os import mkdir, path
import zipfile
import shutil 
    
def cria_chamada_ficheiros():
    # from typing import Any, Dict, List, Optional, Sequence, Tuple, Union, ValuesView

    from .constantes import CHAMADA_FICHEIROS_HEAD
    
    str_f = ""
    for f in CHAMADA_FICHEIROS_HEAD:
        str_f += f
    
    fapp.config['CHAMADA_FICHEIROS_HEAD'] = str_f

    from .constantes import CHAMADA_FICHEIROS_BODY_INICIO
    
    str_f = ""
    for f in CHAMADA_FICHEIROS_BODY_INICIO:
        str_f += f
    
    fapp.config['CHAMADA_FICHEIROS_BODY_INICIO'] = str_f

    from .constantes import CHAMADA_FICHEIROS_BODY_FIM
    
    str_f = ""
    for f in CHAMADA_FICHEIROS_BODY_FIM:
        str_f += f
    
    fapp.config['CHAMADA_FICHEIROS_BODY_FIM'] = str_f

    # Adicionar o modals.html como var ao projeto
    fapp.config['FICHEIRO_MODALS_PROPRIETARIO'] = PASTAS["static_c_bd_absoluta"] + "/html/modals.html"

def __isdir(z, name):
    return any(x.startswith("%s/" % name.rstrip("/")) for x in z.namelist())

def teste_pasta_static():
    extrair = 0

    # apresenta_caixa_mensagens(texto_mensagem=PASTAS["static_absoluta"])
    # Teste à pasta static do projeto
    if not path.exists(PASTAS["static_absoluta"]):
        mkdir(PASTAS["static_absoluta"])
        extrair = 1
    else:
        # Teste à pasta c_bd dentro da pasta static do projeto
        if not path.exists(PASTAS["static_c_bd_absoluta"]):
            extrair = 2
        else:
            # Teste a todos os ficheiros necessário para a importação
            for c in FICHEIROS_NECESSARIOS:
                transforma_caminho = FICHEIROS_NECESSARIOS[c]
                # apresenta_caixa_mensagens(texto_mensagem=f"As 4 primeiras letras: {FICHEIROS_NECESSARIOS[c][:4].upper()}")
                if not path.exists(PASTAS["projeto"] + f"{transforma_caminho}") and FICHEIROS_NECESSARIOS[c][:4].upper() != "HTTP":
                    shutil.rmtree(PASTAS["static_c_bd_absoluta"])
                    extrair = PASTAS["projeto"] + f"{transforma_caminho}"
                    break
    
    # apresenta_caixa_mensagens(texto_mensagem=f"Extrair ficheiros: {extrair}")
    if extrair != 0:
        cam_zip = path.join(PASTAS["absoluta_ficheiro"],"assets.zip")
        from .constantes import PASTA_GERAL_PROJETO, PASTA_ASSETS

        try:
            with zipfile.ZipFile(cam_zip, 'r') as zip_ref:
                zip_ref.extractall(PASTAS["static_absoluta"])
                
                if __isdir(zip_ref, PASTA_ASSETS):
                    if path.exists(path.join(PASTAS["static_absoluta"], PASTA_ASSETS)):
                        shutil.move(path.join(PASTAS["static_absoluta"], PASTA_ASSETS),
                            path.join(PASTAS["static_absoluta"], PASTA_GERAL_PROJETO))

        except zipfile.BadZipFile:
            from .mensagens.mensagem import cria_mensagem, MENSAGENS
            mensagem = MENSAGENS(codigo_mensagem="X00001", titulo_mensagem="FICHEIRO ZIP",
                texto_mensagem="O ficheiro ZIP com os assets com problemas!")
            cria_mensagem(mensagem)
            
def init_bd(ligacao : LIGACAO = None):
    """
        Início da módulo/libraria de base de dados\n
        \tligação: deve especificar uma ligação caso não tenha uma definida no config com o nome CFG_CLASS_BD\n
        No caso de pertender efetuar uma nova ligação chame a class LIGACAO em .connector.ligacao
    """
    if not fapp:
        cria_mensagem(2023, f"{i.stack()[1][3].upper()}")
        return False
    
    if not ligacao is None and not isinstance(ligacao, dict):
        cria_mensagem(1002, f"{i.stack()[1][3].upper()}")
        return False

    # Para criar chamada dos ficheiros css e js na masterpage
    cria_chamada_ficheiros()

    # Teste da pasta c_bd dentro da pasta static do projeto
    teste_pasta_static()
    
    nova_bd = BASE_DADOS(fapp, conectar(ligacao))
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
