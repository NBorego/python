import PySimpleGUI as sg

#tema usado
sg.theme('reddit')

#Variaveis
tamanho_input = (20, 1)
#layout
layout = [
    [sg.Text('Numero 1'), sg.Input(key='num1',size=(tamanho_input))],
    [sg.Text('Numero 2'), sg.Input(key='num2',size=(tamanho_input))],
    [sg.Button('Somar'), sg.Button('Subtrair'), sg.Button('Multiplicar'), sg.Button('Dividir')],
    [sg.Output(size=(40,20), key='log')],
    [sg.Button('Limpar Tela'), sg.Button('Sair')]
]

#janela
janela = sg.Window('Somador v3', layout)
#ler eventos
while True:
    eventos, valores = janela.read()
    #botoes são os eventos
    if eventos == sg.WINDOW_CLOSED or eventos == 'Sair':
        break
    if eventos == 'Limpar Tela':
        janela['log'].update('')
    try:
        n1 = int(valores["num1"])
        n2 = int(valores["num2"])
        match eventos:
            case 'Somar':
                print(f'A soma entre {n1} + {n2} é igual a {n1 + n2}')
            case 'Subtrair':
                print(f'A subtração entre {n1} - {n2} é igual a {n1 - n2}')
            case 'Multiplicar':
                print(f'A multiplicação entre {n1} x {n2} é igual a {n1 * n2}')
            case 'Dividir':
                divisao = n1 / n2
                print(f'A divisão entre {n1} / {n1} é igual a {divisao:.1f}')    
    except(ValueError):
        print('='*35)
        print('ERRO AO FAZER A CONTA!!!')
        print('POSSIVEIS ERROS:')
        print('-CARACTERES ESPECIAS')
        print('-LETRAS')
        print('-NENHUM VALOR DIGITADO')
        print('='*35)