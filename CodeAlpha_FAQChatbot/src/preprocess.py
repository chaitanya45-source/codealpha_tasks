import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w.isalnum()]
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if w not in stop_words]
    return " ".join(tokens)
