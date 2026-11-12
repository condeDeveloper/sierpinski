"""O juiz: a formula dos digitos, que nunca constroi uma linha.

O teorema de Lucas diz que, para p PRIMO, o binomial C(n,k) e divisivel por p
exatamente quando algum digito de k na base p passa do digito correspondente
de n. Contar os k que nao passam em nenhuma casa e entao um produto:

    nao divisiveis na linha n = produto de (digito + 1), nos digitos de n na base p

Para n = 4 e p = 2: 4 em base 2 e 100, digitos 0, 0, 1, e o produto e
1 * 1 * 2 = 2. A linha 4 e 1, 4, 6, 4, 1, e os impares sao os dois uns.

O arquivo nao sabe somar vizinhos e nao sabe o que e uma linha de Pascal. Ele
le os digitos de um numero e multiplica. Se concorda com a construcao burra,
nenhuma das duas esta errada.

**A hipotese de primo nao e enfeite.** A formula e enunciada para primos, e o
projeto mede o que acontece quando ela e aplicada a um composto -- que e onde
ela quebra, e por quanto.
"""

from .nucleo import digitos_na_base


def pela_formula(n, base):
    """O produto dos digitos mais um.

    Aplicavel a qualquer base: cabe a quem chama saber se a base e prima. Se
    nao for, o numero que sai nao tem garantia nenhuma -- e e justamente isso
    que as medidas deste projeto mostram.
    """
    produto = 1
    for d in digitos_na_base(n, base):
        produto *= d + 1
    return produto


def linha_cheia(n, p):
    """A linha n nao tem NENHUMA entrada divisivel por p?

    Pela formula, isso acontece quando o produto bate com o tamanho da linha,
    que e n+1. Em base p isso quer dizer que todo digito de n vale p-1.
    """
    return pela_formula(n, p) == n + 1


def todos_os_digitos_sao_o_maximo(n, p):
    """Todo digito de n na base p vale p-1?

    E a condicao que deveria ser equivalente a linha cheia. Esta separada da
    outra de proposito: sao duas afirmacoes, e a bateria confere que elas
    coincidem em vez de supor.
    """
    return all(d == p - 1 for d in digitos_na_base(n, p))
