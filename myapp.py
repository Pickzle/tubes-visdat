import yfinance as yf # Import Dataset 

from bokeh.models.widgets import Tabs # import Tabs digunakna untuk membuat tab halaman website
from bokeh.io import curdoc # import curdoc 

# Memanggil fungsi Tab Korelasi dan Line 
from correlation import create_correlation_tab 
from LineChart import create_lineplot_tab

# ANGGOTA
# ARSY BAGJA MUGIA GUNAWAN - 1301204018
# ALDONI IBRAHIM - 1301204479 #

# Membuat instance yfinance
yf.pdr_override()

# Membuat tab visualisasi correlation
correlation_tab = create_correlation_tab(yf)

# Membuat tab visualisasi line plot
lineplot_tab = create_lineplot_tab(yf)

# Membuat objek Tabs
tabs = Tabs(tabs=[correlation_tab, lineplot_tab])

# Menambahkan tabs ke dokumen Bokeh
curdoc().add_root(tabs)
