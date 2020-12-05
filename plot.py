import pandas
import os.path
from os import path
import pygal
from pygal.style import Style


def movimientosPlot(df, style):
    c = pygal.Bar(
        title = "Movimientos Realizados (Menor es mejor)",
        style = style,
        x_title = 'Estado Inicial',
        y_title = 'Movimientos',
        width = 1200,
        x_label_rotation = 270
    )

    c.add('DFS', df['Movimientos DFS'])
    c.add('BFS', df['Movimientos BFS'])
    c.add('BFS_e', df['Movimientos BFS_e'])

    c.x_labels = df['Estado Inicial']

    #c.render_to_file('movimientosPlot.svg')
    c.render_in_browser()


def tiempoPlot(df, style):
    c = pygal.Bar(
        title = "Tiempo en Finalizar (Menor es mejor)",
        style = style,
        x_title = 'Estado Inicial',
        y_title = 'Tiempo (Seg.)',
        width = 1200,
        x_label_rotation = 270
    )

    c.add('DFS', df['Tiempo DFS'])
    c.add('BFS', df['Tiempo BFS'])
    c.add('BFS_e', df['Tiempo BFS_e'])

    c.x_labels = df['Estado Inicial']

    #c.render_to_file('tiempoPlot.svg')
    c.render_in_browser()


def main():
    if path.exists('plot.csv'):
        df = pandas.read_csv(r'plot.csv')

        custom_style = Style(
            colors=('#0343df', '#e50000', '#cf247f'),
            font_family='Roboto,Helvetica,Arial,sans-serif',
            background='transparent',
            label_font_size=12,
        )


        movimientosPlot(df, custom_style)
        tiempoPlot(df, custom_style)

        
        print(df)
        input("\nPresiona Enter para continuar...")
    else:
        print("\nNo se ha creado el archivo 'plot.csv', por favor ejecuta: torre-de-hanoi.py")
        input("\nPresiona Enter para continuar...")

main()