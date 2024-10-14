import string

def preprocess_text(text):
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, '')
    return text.split()

def count_word_occurrences(word, documents):
    word = word.lower()
    result = []

    for idx, doc in enumerate(documents):
        words = preprocess_text(doc)
        count = words.count(word)

        if count > 0:
            result.append((idx, count))
    result.sort(key=lambda x: (-x[1], x[0]))

    return [doc[0] for doc in result]

def search_documents(documents, queries):
    for query in queries:
        result = count_word_occurrences(query, documents)
        print(result)

if __name__ == "__main__":
    ld = int(input("PODAJ LICZBĘ DOKUMENTÓW: "))

    documents = [input(f"DOKUMENT {i + 1}: ").strip() for i in range(ld)]

    lz = int(input("PODAJ LICZBĘ ZAPYTAŃ: "))

    queries = [input(f"ZAPYTANIE {i + 1}: ").strip().lower() for i in range(lz)]

    search_documents(documents, queries)

