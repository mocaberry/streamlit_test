import streamlit as st  
from PIL import Image       #로컬에 있는 이미지 가져올 때 사용

#사이드바 화면
st.sidebar.header("로그인")
user_id = st.sidebar.text_input("아이디 입력",value='', max_chars=15)
user_password = st.sidebar.text_input("패스워드 입력",value="",type='password')

if user_id =="lucia" and user_password == '1234':
    st.sidebar.header("그림 목록")
    sel_options = ["","진주 귀걸이를 한 소녀", "별이 빛나는 밤", "절규", "생명의 나무", "월화정인"]
    user_opt = st.sidebar.selectbox("좋아하는 작품은?", sel_options, index=0)
    st.sidebar.write("**선택한 그림은?", user_opt)   #write는 print와 같은 개념

    # 메인 화면
    st.subheader("메인 화면")
    image_files = ["welcome.png","Vermeer.png","Gogh.png","Munch.png","Klimt.jpg","ShinYoonbok.png"]   
    #sel_options랑  순서가 맞아야 함
    sel_index = sel_options.index(user_opt)
    img_file = image_files[sel_index]
    img_local = Image.open(f"{img_file}")     
    st.image(img_local, caption=user_opt)



# 실행방법 터미널에서 streamlit run streamlit_test.py 이라고 치고, 
# 새창이 뜬 상태로 계속 작업 
# 혹 창이 닫아졌을 때는 터미널에 떠 있는 Local URL 주소로 다시 연결
