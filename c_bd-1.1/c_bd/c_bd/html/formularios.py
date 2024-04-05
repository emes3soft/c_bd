from .constantes import FORMULARIOS as FRM, PREDEFINICOES as PRED
from ..mensagens.mensagem_popup import apresenta_caixa_mensagens, CAIXA_MENSAGENS as CM

class INPUT():
    id_nome = None
    classes = None
    tipo = None
    tamanho_maximo = None
    texto_informativo = None
    texto_rotulo = None
    valor_minimo = None
    valor_maximo = None
    valor_elemento = None
    ativo = True
    so_leitura = False
    linha = None
    colunas = None

    def __init__(self, id_nome : str, linha : int = 0, colunas : list = PRED.colunas_valores, tipo = FRM.TIPO_ELEMENTO_INPUT.texto, 
        classes :  str = None, tamanho_maximo : str = None, texto_informativo : str = None, texto_rotulo : str = None, 
        valor_elemento = None, valor_minimo_maximo : list = [], ativo : bool = True, so_leitura : bool = False):

        self.html = ""
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
        
        from ..funcoes_gerais import devolve_membros_class

        encontrou = False
        for elem in devolve_membros_class(FRM.TIPO_ELEMENTO_INPUT, 2):
            if tipo == elem[1]:
                encontrou = True

        if not encontrou:
            print (f"********** Falha na declaração do tipo de elemento: {tipo} ************")
            return None
        elif tipo == FRM.TIPO_ELEMENTO_INPUT.numero:
            classes += " numero"
            self.tipo = FRM.TIPO_ELEMENTO_INPUT.texto
        elif tipo == FRM.TIPO_ELEMENTO_INPUT.codigo_postal:
            classes += " codigopostal"
            self.tipo = FRM.TIPO_ELEMENTO_INPUT.texto
        else:
            self.tipo = tipo
        
        if id_nome is None:
            print ("********** Falha na declaração do id_nome do elemento ************")
            return None
        
        self.linha = linha
        self.colunas = colunas
        self.id_nome = id_nome

        self.classes = "" if classes is None else (" " if classes[0] != " " else "") + classes
        self.tamanho_maximo =  f" maxlength='{tamanho_maximo}'" if str(tamanho_maximo).isnumeric() else ""
        self.texto_informativo = "" if texto_informativo is None else texto_informativo.strip()
        self.texto_rotulo = "Sem Rótulo" if texto_rotulo is None else texto_rotulo.strip()
        self.valor_elemento = "" if valor_elemento is None else f" value='{str(valor_elemento)}'"
        self.ativo = "" if not isinstance(ativo, bool) is None else ("" if ativo else " disabled")
        self.so_leitura = "" if not isinstance(so_leitura, bool) is None else ("" if so_leitura or not self.ativo is None else " readonly")

        if not isinstance(valor_minimo_maximo, list):
            self.valor_minimo = None
            self.valor_maximo = None
        else:
            self.valor_minimo = ""
            self.valor_maximo = ""
            if len(valor_minimo_maximo) > 0:
                self.valor_minimo = "" if valor_minimo_maximo[0] is None else f" min='{str(valor_minimo_maximo[0])}'"
            if len(valor_minimo_maximo) > 1:
                self.valor_maximo = "" if valor_minimo_maximo[1] is None else f" max='{str(valor_minimo_maximo[1])}'"

        from ..funcoes_gerais import devolve_informacoes_class

        self.html = str(FRM.ELEMENTOS_HTML.html["input"]).format(self.id_nome, self.id_nome, self.tipo, self.classes, 
            self.tamanho_maximo + self.valor_minimo + self.valor_maximo, self.texto_informativo, self.ativo + self.so_leitura, 
            self.valor_elemento, self.id_nome, self.texto_rotulo)

class TEXTAREA():
    id_nome = None
    classes = None
    tamanho_maximo = None
    texto_informativo = None
    texto_rotulo = None
    valor_elemento = None
    ativo = True
    so_leitura = False
    linha = None
    colunas = None
    altura = None

    def __init__(self, id_nome : str, linha : int = 0, colunas : list = PRED.colunas_valores, altura : str = None,
        classes :  str = None, tamanho_maximo : str = None, texto_informativo : str = None, texto_rotulo : str = None, 
        valor_elemento = None, ativo : bool = True, so_leitura : bool = False):

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
        
        if id_nome is None:
            print ("********** Falha na declaração do id_nome do elemento ************")
            return None
        
        self.linha = linha 
        self.colunas = colunas
        self.id_nome = id_nome

        self.altura = "" if not str(altura).isnumeric() else f" style='height: {str(altura)}px'"
        self.classes = "" if classes is None else (" " if classes[0] != " " else "") + classes
        self.tamanho_maximo =  f" maxlength='{tamanho_maximo}'" if str(tamanho_maximo).isnumeric() else ""
        self.texto_informativo = "" if texto_informativo is None else texto_informativo.strip()
        self.texto_rotulo = "Sem Rótulo" if texto_rotulo is None else texto_rotulo.strip()
        self.valor_elemento = "" if valor_elemento is None else f" value='{str(valor_elemento)}'"
        self.ativo = "" if not isinstance(ativo, bool) is None else ("" if ativo else " disabled")
        self.so_leitura = "" if not isinstance(so_leitura, bool) is None else ("" if so_leitura or not self.ativo is None else " readonly")

        self.html = str(FRM.ELEMENTOS_HTML.html["textarea"]).format(self.id_nome, self.id_nome, self.altura, self.classes, 
            self.tamanho_maximo, self.texto_informativo, self.ativo + self.so_leitura, self.valor_elemento, 
            self.id_nome, self.texto_rotulo)

class SELECT():
    id_nome = None
    classes = None
    texto_informativo = None
    elemento_selecionado = None
    ativo = True
    so_leitura = True
    linha = None
    colunas = None
    informacoes_tabela = [] 
    # [conexão, nome da tabela, campos valor, campos texto, condições tabela]
    # [registos da tabela, campos valor, campos texto]

    def __init__(self, id_nome : str, linha : int = 0, colunas : list = PRED.colunas_valores,
        classes :  str = None, texto_rotulo : str = None, elemento_selecionado : list = None, 
        ativo : bool = True, so_leitura : bool = False, informacoes_tabela : list = None):

        self.html = ""
        
        if not isinstance(informacoes_tabela, list):
            texto = "Falha na declaração das informações da tabela!\nDefina uma de duas situações:\n" + \
            "Situação 1:\n\t[conexão, nome da tabela, campos valor, campos texto, condições tabela]\n" + \
            "Situação 2:\n\t[registos da tabela, campos valor, campos texto]"
            apresenta_caixa_mensagens(CM.erro, texto_mensagem=texto)
            return None
        elif not len(informacoes_tabela) in [3,5]: # == 3 or not len(informacoes_tabela) == 5:
            texto = "A declaração das informações da tabela não se enquadra em nenuma das situações válidas!" + \
            "\nDefina uma de duas situações:\n" + \
            "Situação 1:\n\t[conexão, nome da tabela, campos valor, campos texto, condições tabela]\n" + \
            "Situação 2:\n\t[registos da tabela, campos valor, campos texto]"
            apresenta_caixa_mensagens(CM.erro, texto_mensagem=texto)
            return None

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
        
        if str(id_nome).strip() is None:
            apresenta_caixa_mensagens(CM.erro, texto_mensagem="Falha na declaração do id_nome do elemento!")
            return None
        
        if not isinstance(elemento_selecionado, list):
            elemento_selecionado = None
        elif len(elemento_selecionado) < 2:
            elemento_selecionado = None
        
        self.linha = linha
        self.colunas = colunas
        self.id_nome = id_nome
        self.classes = "" if classes is None or classes == "" else (" " if classes[0] != " " else "") + classes
        self.texto_rotulo = "Sem Rótulo" if texto_rotulo is None else texto_rotulo.strip()
        self.elemento_selecionado = elemento_selecionado
        self.ativo = "" if not isinstance(ativo, bool) is None else ("" if ativo else " disabled")
        self.so_leitura = "" if not isinstance(so_leitura, bool) is None else ("" if so_leitura or not self.ativo is None else " readonly")

        self.opcoes = ""
        
        if len(informacoes_tabela) == 3:
            if not isinstance(informacoes_tabela[0], list):
                apresenta_caixa_mensagens(CM.erro, texto_mensagem="O primeiro elemento de informacoes_tabela deve ser uma lista, mesmo que vazia!")
                return None
            
            campos_valor = [c.strip() for c in str(informacoes_tabela[1]).split(",")]
            campos_texto = [c.strip() for c in str(informacoes_tabela[2]).split(",")]
            campos_todos = campos_valor + campos_texto + ([] if self.elemento_selecionado is None else [self.elemento_selecionado[0]])

            campos_inexistentes = ""
            if informacoes_tabela[0] != []:
                for c in campos_todos:
                    if not c in informacoes_tabela[0][0].keys():
                        campos_inexistentes += c if campos_inexistentes == "" else " ," + c
            
            if campos_inexistentes != "":
                texto = f"O(s) campo(s) {campos_inexistentes} não existe(m) nos registos!"
                apresenta_caixa_mensagens(CM.erro, texto_mensagem=texto)
                return None

            for reg in informacoes_tabela[0]:
                texto_cv = ""
                for cv in campos_valor:
                    texto_cv += str(reg[cv]) if texto_cv == "" else "||" + str(reg[cv])

                texto_ct = ""
                for ct in campos_texto:
                    texto_ct += str(reg[ct]) if texto_ct == "" else " -- " + str(reg[ct])
                
                selecionado = ""
                if self.elemento_selecionado:
                    if (reg[elemento_selecionado[0]] == elemento_selecionado[1]):
                        selecionado = " selected"

                self.opcoes += str(FRM.ELEMENTOS_HTML.html["option"]).format(texto_cv, selecionado, texto_ct)
        else:
            from ..connector.conexao import CONEXAO
            
            if not isinstance(informacoes_tabela[0], CONEXAO):
                texto = "O primeiro valor da lista de informações da tabela tem de ser uma conexao válida!"
                apresenta_caixa_mensagens(CM.erro, texto_mensagem=texto)
                return None
            elif not informacoes_tabela[0].conetado:
                texto = "A conexão relativa ao primeiro valor da lista de informações da tabela não conetada!"
                apresenta_caixa_mensagens(CM.erro, texto_mensagem=texto)
                return None
            elif str(informacoes_tabela[1]) is None:
                texto = "Tem de escrever o nome da tabela válida!"
                apresenta_caixa_mensagens(CM.erro, texto_mensagem=texto)
                return None

            from ..comandos.comandos import CMD_SELECT, executar_comando
            
            campos_valor = [c.strip() for c in str(informacoes_tabela[2]).split(",")]
            campos_texto = [c.strip() for c in str(informacoes_tabela[3]).split(",")]
            campos_todos = campos_valor + campos_texto + ([] if self.elemento_selecionado is None else [self.elemento_selecionado[0]])

            comando = CMD_SELECT(informacoes_tabela[0], informacoes_tabela[1], f"{informacoes_tabela[2]}, {informacoes_tabela[3]}", condicoes=informacoes_tabela[4])
            executar_comando(informacoes_tabela[0], comando)

            if not comando.sucesso:
                texto = f"Comando executado sem sucesso!"
                apresenta_caixa_mensagens(CM.erro, texto_mensagem=texto)
                return None
            
            campos_lista = comando.info_tabelas[0]["campos_lista_str"].split(",")
            campos_inexistentes = ""
            for c in range(len(campos_todos)):
                if not campos_todos[c] in campos_lista:
                    campos_inexistentes += campos_todos[c] if campos_inexistentes == "" else " ," + campos_todos[c]
            
            if campos_inexistentes != "":
                texto = f"O(s) campo(s) {campos_inexistentes} não existe(m) na tabela {informacoes_tabela[1]}!"
                apresenta_caixa_mensagens(CM.erro, texto_mensagem=texto)
                return None
            
            for reg in comando.registos:
                texto_cv = ""
                for cv in campos_valor:
                    texto_cv += str(reg[cv]) if texto_cv == "" else "||" + str(reg[cv])

                texto_ct = ""
                for ct in campos_texto:
                    texto_ct += str(reg[ct]) if texto_ct == "" else " -- " + str(reg[ct])
                
                selecionado = ""
                if self.elemento_selecionado:
                    if (reg[elemento_selecionado[0]] == elemento_selecionado[1]):
                        selecionado = " selected"

                self.opcoes += str(FRM.ELEMENTOS_HTML.html["option"]).format(texto_cv, selecionado, texto_ct)

        self.html = str(FRM.ELEMENTOS_HTML.html["select"]).format(self.id_nome, self.id_nome, self.classes, 
            self.ativo + self.so_leitura, self.opcoes, self.id_nome, self.texto_rotulo)

class FORMULARIO:
    id_nome : str = None
    classes : str = None
    metodo : FRM.METODO = None
    ligacao : str = None
    ficheiros : bool = False
    html : str = None
    titulo : str = None

    def __init__(self, id_nome : str, ligacao : str, ficheiros : bool = False, metodo : FRM.METODO = FRM.METODO.post, 
        elementos : list = [], botoes : list = [], titulo : str = None):
        
        if not titulo is None and titulo != "":
            self.titulo = str(FRM.ELEMENTOS_HTML.html["titulo"]).format(titulo)
            self.classes = "titulo"
        else:
            self.titulo = self.classes = ""
            

        if id_nome is None or id_nome == "":
            print ("********** Falha na declaração do id_nome do formulário ************")
            return None
        
        if ligacao is None or ligacao == "":
            print ("********** Falha na declaração da ligação (action) do formulário ************")
            return None
        
        self.ficheiros = False if not isinstance(ficheiros, bool) else ficheiros
        self.multi_part = " enctype='multipart/form-data'" if self.ficheiros else ""
        
        if not isinstance(metodo, FRM.METODO):
            metodo = FRM.METODO.post

        self.id_nome = id_nome
        self.ligacao = ligacao
        self.metodo = metodo

        self.elementos = ""
        objetos = {}
        if isinstance(elementos, list):
            for e in elementos:
                if isinstance(e,(INPUT,SELECT,TEXTAREA)):
                    if e.linha in objetos.keys():
                        objetos[e.linha].append(e)
                    else:
                        objetos[e.linha] = [e]

            for obj in objetos:
                objeto_html = ""
                for el in objetos[obj]:
                    colunas = ""
                    for c in range(len(el.colunas)):
                        if colunas == "":
                            colunas = PRED.colunas_dimensoes[c] + ("" if el.colunas[c] == "" else f"-{el.colunas[c]}")
                        elif el.colunas[c] != "":
                            colunas += " " + PRED.colunas_dimensoes[c] + f"-{el.colunas[c]}" 
                    
                    objeto_html += str(FRM.ELEMENTOS_HTML.html["colunas"]).format(colunas, ",".join(str(el.colunas)), el.html)
                
                self.elementos += str(FRM.ELEMENTOS_HTML.html["linhas"]).format(f" linha{el.linha}", el.linha, objeto_html)

        self.botoes = ""
        btn = {}
        if isinstance(botoes, list):
            from .botoes import BOTOES_FORMULARIO as BF

            for b in botoes:
                if isinstance(b,BF):
                    if b.linha in btn.keys():
                        btn[b.linha].append(b)
                    else:
                        btn[b.linha] = [b]

            for b in btn:
                btn_html = ""
                for el in btn[b]:
                    colunas = ""
                    for c in range(len(el.colunas)):
                        if colunas == "":
                            colunas = PRED.colunas_dimensoes[c] + ("" if el.colunas[c] == "" else f"-{el.colunas[c]}")
                        elif el.colunas[c] != "":
                            colunas += " " + PRED.colunas_dimensoes[c] + f"-{el.colunas[c]}" 
                    
                    btn_html += str(FRM.ELEMENTOS_HTML.html["colunas"]).format(colunas + el.alinhamento + " botoes", ",".join(str(el.colunas)), el.html)
                
                self.botoes += str(FRM.ELEMENTOS_HTML.html["linhas"]).format(f" botoes{el.linha}", el.linha, btn_html)

        self.html =str(FRM.ELEMENTOS_HTML.html["form"]).format(self.id_nome, self.id_nome, 
            self.classes, self.metodo, self.ligacao, self.ficheiros, self.titulo, self.elementos, self.botoes)