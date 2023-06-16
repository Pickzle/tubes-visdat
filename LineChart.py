import pandas as pd
from bokeh.models import ColumnDataSource, Select, Panel
from bokeh.layouts import column, row
from bokeh.plotting import figure

def create_lineplot_tab(yf):
    # Daftar saham
    saham_list = ["BBCA.JK", "BMRI.JK", "BBNI.JK", "BBRI.JK", "ARTO.JK", "BRIS.JK"]

    # Fungsi untuk mengambil data saham dari yfinance
    def load_saham(saham):
        df = yf.download(saham, start="2021-01-01", end="2021-12-31")['Close']
        return df.dropna()

    # Fungsi untuk mendapatkan data pergerakan saham
    def get_data(saham1, saham2):
        df = pd.concat([load_saham(saham1), load_saham(saham2)], axis=1)
        df.columns = ['saham1', 'saham2']
        df.reset_index(inplace=True)
        return df

    # Membuat sumber data kolom
    data = get_data("BBCA.JK", "BMRI.JK")
    source = ColumnDataSource(data=data)

    # Membuat plot pergerakan saham pertama
    plot1 = figure(width=800, height=300, x_axis_type='datetime', tools='pan,wheel_zoom,xbox_select,reset')
    plot1.line('Date', 'saham1', source=source, line_width=2)
    plot1.circle('Date', 'saham1', source=source, size=2, color=None, selection_color='firebrick')

    # Membuat plot pergerakan saham kedua
    plot2 = figure(width=800, height=300, x_axis_type='datetime', tools='pan,wheel_zoom,xbox_select,reset')
    plot2.line('Date', 'saham2', source=source, line_width=2)
    plot2.circle('Date', 'saham2', source=source, size=2, color=None, selection_color='firebrick')

    # Mengupdate plot berdasarkan saham yang dipilih
    def update_plot(attrname, old, new):
        saham1_val = saham1.value
        saham2_val = saham2.value
        data = get_data(saham1_val, saham2_val)
        source.data = data
        plot1.title.text = saham1_val
        plot2.title.text = saham2_val

    # Membuat select widget
    saham1 = Select(title="Saham 1", options=saham_list, value="BBCA.JK")
    saham2 = Select(title="Saham 2", options=saham_list, value="BMRI.JK")

    # Mengaitkan fungsi update_plot dengan perubahan select widget
    saham1.on_change('value', update_plot)
    saham2.on_change('value', update_plot)

    # Menyusun layout
    layout = column(saham1, saham2, plot1, plot2)
    tab = Panel(child=layout, title="Line Plot")
    return tab
