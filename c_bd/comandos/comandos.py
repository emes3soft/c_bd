from ..mensagens.mensagem import MENSAGENS as M, apresenta_caixa_mensagens, cria_mensagem, tem_mensagens
from ..mensagens.constantes import TIPOS as MT
from ..tabelas.tabelas import TABELAS as T
from ..tabelas.constantes import CAMPOS_TABELA as TC
from ..conexao import CONEXAO
from mysql.connector import errors as ER
import inspect as i

def limpa_objecto_caracteres(objeto : object, caracteres: list = [' '], converte_em_lista : bool = False):
    if caracteres and (isinstance(objeto, str) or isinstance(objeto, list)):
        if isinstance(objeto, str):
            list_objeto = objeto.split(",")

        for k,v in enumerate(list_objeto):
            if v.strip():
                for cs in caracteres:
                    valor = v

                    if v[0] in caracteres:
                        valor = valor[1:]
                    if v[len(v)-1] in caracteres:
                        valor = valor[:-1]
                
                list_objeto[k] = f"'{valor.strip()}'"

        if converte_em_lista:
            return list_objeto
        else:
            temp_str = ""
            for elem in list_objeto:
                if elem.strip():
                    temp_str += elem.strip() + ","

            return temp_str[:-1]

def limpar_comandos():
    limpar = []
    return limpar

from .constantes import REGISTOS_AFETADOS

class COMANDOS:
    comandos = None
    num_registos_afetados : REGISTOS_AFETADOS = None
    comando_sql_final = None
    executado = False
    sucesso = False

    def __init__(self, conexao):
        self.con = conexao
        self.comandos : list = []
        self.num_registos_afetados : REGISTOS_AFETADOS = REGISTOS_AFETADOS
        self.comando_sql_final : str = ""
        self.executado : bool = False
        # delattr(self, "con")
    
    def adiciona_comando(self, comando):
        if isinstance(comando,CMD_DELETE) or isinstance(comando,CMD_UPDATE) or \
            isinstance(comando,CMD_INSERT) or isinstance(comando,CMD_SELECT):
            self.comandos.append(comando)
            
            self.comando_sql_final += ("; " if self.comando_sql_final else "") + comando.comando_sql
        else:
            cria_mensagem(1045, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")

    def limpar_comandos(self):
        self.comandos : list = []
        self.num_registos_afetados : int = 0
        self.comando_sql_final : str = ""
        self.executado : bool = False

    def executar_comandos(self):
        self.executado = False
        self.sucesso = False
        
        if len(self.comandos):
            cria_mensagem(1044, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            return None
        
        self.executado = True
        for p, c in enumerate(self.comandos):
            commit = False if p < len(self.comandos)-1 else True
            
            executar_comando(self.con, c, commit)

            if tem_mensagens():
                self.con.rollback()
                return None

        self.sucesso = True

class CMD_INSERT:
    nome : str = "INSERT"
    obrigatorios : str = "tabela, valores"
    estrutura : str = "INSERT INTO __tabela__ __campos__ VALUES (__valores__)"
    tabelas : str = None
    info_tabelas = None
    campos : str = None
    campos_num : int = 0
    valores : str = None
    valores_num : int = 0
    comando_sql : str = None
    executado : bool = False
    sucesso : bool = False
    num_registos_afetados : int = 0

    def __init__(self, conexao, tabela = None, campos = None, valores = None):
        self.conexao = conexao
        self.tabelas = tabela
        self.campos = campos
        self.valores = valores
        self.cria_comando()
        delattr(self, 'conexao')

    def cria_comando(self):
        if not self.tabelas:
            cria_mensagem(1010, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            return None
        
        if len(self.tabelas.split(TC.separador)) > 1:
            cria_mensagem(1046, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            return None
        
        if not self.campos:
            cria_mensagem(1022, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            return None
        
        if not self.valores:
            cod_msg = "1030"
            cria_mensagem(1030, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            return None
        
        self.info_tabelas = T(self.conexao, self.tabelas).tabelas[0].__dict__

        self.campos = limpa_objecto_caracteres(self.campos, [" ","'",'"'])
        self.valores = limpa_objecto_caracteres(self.valores, [" ","'",'"'])

        if not self.campos or self.campos == "*":
            self.campos = f"({self.info_tabelas["campos_sem_auto_increment"]})"
        else:
            self.campos = f"({self.campos})"

        self.campos_num = len(self.campos.split(','))
        self.valores_num = len(self.valores.split(','))

        if self.campos_num != self.valores_num:
            cria_mensagem(1031, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")

        self.comando_sql = self.estrutura.replace("__tabela__", self.tabelas).replace("__campos__", self.campos).replace("__valores__", self.valores)

class CMD_UPDATE:
    nome : str = "UPDATE"
    estrutura : str = "UPDATE __tabela__ SET __campos_e_valores__ WHERE __condicoes__"
    obrigatorios : str = "*"
    tabelas : str= None
    info_tabelas = None
    campos : str = None
    campos_num : int = 0
    valores : str = None
    valores_num : int = 0
    condicoes : str = None
    comando_sql : str = None
    executado : bool = False
    sucesso : bool = False
    num_registos_afetados : int = 0

    def __init__(self, conexao, tabela, campos, valores, condicoes):
        self.conexao = conexao
        self.tabelas = tabela
        self.campos = campos
        self.valores = valores
        self.condicoes = condicoes
        self.cria_comando()
        delattr(self, 'conexao')

    def cria_comando(self):
        if not self.tabelas:
            cria_mensagem(1010, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            return None
        
        if len(self.tabelas.split(TC.separador)) > 1:
            cria_mensagem(1046, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            return None
        
        if not self.campos:
            cria_mensagem(1021, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            return None
        
        if not self.valores:
            cria_mensagem(1030, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            return None
        
        if not self.condicoes:
            cria_mensagem(1035, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            return None
        
        campos = self.campos.split(",")
        valores = self.valores.split(",")
        
        if len(campos) != len(valores):
            cria_mensagem(1035, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            return None

        self.campos = limpa_objecto_caracteres(self.campos, [" ","'"], True)
        self.valores = limpa_objecto_caracteres(self.valores, [" ","'"], True)

        self.campos_num = len(self.campos)
        self.valores_num = len(self.valores)

        campos_valores = ""

        for k,v in enumerate(self.campos):
            campos_valores += f"{self.campos[k]}={self.valores[k]}, "

        self.info_tabelas = T(self.conexao, self.tabelas).tabelas[0].__dict__
        self.comando_sql = self.estrutura.replace("__tabela__", self.tabelas).replace("__campos_e_valores__", campos_valores[:-2])\
            .replace("__condicoes__", self.condicoes)

class CMD_DELETE:
    nome : str = "DELETE"
    estrutura : str = "DELETE FROM __tabela__ WHERE __condicoes__"
    obrigatorios : str = "*"
    tabelas : str = None
    info_tabelas = None
    condicoes : str = None
    executado : bool = False
    sucesso : bool = False
    num_registos_afetados : int = 0

    def __init__(self, conexao, tabela, condicoes):
        self.conexao = conexao
        self.tabelas = tabela
        self.condicoes = condicoes
        self.cria_comando()
        delattr(self, 'conexao')


    def cria_comando(self):
        if not self.tabelas:
            cria_mensagem(1010, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            return None
        
        if len(self.tabelas.split(TC.separador_campos_tabelas)) > 1:
            cria_mensagem(1046, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            return None
        
        if not self.condicoes:
            cria_mensagem(1035, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            return None
        
        self.info_tabelas = T(self.conexao, self.tabelas).tabelas[0].__dict__
        self.comando_sql = self.estrutura.replace("__tabela__", self.tabelas).replace("__condicoes__", self.condicoes)

class LIMITES:
    comeca_em : int = 0
    num_ppagina : int = 0
    texto : str = ""

    def __init__(self, comeca_em = None, num_ppagina = None):
        self.comeca_em = int(comeca_em)
        self.num_ppagina = int(num_ppagina)
        self.texto = f" LIMIT {comeca_em}, {num_ppagina}" if not comeca_em is None and not num_ppagina is None else ""

class CMD_SELECT:
    nome : str = "SELECT"
    obrigatorios : str = "campos, tabelas"
    campos : str = None
    nomes_campos : str = None
    tabelas : str = None
    info_tabelas = []
    joins : str = None
    condicoes : str = None
    groupby : str = None
    having : str = None
    orderby : str = None
    estrutura = "SELECT __campos__ FROM __tabelas__ __joins__ __condicoes__ __groupby__ __having__ __orderby__ __limites__"
    registos = []
    campos_comando = []
    executado : bool = False
    sucesso : bool = False
    limites : str = None
    num_registos_afetados : int = 0

    def __init__(self, conexao : CONEXAO, tabelas : str, campos : str = "*", nomes_campos : str = None, joins : str = None, condicoes : str = None, 
        groupby : str = None, having : str = None, orderby : str = None, limites : str = None):
        
        self.conexao = conexao
        self.tabelas = tabelas.strip(" ")
        self.campos = campos.strip(" ") if campos else ""
        self.nomes_campos = nomes_campos.strip(" ") if nomes_campos else ""        
        self.joins = joins.strip(" ") if joins else ""
        self.condicoes = " WHERE " + condicoes.strip(" ") if condicoes else ""
        self.groupby = " GROUP BY " + groupby.strip(" ") if groupby else ""
        self.having = " HAVING " + having.strip(" ") if having else ""
        self.orderby = " ORDER BY " + orderby.strip(" ") if orderby else ""
        self.limites = " LIMIT " + limites.strip() if limites else ""
        self.cria_comando()
        delattr(self, 'conexao')

    def cria_comando(self):
        if not self.conexao.conetado:
            cria_mensagem(1000, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            return None

        if not self.tabelas:
            cria_mensagem(1010, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            return None
        
        campos = ""
        tabelas = [t.strip() for t in self.tabelas.split(TC.separador)]

        tbls_joins = []
        # Verifica se existem joins
        if self.joins:
            joins = [j.strip() for j in self.joins.split(TC.separador)]
            texto_join_a_procurar = "join "
            texto_on_a_procurar = " on"

            for j in joins:
                pos = [j.lower().find(texto_join_a_procurar), j.lower().find(texto_on_a_procurar)]

                if pos[0] != -1 and pos[1] != -1:
                    pos[0] += len(texto_join_a_procurar)

                    tbls_joins.append(j[pos[0], pos[1]].strip())
                else:
                    cria_mensagem(1070, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}",j)

        tabelas += tbls_joins

        # Ir buscar informações à tabela caso seja *

        if isinstance(tabelas, list):
            temp_tabelas = []
            for t in tabelas:
                t = t.strip()
                temp_tabela = T(self.conexao, t).tabelas
                
                if temp_tabela:
                    temp_tabelas.append(temp_tabela[0].__dict__)
                    # if not self.campos or not self.campos:
                tbl_aplido = t.split(' ')[1] if len(t.split(" ")) > 1 else t
                
                if tbl_aplido[0] and not campos:
                    self.campos += f", {tbl_aplido}.*"
            
            self.info_tabelas = temp_tabelas
            # apresenta_caixa_mensagens(texto_mensagem="Tabelas: \n" + str(temp_tabelas))
        else:
            self.info_tabelas = T(self.conexao, self.tabelas).tabelas[0].__dict__
        
        # apresenta_caixa_mensagens(texto_mensagem=str(self.info_tabelas)) # [0]["campos"][0].nome))
        if len(self.info_tabelas) == 0:
            cria_mensagem(1010, f"{i.stack()[1][3].upper()} - {self.__class__.__name__}")
            return None

        lista_campos = ""
        if "*" in self.campos:
            for campo in self.info_tabelas[0]["campos"]:
                if "data" in campo.nome.lower():
                    lista_campos += f"DATE_FORMAT({self.info_tabelas[0]["apelido"]}.{campo.nome}, '%d/%m/%Y') AS {campo.nome},"
                else:
                    lista_campos += f"{self.info_tabelas[0]["apelido"]}.{campo.nome},"
            lista_campos = lista_campos[:-1].split(TC.separador)
        else:
            lista_campos = self.campos.split(TC.separador)

        print(f"************** {str(lista_campos)} **************")

        lista_nomes_campos = self.nomes_campos.split(TC.separador)

        # apresenta_caixa_mensagens(texto_mensagem=str(lista_nomes_campos))

        for p,c in enumerate(lista_campos):
            # apresenta_caixa_mensagens(texto_mensagem=str(f"p={p} -- tamanho lista nomes: {len(lista_nomes_campos)-1}"))
            if  p < len(lista_nomes_campos)-1:
                campos += f"{c} AS '{lista_nomes_campos[p].strip()}', "
            else:
                campos += f"{c}, "

        self.campos = campos[:-2]

        if not tem_mensagens():
            self.comando_sql = self.estrutura.replace("__campos__", self.campos).replace("__tabelas__", self.tabelas)\
                .replace("__joins__", " " + self.joins).replace("__condicoes__", self.condicoes)\
                .replace("__groupby__", " " + self.groupby).replace("__having__", " " + self.having)\
                .replace("__orderby__", " " + self.orderby).replace("__limites__", " " + self.limites)
        else:
            self.comando_sql = None

def executar_comando(conexao, comando : object, execucao_automatica : bool = True):
    """
        Função para executar um comando, com ou sem execução automatica\n
        -> conexao - variavél correspondente à conexão\n
        -> comando - comando expecífico (CMD_INSERT, CMD_UPDATE, CMD_DELETE, CMD_SELECT')\n
        -> execucao_automática\n
            -> Verdadeiro se optar por executar o comando no imediato - por defeito (autocommit = True)\n
            -> Falso se necessitar de executar vários comando e só confirmar no final (autocommit = False)\n
    """
    from ..conexao import CONEXAO as C

    if not isinstance(conexao, C):
        cria_mensagem(1000, f"{i.stack()[1][3].upper()} - {__name__}")
        return None
        
    if isinstance(comando, COMANDOS):
        cria_mensagem(1047, f"{i.stack()[1][3].upper()} - {__name__}")
        return None
    
    if isinstance(comando,CMD_DELETE) or isinstance(comando,CMD_UPDATE) or \
        isinstance(comando,CMD_INSERT) or isinstance(comando,CMD_SELECT):
        if hasattr(comando, "comando_sql"):
            con = conexao
            
            if not isinstance(execucao_automatica, bool):
                execucao_automatica = True

            try:
                comando.executado = True
                con.cursor.execute(comando.comando_sql)

                if isinstance(comando,CMD_SELECT): 
                    comando.registos = con.cursor.fetchall()
                    # Testar se existem datas e efetuar a conversão
                    # comando.info_tabelas.tabelas
                    

                comando.num_registos_afetados = con.cursor.rowcount
                comando.campos_comando = [i[0] for i in  con.cursor.description]

                if not con.conexao.autocommit and execucao_automatica: 
                    con.conexao.commit()

                comando.sucesso = True
            except ER.Error as e:
                if not con.autocommit and execucao_automatica: 
                    con.conexao.rollback()
                comando.num_registos_afetados = 0
                comando.sucesso = False

                cod_msg = f"MSQL {str(e.errno)}"
                nova_msg = M(tipo_mensagem=MT.erro,
                    codigo_mensagem=cod_msg, titulo_mensagem=f"{i.stack()[1][3].upper()} - {__name__}",
                    texto_mensagem=f"{e.msg}")
                cria_mensagem(nova_msg) 
        else:
            cria_mensagem(1049, f"{i.stack()[1][3].upper()} - {__name__}")
    else:
        cria_mensagem(1045, f"{i.stack()[1][3].upper()} - {__name__}")

def executar_comandos():
    return