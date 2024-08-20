from nlp_utils import NLPProcessor
from response_handler import ResponseHandler
from weather_service import WeatherService
from database import log_interaction  # Veritabanı fonksiyonunu içe aktarın

class ChatBot:
    def __init__(self):
        self.nlp_processor = NLPProcessor()
        self.response_handler = ResponseHandler()
        self.weather_service = WeatherService()
        self.exit_commands = ("çık", "kapat", "exit", "quit", "görüşürüz", "bye", "bb")

    def greet(self):
        print("Chatbot'a hoş geldiniz! (Çıkmak için 'çık', 'kapat', 'exit', 'bye' veya 'quit' yazabilirsiniz.)")
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if command in reply:
                print("Chatbot: Görüşmek üzere!")
                return True
        return False

    def chat(self):
        reply = input("Siz: ").lower()
        while not self.make_exit(reply):
            normalized_reply = self.nlp_processor.normalize_input(reply)
            if normalized_reply:  # normalize_input bir değer döndürdüyse
                response = self.response_handler.match_reply(normalized_reply, self.weather_service)
                print(f"Chatbot: {response}")
                log_interaction(reply, response)  # Yanıtı ve girdiyi kaydedin
            else:
                print("Chatbot: Anlayamadım, lütfen tekrar eder misiniz?")
            reply = input("Siz: ").lower()
