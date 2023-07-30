import streamlit as st

st.title("Bora Web Site")
input_user_name = st.text_input(label="User Name", value="")

checkbox = st.checkbox('연수 고기 사주기')
btn_clicked = st.button("결제하기", key='confirm_btn', disabled=(checkbox is False))

if btn_clicked:
    con = st.container()
    con.caption("Result")
    con.write(f"역시뽈~ 믿고 있었다구~~♡♡♡♡")
