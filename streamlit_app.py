import time

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"## Write and magic"
st.write("st.write")
"magic"


"## Text elements"
st.markdown("st.markdown")
st.markdown("st.markdown with help", help="Hello!")
st.markdown(
    "Markdown features: **bold** *italic* ~strikethrough~ [link](https://streamlit.io) `code` $a=b$ 🐶 :cat: :material/home: :streamlit: <- -> <-> -- >= <= ~="
)
st.markdown("""
Text colors: 

:blue[blue] :green[green] :orange[orange] :red[red] :violet[violet] :gray[gray] :rainbow[rainbow] :primary[primary]

:blue-background[blue] :green-background[green] :orange-background[orange] :red-background[red] :violet-background[violet] :gray-background[gray] :rainbow-background[rainbow] :primary-background[primary]

:blue-background[:blue[blue]] :green-background[:green[green]] :orange-background[:orange[orange]] :red-background[:red[red]] :violet-background[:violet[violet]] :gray-background[:gray[gray]] :rainbow-background[:rainbow[rainbow]] :primary-background[:primary[primary]]
""")
st.title("st.title")
st.title("st.title with help", help="Hello!")
st.header("st.header")
st.header("st.header with help", help="Hello!")
st.header("st.header with blue divider", divider="blue")
st.header("st.header with green divider", divider="green")
st.header("st.header with orange divider", divider="orange")
st.header("st.header with red divider", divider="red")
st.header("st.header with violet divider", divider="violet")
st.header("st.header with gray divider", divider="gray")
st.header("st.header with rainbow divider", divider="rainbow")
st.subheader("st.subheader")
st.subheader("st.subheader with help", help="Hello!")
st.caption("st.caption")
st.caption("st.caption with help", help="Hello!")
st.code("# st.code\na = 1234")
st.code("# st.code with line numbers\na = 1234", line_numbers=True)
st.code(
    '# st.code with line wrapping\na = "This is a very very very very very very very very very very very very long string"',
    wrap_lines=True,
)
# with st.echo():
#     st.write("st.echo")
st.latex(r"\int a x^2 \,dx")
st.latex(r"\int a x^2 \,dx", help="Hello!")
st.text("st.text")
st.text("st.text with help", help="Hello!")
st.divider()