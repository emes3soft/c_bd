from typing import Any, Dict, List, Optional, Sequence, Tuple, Union, ValuesView

NUMERO_REGISTOS : str = "SELECT count(*) AS contador FROM __tabela__"
TESTE_EXISTE_TABELA : str = "SHOW TABLE STATUS FROM __base_dados__ WHERE Name = '__tabela__'"
DEVOLVE_CAMPOS_TABELA :str = """
    SELECT A.TABLE_NAME as tabela, A.COLUMN_NAME as nome, A.ORDINAL_POSITION as posicao, A.COLUMN_DEFAULT as valor_por_defeito, (CASE WHEN A.IS_NULLABLE = 'NO' THEN FALSE ELSE TRUE END) as nulo, A.DATA_TYPE as tipo_dados, A.CHARACTER_MAXIMUM_LENGTH as comp_max_texto, A.NUMERIC_PRECISION as precisao_numerica, A.NUMERIC_SCALE as precisao_decimal, A.DATETIME_PRECISION as precisao_data, (CASE WHEN A.COLUMN_KEY = 'PRI' THEN TRUE ELSE FALSE END) as chave_primaria, (CASE WHEN A.EXTRA = 'AUTO_INCREMENT' THEN TRUE ELSE FALSE END) as auto_incremento, (CASE WHEN A.COLUMN_KEY = 'MUL' THEN TRUE ELSE FALSE END) as chave_externa, B.REFERENCED_TABLE_NAME AS chave_externa_tabela, B.REFERENCED_COLUMN_NAME AS chave_externa_campo FROM INFORMATION_SCHEMA.COLUMNS A LEFT JOIN information_schema.KEY_COLUMN_USAGE AS B ON A.TABLE_SCHEMA = B.TABLE_SCHEMA AND A.TABLE_NAME = B.TABLE_NAME AND A.COLUMN_NAME = B.COLUMN_NAME WHERE A.TABLE_SCHEMA = '__base_dados__' AND A.TABLE_NAME IN ('__tabela__') ORDER BY A.TABLE_NAME ASC, A.ORDINAL_POSITION ASC
"""

TIPOS_DE_DADOS = {
    "integer" : ["INT", "TINYINT", "SMALLINT", "MEDIUMINT", "BIGINT", "BIT"],
    "real" : ["FLOAT, DOUBLE, DECIMAL"],
    "text" : ["VARCHAR, CHAR, TINYTEXT, TEXT, MEDIUMTEXT, LONGTEXT, JSON, UUID"],
    "binary" : ["BINARY, VARBINARY, TINYBLOB", "BLOB", "MEDIUMBLOB", "LONGBLOB"],
    "datetime" : ["DATE", "TIME", "YEAR", "DATETIME", "TIMESTAMP"],
}

class ICONS:
    VERDADEIRO = "<i class='fa-solid fa-circle-check text-success'></i>"

CAMPOS_VERDADEIRO_FALSO = "nulo, chave_primaria, auto_incremento, chave_externa, bit"

class ESTRUTURA_TABELA_HTML:
    geral = """
        <div class="row">
            <div class="col-12">
                <table class='t_c_bd_unica table table-sm table-striped border-2 border-black caption-top w-100 text-center my-2'>
                    <caption class='bg-primary text-white fs-4 text-center fw-bold'>__caption__</caption>
                    <thead>__thead__</thead>
                    <tbody>__tbody__</tbody>
                    <tfoot>__tfoot__</tfoot>
                </table>
            </div>
        </div>
    """
    tr = "<tr class='__class_tr__'>__tr__</tr>"
    td = "<td class='__class_td__' colspan='__colspan__'>__td__</td>"
    th = "<th class='text-center bg-dark text-white'>__th__</th>"

    def __init__(self, nome : str, titulos : list, campos : list):
        self.nome = nome
        self.titulos = titulos
        self.campos = campos
        self.html = self.construir_tabela()

    class CORES:
        chave_primaria = "bg-info text-black"
        chave_externa = "bg-warning text-black"
        tfoot = "bg-secondary text-white"

    def substituir_tr(self, classe, conteudo):
        return self.tr.replace("__class_tr__", classe).replace("__tr__", conteudo)
    
    def substituir_td(self, classe, colspan, conteudo, nome_coluna, chaves : list):
        conteudo = ICONS.VERDADEIRO if nome_coluna in CAMPOS_VERDADEIRO_FALSO and nome_coluna else conteudo
        if len(chaves) > 0:
            classe += (" " + self.CORES.chave_primaria) if chaves[0] == 1 else (self.CORES.chave_externa if chaves[1] == 1 else "")
        return self.td.replace("__class_td__", classe).replace("__td__", str(conteudo) if conteudo else "").replace("__colspan__", str(colspan))
    
    def substituir_th(self, conteudo):
        return self.th.replace("__th__", conteudo)
    
    def construir_tabela(self):
        html = self.geral.replace("__caption__", f"{self.nome.upper()}")

        colunas = ""
        for t in self.titulos:
            colunas += self.substituir_th(t.upper())
        linhas = self.substituir_tr("", colunas)
        html = html.replace("__thead__", linhas)

        linhas = ""
        for l in self.campos:
            colunas = ""
            chaves = [l.chave_primaria, l.chave_externa] 
            for c in l.__dict__:
                colunas += self.substituir_td("", "", l.__dict__[c],c, chaves)
            linhas += self.substituir_tr("", colunas)
        html = html.replace("__tbody__", linhas)

        
        html = html.replace("__tfoot__", self.substituir_tr("" , self.substituir_td(self.CORES.tfoot, len(self.titulos), f"Nº REGISTOS: {len(self.campos)}", "", [])))
        return html

class CAMPOS_TABELA:
    separador : str = ","
    limitador : str = "'"

class CAMPOS:
    nome : str = None
    posicao : int = 0
    valor_por_defeito : str = None
    nulo : bool = False # YES ou NO
    tipo_dados : str = None
    comp_max_texto : int = 0
    precisao_numerica : int = 0
    precisao_decimal : int = 0
    precisao_data : str = None
    chave_primaria : bool = False # PRI
    auto_incremento : bool = None # AUTO_INCREMENT
    chave_externa : bool = False # MULT
    chave_externa_tabela : str = None
    chave_externa_campo : str = None

    def __init__(self, **kargs):
        for k, v in kargs.items():
            setattr(self, k, v)
