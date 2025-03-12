class WordFrequencyCounter:
    def __init__(self, text):
        self.text = text
        self.word_counts = {}

    def clean_and_split(self):
        words = []
        word = ""
        for char in self.text.lower():
            if char.isalpha():  
                word += char  
            elif word:  
                words.append(word)
                word = ""
        if word:  
            words.append(word)  
        return words  

    def count_words(self):
        words = self.clean_and_split()  
        for word in words:
            if word in self.word_counts:
                self.word_counts[word] += 1  
            else:
                self.word_counts[word] = 1  
        return self.word_counts  

text = "Hello everyone. This is a text, a simple text."
counter = WordFrequencyCounter(text)

print("\nWord Frequency Count:")
for word, count in counter.count_words().items():
    print(f"{word}: {count}")
