from typing import Any, Dict, List, Optional, Sequence, Tuple, Union, ValuesView

class DETALHES:
    tipo : str = None
    classe : str = None
    titulo : str = None
    icon : str = None

    def __init__ (self, tipo, classe, titulo, icon):
        self.tipo = tipo
        self.classe = classe
        self.titulo = titulo
        self.icon = icon

class TIPOS:
    erro = DETALHES("e", "danger", "ERRO __codigo__ (__comando__)", "<i class='fa-solid fa-circle-xmark'></i>")
    sucesso = DETALHES("s", "success", "SUCESSO __codigo__ (__comando__)", "<i class='fa-solid fa-circle-check'></i>")
    informacao = DETALHES("i", "info", "INFORMAÇÃO __codigo__ (__comando__)", "<i class='fa-solid fa-circle-info'></i>")
    aviso = DETALHES("a", "warning", "AVISO __codigo__ (__comando__)" , "<i class='fa-solid fa-circle-exclamation'></i>")
    destaque = DETALHES("d", "primary", "DESTAQUE __codigo__ (__comando__)", "<i class='fa-solid fa-circle-info'></i>")
    escuro = DETALHES("c", "info", "INFORMAÇÃO __codigo__ (__comando__)", "<i class='fa-solid fa-circle-info'></i>")
    cinza = DETALHES("z", "info", "INFORMAÇÃO __codigo__ (__comando__)", "<i class='fa-solid fa-circle-info'></i>")

    def __init__(self): 
        self.todos = [x.tipo for x in self]

class ESTILOS:
    toast : str = """<script>b5toast.mostrar("__classe__", "__mensagem__", "__icon__ __titulo__", __duracao__)</script>"""
    alerta : str = """
        <div class='auto-close alert alert-__classe__ alert-dismissible fade show' data-duracao='__duracao__'>
            <div class='fw-bold'>__icon__  __titulo__</div> 
            __mensagem__ 
            <button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button>
        </div>
    """

class GERAIS:
    duracao_entre_mensagens = 2000
    duracao_minima = 3500
    duracao = 5000
    estilo_predef = ESTILOS.toast

MENSAGENS : Dict[str, Tuple[str, TIPOS, str]] = {
    # ERROS CONEXÃO
    "1000" : [GERAIS.estilo_predef, TIPOS.erro, "Sem conexão!"],
    "1001" : [GERAIS.estilo_predef, TIPOS.erro, "Conexão não definida!"],
    "1002" : [GERAIS.estilo_predef, TIPOS.erro, "Ligação não definida!"],
    "1003" : [GERAIS.estilo_predef, TIPOS.erro, "Problemas na configuração da ligação!"],
    "1004" : [GERAIS.estilo_predef, TIPOS.erro, "Aplicação não definida! Código a incluir (exemplo): <b>bd_app = init_app()</b>"],
    "1005" : [GERAIS.estilo_predef, TIPOS.erro, "A variável indicada não corresponde a um comando!"],
    "1010" : [GERAIS.estilo_predef, TIPOS.erro, "Falta especificar a(s) tabela(s)!"],
    "1011" : [GERAIS.estilo_predef, TIPOS.erro, "A(s) tabela(s) <b>{}</b> especificada no comando não existe!"],
    "1012" : [GERAIS.estilo_predef, TIPOS.erro, "A tabela <b>__tabela__</b> não tem campos definidos!"],
    "1020" : [GERAIS.estilo_predef, TIPOS.erro, "Os campos <b>__campos__</b> não existem na tabela <b>__tabela__</b>!"],
    "1021" : [GERAIS.estilo_predef, TIPOS.erro, "Falta especificar o(s) campos(s) para a(s) tabela(s) <b>__tabela__</b>!"],
    "1022" : [GERAIS.estilo_predef, TIPOS.erro, "Não foram especificados campos(s) para a(s) tabela(s) <b>__tabela__</b>!"],
    "1030" : [GERAIS.estilo_predef, TIPOS.erro, "Falta especificar os valores para os campos da tabela <b>__tabela__!</b>"],
    "1031" : [GERAIS.estilo_predef, TIPOS.erro, "O nº de campos <b>(__ncampos__)</b> não coinside com o nº de valores <b>(__nvalores__)</b>"],
    "1035" : [GERAIS.estilo_predef, TIPOS.erro, "Falta especificar a(s) condições para tabela <b>__tabela__!</b>"],
    "1040" : [GERAIS.estilo_predef, TIPOS.erro, "O comando não corresponde a um comando INSERT!"],
    "1041" : [GERAIS.estilo_predef, TIPOS.erro, "O comando não corresponde a um comando UPDATE!"],
    "1042" : [GERAIS.estilo_predef, TIPOS.erro, "O comando não corresponde a um comando DELETE!"],
    "1043" : [GERAIS.estilo_predef, TIPOS.erro, "O comando não corresponde a um comando SELECT!"],
    "1044" : [GERAIS.estilo_predef, TIPOS.erro, "Não especificou um comando!"],
    "1045" : [GERAIS.estilo_predef, TIPOS.erro, "Não corresponde a nenhum comando válido!"],
    "1046" : [GERAIS.estilo_predef, TIPOS.erro, "Os comandos INSERT, UPDATE e DELETE só permitem utilizar uma tabela!"],
    "1047" : [GERAIS.estilo_predef, TIPOS.erro, "A classe COMANDOS está desativada!"],
    "1048" : [GERAIS.estilo_predef, TIPOS.erro, "O comando não corresponde a um comando SELECT!"],
    "1049" : [GERAIS.estilo_predef, TIPOS.erro, "Não foi possível encontrar um comando sql!"],
    "1060" : [GERAIS.estilo_predef, TIPOS.erro, "Não foi possível criar a tabela. O comando ainda não se encontra executado!"],
    "1070" : [GERAIS.estilo_predef, TIPOS.erro, "JOIN detetado com falha de parâmetros: {}!"],
    # ERROS FORMULARIO
    "2000" : [GERAIS.estilo_predef, TIPOS.erro, "Falha na declaração da linha a que pertence o elemento!"],
    "2001" : [GERAIS.estilo_predef, TIPOS.erro, "A linha tem de ser maior ou igual a 1 para o elemento!"],
    "2002" : [GERAIS.estilo_predef, TIPOS.erro, "Falha na declaração do tipo de elemento!"],
    "2003" : [GERAIS.estilo_predef, TIPOS.erro, "Falha na declaração do id_nome do elemento!"],
    "2004" : [GERAIS.estilo_predef, TIPOS.erro, "Falha na declaração da ligação (action) do formulário!"],
    "2010" : [GERAIS.estilo_predef, TIPOS.erro, "Falha na declaração das informações da tabela!\nDefina uma de duas situações:\n" + \
            "Situação 1:\n\t[conexão, nome da tabela, campos valor, campos texto, condições tabela]\n" + \
            "Situação 2:\n\t[registos da tabela, campos valor, campos texto]!"],
    "2011" : [GERAIS.estilo_predef, TIPOS.erro, "A declaração das informações da tabela não se enquadra em nenuma das situações válidas!" + \
            "\nDefina uma de duas situações:\n" + \
            "Situação 1:\n\t[conexão, nome da tabela, campos valor, campos texto, condições tabela]\n" + \
            "Situação 2:\n\t[registos da tabela, campos valor, campos texto]!"],
    "2015" : [GERAIS.estilo_predef, TIPOS.erro, "O primeiro elemento de informacoes_tabela deve ser uma lista, mesmo que vazia!"],
    "2016" : [GERAIS.estilo_predef, TIPOS.erro, "O(s) campo(s) {0} não existe(m) nos registos!"],
    "2020" : [GERAIS.estilo_predef, TIPOS.erro, "O primeiro valor da lista de informações da tabela tem de ser uma conexao válida!"],
    "2021" : [GERAIS.estilo_predef, TIPOS.erro, "A conexão relativa ao primeiro valor da lista de informações da tabela não conetada!"],
    "2022" : [GERAIS.estilo_predef, TIPOS.erro, "Tem de escrever o nome da tabela válida!"],
    "2023" : [GERAIS.estilo_predef, TIPOS.erro, "Comando executado sem sucesso!"],
    "2024" : [GERAIS.estilo_predef, TIPOS.erro, "O(s) campo(s) {0} não existe(m) na tabela {1}!"],
    "2024" : [GERAIS.estilo_predef, TIPOS.erro, "O(s) campo(s) {0} não existe(m) na tabela {1}!"],
    # ENCRIPTAÇÃO
    "8000" : [GERAIS.estilo_predef, TIPOS.erro, "O ficheiro {} não existe!"],
    "8001" : [GERAIS.estilo_predef, TIPOS.erro, "A identificação do ficheiro {} não existe!"],
    "8002" : [GERAIS.estilo_predef, TIPOS.erro, "O ficheiro de configuração não tem qualquer informação!"],
    "8003" : [GERAIS.estilo_predef, TIPOS.erro, "No ficheiro de configuração existem problemas de configuração!"],
    # GERAIS
    "9000" : [GERAIS.estilo_predef, TIPOS.erro, "Aplicação flask não iniciada!"],
}
