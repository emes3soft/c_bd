CHAVE = [
    b'2ecBhTPtPVPg8gz8',
    b'A3dT2cFcV6Zdko0U',
    b'NevVsNaIorcrZzOZ',
    b'9i7d9vri9GCc0Qec',
    b'8qppuuDRHxAhrzGJ',
    b'ejTvyeFjtwRspLbk',
    b'0FICIS0imbx63zmz',
    b'VVzuXxa8v6JIpPMJ',
    b'eBtjFQGIP7ifIXmT',
    b'l14X3dHXIDuzECu8',
]

FICHEIROS = {
    "base_dados": "bd.c_bd",
}

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

from . import fapp
from .constantes import PASTAS
from .mensagens.mensagem_popup import apresenta_caixa_mensagens, CAIXA_MENSAGENS
from .mensagens.mensagem import cria_mensagem
import os
import inspect as i

def encriptar_ficheiro(texto : str, ficheiro : str = FICHEIROS["base_dados"]):
    from random import randint

    pos = randint(0,9)
    codificacao = AES.new(CHAVE[pos], AES.MODE_CFB)

    ficheiro = os.path.join(PASTAS["static_c_bd_absoluta"], "ficheiros", FICHEIROS["base_dados"])

    if FICHEIROS.get(ficheiro):
        os.remove(ficheiro)

    # apresenta_caixa_mensagens(texto_mensagem=str(texto))
    texto = str(texto).encode()

    with open(ficheiro, "wb") as f:
        f.write(str(pos).encode())
        f.write(codificacao.iv)
        f.write(codificacao.encrypt(pad(texto, AES.block_size)))
    
    f.close()

    return True

def desencriptar_ficheiro(ficheiro:str):
    ficheiro = os.path.join(PASTAS["static_c_bd_absoluta"], "ficheiros", ficheiro)

    if not os.path.exists(ficheiro):
        cria_mensagem(8000, f"{i.currentframe().f_code.co_filename.split('\\')[-1]} - {i.currentframe().f_code.co_name}", ficheiro)
        return False

    try:
        with open(ficheiro, "rb") as f:
            conteudo = f.read()
            f.close()
        
        if not conteudo:
            cria_mensagem(8002, f"{i.currentframe().f_code.co_filename.split('\\')[-1]} - {i.currentframe().f_code.co_name}")
            return False
        
        with open(ficheiro, "rb") as f:
            pos = int(f.read(1).decode())
            iv = f.read(16)
            texto = f.read()
            f.close()
        
        if len(str(pos)) == 0 or len(str(iv)) == 0 or len(str(texto)) == 0:
            cria_mensagem(8003, f"{i.currentframe().f_code.co_filename.split('\\')[-1]} - {i.currentframe().f_code.co_name}")
            return False

    except IOError:
        return False
    except:
        return False

    codificacao = AES.new(CHAVE[pos], AES.MODE_CFB, iv=iv)

    texto_ = unpad(codificacao.decrypt(texto), AES.block_size)

    return texto_.decode('utf-8')

def encriptar_texto(texto : str):
    from random import randint
    from base64 import b64encode
    from flask import json

    pos = randint(0,9)
    codificacao = AES.new(CHAVE[pos], AES.MODE_CFB)

    if texto is None:
        return False
    
    texto = texto.encode()

    txt_cod = codificacao.encrypt(pad(texto, AES.block_size))
    # apresenta_caixa_mensagens(texto_mensagem=f"IV: {codificacao.iv}\nEncriptar: {str(txt_cod)}")

    # encoded_cipher_text = b64encode(str(pos) + codificacao.iv + txt_cod)
    texto_codificado = b64encode(str([pos, str(codificacao.iv), str(txt_cod)]).encode())
    # apresenta_caixa_mensagens(texto_mensagem=f"Encriptar: {texto_codificado}")
    
    return str(texto_codificado)

def desencriptar_texto(texto : str):
    if texto is None:
        return False

    from base64 import b64decode
    from flask import json

    texto = json.loads(str(b64decode(eval(texto)), 'utf-8'))
    pos = texto[0]
    iv = texto[1]
    txt = texto[2]

    codificacao = AES.new(CHAVE[pos], AES.MODE_CFB, iv=eval(iv))

    texto_ = unpad(codificacao.decrypt(eval(txt)), AES.block_size).decode()

    # apresenta_caixa_mensagens(texto_mensagem=f"Mensagem desencriptada: {str(texto_)}")

    return texto_
