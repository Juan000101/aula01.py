import PySimpleGUI as sg
import numpy as np

#Lista para guardar  o layout da janela
layout =  [
    # Erro aqui -> use sg.Txt
    [sg.Txt("Digite a quantidade de numeros que deseja inserir:")],
    [sg.Input()],
    # Erros aqui -> use sg.Btn e sg.btn
    [sg.Btn("ok"),sg.btn("cancelar")]
]

sg.Window("calculadora",layout).read()
