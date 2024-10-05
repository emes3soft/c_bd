from tkinter import *
from tkinter import messagebox as msg

class CAIXA_MENSAGENS:
    informacao = 'i'
    erro = 'e'
    aviso = 'a'

def apresenta_caixa_mensagens(tipo_mensagem : CAIXA_MENSAGENS = CAIXA_MENSAGENS.informacao,
    titulo_mensagem : str = "", texto_mensagem : str = ""):
    root = Tk()
    root.wm_attributes("-topmost", 1)  # make sure top1 is on top to start
    root.withdraw()

    if not isinstance(titulo_mensagem, str):
        titulo_mensagem = str(titulo_mensagem)
    titulo_mensagem = titulo_mensagem.strip()

    if texto_mensagem is None:
        texto_mensagem = "None"
    if isinstance(texto_mensagem, list):
        texto_mensagem = str(texto_mensagem)
    elif isinstance(texto_mensagem, dict):
        texto_mensagem = str(texto_mensagem.__dict__.items())
    
    texto_mensagem = texto_mensagem.strip() if texto_mensagem else "Sem mensagem"

    match(tipo_mensagem):
        case CAIXA_MENSAGENS.informacao:
            msg.showinfo(titulo_mensagem if titulo_mensagem else f"Informação", texto_mensagem if texto_mensagem else "Sem texto de informação!")
        case CAIXA_MENSAGENS.erro:
            msg.showerror(titulo_mensagem if titulo_mensagem else "Erro", texto_mensagem if texto_mensagem else "Sem texto de erro!")
        case CAIXA_MENSAGENS.aviso:
            msg.showwarning(titulo_mensagem if titulo_mensagem else "Aviso", texto_mensagem if texto_mensagem else "Sem texto de aviso!")

    root.destroy()  # Close the main window
