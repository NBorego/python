import PySimpleGUI as sg

#Tema
sg.theme('reddit')
#Variaveis
fonte = ('Arial',14)
tamanho_botao = (4,2)
mensagem = []
#layout
layout = [
    [sg.Multiline('', size=(13,1), disabled=True, font=('Arial',25), no_scrollbar=True, key='tela')],
    [
        sg.Button('C', size=(tamanho_botao), font=(fonte)), 
        sg.Button('Apagar', size=(10,2), pad=3 ,font=(fonte)),
        sg.Button('/', size=(tamanho_botao), font=(fonte))
    ],
    [
        sg.Button('7', size=(tamanho_botao), font=(fonte)), 
        sg.Button('8', size=(tamanho_botao), font=(fonte)), 
        sg.Button('9', size=(tamanho_botao), font=(fonte)),
        sg.Button('x', size=(tamanho_botao), font=(fonte)),

    ],
    [
        sg.Button('4', size=(tamanho_botao), font=(fonte)), 
        sg.Button('5', size=(tamanho_botao), font=(fonte)), 
        sg.Button('6', size=(tamanho_botao), font=(fonte)),
        sg.Button('+', size=(tamanho_botao), font=(fonte)),

    ],
    [
        sg.Button('1', size=(tamanho_botao), font=(fonte)), 
        sg.Button('2', size=(tamanho_botao), font=(fonte)), 
        sg.Button('3', size=(tamanho_botao), font=(fonte)),
        sg.Button('-', size=(tamanho_botao), font=(fonte)),

    ],
    [
        sg.Button('0', size=(10,2), pad=3 ,font=(fonte)), 
        sg.Button('=', size=(10,2), pad=3 ,font=(fonte))
    ],
]
#janela
janela = sg.Window('Calculadora', layout)
#Calculadora
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'C':
        janela['tela'].update('')
    match eventos:
        case '9':
            mensagem.append('9')
            janela['tela'].update(mensagem[-1], append=True)
            print(f'{mensagem}')