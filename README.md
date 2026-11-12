# sierpinski

O triângulo de Pascal módulo `m` varrido linha a linha em Python 3.10+, sem dependência
nenhuma: uma construção que só sabe somar vizinhos, e uma fórmula que só sabe ler dígitos,
conferindo uma à outra.

## O que é

A linha `n` do triângulo são os binomiais `C(n,0)` até `C(n,n)`. Reduzidos módulo `m`, eles
formam o desenho que no caso `m=2` fica conhecido pela forma recursiva de triângulos dentro
de triângulos.

Aqui nada é desenhado. O que interessa é **quantas entradas da linha `n` não são divisíveis
por `m`**, e esse número tem fórmula fechada quando `m` é primo: o produto de
`(dígito + 1)` sobre os dígitos de `n` na base `m`.

A graça é que a fórmula é um teorema **sobre primos**. Então dá para medir exatamente onde
ela deixa de valer.

## Os quatro achados

- **A fórmula acerta nas 1.288 linhas de oito primos, sem um erro — e quebra nos oito
  compostos.** Nos primos 2, 3, 5 e 7 foram 201 linhas cada; em 11, 13, 17 e 19, 121 cada.
  Nos compostos ela erra em **86 a 113** das 121 linhas. Não é um deslize de borda: é a
  hipótese de primo fazendo todo o trabalho.
- **Nas potências de primo a primeira quebra cai exatamente em `n = m`.** Para 4, 8, 9, 16,
  25 e 27 — os seis casos — a fórmula vale até a linha `m-1` e falha na linha `m`. Nos
  compostos de vários primos ela vem antes e sem padrão: `m=6` quebra em 4, `m=10` em 5,
  `m=15` em 6.
- **Ela erra nos dois sentidos.** Em `m=4` a contagem dá 3 e a fórmula diz 2; em `m=6` a
  contagem dá 4 e a fórmula diz 5. Uma fórmula que só subestimasse ainda serviria de limite.
  Esta não serve nem para isso.
- **"Linha cheia" não é "todos os dígitos valem `p-1`".** Abaixo de 100 e com `p=5` são
  **doze** linhas sem nenhuma entrada divisível, e só **duas** têm todos os dígitos máximos.
  A caracterização óbvia pega um sexto do que deveria, e o buraco cresce com `p`: 1 em
  `p=2`, 5 em `p=3`, 10 em `p=5`.

## A fórmula nos primos

| p | linhas conferidas | erros |
|---|---|---|
| 2 | 201 | 0 |
| 3 | 201 | 0 |
| 5 | 201 | 0 |
| 7 | 201 | 0 |
| 11 | 121 | 0 |
| 13 | 121 | 0 |
| 17 | 121 | 0 |
| 19 | 121 | 0 |

## E nos compostos

| m | erros em 121 linhas | primeira quebra | contado | fórmula |
|---|---|---|---|---|
| 4 | 89 | n=4 | 3 | 2 |
| 6 | 113 | n=4 | 4 | 5 |
| 8 | 97 | n=8 | 5 | 2 |
| 9 | 86 | n=9 | 4 | 2 |
| 10 | 107 | n=5 | 4 | 6 |
| 12 | 105 | n=9 | 6 | 10 |
| 14 | 108 | n=8 | 4 | 9 |
| 15 | 107 | n=6 | 5 | 7 |

As potências de primo, separadas, mostram o padrão limpo:

| m | base | primeira quebra |
|---|---|---|
| 4 | 2 | 4 |
| 8 | 2 | 8 |
| 9 | 3 | 9 |
| 16 | 2 | 16 |
| 25 | 5 | 25 |
| 27 | 3 | 27 |

## Linhas sem nenhuma entrada divisível

| p | cheias (até 100) | com dígitos máximos | perdidas pela caracterização óbvia |
|---|---|---|---|
| 2 | 0, 1, 3, 7, 15, 31, 63 | 1, 3, 7, 15, 31, 63 | 1 |
| 3 | 0, 1, 2, 5, 8, 17, 26, 53, 80 | 2, 8, 26, 80 | 5 |
| 5 | 0, 1, 2, 3, 4, 9, 14, 19, 24, 49, 74, 99 | 4, 24 | 10 |

A caracterização **certa** é o produto: a linha `n` é cheia exatamente quando o produto dos
dígitos mais um dá `n+1`. Em base 3, o `n=5` é `12`, e `(2+1)·(1+1) = 6 = 5+1` — cheia, sem
nenhum dígito ser 2. A implicação vale numa direção só, e a bateria testa as duas
separadamente em vez de supor que são a mesma frase.

## Os dois caminhos

A construção é a mais burra possível, de propósito: cada linha sai da anterior somando
vizinhos, como se faz à mão. Nenhum binomial é calculado por fatorial, nenhuma propriedade
é usada. É o lado que não sabe de teoria nenhuma.

A fórmula nunca constrói uma linha: lê os dígitos de um número numa base e multiplica. Os
dois não se tocam, e por isso um erro num dificilmente se repete no outro.

A bateria também tem um caso em que a fórmula **tem que errar** — `m=4`, linha 4. Sem ele,
"acerta nos primos" não teria contraste nenhum.

## O que as medidas me corrigiram

- **Prendi no teste uma lista que eu tinha impresso truncada.** O `print` saiu com `[:10]`
  e eu copiei os dez itens como se fossem a lista inteira; as linhas cheias de `p=5` são
  doze, e o 74 e o 99 ficaram de fora. O teste quebrou na hora, mas o erro é o mesmo de
  sempre num disfarce novo: tratei o que a tela mostrou como se fosse o que o programa
  mediu.
- **Eu ia escrever que linha cheia é "todos os dígitos valem `p-1`".** É a explicação que
  salta aos olhos, e ela implica a linha cheia — mas não o contrário. Deixei as duas
  afirmações em funções separadas justamente para a bateria comparar, e a diferença não foi
  pequena: em `p=5` a caracterização óbvia pega 2 de 12. Separar o que eu teria juntado foi
  o que transformou uma suposição em achado.
- **Eu esperava que a fórmula nos compostos errasse pouco, perto das bordas.** Erra em mais
  de 70% das linhas em todos os oito, e nos dois sentidos. A hipótese de primo não é uma
  condição técnica no enunciado: é o enunciado inteiro.

## Rodar

```bash
pip install -e ".[dev]"
pytest
python -m sierpinski              # tudo
python -m sierpinski compostos    # onde a fórmula quebra
python -m sierpinski cheias       # as linhas sem entrada divisível
python ferramentas/medidor.py
```

## Mapa

| arquivo | o que faz |
|---|---|
| `sierpinski/nucleo.py` | as linhas, somando vizinhos e nada mais |
| `sierpinski/juiz.py` | a fórmula dos dígitos, que nunca constrói uma linha |
| `sierpinski/medidas.py` | primos, compostos, e as linhas cheias |
| `testes/test_medidas.py` | os números acima, presos |

26 testes. MIT.
