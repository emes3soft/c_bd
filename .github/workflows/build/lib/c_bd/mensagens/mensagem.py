from flask import g
from .constantes import MENSAGENS as CM, TIPOS as CT, ESTILOS as CE
from typing import overload

class MENSAGENS:
    estilo : CE = None
    tipo = None
    codigo = None
    titulo = None
    texto = None
    mensagem = None

    def __init__(self, estilo_mensagem : CE = CE.toast, 
        tipo_mensagem = CT.erro, codigo_mensagem : str = None,
        titulo_mensagem : str = None, texto_mensagem : str = None):
        
        self.estilo = estilo_mensagem if isinstance(estilo_mensagem, CE) else CE.toast
        self.tipo = tipo_mensagem if isinstance(tipo_mensagem, CT) else CT.erro
        self.codigo = codigo_mensagem if isinstance(codigo_mensagem, str) else "0X0"
        self.titulo = titulo_mensagem if isinstance(titulo_mensagem, str) else ""
        self.texto = texto_mensagem if isinstance(texto_mensagem) else "Sem Mensagem"
        self.mensagem = self.__cria_mensagem__()

    def __cria_mensagem__(self):
        nova_msg = None

        nova_msg = self.estilo

        nova_msg = nova_msg.replace("__classe__", self.tipo.classe)
        nova_msg = nova_msg.replace("__titulo__", self.tipo.titulo).replace("__comando__", self.titulo).replace("__codigo__", self.codigo)
        nova_msg = nova_msg.replace("__icon__", self.tipo.icon)
        nova_msg = nova_msg.replace("__mensagem__", self.texto)
        nova_msg = nova_msg.replace("__duracao__", str(CM.duracao))
        
        return nova_msg

def devolve_lista_mensagens():
    messages = getattr(g, '_mensagens', None)
    if messages is None:
        g._mensagens = []

    return g._mensagens

@overload
def cria_mensagem(mensagem : MENSAGENS = None):
    """
        Cria mensagem através da classe MENSAGENS\n
        Pernonalização da mensagem
    """
    if not isinstance(mensagem, MENSAGENS):
        return False

    mensagens = devolve_lista_mensagens()
    mensagens.append(mensagem.mensagem)

    setattr(g, '_mensagens', mensagens)
    return True

@overload
def cria_mensagem(codigo_mensagem : int = None, titulo : str = ""):
    """
        Cria mensagem apartir de uma existente na constante MENSAGENS\n
        Basta indicar o código da mensagem
    """
    if not isinstance(codigo_mensagem, int):
        return False

    msg = CM[str(codigo_mensagem)]

    if not CM[str(codigo_mensagem)]:
        return False
    
    if not isinstance(titulo, str):
        titulo = ""
    
    nova = MENSAGENS(estilo_mensagem=msg[0], tipo_mensagem=msg[1], 
        codigo_mensagem=str(codigo_mensagem), texto_mensagem=msg[2],
        titulo_mensagem=titulo)
    
    mensagens = devolve_lista_mensagens()
    mensagens.append(nova)

    setattr(g, '_mensagens', mensagens)
    return True

def tem_mensagens():
    menssages = getattr(g, '_mensagens', None)

    return not menssages is []
