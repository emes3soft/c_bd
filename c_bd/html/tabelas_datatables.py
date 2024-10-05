from flask import jsonify, json
from ..mensagens.mensagem_popup import apresenta_caixa_mensagens, CAIXA_MENSAGENS
from ..comandos.comandos import CMD_SELECT
from .botoes import BOTOES_TABELA as BTN
from .constantes import TABELA
from ..funcoes_gerais import devolve_informacoes_class

class DATATABLE:
    class TIPOS:
        data : str = "date"
        html : str = "html"
        numero : str = "num"
        numero_formatado : str = "num-fmt"
        numero_html : str = "html-num"
        numero_formatado_html : str = "html-num-fmt"
        texto : str = "string"

    class COLUNAS:
        className : str = ""
        data : str = ""
        defaultContent : str = ""
        name : str = ""
        orderable : bool = True
        searchable : bool = True
        title : str = ""
        type : str = ""
        visible : bool = True
        width : int = None
        render : str = None

        def __init__(self, className : str = None, data : str = None, defaultContent : str = None, name : str = None, 
        orderable : str = None, searchable : str = None, title : str = None, type : str = None, visible : bool = True, 
        width : int = None):
            self.className = className
            self.data = data
            self.defaultContent = defaultContent
            self.name = name
            self.orderable = orderable
            self.searchable = searchable
            self.title = title
            self.type = type
            self.visible = visible
            self.width = width
            self.render = None
            self.definicoes = self.__criar_definicoes()

        def __criar_definicoes(self):
            definicoes = {}

            # if self.type == DATATABLE.TIPOS.data:
            #     self.render = TABELA.render_data.replace("'", "|")

            for var in vars(self):
                if not self.__getattribute__(var) is None or var in ['data']:
                    definicoes[var] = self.__getattribute__(var)

            # apresenta_caixa_mensagens(texto_mensagem=str(definicoes))
            return definicoes

    class FIXAR_HEADER_FOOTER:
        header : bool = True
        footer : bool = True
        dicionario : dict = None

        def __init__(self, header : bool = True, footer : bool = True):
            self.header = header
            self.footer = footer
            self.dicionario = self.devolve_em_dicionario()

        def devolve_em_dicionario(self):
            attr_devolver = {}
            attr_devolver["header"] = self.header
            attr_devolver["footer"] = self.footer
            return attr_devolver

    class COLUMN_DEFS_LINHA:
        targets : object = None
        visibility : bool = None
        searchable : bool = None
        orderable : bool = None
        defaultContent : str = ""

        def __init__(self, targets : object = None, visibility : bool = None, searchable : bool = None
            , orderable : bool = None, defaultContent : str = None):
            
            self.targets = targets
            self.visibility = visibility
            self.searchable = searchable
            self.orderable = orderable
            self.defaultContent = defaultContent

            if not targets:
                erro = ""
                return None
            elif not orderable and not visibility and not searchable and not defaultContent:
                erro = ""
                return None

            self.definicoes = self.__cria_definicoes()

        def __cria_definicoes(self):
            definicoes = {}
            for var in vars(self):
                if self.__getattribute__(var):
                    definicoes[var] = self.__getattribute__(var)

            return definicoes

    class METODO_SERVIDOR:
        nenhum = None
        post = 'post'
        get = 'get'

    ajax : dict = {}
    columns : list[COLUNAS] = []
    caption : str = None
    width : int = None
    height : int = None
    info : bool = True
    paging : bool = True
    processing : bool = True
    serverSide : bool = False
    serverMethod : METODO_SERVIDOR =  METODO_SERVIDOR.nenhum
    fixedHeader : FIXAR_HEADER_FOOTER = None
    pageLength : int = 10
    lengthMenu : list = [[2, 10, 25, 50, 100, -1], [2, 10, 25, 50, 100, "Todos"]]
    ordering : bool = True
    columnDefs : list = []
    sucesso : bool = False

    def __init__(self, comando_select : CMD_SELECT = None, endereco_dados : str = None, colunas : list = [], comprimento : int = None, 
    altura : int = None, mostrar_informacao : bool = True, paginacao : bool = True, processando : bool = True, 
    cabecalho_rodape_fixo : FIXAR_HEADER_FOOTER = FIXAR_HEADER_FOOTER(), 
    linhas_por_pagina : int = 10, com_ordenacao : bool = True, definicoes_de_colunas : list = [], botoes : list = [], titulo : str = None):

        if not isinstance(comando_select, CMD_SELECT):
            self.comando_select = None
        else:
            self.comando_select = comando_select
        
        botoes_html = ""
        if not isinstance(botoes,list):
            botoes = None
        else:
            numero_botoes_coluna_operacoes = 0
            for b in botoes:
                if isinstance(b, BTN.BOTAO_EDITAR) or isinstance(b,BTN.BOTAO_ELIMINAR) or isinstance(b, BTN.BOTAO_PERSONALIZADO)\
                or isinstance(b, BTN.BOTAO_VISUALIZAR):
                    botoes_html += b.botao
                    numero_botoes_coluna_operacoes += 1
            
            if len(botoes) > 0:
                colunas.append(DATATABLE.COLUNAS(className="text-center operacoes", orderable=False, searchable=False, 
                    title="Operações", visible=True, defaultContent=botoes_html, type=DATATABLE.TIPOS.html, 
                    width=numero_botoes_coluna_operacoes*TABELA.coluna_operacoes_dimensao_por_botao)) 

        lista_colunas = []
        if isinstance(colunas, list) and colunas != []: 
            for c in range(len(colunas)):
                if isinstance(colunas[c], self.COLUNAS):
                    lista_colunas.append(colunas[c].definicoes)

        self.columns = lista_colunas

        self.width = str(comprimento) + "px" if comprimento else None

        self.height = str(altura) + "px" if altura else None

        if not isinstance(mostrar_informacao, bool): mostrar_informacao = False
        self.info = mostrar_informacao

        if not isinstance(paginacao, bool): paginacao = True
        self.paging = paginacao

        if not isinstance(processando, bool): processando = True
        self.processing = processando

        if not isinstance(com_ordenacao, bool): com_ordenacao = True
        self.ordering = com_ordenacao

        cabecalho_rodape = self.FIXAR_HEADER_FOOTER()
        if not isinstance(cabecalho_rodape_fixo, self.FIXAR_HEADER_FOOTER): cabecalho_rodape_fixo = cabecalho_rodape.dicionario
        self.fixedHeader = cabecalho_rodape_fixo.dicionario

        if not isinstance(linhas_por_pagina, int) or not isinstance(linhas_por_pagina, list): linhas_por_pagina = 5
        self.pageLength = linhas_por_pagina

        self.lengthMenu = [[5, 10, 25, 50, 100, -1], [5, 10, 25, 50, 100, "All"]]

        if not isinstance(definicoes_de_colunas, list) and definicoes_de_colunas != []: definicoes_de_colunas = []
        self.columnDefs = definicoes_de_colunas
        
        if not isinstance(titulo, str):
            titulo = "Sem Título"
        
        botao_adicionar = ""
        for b in botoes:
            if isinstance(b, BTN.BOTAO_ADICIONAR):
                botao_adicionar = b.botao

        self.caption = TABELA.TCAPTION.geral_div.format(titulo, botao_adicionar).replace("'", "|")

        if endereco_dados:
            self.comando_select = None
            self.ajax = {"url" : endereco_dados}
            self.serverSide = True
            self.serverMethod = self.METODO_SERVIDOR.post
            self.tabela_html = self.__cria_tag_tabela_html()
            self.informacoes = self.__cria_informacoes_datatables()
        elif isinstance(comando_select, CMD_SELECT):
            self.ajax = None
            self.serverSide = False
            self.serverMethod = self.METODO_SERVIDOR.nenhum
            self.columns = []
            self.tabela_html = self.__cria_tabela_html()
            self.informacoes = ""
        else:
            apresenta_caixa_mensagens(CAIXA_MENSAGENS.erro, "ERRO DATATABLE", "Tem de associar um comando select (CMD_SELECT) ou um endereço para os dados!")
            self.tabela_html = None
            self.informacoes = None

    def __cria_tag_tabela_html(self):
        from .constantes import PREDEFINICOES
        html = ""
        
        html = TABELA.tabela.format("tabela", PREDEFINICOES.tabela_classe_definicao, "", "", "", "", "", "")

        return html

    def __cria_tabela_html(self):
        from .constantes import PREDEFINICOES
        html = ""

        html_thead = html_tbody = ""

        if self.comando_select: 
            if self.comando_select.sucesso:

                html_thead_colunas = ""
                for c in self.comando_select.campos_comando:
                    html_thead_colunas += TABELA.THEAD.coluna.format(TABELA.THEAD.cores, "", "", str(c))
                
                html_thead = TABELA.THEAD.geral.format("", TABELA.THEAD.linha.format(html_thead_colunas))

                html_registos_linhas = ""

                for reg in self.comando_select.registos:
                    html_registos_colunas = ""
                    for c in reg:
                        html_registos_colunas += TABELA.TBODY.coluna.format(TABELA.TBODY.cores, "", "", reg[c] if reg[c] else '')
                    
                    html_registos_linhas += TABELA.TBODY.linha.format(html_registos_colunas)

                html_tbody = TABELA.TBODY.geral.format("", html_registos_linhas)
        
        html = TABELA.tabela.format("tabela", PREDEFINICOES.tabela_classe_definicao, PREDEFINICOES.tabela_cor_linhas,
            "", "", "", html_thead, html_tbody, "")

        return html

    def __cria_informacoes_datatables(self):
        definicoes = {}
        
        # apresenta_caixa_mensagens(texto_mensagem=str(vars(self)))
        
        colunas_a_apagar = ["columnDefs", "tabela_html"]
        if len(self.__getattribute__("columns")) == 0: colunas_a_apagar.append("columns")
        if not self.__getattribute__("paging"): 
            colunas_a_apagar.append("pageLength")
            colunas_a_apagar.append("lengthMenu")

        colunas_forcar = ["ajax"]

        for var in vars(self):
            if (not self.__getattribute__(var) is None and not var in colunas_a_apagar) or var in colunas_forcar:
                definicoes[var] = self.__getattribute__(var)
        
        # apresenta_caixa_mensagens(texto_mensagem=str(json.dumps(definicoes, ensure_ascii=False, indent=6)))

        return json.dumps(definicoes)

