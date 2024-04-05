from flask import g, current_app as app
from .constantes import GERAIS as CG, TIPOS as CT, ESTILOS as CE, DETALHES as CD, MENSAGENS as CM
from .mensagem_popup import apresenta_caixa_mensagens
from multipledispatch import dispatch

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
        self.tipo = tipo_mensagem if isinstance(tipo_mensagem, CD) else CT.erro
        self.codigo = codigo_mensagem if isinstance(codigo_mensagem, str) else "0X0"
        self.titulo = titulo_mensagem if isinstance(titulo_mensagem, str) else ""
        self.texto = texto_mensagem if isinstance(texto_mensagem, str) else "Sem Mensagem"
        self.mensagem = self.__cria_mensagem__()

    def __cria_mensagem__(self):
        nova_msg = None

        nova_msg = self.estilo

        nova_msg = nova_msg.replace("__classe__", self.tipo.classe)
        nova_msg = nova_msg.replace("__titulo__", self.tipo.titulo).replace("__comando__", self.titulo).replace("__codigo__", self.codigo)
        nova_msg = nova_msg.replace("__icon__", self.tipo.icon)
        nova_msg = nova_msg.replace("__mensagem__", self.texto)
        nova_msg = nova_msg.replace("__duracao__", str(CG.duracao))
        
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

    # str_mensagem = ""
    
    # if mensagens: # and mensagens is not []:
    #     #for mensagem in mensagens:
    #     str_mensagem = mensagens

    # else:
    #     str_mensagem = "Sem mensagens"

    return mensagens

def devolve_lista_mensagens():
    """
        Devolve as mensagens como lista (list)
    """
    mensagens = getattr(g, '_mensagens', None)
    # apresenta_caixa_mensagens(texto_mensagem=str(mensagens))
    # menssagens = app.config.get('MENSAGENS_C_BD')
    if mensagens is None:
        mensagens = []

    return mensagens

@dispatch(MENSAGENS)
def cria_mensagem(mensagem = None):
    """
        Cria mensagem através da classe MENSAGENS\n
        Pernonalização da mensagem
    """
    if not isinstance(mensagem, MENSAGENS):
        return False

    # mensagens = devolve_lista_mensagens()
    # mensagens.append(mensagem.mensagem)

    setattr(g, '_mensagens', mensagem.mensagem)

    # app.config['MENSAGENS_C_BD'] = mensagens
    # apresenta_caixa_mensagens(texto_mensagem=str(app.config['MENSAGENS_C_BD']))
    return True

@dispatch(int,str)
def cria_mensagem(codigo_mensagem = None, titulo = ""):
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
    
    # mensagens = devolve_lista_mensagens()
    # mensagens.append(nova.mensagem)

    setattr(g, '_mensagens', nova.mensagem)

    # app.config['MENSAGENS_C_BD'] = mensagens
    return True

# def devolve_atributos_mensagem(lista_mensagens : list = None):
    
#     if not isinstance(lista_mensagens, list):
#         lista_mensagens = getattr(g, '_mensagens', None)

#     str_m : str = ""
#     if len(lista_mensagens) == 0:
#         str_m = "Sem mensagens!"
#     else:
#         for n, m in enumerate(lista_mensagens):
#             str_m += f"***** Posição: {n} *****\n"
#             str_vars : str = str(vars(m)).replace("{","").replace("}", "").split(", '")
#             for p in str_vars:
#                 t = p.replace("'","").split(":")
#                 str_m += f"--> {t[0].upper()} - {t[1]}\n"

#     return str_m