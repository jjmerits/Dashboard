import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

#all_df = pd.read_csv("C://Users//JJMerits//Documents//indicators_crawling//test_df_all.csv")

st.title('대시보드 테스트 화면')
st.header("제목")
#st.subheader("소제목")
st.write("내용을 입력합니다.")

#st.dataframe(all_df)

st.header("경제지표")

col1, col2 = st.columns(2)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", use_column_width=True)

with col2:
    st.header("Chart Data")
    chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)
