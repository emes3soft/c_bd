from .constantes import CAMPOS, CAMPOS_TABELA, TESTE_EXISTE_TABELA, DEVOLVE_CAMPOS_TABELA, NUMERO_REGISTOS, CAMPOS_VERDADEIRO_FALSO, ESTRUTURA_TABELA_HTML as ETH, ICONS
from ..mensagens.mensagem import cria_mensagem, MENSAGENS as M, apresenta_caixa_mensagens
from ..mensagens.constantes import TIPOS as MT

from mysql.connector import errors
import inspect as i
from array import *

def limpar_tabelas(tbls = None):
    if not tbls:
        return False

    if not isinstance(tbls, TABELAS):
        return False
    
    l = tbls.__init__()
    return l

def cria_info_tabelas(conexao= None, tabelas : str = None):
    tbls = None
    tbls = TABELAS(conexao, tabelas)
    return tbls

def cria_html_tabelas(conexao= None, tabelas : str = None):
    html = ""

    tbls = TABELAS(conexao, tabelas)

    # apresenta_caixa_mensagens(texto_mensagem=f"Tabelas corretas: {len(tbls.__tabelas__.corretas)}")

    for t in tbls.__tabelas__.corretas:
        html += tbls.TABELA_UNICA(conexao, t).tabela_unica_html()

    return html

class TABELAS:
    __tabelas__ = None
    con = None
    nomes : str = None
    tabelas : array = []

    def __init__(self, conexao = None, tabelas : str = None):
        self.__tabelas__ = self.TABELAS_VERIFICACAO

        if not conexao: 
            cria_mensagem(1000, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
        elif not tabelas:
            cria_mensagem(1010, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
        else:
            self.con = conexao
            self.nomes = tabelas
            self.tabelas = self.cria_informacao_tabelas()
            # eliminar a conexao da classe TABELAS
            delattr(self, 'con')

    def verifica_tabelas_existem(self):
        tabelas : str = self.nomes
        self.__tabelas__.incorretas=[]
        self.__tabelas__.incorretas_texto = ""
        self.__tabelas__.corretas=[]
        self.__tabelas__.incorretas_texto = ""
        
        tabelas = tabelas.strip()
        tabelas = tabelas.split(CAMPOS_TABELA.separador)

        for t in tabelas:
            t = t.strip().split(" ")
            if len(t) == 1: t.append(None)

            # apresenta_caixa_mensagens(texto_mensagem="TABELAS: " + str(self.con.ligacao))

            cmd = TESTE_EXISTE_TABELA.replace("__base_dados__", self.con.ligacao["database"]).replace("__tabela__", t[0])
            self.con.cursor.execute(cmd)
            self.con.cursor.fetchall()

            if not self.con.cursor.rowcount or self.con.cursor.rowcount == 0:
                self.__tabelas__.incorretas.append([t[0], t[1] if t[1] else None])
                self.__tabelas__.incorretas_texto += t[0] if not self.__tabelas__.incorretas_texto else f", {t[0]}"
            else:
                self.__tabelas__.corretas.append([t[0], t[1] if t[1] else None])
                self.__tabelas__.corretas_texto += t[0] if not self.__tabelas__.corretas_texto else f", {t[0]}"

        self.__tabelas__.num_corretas = len(self.__tabelas__.corretas)
        self.__tabelas__.num_incorretas = len(self.__tabelas__.incorretas)

        if self.__tabelas__.num_incorretas > 0:
            cria_mensagem(1011, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}", self.__tabelas__.incorretas_texto)
            
    def cria_informacao_tabelas(self):
        tbls = []
        self.verifica_tabelas_existem()

        if len(self.__tabelas__.corretas) == 0:
            return None
        else:
            for t in self.__tabelas__.corretas:
                tbls.append(self.TABELA_UNICA(self.con, t))

        # apresenta_caixa_mensagens(texto_mensagem=str((tbls)))
        return tbls
    
    class TABELAS_VERIFICACAO:
        corretas : array = []
        corretas_texto : str = ""
        num_corretas = None
        incorretas : array = []
        incorretas_texto : str = ""
        num_incorretas = None

        def __init__(self):
            self.corretas = []
            self.corretas_texto = ""
            self.num_corretas = 0
            self.incorretas = []
            self.incorretas_texto = ""
            self.num_incorretas = 0

    class TABELA_UNICA():
        con = None
        nome : str = None
        apelido : str = None
        num_campos : int = None
        num_registos : int = None
        campos : list = []
        titulos : list = []
        campos_lista_str : str = ""
        campos_sem_chave_primaria : str = ""
        campos_sem_auto_increment : str = ""

        def __init__(self, conexao, tabela : list = None):
            self.con = conexao
            self.nome : str = tabela[0]
            self.apelido : str = tabela[1]
            self.num_campos = 0
            self.num_registos : int = 0
            self.campos_lista_str : str = ""
            self.campos_sem_chave_primaria : str = ""
            self.campos_sem_auto_increment : str = ""
            self.cria_estrutura_tabela()
            delattr(self, 'con')
                
        def cria_estrutura_tabela(self):
            cmd = DEVOLVE_CAMPOS_TABELA.replace("__base_dados__", self.con.ligacao["database"]).replace("__tabela__", self.nome)

            try:
                self.titulos = []
                self.con.cursor.execute(cmd)
                tbl_campos = self.con.cursor.fetchall()
                # num_fields = len( self.con.cursor.description)
                #field_names = [i[0] for i in  self.con.cursor.description]
                self.titulos = [i[0] for i in  self.con.cursor.description]

                if not tbl_campos:
                    return None

                self.num_campos = len(tbl_campos)
                # apresenta_caixa_mensagens(texto_mensagem=f"Nº de campos: {len(tbl_campos)}")
                if self.num_campos > 0:
                    self.existe = True
                    self.campos = []

                    for c in tbl_campos:
                        self.campos.append(CAMPOS(**c))
                        self.campos_lista_str += f",{c["nome"]}" if self.campos_lista_str else c["nome"]
                        if not c["chave_primaria"]:
                            self.campos_sem_chave_primaria += f",{c["nome"]}" if self.campos_sem_chave_primaria else c["nome"]
                        if not c["auto_incremento"]:
                            self.campos_sem_auto_increment += f",{c["nome"]}" if self.campos_sem_auto_increment else c["nome"]

                    #apresenta_caixa_mensagens(texto_mensagem=str(self.campos))

                    cmd = NUMERO_REGISTOS.replace("__tabela__", self.nome)
                    self.con.cursor.execute(cmd)
                    num_registos = self.con.cursor.fetchall()

                    self.num_registos = num_registos[0]

                    cmd = NUMERO_REGISTOS.replace("__tabela__", self.nome)

                    self.con.cursor.execute(cmd)
                    self.num_registos = self.con.cursor.fetchone()["contador"]
                else:
                    self.existe = False
                    self.campos = []
                    self.num_registos = 0
                    self.num_campos = 0

                    cria_mensagem(1013, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            except errors.Error as e:
                    cria_mensagem(1012, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
        
        def tabela_unica_html(self):
            if not self.nome:
                cria_mensagem(1010, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
                return False

            tabela = ETH(f"{self.nome.capitalize()} {self.apelido.upper()}", self.titulos, self.campos)

            return ETH(f"{self.nome.capitalize()} {self.apelido.upper()}", self.titulos, self.campos).html
