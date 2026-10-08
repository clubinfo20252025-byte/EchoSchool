import streamlit as st
from database import init_database, get_eleves, enregistrer_alerte, get_alertes

# ==================== إعدادات الصفحة ====================
st.set_page_config(
    page_title="EchoSchool",
    page_icon="📚",
    layout="centered"
)

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
    enregistrer_alerte(eleve_nom, eleve_tel, motif)
    st.success(f"✅ تم تسجيل التنبيه لـ {eleve_nom}")
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