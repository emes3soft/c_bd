from ..mensagens.mensagem_popup import apresenta_caixa_mensagens
from ..mensagens.constantes import ESTILOS, TIPOS
from multipledispatch import dispatch

@dispatch(dict, str)
def verifica_chave_existe_dicionario(dicionario : dict, chave : str):
    if chave in dicionario.keys():
        return True
    else:
        return False

@dispatch(dict, int)
def verifica_chave_existe_dicionario(dicionario : dict, chave : int):
    if chave in dicionario.keys():
        return True
    else:
        return False

@dispatch(dict, str)
def devolve_chave_existe_dicionario(dicionario : dict, chave : str):
    if chave in dicionario.keys():
        return dicionario[chave]
    else:
        return ""

@dispatch(dict, int)
def verifica_chave_existe_dicionario(dicionario : dict, chave : int):
    if chave in dicionario.keys():
        return dicionario[chave]
    else:
        return ""

def devolve_informacoes_class(classe):
    definicoes = {}

    for var in vars(classe):
        if not classe.__getattribute__(var) is None:
            definicoes[var] = classe.__getattribute__(var)
    
    return definicoes

def devolve_membros_class(classe, devolve = 2):
    """ 
        Devolve as constantes de uma classe.\n
        \tclasse - nome da classe\n
        \tdevolve - indica o tipo de devolução\n
        \t\t 0 - devolve os nomes das constantes
        \t\t 1 - devolve os valores das constantes\n
        \t\t 2 - devolve os nomes e os valores das constantes
    """
    import inspect as i

    if not i.isclass(classe):
        apresenta_caixa_mensagens(texto_mensagem="O objeto classe não é uma class!")
        return []

    atributos = i.getmembers(classe, lambda a:not(i.isroutine(a)))

    devolver = []

    if str(devolve) == '0' or str(devolve) == '1':
        devolver = [a[int(devolve)] for a in atributos if not(a[0].startswith('__') and a[0].endswith('__'))]
    elif str(devolve) == '2':
        devolver = [a for a in atributos if not(a[0].startswith('__') and a[0].endswith('__'))]

    return devolver


def ler_json_file(ficheiro, nome_info, nome_valor=None, pasta=False):
    from os import path
    from .. import app
    from flask import json
    from ..constantes import PASTA_GERAL_PROJETO

    if pasta:
        ficheiro = path.join(app.static_folder, PASTA_GERAL_PROJETO, "json", ficheiro)
    
    if not path.isfile(ficheiro):
        apresenta_caixa_mensagens(TIPOS.erro, "ERRO", f"O ficheiro {ficheiro} de configuração json não existe!")
        return False

    f = open(ficheiro, 'r', encoding='utf-8')
    try:
        data = json.load(f)
    except ValueError as e:
        apresenta_caixa_mensagens(TIPOS.erro, "ERRO", f"O ficheiro não tem uma configuração json válida!")
        return False
    f.close()

    teste_encontrou=False
    for info in data:
        if info == nome_info:
            teste_encontrou=True

    if not teste_encontrou:
        apresenta_caixa_mensagens(TIPOS.erro, "ERRO", f"Não existe no ficheiro json as configurações para as informações sobre {nome_info}!")
        return False

    dados_devolver=data[nome_info]

    if nome_valor:
        teste_encontrou=False
        for info in dados_devolver:
            if info == nome_valor:
                teste_encontrou=True

        if not teste_encontrou:
            apresenta_caixa_mensagens(TIPOS.erro, "ERRO", f"Não existe no ficheiro json as configurações para {nome_info} e na importação dos dados {nome_valor}!")
            return False
        else:
            dados_devolver=data[nome_info][nome_valor]

    return dados_devolver

def escrever_json_file(ficheiro, nome_valor, valor, pasta=True):
    from os import path
    from .. import app
    from flask import json
    from ..constantes import PASTA_GERAL_PROJETO

    if not nome_valor or not valor:
        apresenta_caixa_mensagens(TIPOS.erro, "ERRO", "Os valores passados para a função escrever_json_file_info() estão incorrectos!")
        return False

    if pasta:
        ficheiro = path.join(app.static_folder, PASTA_GERAL_PROJETO, "json", ficheiro)
    
    if not path.isfile(ficheiro):
        apresenta_caixa_mensagens(TIPOS.erro, "ERRO", f"O ficheiro {ficheiro} de configuração json não existe!")
        return False

    f=open(ficheiro, 'r', encoding='utf-8')
    try:
        data = json.load(f)
    except ValueError as e:
        apresenta_caixa_mensagens(TIPOS.erro, "ERRO", f"O ficheiro não tem uma configuração json válida!")
        return False
    f.close()

    teste_encontrou=False
    for info in data:
        if info == nome_valor:
            teste_encontrou=True

    if not teste_encontrou:
        apresenta_caixa_mensagens(TIPOS.erro, "ERRO", f"Não existe no ficheiro json as configurações para as informações sobre {nome_valor}!")
        return False

    data[nome_valor] = valor

    f = open(ficheiro, "w", encoding='utf-8')
    json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()

    return True