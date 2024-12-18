import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('averaged_perceptron_tagger_rus')

# Функция для анализа текста
def analyze_text(text):
    # Токенизация текста
    words = word_tokenize(text.lower())  # Приводим к нижнему регистру
    # Определение частей речи
    pos_tags = pos_tag(words)

    # Формирование результирующего списка
    result = [(word, tag) for word, tag in pos_tags]

    return result
