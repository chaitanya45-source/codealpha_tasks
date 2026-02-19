from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.preprocess import preprocess

class FAQChatbot:

    def __init__(self, faq_data):
        self.faq_data = faq_data

        questions = [faq[0] for faq in faq_data]
        processed = [preprocess(q) for q in questions]

        self.vectorizer = TfidfVectorizer()
        self.faq_vectors = self.vectorizer.fit_transform(processed)

    def get_response(self, user_query):
        user_query = preprocess(user_query)
        user_vector = self.vectorizer.transform([user_query])

        similarity = cosine_similarity(user_vector, self.faq_vectors)

        best_index = similarity.argmax()
        score = similarity[0][best_index]

        if score < 0.2:
            return "Sorry, I don't understand."

        return self.faq_data[best_index][1]
