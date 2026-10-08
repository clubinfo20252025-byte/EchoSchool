"""
ملف alerte.py - نسخة محاكاة (بدون Twilio)
"""

AUDIO_URLS = {
    "تغيب": "https://raw.githubusercontent.com/clubinfo20252025-byte/EchoSchool/main/audio/ghiyab.mp3",
    "تأخر": "https://raw.githubusercontent.com/clubinfo20252025-byte/EchoSchool/main/audio/taakhor.mp3",
    "ملاحظة سلوكية": "https://raw.githubusercontent.com/clubinfo20252025-byte/EchoSchool/main/audio/suluk.mp3"
}

def alerter_parent(nom, numero, motif, url_audio=None):
    """محاكاة إرسال SMS + مكالمة صوتية"""
    messages = {
        "تغيب": f"تنبيه مدرسي: {nom} غاب اليوم. المرجو التواصل مع المدرسة.",
        "تأخر": f"تنبيه مدرسي: {nom} تأخر عن الحصة. المرجو المتابعة.",
        "ملاحظة سلوكية": f"تنبيه مدرسي: ملاحظة بخصوص {nom}. المرجو التواصل."
    }
    
    message_sms = messages.get(motif, f"تنبيه بخصوص {nom}")
    
    return {
        'sms': True,
        'appel': True,
        'sms_info': f"📱 SMS إلى {numero}: {message_sms}",
        'call_info': f"📞 مكالمة صوتية إلى {numero} بالرسالة: {motif}",
        'audio_url': url_audio or AUDIO_URLS.get(motif, "")
    }
