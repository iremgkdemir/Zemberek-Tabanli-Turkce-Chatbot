from chatbot import ChatBot
from database import fetch_all_logs, fetch_logs_by_date, clear_old_logs
import calendar
from datetime import datetime

def display_all_logs():
    """
    Veritabanındaki tüm kayıtları görüntüler.
    """
    logs = fetch_all_logs()
    for log in logs:
        print(f"ID: {log[0]}, User: {log[1]}, Bot: {log[2]}, Time: {log[3]}")

def display_logs_by_date(start_date, end_date):
    """
    Belirli bir tarih aralığındaki kayıtları görüntüler.
    """
    logs = fetch_logs_by_date(start_date, end_date)
    for log in logs:
        print(f"ID: {log[0]}, User: {log[1]}, Bot: {log[2]}, Time: {log[3]}")

def display_logs_by_month(year, month):
    """
    Verilen yıl ve ay için kayıtları görüntüler.
    """
    # Ayın ilk günü ve son gününü belirle
    start_date = f"{year}-{month:02d}-01"
    last_day = calendar.monthrange(year, month)[1]
    end_date = f"{year}-{month:02d}-{last_day:02d}"

    print(f"\n{year} Yılı {month}. Ay İçin Kayıtlar ({start_date} - {end_date}):")
    display_logs_by_date(start_date, end_date)

if __name__ == "__main__":
    # Eski kayıtları bir kereye mahsus temizle
    # clear_old_logs()
    
    # Chatbot'u başlat
    bot = ChatBot()
    bot.greet()

    # Veritabanındaki tüm kayıtları görüntüle
    print("\nTüm Kayıtlar:")
    display_all_logs()

    # Belirli bir ay için kayıtları görüntüle (Örneğin Ağustos 2024)
    display_logs_by_month(2024, 8)



