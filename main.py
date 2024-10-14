
import string
from collections import defaultdict

documents = [
    "Your care set up, do not pluck my care down.",
    "My care is loss of care with old care done.",
    "Your care is gain of care when new care is won."
]

def preprocess_text(text):
    punc = string.punctuation
    s = list(text)
    clean_text = "".join([char for char in s if char not in punc])
    return clean_text.lower().split()

def count_word_occurrences(word, documents):
    word_counts = defaultdict(int)

    for idx, doc in enumerate(documents):
        words = preprocess_text(doc)
        count = sum(1 for w in words if w == word)
        if count > 0:
            word_counts[idx] = count

    sorted_docs = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    return [doc[0] for doc in sorted_docs]

texts = [[word for word in preprocess_text(document)] for document in documents]

replacements = (', ', '-', '!', '?')
for doc in documents:
    my_str = doc
    for r in replacements:
        my_str = my_str.replace(r, ' ')
    words_replaced = my_str.split()

frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

for _ in range(1):
    care_order = count_word_occurrences("care", documents)
    print("Dokumenty posortowane według częstotliwości występowania słowa 'care':", care_order)

    is_order = count_word_occurrences("is", documents)
    print("Dokumenty posortowane według częstotliwości występowania słowa 'is':", is_order)



