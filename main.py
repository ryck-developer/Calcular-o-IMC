from modulos.pessoa import Pessoa

clientes = [
    Pessoa(
        nome=input(f"\nDigite o seu nome: "),
        altura=float(input("Digite a sua altura: ")),
        peso=float(input("Digite o seu peso: "))
    )
    for i in range(2)
]

print('CALCULAR IMC'.center(50, '-'))
for pessoa in clientes:
    print(f"O IMC de {pessoa.nome} é {pessoa.getIMC()}")