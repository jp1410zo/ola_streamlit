import streamlit as st
import pandas as pd
import numpy as np



st.write("Olá mundo! Vai Brasil")
st.write("Hoje é 3 x 0")

"""
# Meu primeiro app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write("Tabelha estatica com write MAGIC")
df


st.write("Tabela estatica com table")
st.table(df)


st.write("Gerando dados aleatório")
dataframe = np.random.randn(10,20)
st.dataframe(dataframe)



st.write("Destacando alguns elementos")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))


st.write("Grafico de linhas com st.line_chart()")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write("Usando st.maps() para plotar dados em um mapa")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

st.write("Componentes de layout/front end")
x = st.slider('x',   
        min_value=10,
        max_value=50,
        step=2)  # 👈 this is a widget

st.write(x, 'ao quadrado é', x * x)


st.write("Recebendo entrada da usuario com text input")

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name
