import sqlite3
from datetime import datetime
import pytz
import pandas as pd

def create_connection():
    """
    Veritabanı dosyasına bağlanır. Dosya yoksa oluşturur.
    """
    conn = sqlite3.connect('chatbot.db')
    return conn

def create_table():
    """
    Veritabanında chat_logs tablosunu oluşturur.
    """
    conn = create_connection()
    cursor = conn.cursor()

    # Tabloyu oluşturma (Eğer tablo zaten yoksa)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chat_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT NOT NULL,
            bot_response TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

def log_interaction(user_input, bot_response):
    """
    Kullanıcı girdisi ve chatbot yanıtını veritabanına kaydeder.
    """
    conn = create_connection()
    cursor = conn.cursor()

    # Zaman damgasını al ve İstanbul zaman diliminde kaydet, saatlerde sadece "." kullan
    tz = pytz.timezone('Europe/Istanbul')
    timestamp = datetime.now(tz).strftime('%Y-%m-%d %H.%M.%S')  # Noktalı format

    # Veri ekleme sorgusu
    cursor.execute('''
        INSERT INTO chat_logs (user_input, bot_response, timestamp)
        VALUES (?, ?, ?)
    ''', (user_input, bot_response, timestamp))

    conn.commit()
    conn.close()


def fetch_all_logs():
    """
    Veritabanındaki tüm sohbet kayıtlarını alır ve zaman dilimini ayarlar.
    """
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM chat_logs')
    rows = cursor.fetchall()

    conn.close()

    # Zaman dilimini ayarlama
    tz = pytz.timezone('Europe/Istanbul')
    logs = []
    for row in rows:
        log_id, user_input, bot_response, timestamp = row
        # print(f"Raw timestamp from DB: {timestamp}")  # Ham zaman damgasını yazdır

        # İlk olarak noktalı formatta dene
        try:
            local_time = datetime.strptime(timestamp, '%Y-%m-%d %H.%M.%S').astimezone(tz)
        except ValueError:
            # Eğer bu çalışmazsa eski formatı dene
            local_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').astimezone(tz)

        logs.append((log_id, user_input, bot_response, local_time.strftime('%Y-%m-%d %H.%M.%S')))

    return logs


def fetch_logs_by_date(start_date, end_date):
    """
    Verilen tarih aralığındaki sohbet kayıtlarını alır.
    """
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM chat_logs WHERE timestamp BETWEEN ? AND ?
    ''', (start_date, end_date))
    rows = cursor.fetchall()

    conn.close()
    return rows



def clear_old_logs():
    """
    Veritabanındaki tüm eski kayıtları siler.
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM chat_logs')  # Tüm eski kayıtları sil
    conn.commit()
    conn.close()

# Tablonun oluşturulması için fonksiyonu çalıştırıyoruz
create_table()
