import re
import random
from datetime import datetime  

class ResponseHandler:
    def __init__(self):
        self.support_responses = {
            'weather_info': r'\b(hava durumu|hava nasıl|bugün hava nasıl|manisa hava durumu|izmir hava durumu)\b',
            'date_time_info': r'\b(bugün günlerden ne|hangi gündeyiz|tarih nedir|saat kaç|tarih|saat|gün|günler)\b',
            'help': r'\b(yardım|neler yapabiliyorsun|ne yapabilirsin|yapabilirsin|hangi bilgileri verebilirsin|bilgi|bilgiler|yardımcı)\b',
            'chatbot_info': r'\b(sen kimsin|kimsin sen|kimsin|yaşın kaç|cinsiyetin ne|adın ne)\b',
            'chatbot_mood': r'\b(nasılsın|bugün nasılsın|nasıl|naber|naber chatbot|iyi misin|his)\b',
            'introduction': r'\b(selam|merhaba|günaydın|iyi günler|iyi akşamlar|iyi geceler)\b'
        }
        self.days_of_week = {
            "Monday": "Pazartesi",
            "Tuesday": "Salı",
            "Wednesday": "Çarşamba",
            "Thursday": "Perşembe",
            "Friday": "Cuma",
            "Saturday": "Cumartesi",
            "Sunday": "Pazar"
        }

    def match_reply(self, reply, weather_service):
        for intent, regex_pattern in self.support_responses.items():
            found_match = re.search(regex_pattern, reply)
            if found_match and intent == 'chatbot_info':
                return self.chatbot_info()
            elif found_match and intent == 'weather_info':
                return weather_service.weather_info(reply)
            elif found_match and intent == 'date_time_info':
                return self.date_time_info()
            elif found_match and intent == 'help':
                return self.help()
            elif found_match and intent == 'chatbot_mood':
                return self.chatbot_mood_conversation()
            elif found_match and intent == 'introduction':
                return self.introduction()
        return self.no_match_intent()

    def chatbot_info(self):
        responses = [
            "Herhangi bir cinsiyete / yaşa sahip olmayan bir AI chatbot'um ve size yardımcı olmak için buradayım.",
        ]
        return random.choice(responses)

    def date_time_info(self):
        current_time = datetime.now().strftime("%d/%m/%Y %H.%M.%S")
        weekday = self.days_of_week[datetime.now().strftime("%A")]
        return f"Bugün {weekday}, şu anki tarih ve saat: {current_time}."

    def help(self):
        responses = [
            "Size çeşitli bilgiler sağlayabilirim. Hava durumu, tarih gibi konularda sorular sorabilirsiniz.",
            "Benimle sohbet edebilir ve basit sorular sorabilirsiniz. Hava durumu, tarih gibi konularda sorular sorabilirsiniz. Elimden geleni yaparım!"
        ]
        return random.choice(responses)

    def chatbot_mood_conversation(self):
        print("Chatbot: Teşekkür ederim, iyiyim! Sen nasılsın?")
        user_response = input("Siz: ").lower()

        if any(word in user_response for word in ["iyi", "iyiyim", "harika"]):
            return "Bunu duyduğuma sevindim! Size nasıl yardımcı olabilirim?"
        elif any(word in user_response for word in ["kötü", "kötüyüm", "mutsuz", "üzgün", "fena değilim"]):
            return "Üzgünüm bunu duyduğuma, bir şeyler yapmak ister misiniz? Belki biraz hava durumu bilgisi veya günün tarihi hakkında konuşabiliriz."
        else:
            return "Anlıyorum. Başka bir konuda yardımcı olabilir miyim?"

    def introduction(self):
        responses = [
            "Merhaba! Ben bir chatbot'um ve size yardımcı olmak için buradayım.",
            "Selam! Ben bir chatbot'um ve size yardımcı olmak için buradayım.",
        ]
        return random.choice(responses)

    def no_match_intent(self):
        responses = [
            "Üzgünüm, bunu tam olarak anlayamadım. Başka bir şey sormak ister misiniz?",
            "Bu konuda bilgiye sahip değilim, ama başka bir şey hakkında konuşabiliriz!",
            "Tam olarak ne demek istediğinizi anlamadım, lütfen farklı bir şekilde sorar mısınız?"
        ]
        return random.choice(responses)


