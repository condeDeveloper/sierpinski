"""O triangulo de Pascal modulo m, construido linha a linha.

A linha n sao os binomiais C(n,0) ate C(n,n). Reduzidos modulo m, eles formam
o desenho que no caso m=2 fica conhecido pela forma recursiva de triangulos
dentro de triangulos.

Aqui nada e desenhado: o que interessa e **quantas entradas da linha n NAO sao
divisiveis por m**. Esse numero tem uma formula fechada quando m e primo, e a
graca do projeto e que a formula e um teorema sobre primos -- entao da para
medir exatamente onde ela deixa de valer.

A construcao e a mais burra possivel, de proposito: cada linha sai da anterior
somando vizinhos. Nenhum binomial e calculado por fatorial, nenhuma
propriedade e usada. E o lado que nao sabe de teoria nenhuma.
"""


def linha(n, m=None):
    """A linha n do triangulo, opcionalmente reduzida modulo m.

    Sai da linha anterior somando vizinhos, como se faz a mao.
    """
    atual = [1]
    for _ in range(n):
        anterior = atual
        atual = [1]
        for i in range(len(anterior) - 1):
            v = anterior[i] + anterior[i + 1]
            atual.append(v % m if m else v)
        atual.append(1)
    return atual


def linhas_ate(n, m=None):
    """Todas as linhas de 0 ate n, cada uma a partir da anterior."""
    saida = []
    atual = [1]
    for _ in range(n + 1):
        saida.append(list(atual))
        anterior = atual
        atual = [1]
        for i in range(len(anterior) - 1):
            v = anterior[i] + anterior[i + 1]
            atual.append(v % m if m else v)
        atual.append(1)
    return saida


def nao_divisiveis(n, m):
    """Quantas entradas da linha n nao sao divisiveis por m.

    Contado direto, olhando entrada por entrada. Nenhuma formula.
    """
    return sum(1 for v in linha(n, m) if v % m != 0)


def digitos_na_base(n, base):
    """Os digitos de n na base dada, do menos para o mais significativo."""
    if n == 0:
        return [0]
    saida = []
    while n:
        saida.append(n % base)
        n //= base
    return saida


def e_primo(k):
    """Divisao por tentativa. O dominio aqui e pequeno e nao pede mais."""
    if k < 2:
        return False
    if k % 2 == 0:
        return k == 2
    d = 3
    while d * d <= k:
        if k % d == 0:
            return False
        d += 2
    return True
