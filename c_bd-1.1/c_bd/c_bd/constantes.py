from . import app
from os import path
from numpy import concatenate
import pathlib

PASTA_GERAL_PROJETO = "c_bd"
CARATERES_SUBSTITUIR_CAMINHOS_CONFIG = [["/","_"]]
TRANSFORMAR_EM_MAIUSCILAS = True

PASTAS = {
    "static_c_bd_relativa" : f"/{path.relpath(app.static_folder)}/{PASTA_GERAL_PROJETO}",
    "static_c_bd_absoluta" : f"{str(pathlib.Path().resolve())}\\{path.relpath(app.static_folder)}\\{PASTA_GERAL_PROJETO}",
    "relativa_ficheiro" : f"/{path.relpath(__file__)}",
    "absoluta_ficheiro" : f"{str(pathlib.Path(__file__).parent.resolve())}",
    "static_relativa" : f"/{path.relpath(app.static_folder)}",
    "static_absoluta" : f"{path.abspath(app.static_folder)}",
    "projeto" : f"{str(pathlib.Path().resolve())}"
}

CAMINHOS_A_CRIAR = {
    "css" : f"{PASTAS['static_c_bd_relativa']}/css",
    "js" : f"{PASTAS['static_c_bd_relativa']}/js", 
    "dt" : f"{PASTAS['static_c_bd_relativa']}/DataTables",
    "bt" : f"{PASTAS['static_c_bd_relativa']}/bootstrap",
    "bscss" : f"{PASTAS['static_c_bd_relativa']}/bootstrap/css",
    "bsjs" : f"{PASTAS['static_c_bd_relativa']}/bootstrap/js",
    "bsicon" : f"{PASTAS['static_c_bd_relativa']}/bootstrap/icons",
    "tabcss" : f"{PASTAS['static_c_bd_relativa']}/tabulator/css",
    "tabjs" : f"{PASTAS['static_c_bd_relativa']}/tabulator/js"
}

FICHEIROS_NECESSARIOS = {
    "varscss" : CAMINHOS_A_CRIAR['css'] + "/vars.css",
    "formcss" : CAMINHOS_A_CRIAR['css'] + "/formulario.css",
    "ctabcss" : CAMINHOS_A_CRIAR['css'] + "/tabulator.css",
    "bscss" : CAMINHOS_A_CRIAR['bscss'] + "/bootstrap.min.css", #"/bootstrap.min.css",
    "bsjs" : CAMINHOS_A_CRIAR['bsjs'] + "/bootstrap.bundle.min.js",
    "tabcss" : CAMINHOS_A_CRIAR['tabcss'] + "/tabulator.min.css", # "/tabulator_bootstrap5.min.css"
    "tabjs" : CAMINHOS_A_CRIAR['tabjs'] + "/tabulator.js",
    "dtcss" :  CAMINHOS_A_CRIAR['dt'] + "/datatables.min.css",
    "dtbscss" :  CAMINHOS_A_CRIAR['dt'] + "/DataTables-2.0.0/css/dataTables.bootstrap5.min.css",
    "dtjs" : CAMINHOS_A_CRIAR['dt'] + "/datatables.min.js",
    "dtbsjs" : CAMINHOS_A_CRIAR['dt'] + "/DataTables-2.0.0/js/dataTables.bootstrap5.min.js",
    "ttcss" : CAMINHOS_A_CRIAR['css'] + "/tooltips.css",
    "bdcss" : CAMINHOS_A_CRIAR['css'] + "/base_dados.css",
    "bdjs" : CAMINHOS_A_CRIAR['js'] + "/base_dados.js",
    "dbconf" : CAMINHOS_A_CRIAR['js'] + "/datatable_conf.js",
    "jq" : CAMINHOS_A_CRIAR['js'] + "/jquery-3.7.1.js",
    "gerais" : CAMINHOS_A_CRIAR['js'] + "/gerais.js",
    "mdlcss" : CAMINHOS_A_CRIAR['css'] + "/modals.css",
    "mdljs" : CAMINHOS_A_CRIAR['js'] + "/modals.js",
    "b5" : CAMINHOS_A_CRIAR['js'] + "/b5toast.js",
    "mml" : CAMINHOS_A_CRIAR['js'] + "/moment-with-locales.js",
    "mm" : CAMINHOS_A_CRIAR['js'] + "/autoclose_alert.js",
    "ac" : CAMINHOS_A_CRIAR['js'] + "/autoclose_alert.js",
    "cbd" : CAMINHOS_A_CRIAR['js'] + "/classe_bd.js",
    "ttp" : CAMINHOS_A_CRIAR['js'] + "/tooltips.js",
    "fa" : "https://kit.fontawesome.com/807d5b300d.js"
}

ESTRUTURA_CHAMADA_FICHEIRO = {
    "css" : "<link rel='stylesheet' href='__ficheiro__'>",
    "js" : "<script src='__ficheiro__'></script>",
    "js_module" : "<script type='module' src='__ficheiro__'></script>",
    "js_anonymous" : "<script src='__ficheiro__' crossorigin='anonymous'></script>"
}

CHAMADA_FICHEIROS_HEAD = [
    ESTRUTURA_CHAMADA_FICHEIRO["css"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["bscss"]),
    # ESTRUTURA_CHAMADA_FICHEIRO["css"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["varscss"]),
    ESTRUTURA_CHAMADA_FICHEIRO["css"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["mdlcss"]),
    ESTRUTURA_CHAMADA_FICHEIRO["css"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["dtcss"]),
    ESTRUTURA_CHAMADA_FICHEIRO["css"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["dtbscss"]),
    ESTRUTURA_CHAMADA_FICHEIRO["css"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["ttcss"]),
    ESTRUTURA_CHAMADA_FICHEIRO["css"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["formcss"]),
    ESTRUTURA_CHAMADA_FICHEIRO["css"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["bdcss"]),
    ESTRUTURA_CHAMADA_FICHEIRO["js_anonymous"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["fa"]),
    # ESTRUTURA_CHAMADA_FICHEIRO["css"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["ctabcss"]), # style
]

CHAMADA_FICHEIROS_BODY_INICIO = [
    ESTRUTURA_CHAMADA_FICHEIRO["js"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["jq"]),
    ESTRUTURA_CHAMADA_FICHEIRO["js"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["bsjs"]),
    ESTRUTURA_CHAMADA_FICHEIRO["js"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["b5"]),
]

CHAMADA_FICHEIROS_BODY_FIM = [
    ESTRUTURA_CHAMADA_FICHEIRO["js"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["gerais"]),
    ESTRUTURA_CHAMADA_FICHEIRO["js"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["mdljs"]),
    # ESTRUTURA_CHAMADA_FICHEIRO["js"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["tabjs"]),
    ESTRUTURA_CHAMADA_FICHEIRO["js"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["mml"]),
    ESTRUTURA_CHAMADA_FICHEIRO["js"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["mm"]),
    # ESTRUTURA_CHAMADA_FICHEIRO["js"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["ac"]),
    ESTRUTURA_CHAMADA_FICHEIRO["js"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["cbd"]),
    ESTRUTURA_CHAMADA_FICHEIRO["js"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["dtjs"]),
    ESTRUTURA_CHAMADA_FICHEIRO["js"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["dtbsjs"]),
    ESTRUTURA_CHAMADA_FICHEIRO["js_module"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["bdjs"]),
    ESTRUTURA_CHAMADA_FICHEIRO["js"].replace("__ficheiro__", FICHEIROS_NECESSARIOS["ttp"]),
]

CHAMADA_FICHEIROS_TODOS = concatenate((CHAMADA_FICHEIROS_HEAD, CHAMADA_FICHEIROS_BODY_INICIO, CHAMADA_FICHEIROS_BODY_FIM))