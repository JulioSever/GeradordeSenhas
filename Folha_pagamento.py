  #Desconto do imposto de renda -11%
#Desconto FGT até 900: ISENTO ===== até 1500  -5% === até 2500 10% 

from time import sleep #Importando a biblioteca 'time' para realizar a pausa no programa!


#Introdução ao programa!
print('\033[33m='*50)
print('       \033[33mBem vindo a folha de Pagamentos!!')
print('\033[33m='*50)
sleep(2) # Pausa de 2 segundos até o proximo


while True: #Jogando um looping para realizar a conferencia de mais de um funcionario
    try: #Realizando a conferencia de entrada de dados, certificando que o usuario vai digitar apenas números
        nome = input(f"\033[mDigite o nome do funcionário: ")
        salario = float(input(f"Digite o salário bruto (sem vírgulas) do funcionário {nome}: "))
        horas_extras = float(input(f"Digite a quantidade de horas extras que o funcionário {nome} fez no mês: "))
        

    except ValueError: #Faz a tratativa do erro
        print(f'Digite um numero válido')
        continue
    # Supondo uma jornada de trabalho de 44 horas semanais (176 horas mensais)
    horas_trabalhadas_mes = 176

    # Calculando o valor da hora normal
    valor_hora_normal = salario / horas_trabalhadas_mes

    # Calculando o valor da hora extra
    valor_hora_extra = valor_hora_normal * 1.5

    # Calculando o valor total das horas extras
    valor_total_horas_extras = valor_hora_extra * horas_extras

    #Calculando o valor do salario com a hora extra
    salario_com_valor_da_extra = salario + valor_total_horas_extras

    #Calculando o imposto de renda com desconto de 5%
    imposto_cinco_porc=(salario * 5) / 100

    #Calculando o imposto de renda com desconto de 10%
    imposto_dez_porc = (salario * 10) / 100

    
    if salario<=900:
        print(f'O funcionario {nome} vai receber:{valor_total_horas_extras:.2f} de hora extra ')
        sleep(1.5)
        print(f'E o pagamento do funcionario {nome} vai ser de {salario_com_valor_da_extra:.2f}')
    elif salario <=1500:
            print(f'O valor do desconto do imposto é de: {imposto_cinco_porc} ')
            sleep(1.5)
            print(f'o Valor da Hora extra é de: {valor_total_horas_extras:.2f}')
            sleep(1.5)
            print(f'Sendo assim o funcionario {nome} vai receber um total de: {salario - imposto_cinco_porc + valor_total_horas_extras:.2f}')
    else:
            print(f'O valor do desconto do imposto é de: {imposto_dez_porc} ')
            sleep(1.5)
            print(f'o Valor da Hora extra é de: {valor_total_horas_extras:.2f}')
            sleep(1.5)
            print(f'\033[33mSendo assim o funcionario {nome} vai receber um total de: {salario - imposto_dez_porc + valor_total_horas_extras:.2f}')
    

        #Verificando se o usuario deseja sair ou continuar::::
    try:
        sair= input(f'Digite uma opção\n Oque deseja fazer? \033[31mS[sair]\033[m \033[32mC[continuar]\033[m:').upper()
        if sair.startswith('C'):
            continue
    except ValueError:
            print(f'Digite uma opção válida')
    else:
            print(f'Fechando o sistema...')
            sleep(1.5)
            break 

