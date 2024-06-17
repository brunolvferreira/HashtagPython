#!/usr/bin/env python
# coding: utf-8

# ## 7.2 Índice e Tamanho de Texto
0 1 2 3 4 5 6 7 8 9 10 11 12 13
l i r a @ g m a i l  .  c  o m

Pegar um item de uma string: texto[índice]
Pegar o tamanho de um texto: len(texto)
# In[9]:


email = 'lira@gmail.com'
nome = 'João Lira'

print('Email possui', len(email), 'caracteres.')
print('Nome possui', len(nome), 'caracteres.')

print('Índice 4 do e-mail:', email[4])  # retorna o índice 4 da string e-mail, o '@'


# ## 7.3 String Índice Negativo e Pedaço de Texto

# In[ ]:


Texto: lira@gmail.com

-14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  l   i   r   a   @  g  m  a  i  l  .  c  o  m
  0   1   2   3   4  5  6  7  8  9 10 11 12 13
  
Para pegar um texto de trás para frente: texto[índice] -> onde índice é negativo
Para pegar o pedaço de um texto use : (dois pontos). texto[:indice] ou texto[indice:] ou ainda texto[indice:indice]


# In[16]:


email = 'lira@gmail.com'
nome = 'João Paulo Lira'

print(email[-1])  # retorna 'm'
print(email[:-10])  # retorna 'lira' (não inclui o índice quando pega texto pra trás)
print(email[5:])  # retorna 'gmail.com'  (inclui o índice quando pega texto pra frente)


# Exercícios para Fixação:
# Basta completar os prints de forma correta

# In[21]:


print('Tamanho do e-mail ' + str(len(email)) + ' caracteres')
print('Primeiro Caractere ' + email[0]) 
print('Último Caractere ' + email[-1])
print('Servidor do email ' + email[5:10])  # retorna 'gmail'


# ## 7.4 Operações com String
# 
# str ===> transforma número em string<br>
# in ===> verifica se um texto está contido dentro do outro<br>
# operador + ===> concatenar string<br>
# format e {} ===> substitui valores<br>
# %s ===> substitui textos<br>
# %d ===> substitui números decimais<br>
# 
# Vamos deixar uma cartilha para download

# In[23]:


faturamento = 1000
custo = 500
lucro = faturamento - custo


# Uso do str() e do concatenar com +

# In[25]:


print ('O faturamento da loja foi de: ' + str(faturamento))  # str() transforma em str o int faturamento


# Uso do Format

# In[31]:


print('Faturamento de {0}, custo de {1} e lucro de {2}. Lembrando, faturamento de {0}.'.format(faturamento, custo, lucro))
# uma vez informado o índice dentro dos {} para um item, deve-se preencher todos os outros.
# a vantagem é não precisar declarar mais um índice na lista, podendo reutilizar o 'faturamento' no exemplo.


# Uso do %s e %d

# In[33]:


print ('O faturamento foi de: %d, custo de %d e lucro de %d' % (faturamento, custo, lucro))
# aplicação similar ao .format


# Uso do in (mais exercícios práticos nas próximas aulas)

# In[34]:


print('@' in 'lira@gmail.com')  # true
print('@' in 'lira.gmail.com')  # false


# In[ ]:

# ## 7.5 "Fórmulas" de Texto - Métodos de String
# 
# ## Estrutura:
# 
# - Normalmente usamos a estrutura texto.método() para fazer as modificações que queremos
# - Alguns métodos pedem "argumentos", que são informações que temos que passar para a fórmula (método) para ela funcionar. Esses argumentos são passados dentro do parênteses
# 
# ## Como usar:
# 
# Não decore os métodos, os que você for mais usando com o tempo você vai decorar o que precisar.
# 
# Mas a dica é: use essa lista para consulta e busque entender como os métodos funcionam e suas aplicações, para poder consultar e usar quando precisar.

# - capitalize() -> Coloca a 1ª letra Maiúscula
    Uso: 
        texto = 'lira'
        print(texto.capitalize())
    Resultado: 
        'Lira'
# - casefold() -> Transforma TODAS as letras em minúsculas (existe lower() mas o casefold é melhor normalmente)
    Uso: 
        texto = 'Lira'
        print(texto.casefold())
    Resultado: 
        'lira'
# - count()	-> Quantidade de vezes que um valor aparece na string
    Uso:
        texto = 'lira@yahoo.com.br'
        print(texto.count('.'))
    Resultado:
        2
# - endswith() -> Verifica se o texto termina com um valor específico e dá como resposta True ou False
    Uso:
        texto = 'lira@gmail.com'
        print(texto.endswith('gmail.com'))
    Resultado:
        True
# - find() -> Procura um texto dentro de outro texto e dá como resposta a posição do texto encontrado
    Uso:
        texto = 'lira@gmail.com'
        print(texto.find('@'))
    Resultado:
        4
    Obs: lembrando como funciona a posição nas strings, então o @ está na posição 4
    l i r a @ g m a i l  .  c  o  m
    0 1 2 3 4 5 6 7 8 9 10 11 12 13
# - format() -> Formata uma string de acordo com os valores passados. Já usamos bastante ao longo do programa.
    Uso:
        faturamento = 1000
        print('O faturamento da loja foi de {} reais'.format(faturamento))
    Resultado:
        'O faturamento da loja foi de 1000 reais'
# - isalnum() -> Verifica se um texto é todo feito com caracteres alfanuméricos (letras e números) -> letras com acento ou ç são considerados letras para essa função.
    Uso:
        texto = 'João123'
        print(texto.isalnum())
    Resultado:
        True
    Obs: se o texto fosse 'Jo~ao' ou então 'Joao#' o resultado seria False 
# - isalpha() -> Verifica se um texto é todo feito de letras.
    Uso:
        texto = 'João'
        print(texto.isalpha())
    Resultado:
        True
    Obs: nesse caso se o texto fosse 'Joao123' o resultado seria False, porque 123 não são letras.
# - isnumeric()	-> Verifica se um texto é todo feito por números.
    Uso:
        texto = '123'
        print(texto.isnumeric())
    Resultado:
        True
    Obs: existem os métodos isdigit() e isdecimal() que tem variações pontuais em caracteres especiais tipo textos com frações e potências, mas para 99% dos casos eles não vão ser necessários.
# - replace() -> Substitui um texto por um outro texto em uma string.
    Uso:
        texto = '1000.00'
        print(texto.replace('.', ','))
    Resultado
        '1000,00'
    Obs: o replace precisa de 2 argumentos para funcionar. O 1º é o texto que você quer trocar. O 2º é o texto que você quer colocar no lugar daquele texto que você está tirando.
# - split()	-> Separa uma string de acordo com um delimitador em vários textos diferentes.
    Uso:
        texto = 'lira@gmail.com'
        print(texto.split('@'))
    Resultado:
        ['lira', 'gmail.com']

# - splitlines() -> separa um texto em vários textos de acordo com os "enters" do texto
    Uso:
        texto = '''Olá, bom dia
        Venho por meio desse e-mail lhe informar o faturamento da loja no dia de hoje.
        Faturamento = R$2.500,00
        '''
        print(texto.splitlines())
    Resultado:
        ['Olá, bom dia', 'Venho por meio desse e-mail lhe informar o faturamento da loja no dia de hoje.', 'Faturamento = R$2.500,00']
# - startswith() -> Verifica se a string começa com determinado texto
    Uso:
        texto = 'BEB123453'
        print(texto.startswith('BEB'))
    Resultado:
        True
# - strip()	-> Retira caracteres indesejados dos textos. Por padrão, retira espaços "extras" no início e no final
    Uso:
        texto = ' BEB123453 '
        print(texto.strip())
    Resultado:
        'BEB123453'
# - title() -> Coloca a 1ª letra de cada palavra em maiúscula
    Uso:
        texto = 'joão paulo lira'
        print(texto.title())
    Resultado:
        'João Paulo Lira'
# - upper()	-> Coloca o texto todo em letra maiúscula
    Uso:
        texto = 'beb12343'
        print(texto.upper())
    Resultado:
        'BEB12343'
# ## Exercitando

# In[5]:


texto = ' BEB123453 '
print(texto.strip())






