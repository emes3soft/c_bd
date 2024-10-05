from .constantes import PREDEFINICOES as PRED

def Colunas_Teste_Validacao(colunas):
    if not isinstance(colunas, list):
        colunas = PRED.colunas_valores
    elif colunas == []:
        colunas = PRED.colunas_valores
    else:
        for c in range(len(colunas)):
            if not str(colunas[c]).isnumeric() and str(colunas[c]) != "":
                colunas[c] = ""
    
    return colunas

def Colunas_Devolve_Texto_com_Dimensoes(colunas):
    col_str == ""
    for c in range(len(colunas)):
        if col_str == "":
            col_str = PRED.colunas_dimensoes[c] + ("" if colunas[c] == "" else f"-{colunas[c]}")
        elif colunas[c] != "":
            col_str += " " + PRED.colunas_dimensoes[c] + f"-{colunas[c]}" 
    
    return col_str
