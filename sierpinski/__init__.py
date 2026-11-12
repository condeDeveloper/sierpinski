"""Pascal modulo m varrido linha a linha, com a formula dos digitos como juiz."""

from .nucleo import (linha, linhas_ate, nao_divisiveis, digitos_na_base, e_primo)
from .juiz import pela_formula, linha_cheia, todos_os_digitos_sao_o_maximo

__all__ = ['linha', 'linhas_ate', 'nao_divisiveis', 'digitos_na_base',
           'e_primo', 'pela_formula', 'linha_cheia',
           'todos_os_digitos_sao_o_maximo']
