from flask import g
from .. import fapp
from .constantes import GERAIS as CG, TIPOS as CT, ESTILOS as CE, DETALHES as CD, MENSAGENS as CM
from .mensagem_popup import apresenta_caixa_mensagens
from multipledispatch import dispatch

class MENSAGENS:
    estilo : CE = None
    tipo = None
    codigo = None
    titulo = None
    texto = None
    duracao = None
    mensagem = None

    def __init__(self, estilo_mensagem : CE = CE.toast, tipo_mensagem = CT.erro, 
        codigo_mensagem : str = None, titulo_mensagem : str = None, texto_mensagem : str = None,
        duracao_mensagem : str = None):
        
        self.estilo = estilo_mensagem if isinstance(estilo_mensagem, CE) else CE.toast
        self.tipo = tipo_mensagem if isinstance(tipo_mensagem, CD) else CT.erro
        self.codigo = codigo_mensagem if isinstance(codigo_mensagem, str) else "0X0"
        self.titulo = titulo_mensagem if isinstance(titulo_mensagem, str) else ""
        self.texto = texto_mensagem if isinstance(texto_mensagem, str) else "Sem Mensagem"
        self.duracao = str(CG.duracao) if not str(duracao_mensagem).isnumeric() else (str(CG.duracao) if int(duracao_mensagem) < CG.duracao_minima else str(duracao_mensagem))
        self.mensagem = self.__cria_mensagem__()

    def __cria_mensagem__(self):
        nova_msg = None

        nova_msg = self.estilo

        nova_msg = nova_msg.replace("__classe__", self.tipo.classe)
        nova_msg = nova_msg.replace("__titulo__", self.tipo.titulo).replace("__comando__", self.titulo).replace("__codigo__", self.codigo)
        nova_msg = nova_msg.replace("__icon__", self.tipo.icon)
        nova_msg = nova_msg.replace("__mensagem__", self.texto)
        nova_msg = nova_msg.replace("__duracao__", self.duracao)
        
        return nova_msg

def tem_mensagens():
    """
        Devolve True se houver mensagens e False caso contrário
    """
    mensagens = getattr(g, '_mensagens', None)

    return mensagens is not None # and mensagens is not [] 

def devolve_mensagens():
    """
        Devolve as mensagens como texto (string)
    """
    mensagens = getattr(g, '_mensagens', None)

    if mensagens is None:
        mensagens = []

    mensagens = "".join(mensagens)

    setattr(g, '_mensagens', None)

    return mensagens

def __devolve_lista_mensagens():
    """
        Devolve as mensagens como lista (list)
    """
    mensagens = getattr(g, '_mensagens', None)

    if mensagens is None:
        mensagens = []

    return mensagens

@dispatch(MENSAGENS)
def cria_mensagem(mensagem = None):
    """
        Cria mensagem personalizada através da classe MENSAGENS\n
        \tDeve obdecer aos parametros da classe MENSAGENS
    """

    if not isinstance(mensagem, MENSAGENS):
        return False
    
    mgs = __devolve_lista_mensagens()
    mgs.append(mensagem.mensagem)

    setattr(g, '_mensagens', mgs)
    return True

@dispatch(int,str)
def cria_mensagem(codigo_mensagem : int = None, titulo : str = ""):
    """
        Cria mensagem apartir de uma existente na constante MENSAGENS\n
        \tcodigo_mensagem - código da mensagem existente nas constantes\n
        \ttitulo - definir o título para a mensagem\n
        \ttexto_a_adicionar - titulo extra a adicionar/incluir
    """
    if not isinstance(codigo_mensagem, int):
        return False

    msg = CM[str(codigo_mensagem)]

    if not CM[str(codigo_mensagem)]:
        return False
    
    if not isinstance(titulo, str):
        titulo = ""

    mgs = __devolve_lista_mensagens()

    nova = MENSAGENS(estilo_mensagem=msg[0], tipo_mensagem=msg[1], 
        codigo_mensagem=str(codigo_mensagem), texto_mensagem=msg[2],
        titulo_mensagem=titulo, duracao_mensagem=CG.duracao + (len(mgs) * CG.duracao_entre_mensagens))
    
    mgs.append(nova.mensagem)

    setattr(g, '_mensagens', mgs)

    return True

@dispatch(int,str, str)
def cria_mensagem(codigo_mensagem : int = None, titulo : str = "", texto_a_adicionar : str = ""):
    """
        Cria mensagem apartir de uma existente na constante MENSAGENS\n
        \tcodigo_mensagem - código da mensagem existente nas constantes\n
        \ttitulo - definir o título para a mensagem\n
        \ttexto_a_adicionar - titulo extra a adicionar/incluir
    """
    if not isinstance(codigo_mensagem, int):
        return False

    msg = CM[str(codigo_mensagem)]

    if not CM[str(codigo_mensagem)]:
        return False
    
    if not isinstance(titulo, str):
        titulo = ""
    
    texto_a_adicionar = "" if not texto_a_adicionar else str(texto_a_adicionar).strip()
    txt = [""]
    if texto_a_adicionar:
        txt = str(texto_a_adicionar).split(",")
        txt = [t.strip() for t in txt if t != ""]
    
    # apresenta_caixa_mensagens(texto_mensagem=f"Texto a adicionar: {str(txt)}")

    mgs = __devolve_lista_mensagens()
    
    nova = MENSAGENS(estilo_mensagem=msg[0], tipo_mensagem=msg[1], 
        codigo_mensagem=str(codigo_mensagem), texto_mensagem=msg[2] % tuple(txt) if len(txt) > 1 else txt[0],
        titulo_mensagem=titulo, duracao_mensagem=CG.duracao + (len(mgs) * CG.duracao_entre_mensagens))

    mgs.append(nova.mensagem)

    setattr(g, '_mensagens', mgs)

    return True