from .constantes import BOTOES, MODAL, PREDEFINICOES as PRED

btpv = BOTOES.BOTOES_TIPO_PASSAGEM_VARIAVEIS

class BOTOES_TABELA:
    class BOTAO_ADICIONAR:
        cores : str = None
        classes : str = BOTOES.separador
        hiperligacao : str = "#"
        tipo_passagem : str = None
        passagem_variaveis : str = None
        modal : bool = None
        tamanho = BOTOES.tamanho
        icon : str = ""
        texto : str = ""
        botao : str = None

        def __init__(self, hiperligacao = "#", tipo_passagem_variaveis = btpv.url, passagem_variaveis = None, modal = False, 
            cor_fundo = None, cor_letra = None, classes = None, tamanho = None, icon = None, texto = None):

            self.hiperligacao = hiperligacao
            self.tipo_passagem = btpv.url if not not isinstance(tipo_passagem_variaveis, btpv) else tipo_passagem_variaveis
            self.passagem_variaveis = "" if not passagem_variaveis else passagem_variaveis
            self.modal = "" if not isinstance(modal, str) else modal
            self.cor_fundo = cor_fundo if cor_fundo else f"{BOTOES.cor_fundo}"
            self.cor_letra = cor_letra if cor_letra else "text-bg-primary"
            self.classes = classes if classes else ""
            self.tamanho = tamanho if tamanho else BOTOES.tamanho
            if isinstance(icon, int):
                self.icon = BOTOES.icons_adicionar[str(icon)] if icon in [1,2,3] else BOTOES.icons_adicionar["1"]
            elif isinstance(icon, str) and icon.isnumeric():
                icon = int(icon)
                self.icon = BOTOES.icons_adicionar[str(icon)] if icon in [1,2,3] else BOTOES.icons_adicionar["1"]
            else:
                self.icon = icon if icon else BOTOES.icons_adicionar["1"]
            self.texto = texto if texto else "Adicionar"
            
            self.icon = self.icon.format(f" {self.cor_letra} {self.tamanho} {self.cor_fundo}")

            self.botao = BOTOES.botao_html.format(BOTOES.tooltip, f"{BOTOES.separador} {self.classes}", self.hiperligacao, 
                self.tipo_passagem, self.passagem_variaveis, self.modal, self.texto, self.icon).replace("'", "|")

    class BOTAO_EDITAR:
        cor_fundo : str = None
        cor_letra : str = None
        classes : str = BOTOES.separador
        hiperligacao : str = "#"
        tipo_passagem : str = None
        passagem_variaveis : str = None
        modal : str = None
        tamanho = BOTOES.tamanho
        icon : str = ""
        texto : str = ""
        botao : str = None

        def __init__(self, hiperligacao = "#", tipo_passagem_variaveis = btpv.url, passagem_variaveis = None, modal = None, 
            cor_fundo = None, cor_letra = None, classes = None, tamanho = None, icon = None, texto = None):

            self.hiperligacao = hiperligacao
            self.tipo_passagem = btpv.url if not not isinstance(tipo_passagem_variaveis, btpv) else tipo_passagem_variaveis
            self.passagem_variaveis = "" if not passagem_variaveis else passagem_variaveis
            self.modal = "" if not isinstance(modal, str) else modal
            self.cor_fundo = cor_fundo if cor_fundo else f"{BOTOES.cor_fundo}"
            self.cor_letra = cor_letra if cor_letra else "text-warning"
            self.classes = classes if classes else ""
            self.tamanho = tamanho if tamanho else BOTOES.tamanho
            if isinstance(icon, int):
                self.icon = BOTOES.icons_editar[str(icon)] if icon in [1,2,3] else BOTOES.icons_editar["1"]
            elif isinstance(icon, str) and icon.isnumeric():
                icon = int(icon)
                self.icon = BOTOES.icons_editar[str(icon)] if icon in [1,2,3] else BOTOES.icons_editar["1"]
            else:
                self.icon = icon if icon else BOTOES.icons_editar["1"]
            self.texto = texto if texto else "Editar"
            
            self.icon = self.icon.format(f" {self.cor_letra} {self.tamanho} {self.cor_fundo}")

            self.botao = BOTOES.botao_html.format(BOTOES.tooltip, f"{BOTOES.separador} {self.classes}", self.hiperligacao, 
                self.tipo_passagem, self.passagem_variaveis, self.modal, self.texto, self.icon).replace("'", "|")

    class BOTAO_ELIMINAR:
        cor_fundo : str = None
        cor_letra : str = None
        classes : str = BOTOES.separador
        hiperligacao : str = "#"
        tipo_passagem : str = None
        passagem_variaveis : str = None
        modal : str = None
        tamanho = BOTOES.tamanho
        icon : str = ""
        texto : str = ""
        botao : str = None

        def __init__(self, hiperligacao = "#", tipo_passagem_variaveis = btpv.url, passagem_variaveis = None, modal = None, 
            cor_fundo = None, cor_letra = None, classes = None, tamanho = None, icon = None, texto = None):

            self.hiperligacao = hiperligacao
            self.tipo_passagem = btpv.url if not not isinstance(tipo_passagem_variaveis, btpv) else tipo_passagem_variaveis
            self.passagem_variaveis = "" if not passagem_variaveis else passagem_variaveis
            self.modal = "" if not isinstance(modal, str) else modal
            self.cor_fundo = cor_fundo if cor_fundo else f"{BOTOES.cor_fundo}"
            self.cor_letra = cor_letra if cor_letra else "text-danger"
            self.classes = classes if classes else ""
            self.tamanho = tamanho if tamanho else BOTOES.tamanho
            if isinstance(icon, int):
                self.icon = BOTOES.icons_eliminar[str(icon)] if icon in [1,2,3] else BOTOES.icons_eliminar["1"]
            elif isinstance(icon, str) and icon.isnumeric():
                icon = int(icon)
                self.icon = BOTOES.icons_eliminar[str(icon)] if icon in [1,2,3] else BOTOES.icons_eliminar["1"]
            else:
                self.icon = icon if icon else BOTOES.icons_eliminar["1"]
            self.texto = texto if texto else "Eliminar"
            
            self.icon = self.icon.format(f" {self.cor_letra} {self.tamanho} {self.cor_fundo}")
            
            self.botao = BOTOES.botao_html.format(BOTOES.tooltip, f"{BOTOES.separador} {self.classes}", self.hiperligacao, 
                self.tipo_passagem, self.passagem_variaveis, self.modal, self.texto, self.icon).replace("'", "|")

    class BOTAO_VISUALIZAR:
        cor_fundo : str = None
        cor_letra : str = None
        classes : str = BOTOES.separador
        hiperligacao : str = "#"
        tipo_passagem : str = None
        passagem_variaveis : str = None
        modal : str = None
        tamanho = BOTOES.tamanho
        icon : str = ""
        texto : str = ""
        botao : str = None

        def __init__(self, hiperligacao = "#", tipo_passagem_variaveis = btpv.url, passagem_variaveis = None, modal = None, 
            cor_fundo = None, cor_letra = None, classes = None, tamanho = None, icon = None, texto = None):
            
            self.hiperligacao = hiperligacao
            self.tipo_passagem = btpv.url if not not isinstance(tipo_passagem_variaveis, btpv) else tipo_passagem_variaveis
            self.passagem_variaveis = "" if not passagem_variaveis else passagem_variaveis
            self.modal = "" if not isinstance(modal, str) else modal
            self.cor_fundo = cor_fundo if cor_fundo else f"{BOTOES.cor_fundo}"
            self.cor_letra = cor_letra if cor_letra else "text-success"
            self.classes = classes if classes else ""
            self.tamanho = tamanho if tamanho else BOTOES.tamanho
            if isinstance(icon, int):
                self.icon = BOTOES.icons_visualizar[str(icon)] if icon in [1,2,3] else BOTOES.icons_visualizar["1"]
            elif isinstance(icon, str) and icon.isnumeric():
                icon = int(icon)
                self.icon = BOTOES.icons_visualizar[str(icon)] if icon in [1,2,3] else BOTOES.icons_visualizar["1"]
            else:
                self.icon = icon if icon else BOTOES.icons_visualizar["1"]

            self.texto = " " + texto if texto else "Visualizar"
            
            self.icon = self.icon.format(f" {self.cor_letra} {self.tamanho} {self.cor_fundo}")

            self.botao = BOTOES.botao_html.format(BOTOES.tooltip, f"{BOTOES.separador} {self.classes}", self.hiperligacao, 
                self.tipo_passagem, self.passagem_variaveis, self.modal, self.texto, self.icon).replace("'", "|")

    class BOTAO_PERSONALIZADO:
        cor_fundo : str = ""
        cor_letra : str = ""
        classes :str = BOTOES.separador
        hiperligacao : str = None
        tipo_passagem : str = None
        passagem_variaveis : str = None
        modal : str = None
        tamanho : str = BOTOES.tamanho
        icon : str = ""
        texto : str = ""
        botao : str = None

        def __init__(self, hiperligacao = "#", tipo_passagem_variaveis = btpv.url, passagem_variaveis = None, modal = None, 
            cor_fundo = None, cor_letra = None, classes = None, tamanho = None, icon = None, texto = None):
            
            self.hiperligacao = hiperligacao
            self.tipo_passagem = btpv.url if not not isinstance(tipo_passagem_variaveis, btpv) else tipo_passagem_variaveis
            self.passagem_variaveis = "" if not passagem_variaveis else passagem_variaveis
            self.modal = "" if not isinstance(modal, str) else modal
            self.cor_fundo = cor_fundo if cor_fundo else f"{BOTOES.cor_fundo}"
            self.cor_letra = cor_letra if cor_letra else "text-info"
            self.classes = classes if classes else ""
            self.tamanho = tamanho if tamanho else BOTOES.tamanho

            if icon:
                if icon.find("{}") == -1:
                    posicao : int = icon.find("'></i>")
                    if posicao > -1:
                        icon = icon[:posicao] + "{}" + icon[posicao:]

            self.icon = icon if icon else ""
            self.texto = texto.capitalize() if texto else ""

            self.icon = self.icon.format(f" {self.cor_letra} {self.tamanho} {self.cor_fundo}")

            self.botao = BOTOES.botao_html.format(BOTOES.tooltip, f"{BOTOES.separador} {self.classes}", self.hiperligacao, 
                self.tipo_passagem, self.passagem_variaveis, self.modal, self.texto, self.icon).replace("'", "|")

class BOTOES_FORMULARIO:
    linha = None
    colunas = None
    alinhamento : BOTOES.BOTOES_ALINHAMENTOS = None
    estilo : BOTOES.BOTOES_FORMULARIO_ESTILO = None
    tipo : BOTOES.BOTOES_FORMULARIO_TIPOS = None
    id_nome = None
    classe : str = None
    ligacao : str = None
    modal : MODAL.BOTAO_MODAL = MODAL.BOTAO_MODAL.nenhum
    tamanho_botao : str = None
    icon : str = None
    texto : str = None

    def __teste_tamanho_botao(self, tamanho_a_avaliar):
        if isinstance(tamanho_a_avaliar, int):
            tamanho_a_avaliar = f" width='{tamanho_a_avaliar}px'"
        elif isinstance(tamanho_a_avaliar, str):
            posicao_primeira_letra : int = ""

            for pos in range(len(tamanho_a_avaliar)):
                if not tamanho_a_avaliar[pos].isnumeric():
                    posicao_primeira_letra = pos

            if posicao_primeira_letra is None:
                tamanho_a_avaliar = ""
            elif posicao_primeira_letra == 0:
                tamanho_a_avaliar = ""
            elif tamanho_a_avaliar[:posicao_primeira_letra-1].isnumeric():
                if int(tamanho_a_avaliar[:posicao_primeira_letra-1]) < BOTOES.botoes_formulario_tamanho:
                    tamanho_a_avaliar = f" width='{BOTOES.botoes_formulario_tamanho}px'"
                else:
                    tamanho_a_avaliar = f" width='{tamanho_a_avaliar[:posicao_primeira_letra-1]}px'"
            else:
                tamanho_a_avaliar = f" width='{BOTOES.botoes_formulario_tamanho}px'"
        else:
            tamanho_a_avaliar = ""

        return tamanho_a_avaliar

    def __init__(self, linha : int, colunas : list = PRED.colunas_valores, 
    alinhamento : BOTOES.BOTOES_ALINHAMENTOS = BOTOES.BOTOES_ALINHAMENTOS.esquerda,
    estilo : BOTOES.BOTOES_FORMULARIO_ESTILO = BOTOES.BOTOES_FORMULARIO_ESTILO.informacao, 
    tipo : BOTOES.BOTOES_FORMULARIO_TIPOS = BOTOES.BOTOES_FORMULARIO_TIPOS.botao, id_nome : str = None, 
    classe : str = None, ligacao : str = None, modal : MODAL.BOTAO_MODAL = MODAL.BOTAO_MODAL.nenhum, 
    tamanho : str = None, icon : str = None, texto : str = None):

        from ..mensagens.mensagem_popup import apresenta_caixa_mensagens

        if not isinstance(linha, int):
            apresenta_caixa_mensagens(texto_mensagem=f"Falha na declaração da linha a que pertence o elemento {id_nome}")
            return None
        elif linha <= 0:
            apresenta_caixa_mensagens(texto_mensagem=f"A linha tem de ser maior ou igual a 1 para o elemento {id_nome}")
            return None

        if not isinstance(colunas, list):
            colunas = PRED.colunas_valores
        elif colunas == []:
            colunas = PRED.colunas_valores
        else:
            for c in range(len(colunas)):
                if not str(colunas[c]).isnumeric() and str(colunas[c]) != "":
                    colunas[c] = ""

        self.linha = linha
        self.colunas = colunas

        from ..funcoes_gerais import devolve_membros_class

        if not alinhamento in devolve_membros_class(BOTOES.BOTOES_ALINHAMENTOS,1):
            self.alinhamento = BOTOES.BOTOES_ALINHAMENTOS.esquerda
        else:
            self.alinhamento = alinhamento

        if not estilo in devolve_membros_class(BOTOES.BOTOES_FORMULARIO_ESTILO, 1):
            self.estilo = BOTOES.BOTOES_FORMULARIO_ESTILO.informacao
        else:
            self.estilo = estilo

        if not tipo in  devolve_membros_class(BOTOES.BOTOES_FORMULARIO_TIPOS, 1):
            self.tipo = BOTOES.BOTOES_FORMULARIO_TIPOS.botao
        else:
            self.tipo = tipo

        if not isinstance(id_nome, str):
            self.id_nome = ""
        else:
            self.id_nome = id_nome

        if not isinstance(classe, str):
            self.classe = ""
        else:
            self.classe = classe if classe[0] == " " else " " + classe

        if not isinstance(ligacao, str):
            self.ligacao = None
        else:
            self.ligacao = ligacao

        if not modal in devolve_membros_class(MODAL.BOTAO_MODAL,1):
            self.modal = MODAL.BOTAO_MODAL.nenhum
        else:
            self.modal = modal
            
            if self.modal == MODAL.BOTAO_MODAL.abrir:
                self.modal = self.modal.format(self.id_nome)

        self.tamanho = self.__teste_tamanho_botao(tamanho)
        
        if icon is None:
            self.icon = ""
        else:
            self.icon = icon
        
        if not texto:
            self.texto = "Botão"
        else:
            self.texto = texto

        if not self.ligacao:
            self.html = BOTOES.botoes_formulario.format(self.tipo, self.id_nome, self.classe + self.estilo, 
            self.tamanho + self.modal, self.texto)
        else:
            self.html = BOTOES.botoes_formulario_hiperligacao.format(self.tipo, self.id_nome, self.ligacao,
            self.classe + self.estilo, self.tamanho + self.modal, self.texto)

