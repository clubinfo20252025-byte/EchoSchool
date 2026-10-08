import streamlit as st
from database import init_database, get_eleves, enregistrer_alerte, get_alertes
from alerte import alerter_parent, AUDIO_URLS

# ==================== إعدادات الصفحة ====================
st.set_page_config(
    page_title="EchoSchool",
    page_icon="📚",
    layout="centered"
)

st.markdown("""
    <style>
    .main { padding: 1rem; }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 14px;
        border-radius: 12px;
        border: none;
        font-weight: bold;
    }
    h1 { font-size: 26px !important; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# ==================== التهيئة ====================
init_database()

# ==================== العنوان ====================
st.title("📚 EchoSchool")
st.caption("نظام التنبيهات المدرسية للعالم القروي")
st.markdown("---")

# ==================== اختيار التلميذ ====================
st.subheader("👤 اختيار التلميذ")

eleves = get_eleves()

if not eleves:
    st.warning("⚠️ لا يوجد تلاميذ في قاعدة البيانات")
    st.stop()

options = [f"{e[1]} - {e[2]}" for e in eleves]
choix = st.selectbox("التلميذ", options, index=0)

index = options.index(choix)
eleve = eleves[index]
eleve_id, eleve_nom, eleve_classe, eleve_tel = eleve

st.info(f"📱 هاتف الولي: {eleve_tel}")

# ==================== سبب التنبيه ====================
st.subheader("📝 سبب التنبيه")

motif = st.radio(
    "اختاري السبب:",
    ["تغيب", "تأخر", "ملاحظة سلوكية"],
    horizontal=True
)

# ==================== زر الإرسال ====================
st.markdown("---")

if st.button("📤 إرسال التنبيه لولي الأمر", use_container_width=True):
    url_audio = AUDIO_URLS.get(motif, "")
    
    with st.spinner("جاري إرسال التنبيه..."):
        resultat = alerter_parent(eleve_nom, eleve_tel, motif, url_audio)
        enregistrer_alerte(eleve_nom, eleve_tel, motif)
    
    st.success(f"✅ تم إرسال SMS + مكالمة صوتية لولي أمر {eleve_nom}")
    st.info(resultat['sms_info'])
    st.info(resultat['call_info'])
    st.balloons()

# ==================== سجل التنبيهات ====================
st.markdown("---")
st.subheader("📋 سجل التنبيهات")

alertes = get_alertes()

if alertes:
    for a in alertes:
        st.markdown(f"*👤 {a[0]}* | 📝 {a[1]} | 🕐 {a[2]} | {a[3]}")
        st.markdown("---")
else:
    st.write("لا توجد تنبيهات بعد.")

st.caption("💚 EchoSchool - محاربة الهدر المدرسي")
