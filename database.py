import sqlite3
from datetime import datetime

def init_database():
    conn = sqlite3.connect('digischool.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS eleves (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        classe TEXT NOT NULL,
        tel_parent TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS alertes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        eleve_nom TEXT,
        tel_parent TEXT,
        motif TEXT,
        date TEXT,
        statut TEXT
    )''')
    c.execute("SELECT COUNT(*) FROM eleves")
    if c.fetchone()[0] == 0:
        eleves_demo = [
            ('أحمد بناني', '3 ابتدائي', '+212600000001'),
            ('فاطمة العلوي', '4 ابتدائي', '+212600000002'),
            ('يوسف الإدريسي', '5 ابتدائي', '+212600000003'),
            ('خديجة أمزيل', '3 ابتدائي', '+212600000004'),
            ('عمر التازي', '6 ابتدائي', '+212600000005'),
        ]
        c.executemany("INSERT INTO eleves (nom, classe, tel_parent) VALUES (?, ?, ?)", eleves_demo)
    conn.commit()
    conn.close()
    print("✅ قاعدة البيانات جاهزة")

def get_eleves():
    conn = sqlite3.connect('digischool.db')
    c = conn.cursor()
    c.execute("SELECT id, nom, classe, tel_parent FROM eleves")
    result = c.fetchall()
    conn.close()
    return result

def enregistrer_alerte(eleve_nom, tel_parent, motif):
    conn = sqlite3.connect('digischool.db')
    c = conn.cursor()
    date = datetime.now().strftime('%Y-%m-%d %H:%M')
    c.execute("INSERT INTO alertes (eleve_nom, tel_parent, motif, date, statut) VALUES (?, ?, ?, ?, ?)",
        (eleve_nom, tel_parent, motif, date, "✅ تم الإرسال"))
    conn.commit()
    conn.close()

def get_alertes():
    conn = sqlite3.connect('digischool.db')
    c = conn.cursor()
    c.execute("SELECT eleve_nom, motif, date, statut FROM alertes ORDER BY id DESC LIMIT 20")
    result = c.fetchall()
    conn.close()
    return result

if __name__ == "__main__":
    init_database()