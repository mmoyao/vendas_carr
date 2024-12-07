import pandas as pd
import plotly.express as px
import streamlit as st

# Carregar os dados
car_data = pd.read_csv('vehicles.csv')

# Título do aplicativo
st.title('Venda de Veículos')

# Exibir o conjunto de dados
if st.checkbox('Mostrar dados do conjunto de dados'):
    st.write(car_data)

# Criar botão para histograma
st.subheader('Histograma do Odômetro')
if st.button('Criar histograma'):
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# Criar gráfico de dispersão
st.subheader('Gráfico de Dispersão')
if st.button('Criar gráfico de dispersão'):
    st.write('Criando um gráfico de dispersão para preço e ano do veículo')
    fig_scatter = px.scatter(car_data, x='year', y='price', 
                             title='Preço versus Ano',
                             labels={'year': 'Ano', 'price': 'Preço'})
    st.plotly_chart(fig_scatter, use_container_width=True)

# Instruções para adicionar novas funcionalidades
st.write("Selecione as opções acima para visualizar os dados e gráficos.")