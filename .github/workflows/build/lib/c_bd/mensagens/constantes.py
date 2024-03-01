from typing import Any, Dict, List, Optional, Sequence, Tuple, Union, ValuesView

# CNX_POOL_ARGS: Tuple[str, str, str] = ("pool_name", "pool_size", "pool_reset_session")

# class ERROS:
#     erro = {
#         "1000" : "Sem conexão!",
#         "1001" : "Conexão não definida!",
#         "1004" : "Aplicação não definida! Código a incluir (exemplo): <b>bd_app = init_app()</b>",
#         "1005" : "A variável indicada não corresponde a um comando!",
#         "1010" : "Falta especificar a(s) tabela(s)!",
#         "1011" : "A(s) tabela(s) <b>__tabelas__</b> especificada no comando não existe!",
#         "1012" : "A tabela <b>__tabela__</b> não tem campos definidos!",
#         "1020" : "Os campos <b>__campos__</b> não existem na tabela <b>__tabela__</b>!",
#         "1021" : "Falta especificar o(s) campos(s) para a(s) tabela(s) <b>__tabela__</b>!",
#         "1022" : "Não foram especificados campos(s) para a(s) tabela(s) <b>__tabela__</b>!",
#         "1030" : "Falta especificar os valores para os campos da tabela <b>__tabela__!</b>",
#         "1031" : "O nº de campos <b>(__ncampos__)</b> não coinside com o nº de valores <b>(__nvalores__)</b>",
#         "1035" : "Falta especificar a(s) condições para tabela <b>__tabela__!</b>",
#         "1040" : "O comando não corresponde a um comando INSERT!",
#         "1041" : "O comando não corresponde a um comando UPDATE!",
#         "1042" : "O comando não corresponde a um comando DELETE!",
#         "1043" : "O comando não corresponde a um comando SELECT!",
#         "1044" : "Não especificou um comando!",
#         "1045" : "Não corresponde a nenhum comando válido!",
#         "1046" : "Os comandos INSERT, UPDATE e DELETE só permitem utilizar uma tabela!",
#         "1047" : "A classe COMANDOS está desativada!",
#         "1048" : "O comando não corresponde a um comando SELECT!",
#     }

#     avisos = {
        
#     }

#     sucessos = {
        
#     }
    
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
    toast : str = """
        <script>
            b5toast.mostrar("__classe__", "__mensagem__", "__icon__ __titulo__", __duracao__)
        </script>
        """
    alerta : str = """
        <div class='auto-close alert alert-__classe__ alert-dismissible fade show' data-duracao='__duracao__'>
            <div class='fw-bold'>__icon__  __titulo__</div> 
            __mensagem__ 
            <button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button>
        </div>
    """

class GERAIS:
    duracao = 5000
    estilo_predef = ESTILOS.toast

MENSAGENS : Dict[str, Tuple[str, TIPOS, str]] = {
    "1000" : [GERAIS.estilo_predef, TIPOS.erro, "Sem conexão!"],
    "1001" : [GERAIS.estilo_predef, TIPOS.erro, "Conexão não definida!"],
    "1004" : [GERAIS.estilo_predef, TIPOS.erro, "Aplicação não definida! Código a incluir (exemplo): <b>bd_app = init_app()</b>"],
    "1005" : [GERAIS.estilo_predef, TIPOS.erro, "A variável indicada não corresponde a um comando!"],
    "1010" : [GERAIS.estilo_predef, TIPOS.erro, "Falta especificar a(s) tabela(s)!"],
    "1011" : [GERAIS.estilo_predef, TIPOS.erro, "A(s) tabela(s) <b>__tabelas__</b> especificada no comando não existe!"],
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
}
