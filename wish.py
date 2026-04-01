import streamlit as st

# Website ka title aur icon
st.set_page_config(page_title="Happy Advance Birthday!", page_icon="🎂")

# Page change karne ke liye memory
if 'page' not in st.session_state:
    st.session_state.page = 0

def next_page():
    st.session_state.page += 1

# Page 0: Welcome Message
if st.session_state.page == 0:
    st.title("Ek Special Surprise! 🎁")
    st.write("29 April aane mein thoda waqt hai, par main wait nahi kar paya!")
    st.write("Tumhare liye ek chhota sa quiz hai. Ready?")
    st.button("Haan, Main Ready Hu! ❤️", on_click=next_page)

# Page 1: Pehla Sawal
elif st.session_state.page == 1:
    st.title("Sawal 1 💭")
    st.write("Humari sabse favorite memory kaun si hai?")
    ans1 = st.radio("Choose multipul :", ["First Kiss Moment(❁´◡`❁)", "Our First Hug 🫂", "First time milna", "All of Above"])
    st.success("Aww! Yeh meri bhi favorite hai! 🥰")
    st.button("Next Question", on_click=next_page)

# Page 2: Dusra Sawal
elif st.session_state.page == 2:
    st.title("Sawal 2 🍕")
    st.write("Agar main ek khana (food) hota, toh main kya hota?")
    ans2 = st.radio("Choose karo:", ["Pizza", "Maggi", "Biryani", "Kuch aur..."])
    st.button("Next Question", on_click=next_page)

# Page 3: Teesra Sawal
elif st.session_state.page == 3:
    st.title("Sawal 3 🥺")
    st.write("Mujhe tumhari kaun si aadat sabse zyada pasand nhi hai?")
    ans3 = st.text_area("Batao batao...")
    if ans3: 
        st.button("Next Question", on_click=next_page)

# Page 4: Chautha Sawal
elif st.session_state.page == 4:
    st.title("Aakhri Sawal! 🙈")
    st.write("Kya tum is duniya ki sabse pyari wife ho?")
    ans4 = st.radio("Jawab do:", ["Bilkul, nhi!", "100% Yes!","Pure ki pure!"])
    st.button("Ready to Surprise! 🎊", on_click=next_page)

# Page 5: Final Wish
elif st.session_state.page == 5:
    st.balloons() # Screen par balloons udayega
    st.title("🎂 Happy Advance Birthday! 🎂")
    st.subheader("29 April 2026 Today is my Wife's Birthday!")
    st.write("Tum meri zindagi ki sabse khubsurat wajah ho. Tumhare sath har din special hota hai.")
    st.write("I love you sooooooo much my dear wife My dear Bubu ! ❤️")