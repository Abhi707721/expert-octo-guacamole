import streamlit as st
import datetime
from streamlit_lottie import st_lottie
import requests
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# एनीमेशन के लिंक्स (हम यहाँ दो अलग-अलग एनीमेशन लोड कर रहे हैं)
lottie_hearts = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_96bovdur.json") # तैरते हुए दिल
lottie_cake = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_myejig9v.json")   # नाचता हुआ केक
    # Nobita-Shizuka का प्यारा एनिमेशन लोड करना
lottie_nobita_shizuka = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_k84wkkis.json") # एक साथ बैठे हुए

# नया डिजाइन और फोंट सेटअप
st.markdown("""
    <style>
    /* Google Font को इम्पोर्ट करना */
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');

    .stApp {
        background: linear-gradient(to right, #ff9a9e, #fecfef);
        font-family: 'Dancing Script', cursive; /* यहाँ फोंट लागू किया गया है */
    }
    
    h1, h2, h3 {
        color: #d63384 !important;
        text-align: center;
        font-family: 'Dancing Script', cursive;
    }
    </style>
    """, unsafe_allow_html=True)
st_lottie(lottie_hearts, height=300, key="hearts")

# यहाँ month और day की जगह सही नंबर सोचिए
target_date = datetime.datetime(2026, 4, 29)

# आज की तारीख और समय पता करें
today = datetime.datetime.now()

# दोनों के बीच का अंतर निकालें
time_remaining = target_date - today

# दिनों की संख्या निकालें
days = time_remaining.days

# शर्त (Condition) चेक करें
# सुंदर तरीके से टाइमर दिखाने के लिए
days = time_remaining.days
if days == 0:
    st.balloons()
    st_lottie(lottie_cake, height=200, key="cake") 
    
    # यहाँ Nobita-Shizuka का वो प्यारा एनीमेशन दिखेगा! 💖
    st_lottie(lottie_nobita_shizuka, height=250, key="love_animation")
    
    st.header("🎉 Happy Birthday Ji! 🥳")
    st.subheader("आज आपका सबसे खास दिन है! ❤️")
    
    # अगर आज ही जन्मदिन है
    st.balloons() # ढेर सारे गुब्बारे उड़ाने के लिए
    st.header("🎉 Happy Birthday Ji! 🥳")
    st.subheader("आज आपका सबसे खास दिन है! ❤️")
    
elif days < 0:
    # अगर जन्मदिन बीत गया है
    st.header("🎁 आशा है आपका जन्मदिन शानदार रहा होगा!")
else:
    # अगर अभी दिन बाकी हैं (टाइमर दिखाएं)
    st.subheader("🎂 आपके जन्मदिन में अब सिर्फ इतना समय बचा है:")
    st.title(f"✨ {days} दिन ✨")
    


# Website ka title aur icon
st.set_page_config(page_title="Happy Birthday Ji !", page_icon="🎂")

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
    st.title("🎂 Happy Birthday My Mrs! 🎂")
    st.subheader("29 April 2026 Today is my Wife's Birthday!")
    st.write("Tum meri zindagi ki sabse khubsurat wajah ho. Tumhare sath har din special hota hai.")
    st.write("I love you sooooooo much my dear wife My dear Bubu ! ❤️")
