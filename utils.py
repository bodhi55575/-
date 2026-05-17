# utils.py — функции для работы с файлами (с чисткой текста)

def clean_word(word):
    """Очищает слово от знаков препинания и приводит к нижнему регистру."""
    return ''.join(char.lower() for char in word if char.isalpha())

def count_lines(filename):
    """Считает строки в файле."""
    with open(filename, 'r', encoding='utf-8') as f:
        return len(f.readlines())

def get_unique_words(filename):
    """Возвращает уникальные слова (после очистки)."""
    words = set()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                cleaned = clean_word(word)
                if cleaned:
                    words.add(cleaned)
    return words

def get_top_words(filename, n=10):
    """Возвращает топ-n слов (после очистки)."""
    freq = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                cleaned = clean_word(word)
                if cleaned:
                    freq[cleaned] = freq.get(cleaned, 0) + 1
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n]