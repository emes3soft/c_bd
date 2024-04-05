from ..mensagens.mensagem_popup import apresenta_caixa_mensagens

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