import tkinter as tk
from tkinter import messagebox as msg

class CAIXA_MENSAGENS:
    informacao = 'i'
    erro = 'e'
    aviso = 'a'

def apresenta_caixa_mensagens(tipo_mensagem : CAIXA_MENSAGENS = CAIXA_MENSAGENS.informacao,
    titulo_mensagem : str = "", texto_mensagem : str = ""):
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    titulo_mensagem = titulo_mensagem.strip()
    if not texto_mensagem:
        texto_mensagem = "Sem mensagem!"
    else:
        texto_mensagem = texto_mensagem.strip()

    match(tipo_mensagem):
        case CAIXA_MENSAGENS.informacao:
            msg.showinfo(titulo_mensagem if titulo_mensagem else "Informação", texto_mensagem if texto_mensagem else "Sem texto de informação!")
        case CAIXA_MENSAGENS.erro:
            msg.showerror(titulo_mensagem if titulo_mensagem else "Erro", texto_mensagem if texto_mensagem else "Sem texto de erro!")
        case CAIXA_MENSAGENS.aviso:
            msg.showwarning(titulo_mensagem if titulo_mensagem else "Aviso", texto_mensagem if texto_mensagem else "Sem texto de aviso!")
    
    root.destroy()  # Close the main window
