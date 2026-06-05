from pathlib import Path
from collections import Counter

def count_lines(filename):
    return len(Path(filename).read_text(encoding='utf-8').split('\n'))

def get_unique_words(filename):
    # Пример с базовой очисткой
    text = Path(filename).read_text(encoding='utf-8').lower()
    words = text.split()
    return set(words)

def get_top_words(filename, k=10):
    text = Path(filename).read_text(encoding='utf-8')
    words = text.lower().split()
    return Counter(words).most_common(k)