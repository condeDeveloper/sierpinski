"""As linhas de Pascal, construidas somando vizinhos e nada mais."""

from sierpinski.nucleo import (
    digitos_na_base,
    e_primo,
    linha,
    linhas_ate,
    nao_divisiveis,
)


def test_linhas_pequenas_a_mao():
    assert linha(0) == [1]
    assert linha(1) == [1, 1]
    assert linha(2) == [1, 2, 1]
    assert linha(3) == [1, 3, 3, 1]
    assert linha(4) == [1, 4, 6, 4, 1]
    assert linha(5) == [1, 5, 10, 10, 5, 1]


def test_tamanho_e_simetria_da_linha():
    for n in range(12):
        l = linha(n)
        assert len(l) == n + 1
        assert l == l[::-1]


def test_soma_da_linha_e_potencia_de_dois():
    for n in range(14):
        assert sum(linha(n)) == 2 ** n


def test_linha_reduzida_bate_com_a_inteira():
    for n in range(10):
        for m in (2, 3, 5, 7):
            assert linha(n, m) == [v % m for v in linha(n)]


def test_linhas_ate_devolve_todas():
    todas = linhas_ate(5)
    assert len(todas) == 6
    for n, l in enumerate(todas):
        assert l == linha(n)


def test_nao_divisiveis_conta_certo():
    # Linha 4 e 1, 4, 6, 4, 1: dois impares.
    assert nao_divisiveis(4, 2) == 2
    # Linha 3 e 1, 3, 3, 1: quatro impares.
    assert nao_divisiveis(3, 2) == 4
    assert nao_divisiveis(0, 2) == 1


def test_digitos_na_base():
    assert digitos_na_base(0, 2) == [0]
    assert digitos_na_base(4, 2) == [0, 0, 1]
    assert digitos_na_base(5, 3) == [2, 1]
    assert digitos_na_base(26, 3) == [2, 2, 2]


def test_digitos_reconstroem_o_numero():
    for n in range(0, 200):
        for base in (2, 3, 5, 7, 10):
            ds = digitos_na_base(n, base)
            assert sum(d * base ** i for i, d in enumerate(ds)) == n


def test_e_primo():
    assert [k for k in range(2, 30) if e_primo(k)] == \
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert not e_primo(1)
    assert not e_primo(0)
    assert not e_primo(-7)
