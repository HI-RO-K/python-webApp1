import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st

st.title('米国株価可視化アプリ')

st.sidebar.write("""
                 # GAFA株価
                 # こちらは株価可視化ツールです。以下のオプションから表示日数を指定できます。
                 """)

st.sidebar.write("""
                 ## 表示日数選択
                 """)

st.sidebar.slider('日数', 1, 50, 20)