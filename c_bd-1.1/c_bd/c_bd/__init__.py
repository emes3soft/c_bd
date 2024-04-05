# from flask import Flask
from flask import current_app as app
# from .mensagens import mensagem
from .mensagens.mensagem_popup import apresenta_caixa_mensagens
from .constantes import FICHEIROS_NECESSARIOS
from os import mkdir
import pathlib
import os.path as path
import zipfile
import shutil 

# app = Flask(__name__)

def cria_chamada_ficheiros():
    # from typing import Any, Dict, List, Optional, Sequence, Tuple, Union, ValuesView

    from .constantes import CHAMADA_FICHEIROS_HEAD
    
    str_f = ""
    for f in CHAMADA_FICHEIROS_HEAD:
        str_f += f
    
    app.config['CHAMADA_FICHEIROS_HEAD'] = str_f

    from .constantes import CHAMADA_FICHEIROS_BODY_INICIO
    
    str_f = ""
    for f in CHAMADA_FICHEIROS_BODY_INICIO:
        str_f += f
    
    app.config['CHAMADA_FICHEIROS_BODY_INICIO'] = str_f

    from .constantes import CHAMADA_FICHEIROS_BODY_FIM
    
    str_f = ""
    for f in CHAMADA_FICHEIROS_BODY_FIM:
        str_f += f
    
    app.config['CHAMADA_FICHEIROS_BODY_FIM'] = str_f

def teste_pasta_static():
    extrair = 0

    from .constantes import PASTAS
    
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
                transforma_caminho = FICHEIROS_NECESSARIOS[c].replace('/','\\')
                # apresenta_caixa_mensagens(texto_mensagem=f"As 4 primeiras letras: {FICHEIROS_NECESSARIOS[c][:4].upper()}")
                if not path.exists(PASTAS["projeto"] + f"{transforma_caminho}") and FICHEIROS_NECESSARIOS[c][:4].upper() != "HTTP":
                    shutil.rmtree(PASTAS["static_c_bd_absoluta"])
                    extrair = PASTAS["projeto"] + f"{transforma_caminho}"
                    break
    
    # apresenta_caixa_mensagens(texto_mensagem=f"Extrair ficheiros: {extrair}")
    if extrair != 0:
        cam_zip = f"{PASTAS["absoluta_ficheiro"]}\\assets.zip"
        with zipfile.ZipFile(cam_zip, 'r') as zip_ref:
            zip_ref.extractall(PASTAS["static_absoluta"])