import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""# Приложение, отображающее стоимость и объем продаваемых акций за каждый день, начиная 1 января 2005 по 28 ноября 2011 года""")

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2005-1-1', end='2023-11-28')

st.write("""***Стоимость акций компании APPLE за последние 18 лет***""")
st.line_chart(tickerDf.Close)
st.write("""***Количество продаваемых акций компании APPLE за последние 18 лет***""")
st.line_chart(tickerDf.Volume)
