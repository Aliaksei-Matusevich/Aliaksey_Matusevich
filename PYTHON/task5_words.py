text = "Во входной строке записан текст Словом считается последовательность непробельных символов идущих подряд слова разделены одним или большим числом пробелов или символами конца строки Определите сколько различных слов содержится в этом тексте"
words = set(text.lower().split())
print("Колличество различных слов в тексе =",len(words))