import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Pagina de desafio https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer

# 1. Importa los datos desde el archivo CSV "fcc-forum-pageviews.csv"
# - Asegúrate de convertir la columna 'date' a tipo fecha.
# - Establece 'date' como índice del DataFrame.
df = None

# 2. Limpia los datos:
# - Filtra los días donde las visualizaciones de página ('page_views')
#   estén fuera del rango del 2.5% inferior o superior del conjunto de datos.
#   (Es decir, elimina los valores más extremos).
df = None


# 3. Define la función para el gráfico de líneas
def draw_line_plot():
    # 4. Crea una figura con Matplotlib
    # - Dibuja una línea con las visualizaciones diarias (page_views) a lo largo del tiempo.
    # - Usa color='red' y linewidth=1 (opcional).
    # - El título debe ser: "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
    # - Etiqueta el eje X como "Date" y el eje Y como "Page Views"

    # Ejemplo: fig, ax = plt.subplots(figsize=(12, 6))
    fig = None





    # 5. Guarda la figura con tu nombre y catplot al final. (Ejemplo: Elena_Nito_catplot.png)
    fig.savefig('line_plot.png')
    return fig

# 6. Define la función para el gráfico de barras
def draw_bar_plot():
    # 7. Crea una copia del DataFrame limpio (df) para trabajar.
    df_bar = None

    # 8. Prepara los datos para el gráfico de barras:
    # - Crea dos columnas nuevas: 'year' y 'month'.
    # - Agrupa los datos por 'year' y 'month' para calcular el promedio
    #   de visualizaciones diarias.
    # - Usa df.groupby(['year', 'month'])['page_views'].mean().unstack()

    # 9. Crea la figura del gráfico de barras:
    # - Usa el método plot(kind='bar') o seaborn.barplot().
    # - La leyenda debe mostrar los meses (Jan, Feb, ..., Dec) con el título "Months".
    # - Etiqueta el eje X como "Years" y el eje Y como "Average Page Views".
    fig = None


    # 10. Guarda la figura con tu nombre y catplot al final. (Ejemplo: Elena_Nito_catplot.png)
    fig.savefig('bar_plot.png')
    return fig

# 11. Define la función para los boxplots
def draw_box_plot():
    # 12. Prepara los datos (esta parte ya está hecha)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    
    # 13. Crea una figura con dos subgráficos lado a lado (1 fila, 2 columnas).
    # - Tamaño sugerido: (15, 6)
    # - Usa seaborn.boxplot() para cada uno.

    # 14. Primer gráfico (a la izquierda):
    # - Muestra la distribución por año.
    # - Eje X: 'year', Eje Y: 'page_views'
    # - Título: "Year-wise Box Plot (Trend)"

    # 15. Segundo gráfico (a la derecha):
    # - Muestra la distribución por mes.
    # - Eje X: 'month', Eje Y: 'page_views'
    # - Asegúrate de que los meses estén ordenados de Jan a Dec.
    # - Título: "Month-wise Box Plot (Seasonality)"

    fig = None


    # 16. Guarda la figura con tu nombre y catplot al final. (Ejemplo: Elena_Nito_catplot.png)
    fig.savefig('box_plot.png')
    return fig
