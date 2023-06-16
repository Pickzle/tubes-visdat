import pandas as pd
from bokeh.models import ColumnDataSource, Select, Panel
from bokeh.layouts import column, row
from bokeh.plotting import figure

def create_correlation_tab(yf):
    # Daftar saham
    saham_list = ["BBCA.JK", "BRPT.JK", "GOTO.JK", "BMRI.JK", "BBRI.JK", "BRIS.JK"]

    # Fungsi untuk mengambil data saham dari yfinance
    def load_saham(saham):
        df = yf.download(saham, start="2021-01-01", end="2023-06-15")['Close']
        return df.dropna()

    # Fungsi untuk mendapatkan data korelasi
    def get_data(saham1, saham2):
        df = pd.concat([load_saham(saham1), load_saham(saham2)], axis=1)
        df.columns = ['saham1', 'saham2']
        df['saham1_returns'] = df['saham1'].pct_change()
        df['saham2_returns'] = df['saham2'].pct_change()
        df.dropna(inplace=True)
        return df

    # Membuat sumber data kolom
    data = get_data("BBCA.JK", "BRPT.JK")
    source = ColumnDataSource(data=data)

    # Membuat plot korelasi
    corr = figure(width=600, height=400, tools="pan,wheel_zoom,box_select,reset")
    corr.circle("saham1_returns", "saham2_returns", source=source, size=4, alpha=0.6, selection_color="red")

    # Mengupdate plot berdasarkan saham yang dipilih
    def update_plot(attrname, old, new):
        saham1_val = saham1.value
        saham2_val = saham2.value
        data = get_data(saham1_val, saham2_val)
        source.data = data
        corr.title.text = f"{saham1_val} returns vs {saham2_val} returns"

    # Membuat select widget
    saham1 = Select(title="Saham 1", options=saham_list, value="BBCA.JK")
    saham2 = Select(title="Saham 2", options=saham_list, value="BRPT.JK")

    # Mengaitkan fungsi update_plot dengan perubahan select widget
    saham1.on_change('value', update_plot)
    saham2.on_change('value', update_plot)

    # Menyusun layout
    layout = column(saham1, saham2, corr)
    tab = Panel(child=layout, title="Korelasi Saham")
    return tab
