import PySimpleGUI as sg
import numpy as np

def main():
    # Lista para guardar o layout da janela de entrada de N
    layout = [
        [sg.Txt("Digite a quantidade de números que deseja inserir:")],
        [sg.Input(key='N')],
        [sg.Btn("ok"), sg.Btn("cancelar")]
    ]
    janela = sg.Window("Calculadora", layout)

    n = 0
    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED or evento == "cancelar":
            janela.close()
            return # Sai da função main se cancelar na primeira janela
        if evento == "ok":
            try:
                n = int(valores['N'])
                if n <= 0:
                    sg.popup("Insira somente números positivos")
                    continue
                break
            except:
                sg.popup("Por favor, insira um valor válido")
    janela.close()

    numeros = []  # Outra lista

    for i in range(n):
        layout = [
            [sg.Txt(f"Digite o {i+1}° número")],
            [sg.Input(key='Campeao')],
            [sg.Btn("ok"), sg.Btn("Cancelar")]
        ]
        janela = sg.Window("Entrada de número", layout)

        while True:
            eventos, valores_loop = janela.read() # Renomeado valores para evitar conflito
            if eventos == sg.WIN_CLOSED or eventos == "Cancelar":
                janela.close()
                return # Sai da função main se cancelar na janela de números
            if eventos == 'ok':
                try:
                    num = float(valores_loop['Campeao'])
                    numeros.append(num)
                    break
                except:
                    sg.popup("Por favor, insira valores válidos")
        janela.close()

    # Utilização do numpy
    vetor = np.array(numeros)
    soma = np.sum(vetor)
    media = np.mean(vetor)

    # Resultados
    resultado_layout = [
        [sg.Txt("Elementos do vetor")],
        [sg.Txt(",".join(map(str, vetor)))],
        [sg.Txt(f"Soma dos elementos = {soma}")],
        [sg.Txt(f"Media dos elementos = {media}")],
        [sg.Btn("Fechar")]
    ]
    resultado_janela = sg.Window("Resultado", resultado_layout)

    while True:
        eventoResultado, valoresResultado = resultado_janela.read()
        print(eventoResultado)
        if eventoResultado == sg.WIN_CLOSED or "Fechar" in eventoResultado:
            resultado_janela.close()
            print("entrei if")
            break
    resultado_janela.close()

# Esta linha chama a função main() quando o script é executado
if __name__ == "__main__":
    main()