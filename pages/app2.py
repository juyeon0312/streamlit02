#https://docs.streamlit.io/develop/api-reference


import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
             'https://i.imgur.com/ECROFMC.png', 
             'https://i.imgur.com/MDKQoDc.jpg']


# 검색창 
title = st.text_input("검색하실 애니메이션 입력", "")



# 입력창에서 데이터를 받아서 해당 문자열이 일치하는 이미지를 화면에 출력해 보세요.
if title == ani_list[0]:
    st.image(img_list[0])
elif title == ani_list[1]:
    st.image(img_list[1])
elif title == ani_list[2]:
    st.image(img_list[2])




