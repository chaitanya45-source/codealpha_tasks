from data_loader import load_faqs
from chatbot import FAQChatbot

faq_data = load_faqs("../data/faqs.txt")

bot = FAQChatbot(faq_data)

print("FAQ Chatbot Ready!")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    print("Bot:", bot.get_response(query))
