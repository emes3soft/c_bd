from jinja2 import FileSystemLoader
from markupsafe import Markup
from flask import current_app
from os.path import join, isfile
from .constantes import MODAL as MD
from .botoes import BOTOES_FORMULARIO as BF
from ..mensagens.mensagem_popup import apresenta_caixa_mensagens

class MODAL:
    id_nome : str = None
    classes : str = None
    tamanho = MD.TAMANHO.normal
    titulo : str = None

class MODAL_FORMULARIO:
    id_nome : str = None
    classes : str = None
    tamanho = MD.TAMANHO.normal
    titulo : str = None
    formulario_nome : str = None
    formulario_ligacao : str = None
    modal_body : str = None
    modal_footer : str = None

class MODAL_PROPRIETARIO:
    html : str = None

    def __init__(self):
        ficheiro = join(current_app.static_folder,"c_bd","html","modals.html")

        if not isfile(ficheiro):
            print ("************* Não foi encontrado o ficheiro modals.html *************")
        else:
        #     pasta_cbd_html = str(join(current_app.static_folder,"c_bd","html")).replace("\\", "\\\\")
        #     apresenta_caixa_mensagens(texto_mensagem=f"Carregada a pasta {pasta_cbd_html}")
        #     FileSystemLoader([current_app.template_folder, pasta_cbd_html])
        
            with open(ficheiro) as file:
                self.html = Markup(file.read()).unescape()
            # apresenta_caixa_mensagens(texto_mensagem=self.html)