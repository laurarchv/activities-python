# escreva um programa que pergunte a quantidade de km percorridos por
# um carro alugado pelo usuário, assim como a quantidade de dias em que
# esteve com ele. o carro custa 60 por dia e 0,15 por km rodado

# variaveis
km_percorridos = float(input("Km percorridos: "))
dias_alugados = int(input("Dias alugados: "))

# calculo
preco_por_dia = 60.00
preco_por_km = 0.15

custo_dias = dias_alugados * preco_por_dia
custo_km = km_percorridos * preco_por_km
custo_total = custo_dias + custo_km

print(f"O total a pagar pelo aluguel do carro é: R$ {custo_total:.2f}")