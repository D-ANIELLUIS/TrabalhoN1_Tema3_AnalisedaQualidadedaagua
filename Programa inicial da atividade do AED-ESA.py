print("Análise da Qualidade da Água em Açude")
print("Classe 3")
print("Destinadas ao consumo humano após tratamento convencional, à irrigação de culturas arbóreas, cerealíferas e forrageiras e à dessedentação de animais.")

# Definindo variáveis e suas perguntas
perguntas = {
    "a": "A água apresenta efeito tóxico agudo a organismos? ",
    "b": "A água apresenta materias flutuantes, inclusive espumas não naturais? ",
    "c": "A água apresenta óleos e graxas? ",
    "d": "A água apresenta gosto ou odor? ",
    "e": "A água apresenta corantes após o processo de coagulação, sedimentação e filtração? ",
    "f": "A água apresenta resíduos sólidos objetáveis? ",
    "g": "A água apresenta coliformes uma concentração maior que 1000 coliformes termotolerantes por 100ml? ",
    "h": "A água apresenta cianobactérias maior que 50.000 cel/ml ou 5mm³/L? ",
    "i": "A água atende ao DBO 5 dias a 20°C até 10mg/L O2? ",
    "j": "A água apresenta OD > 4mg/L O2? ",
    "l": "A água tem turbidez até 100 UNT? ",
    "m": "A água apresenta cor verdadeira inferior a 75mg Pt/L? ",
    "n": "A água tem que ter o pH entre 6 e 9? "
}

# Armazenando as respostas
respostas = {}

# Preenchendo as respostas
for variavel, pergunta in perguntas.items():
    resposta = input(pergunta).lower()
    respostas[variavel] = resposta

# Verificando se todas as respostas são "não"
todas_nao = all(
    resposta == "não" or "Não" or "Nao" or "nao" for resposta in respostas.values())

# Imprimindo o resultado
if todas_nao:
    print("A água está própria para uso.")
else:
    print("A água precisa ser tratada.")
