import folium
from folium.plugins import HeatMap
import pandas as pd

#locais = []

ler = pd.read_excel('local.xlsx')

mapa = folium.Map(location=[-9.026078, -70.441312],
    zoom_start=8)

#for index, linha in ler.iterrows():
#    temp = [linha["LAT"],linha["LONG"]]
#    locais.append(temp)

locais = ler[["LAT", "LONG"]].values.tolist()

HeatMap(locais, radius=50).add_to(mapa)

mapa.save('mapa.html')



