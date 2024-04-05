from ..mensagens.mensagem_popup import apresenta_caixa_mensagens, CAIXA_MENSAGENS

class PREDEFINICOES:
    colunas_dimensoes = ["col","col-xs","col-sm","col-md","col-lg","col-xl","col-xxl"]
    colunas_valores = ["","","","","","",""]
    tabela_classe_definicao = "tabela_c_bd"
    tabela_cor_linhas = "black"
    tabela_outras_classes = ""
    classe_thead = "bg-dark text-white"
    outras_classes_thead = "fs-4"
    botoes_tamanho = "fs-5"
    botoes_tamanho_adicionar = 'fs-4'
    botoes_tamanho_coluna = 150
    configuracao_colunas = {"columns": []}
    linhas = """ <div class="row" data-linha="{}">{}</div> """
    colunas = """ <div class="{}" data-colunas="{}">{}</div> """
    
    class TIPO_DE_MODAL_INFOS:
        nome : str
        icon : str

        def __init__(self, classe, nome, icon):
            self.classe = classe
            self.nome = nome
            self.icon = icon

class FORMULARIOS:
    class METODO:
        get : str = "GET"
        post : str = "POST"

    class ELEMENTOS_HTML:
        html : dict = {
            "linhas" : """ <div class="row{}" data-linha="{}">{}</div> """,
            "colunas" : """ <div class="{}" data-colunas="{}">{}</div> """,
            "titulo" : """
                <div class="row titulo-formulario">
                    <div class="col text-center py-2">
                        {}
                    </div>
                </div>
            """,
            "form" : """
                <form id="{}" name="{}" class="{}" method="{}" action="{}" {} novalidate autocomplete="off">
                    <div class="title">
                        {}
                    </div>
                    <fieldset>
                        {}
                    </fieldset>
                    <div class="buttons">
                        {}
                    </div>
                </form>
            """,
            "input" : """
                <div class="caixa_texto">
                    <input id="{}" name="{}" type="{}" class="form-control form-control-sm{}"{} placeholder="{}"{}{} autocomplete="off">
                    <label for="{}">{}</label>
                </div>
            """,
            "select" : """
                <div class="caixa_texto">
                    <select id="{}" name="{}" class="form-select form-select-sm{}" aria-label=""{}>
                        {}
                    </select>
                    <label for="{}">{}</label>
                </div>
            """,
            "textarea" : """
                <div class="caixa_texto">
                    <textarea id="{}" name="{}"{} class="form-control{}"{} placeholder="{}"{} autocomplete="off">{}</textarea>
                    <label for="{}">{}</label>
                </div>
            """,
            "option" : """
                <option value="{}"{}>{}</option>
            """,
        }

    class ELEMENTOS:
        input : str = "input"
        select : str = "select"
        textarea : str = "textarea"
        botao : str = "button"

    class TIPO_ELEMENTO_BOTAO:
        nenhum : str = ""
        submeter : str = "submit"
        reiniciar : str = "reset"
        botao : str = "button"
    
    class TIPO_ELEMENTO_INPUT:
        nenhum : str = ""
        botao = "button"
        botao_selecao ="checkbox"
        cor = "color"
        data = "date"
        data_hora_local = "datetime-local"
        correio_eletronico = "email"
        ficheiro = "file"
        escondido = "hidden"
        imagem = "image"
        mes = "month"
        numero = "number"
        palavra_passe ="password"
        botao_escolha = "radio"
        intervalo = "range"
        reiniciar = "reset"
        procura = "search"
        submeter = "submit"
        telefone = "tel"
        texto = "text"
        hora = "time"
        ligacao = "url"
        semana = "week"
        codigo_postal = "codigopostal"

class MODAL:
    class TAMANHO:
        sm = " modal-sm"
        lg = " modal-lg"
        xl = " modal-xl"
        normal = ""
        ecra_completo = " modal-fullscreen"

    class ALINHAMENTO:
        inicio = "text-start"
        centro = "text-center"
        fim = "text-end"

    class TIPO_DE_MODAL:
        normal = PREDEFINICOES.TIPO_DE_MODAL_INFOS("mdlNormal", "mdlNormalGeral", "")
        erro = PREDEFINICOES.TIPO_DE_MODAL_INFOS("mErro", "mdlErroGeral", "<i class='fa-solid fa-circle-xmark'></i>")
        aviso = PREDEFINICOES.TIPO_DE_MODAL_INFOS("mAviso", "mdlAvisoGeral", "<i class='fa-solid fa-triangle-exclamation'></i>")
        informacao = PREDEFINICOES.TIPO_DE_MODAL_INFOS("mInfo", "mdlInfoGeral", "<i class='fa-solid fa-circle-info'></i>")
        confirmacao = PREDEFINICOES.TIPO_DE_MODAL_INFOS("mConf", "mdlConfGeral", "<i class='fa-solid fa-circle-question'></i>")
        confirmacao_eliminacao = PREDEFINICOES.TIPO_DE_MODAL_INFOS("mConfEl", "mdlConfEliminar", "<i class='fa-solid fa-circle-question'></i>")

    class BOTAO_MODAL:
        abrir = """ data-bs-target="#{}" data-bs-toggle="modal" """
        fechar = """ data-bs-dismiss='modal'"""
        nenhum = ""

    modal_Normal = """
        <div class="modal mdlNormal" id="mdlNormalGeral" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                    <div class="row modal-caixa">
                        <div class="col bg-secondary">
                            <div class="row">
                                <div class="col-12 modal-titulo">
                                    {}
                                </div>
                                <div class="col-12 modal-texto text-bg-light">
                                    {}
                                </div>
                                <div class="col-12 modal-botoes mb-2">
                                    <div class="mt-2 text-center"><button type="button" class="btn btn-danger fw-bold w-100" data-bs-dismiss="modal">Fechar</button></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """

    geral_com_formulario = """
        <div id="{}" class="modal{}" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable{}">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title text-center" id="staticBackdropLabel">{}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <form id="{}" class="" method="post" action="{}">
                        <div class="modal-body">
                            {}
                        </div>

                        <div class="modal-footer">
                            {}
                        </div>
                    </form>
                </div>
            </div>
        </div>
    """

    geral_sem_formulario = """
        <div id="{}" class="modal{}" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable{}">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title text-center" id="staticBackdropLabel">{}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        {}
                    </div>

                    <div class="modal-footer">
                        {}
                    </div>
                </div>
            </div>
        </div>
    """

class BOTOES:
    tamanho = "" # "fa-lg"
    tooltip = "tooltip-tabela"
    cor_fundo = ""
    separador = ""
    tamanho_min_coluna = 100
    botao_html = "<span class='{} {} text-decoration-none' data-href='{}' data-passagem='{}' data-vars='{}' data-modal='{}' data-bs-toggle='tooltip-botoes' data-bs-title='{}'>{}</span>"
    icons_adicionar = {
        "1" : "<i class='fa-solid fa-square-plus{}'></i>",
        "2" : "<i class='fa-solid fa-circle-plus{}'></i>",
        "3" : "<i class='fa-regular fa-square-plus{}'></i>",
    }
    icons_editar = {
        "1" : "<i class='fa-solid fa-pen-to-square{}'></i>",
        "2" : "<i class='fa-solid fa-pen{}'></i>",
        "3" : "<i class='fa-solid fa-square-pen{}'></i>",
    }
    icons_eliminar = {
        "1" : "<i class='fa-solid fa-trash{}'></i>",
        "2" : "<i class='fa-solid fa-square-minus{}'></i>",
        "3" : "<i class='fa-solid fa-eraser __tamanho__'></i>",
    }
    icons_visualizar = {
        "1" : "<i class='fa-solid fa-eye{}'></i>",
        "2" : "<i class='fa-regular fa-eye{}'></i>",
        "3" : "<i class='fa-solid fa-magnifying-glass{}'></i>",
    }

    botoes_formulario = """<button type="{}" id="{}" class="btn{}"{}>{}</button>"""
    botoes_formulario_hiperligacao = """<a type="{}" id="{}" href="{}" class="btn {}"{}>{}</a>"""
    botoes_formulario_tamanho = 150

    class BOTOES_ALINHAMENTOS:
        esquerda : str = " text-start"
        centro : str = " text-center"
        direita : str = " text-end"

    class BOTOES_TIPO_PASSAGEM_VARIAVEIS:
        url : str = "url"
        ligacao : str = "ligacao"

    class BOTOES_FORMULARIO_TIPOS:
        submeter : str = "submit"
        limpar : str = "reset"
        botao : str = "button"
    
    class BOTOES_FORMULARIO_ESTILO:
        personalizado : str = ""
        erro : str = " btn-danger"
        aviso : str = " btn-warning"
        sucesso : str = " btn-success"
        informacao : str = " btn-info"
        primario : str = " btn-primary"
        secundario : str = " btn-secondary"
        claro : str = " btn-light"
        escuro : str = " btn-dark"
        erro_outline : str = " btn-outline-danger"
        aviso_outline : str = " btn-outline-warning"
        sucesso_outline : str = " btn-outline-success"
        informacao_outline : str = " btn-outline-info"
        primario_outline : str = " btn-outline-primary"
        secundario_outline : str = " btn-outline-secondary"
        claro_outline : str = " btn-outline-light"
        escuro_outline : str = " btn-outline-dark"

class TABELA:
    tabela = "<table id='{}' class='{} w-100 table display table-sm table-striped table-hover caption-top{}'>{}{}{}{}{}</table>"

    render_data = "function (data, type, row) {return moment(new Date(data).toString()).format('DD/MM/YYYY');}"

    colunas_dimensoes = PREDEFINICOES.colunas_valores

    coluna_operacoes_dimensao_por_botao = 27

    tabela_definicao_colunas = "<div class='{}'{}{}>{}</div>"
    tabela_definicao_linhas = "<div class='row'>{}</div>"

    titutlo = "<caption class='{}'>{}</caption>"
    # colgroup = "<colgroup>{}</colgroup>"
    # cols = "<col />"
    colunas_span = "col-span={}"
    linhas_span = "row-span={}"

    class TCAPTION:
        geral = "<caption class='{}'>{}</caption>"
        geral_div = "<div class='row align-items-center'><div class='col-10 text-center'>{}</div><div class='col-2 text-end icon'>{}</div></div>"
        classes = ""
        cores = ""

    class THEAD:
        geral = "<thead class='{}'>{}</thead>"
        cores = PREDEFINICOES.classe_thead
        outras_classes = PREDEFINICOES.outras_classes_thead
        linha = "<tr>{}</tr>"
        coluna = "<th class='{}'{}{}>{}</th>"
        mostrar = ""
        conteudo = []

    class TBODY:
        geral = "<tbody class='{}'>{}</tbody>"
        cores = "table-white"
        botoes_cor_fundo = "bg-secondary bg-opacity-25"
        linha = "<tr>{}</tr>"
        coluna = "<td class='{}'{}{}>{}</td>"
        coluna_classes = ""
        conteudo = []

    class TFOOT:
        geral = "<tfoot class='{}'>__tfoot__</tfoot>"
        cores = "bg-secondary text-white"
        linha = "<tr>{}</tr>"
        coluna = "<td class='{}'{}{}>{}</td>"
        coluna_classes = "text-center"
        num_registos = "<span><b>Nº de Registos: <span class='text-bg-info px-2'>{}<span><b></span>"

class TABULATOR:
    class TIPO_CONTEUDO:
        formulario : str = "form"
        json : str = "json"

    class ROLAR_PARA_POSICAO_DA_LINHA:
        baixo : str = "bottom"
        centro : str = "center"
        topo : str = "top"
        perto_de : str = "nearest"

    class VALIDADOR:
        bloqueio : str = "blocking "
        destacar : str = "highlight"
        manual : str = "manual"

    __LINGUAGENS = {
        # Adição da linguagem em português
        "pt-pt":{ 
            "pagination":{
                "first":"Primeiro",
                "first_title":"Primeira Página",
                "last":"Última",
                "last_title":"Última Página",
                "prev":"Anterior",
                "prev_title":"Página Anterior",
                "next":"Próxima",
                "next_title":"Próxima Página",
                "all":"Todos",
            },
            "pag_size" : "Nº de linhas"
        }
    }

    # Informação
    data : list = None #data
    # informação percistente
    persistence : dict = {"sort" : True, "filter" : True, "columns" : True}
    # Apresentacção
    layout : str = "fitColumns" # layout
    responsiveLayout : str = "collapse" # o resto dos dados numa nova linha
    # Tamanhos
    height : str  = "auto"
    width : str = "auto"
    maxWidth : str = "auto"
    maxHeight : str = "auto"
    autoResize : bool = True
    # Texto quando não existem registos
    placeholder = "Não existem registos"
    # reactiveData : bool = True
    # Paginação
    paginacao : str = "local"
    paginacao_nlinhas : int = 6
    paginacao_nlinhas_selector : list = [3, 6, 8, 10]
    colunas_moviveis : bool = True
    paginacao_contador : str = "rows"
    # Linhas
    scrollToRowPosition : ROLAR_PARA_POSICAO_DA_LINHA =  ROLAR_PARA_POSICAO_DA_LINHA.topo
    resizableRows : bool  = True
    # Colunas
    autoColumns : bool = True
    resizableColumnFit : bool = True
    columns: list = []
    resizable : bool = True
    # variáveis iniciais
    inicialOrder : list = []
    initialFilter : list = []
    initialHeaderFilter : list = []
    # Separador
    nestedFieldSeparator : str = "|"
    # Linguagens
    langs : dict = __LINGUAGENS
    locate : str = "pt-pt"
    # Colucação de dados/informação
    ajaxURL : str = "" # resposta tipo json
    ajaxConfig : str = "POST"
            # "form" - send parameters as form data (default option)
            # "json" - send parameters as JSON encoded string
    ajaxContentType : TIPO_CONTEUDO = TIPO_CONTEUDO.json
    # Validações
    validationMode : VALIDADOR = VALIDADOR.bloqueio

    class COLUNAS:
        class ALIGN_HORIZONTAL_CABECALHO:
            esquerda : str = "left"
            centro : str = "center"
            direita : str = "right"

        class ALIGN_HORIZONTAL:
            esquerda : str = "left"
            centro : str = "center"
            direita : str = "right"

        class ALIGN_VERTICAL:
            topo : str = "top"
            centro : str = "center"
            fundo : str = "bottom"

        class ORDENACAO:
            nehuma : str = ""
            numero : str = "number"
            data : str = "date"

            class DIRECAO:
                nenhuma : str = ""
                ascendente : str = "asc"
                descendente : str = "desc"

        class CALCULOS:
            nenhum : str = ""
            contagem : str = "count"
            media : str = "avg"
            maximo : str = "max"
            minimo : str = "min"
            sumatorio : str = "sum"
            concatenar : str = "concat"
            unico : str = "unique" # tipo o select distinct

        class FORMATOS:
            nenhum : str = ""
            dinheiro : str = "money"
            imagem : str = "image"
            hiperligacao : str = "link"
            verdadeiro : str = "tick"
            verdadeiro_falso : str = "tickCross"
            cor : str = "color"
            estrelas : str = "star"
            progresso : str = "progress"
            botao_verdadeiro : str = "buttonTick"
            botao_falso : str = "buttonCross"
            numero_linha : str = "rownum"
            data : str = "datetime"
            data_hora : str = "datetime"
            hora : str = "datetime"
            diferenca_datas : str = "datetimediff"
            grafico : str = "chartFormatter"

        class VALIDADORES:
            nenhum : str = ""
            unico : str = "unique"
            requerido : str = "required"
            inteiro : str = "integer"
            flotuante : str = "float"
            numerico : str = "numeric"
            texto : str =  "string"
            alfanumerico : str = "alphanumeric"
            min_numero : str = "min:__tamanho__"
            max_numero : str = "max:__tamanho__"
            min_tamanho : str = "minLength:__tamanho__"
            max_tamanho : str = "maxLength:__tamanho__"
            valores_lista : str = "in:__valores__" # in:red|green|blue - valores separador por |
            expressao_reg : str = "regex:__expressao__"

            def validador_num_min(self, tamanho : int):
                if not isinstance(tamanho, int):
                    return ""
                return self.min_numero.replace("__tamanho__", tamanho)

            def validador_num_max(self, tamanho : int):
                if not isinstance(tamanho, int):
                    return ""
                return self.max_numero.replace("__tamanho__", tamanho)

            def validador_tam_min(self, tamanho : int):
                if not isinstance(tamanho, int):
                    return ""
                return self.min_tamanho.replace("__tamanho__", tamanho)

            def validador_tam_max(self, tamanho : int):
                if not isinstance(tamanho, int):
                    return ""
                return self.max_tamanho.replace("__tamanho__", tamanho)
            
            def validador_lista_valores (self, valores : list):
                if not isinstance(valores, list):
                    return ""
                
                return self.valores_lista.replace("__valores__","|".join(valores))

            def validador_expressao (self, expressao : str):
                if not isinstance(expressao, str):
                    return ""
                
                return self.valores_lista.replace("__expressao__",expressao)

        title : str = ""
        field : str = ""
        headerFilter : bool = True
        headerVertical : bool = True
        frozen : bool = True
        hozAlign : ALIGN_HORIZONTAL = ALIGN_HORIZONTAL.esquerda
        vertAlign : ALIGN_VERTICAL = ALIGN_VERTICAL.centro
        headerHozAlign : ALIGN_HORIZONTAL_CABECALHO = ALIGN_HORIZONTAL_CABECALHO.centro
        sorter : ORDENACAO = ORDENACAO.nehuma
        dir : ORDENACAO.DIRECAO = ORDENACAO.DIRECAO.nenhuma
        width : int = 0
        formatter : FORMATOS = FORMATOS.nenhum
        formatterParams : dict = {}
        editor : str = ""
        editorParams : dict = {}
        columns : list = []
        topCalc : CALCULOS = CALCULOS.nenhum
        bottomCalc : CALCULOS = CALCULOS.nenhum
        headerWordWrap : bool = True
        visible : bool = True
        headerVisible : bool = True
        validator : list = []
        headerPopup : str = ""
        headerPopupIcon : str = ""
        tooltip : bool = True
        headerTooltip : bool = True


        def adiciona_validador_lista(self, validador : VALIDADORES):
            if not isinstance(validador, self.VALIDADORES):
                apresenta_caixa_mensagens(CAIXA_MENSAGENS.erro, "ERRO",
                    "Validador não permitido ou inexistente!")
            
            self.validator.push(validador)

