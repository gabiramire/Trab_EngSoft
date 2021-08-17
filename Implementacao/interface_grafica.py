# sudo apt-get install python3-tk 
# pip install pysimplegui
import PySimpleGUI as sg

class Tela():
    def __init__(self,title, layout):
        # Create the Window
        window = sg.Window('Window Title', layout)
        # Event Loop to process "events"
        while True:             
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancel'):
                break

layout = [
            [sg.Text("""    
            A - Criar Receita
            B - Pesquisa
            C - Minhas Receitas
            D - Pesquisar uma receita própria
            E - Minha Conta 
            
            F - Sair
                                """)],
            [sg.Text('Resposta: '), sg.InputText()],

            [sg.Button('OK')]
]
title = "Menu Usuáro"
a = Tela(layout, title)
x =  ''
while True:
    if x != 'a':
        a.run
    else:
        break