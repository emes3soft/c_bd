from flask import current_app as app, redirect, url_for
from functools import wraps

def teste_validacao():
    def entrada_necessaria(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not app:
                return redirect(url_for('erros.sem_app'))
            return f(*args, **kwargs)
        return decorated_function
    return entrada_necessaria