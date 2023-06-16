import yfinance as yf # Import Dataset 

from bokeh.models.widgets import Tabs # import Tabs digunakna untuk membuat tab halaman website
from bokeh.io import curdoc # import curdoc 

# Memanggil fungsi Tab Korelasi dan Line 
from correlation import create_correlation_tab 
from LineChart import create_lineplot_tab

# Membuat Tab 
tab1 = create_correlation_tab(yf)
tab2 = create_lineplot_tab(yf)

# Masukkan semua tab ke dalam satu aplikasi
tabs = Tabs(tabs = [tab1, tab2])

# Put the tabs in the current document for display
curdoc().add_root(tabs)
curdoc().title = "Pergerakan Saham-saham di Indonesia"