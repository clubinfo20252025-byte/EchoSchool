from twilio.rest import Client

# ⚠️ ضعي هنا مفاتيحك من Twilio
ACCOUNT_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxx"
AUTH_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
TWILIO_NUMBER = "+1xxxxxxxxxx"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def envoyer_sms(numero, message):
    """إرسال رسالة SMS"""
    try:
        msg = client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=numero
        )
        return True, msg.sid
    except Exception as e:
        return False, str(e)

def envoyer_appel(numero, url_audio):
    """إجراء مكالمة صوتية آلية"""
    try:
        call = client.calls.create(
            twiml=f'<Response><Play>{url_audio}</Play></Response>',
            from_=TWILIO_NUMBER,
            to=numero
        )
        return True, call.sid
    except Exception as e:
        return False, str(e)

def alerter_parent(nom, numero, motif, url_audio):
    """إرسال SMS + مكالمة"""
    message_sms = f"تنبيه مدرسي: {nom} - {motif}. المرجو التواصل مع المدرسة."
    sms_ok, sms_info = envoyer_sms(numero, message_sms)
    call_ok, call_info = envoyer_appel(numero, url_audio)
    
    return {
        'sms': sms_ok,
        'appel': call_ok,
        'sms_info': sms_info,
        'call_info': call_info
    }