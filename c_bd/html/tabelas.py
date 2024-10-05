from ..comandos.comandos import CMD_SELECT as CS, CMD_UPDATE as CU, CMD_INSERT as CI, CMD_DELETE as CD, COMANDOS as C
from ..mensagens.mensagem import cria_mensagem, apresenta_caixa_mensagens
import inspect as i

def desenha_tabelas_html(comando : C):
    return

def desenha_tabela_html(comando_select : CS):
    if not isinstance(comando_select, CS):
        cria_mensagem(1043, f"{i.stack()[1][3].upper()} - {__name__}")
        return False
    
    if not comando_select.executado:
        cria_mensagem(1060, f"{i.stack()[1][3].upper()} - {__name__}")
        return False

    # apresenta_caixa_mensagens(texto_mensagem=str(comando_select.campos_comando))
    
    return str(comando_select.campos_comando)