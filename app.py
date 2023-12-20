import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title='IBGE - SIDRA', page_icon=':mag_right:', layout='wide')

tabelas = pd.read_csv('codigos_tabelas.txt',sep='\t', names=['cod', 'tabela'])


st.title('Exploração dados SIDRA')

col1, col2 = st.columns([.8, .2])

tabOpt = col1.selectbox(label='Selecione a tabela', options=tabelas.tabela, index=None)

resoOpt = col2.selectbox(label='Selecione o nível de território', options=['UF', 'Municipio'])
territorios = {'UF':'3', 'Municipio':'6'}





if tabOpt:
    tableCode = tabelas.query("tabela == @tabOpt").cod.values[0]
    tabOptCol, tabCodeCol = st.columns(2)
    
    tabOptCol.success(f'Tabela: {tabOpt} | Código: {tableCode} | Territorio: {resoOpt}')
    tabCodeCol.success(f"URL: https://apisidra.ibge.gov.br/values/t/{tableCode}/n{territorios.get(resoOpt)}/all")

    with st.spinner('Carregando tabelas de dados do IBGE...aguarde'):
        data = requests.get(f"https://apisidra.ibge.gov.br/values/t/{tableCode}/n{territorios.get(resoOpt)}/all").json()
        st.divider()
        st.dataframe(data, use_container_width=True)

