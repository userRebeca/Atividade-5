import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.io as pio

st.title("DASHVACINAS - um quadro informativos sobre covid19 - 2021")

st.set_page_config(page_title = "DASHVACINA", layout = "wide")

pio.templates.default = 'plotly'

df = pd.read_csv('vacinacao_corrigido.csv')

df['date'] = pd.to_datetime(df['date'])

fig1 = px.line(df, x = 'date', y = 'total_vaccinations', color = 'location', title = "Total de Vacinações por Data e Países" )
fig1.update_layout(xaxis_title = "Data", yaxis_title = "Total de vacinações")
fig1.show()

st.plotly_chart(fig1, use_contend_width = True)

df_br_eua_ind = df.query('location == "BRAZIL" or location == "INDIA" or location == "UNITED STATES"')

fig2 = px.pie(df_br_eua_ind, values = 'people_fully_vaccinated', names = 'location', title = "Pessoas Totalmente Vacinadas")
fig2.show()

st.plotly_chart(fig2, use_contend_width = True)

