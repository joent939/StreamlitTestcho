import streamlit as st

st.title("강보라 Web Site")
input_user_name = st.text_input(label="User Name", value="")

checkbox = st.checkbox('연수 고기 사주기')
btn_clicked = st.button("Confirm", key='confirm_btn', disabled=(checkbox is False))

if btn_clicked:
    con = st.container()
    con.caption("Result")
    con.write(f"Hello~ 뽈 고마워 고기 잘먹을께")
