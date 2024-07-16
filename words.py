words = ["hello", "I", "hate", "these", "videos"]
for word in words:
    print(word.upper())
def print_upper_words(words):
   
    for word in words:
        print(word.upper())
        
def print_upper_words(words):
    
    for word in words:
        if word.lower().startswith('e'):
            print(word.upper())

def print_upper_words(words, start_letters):
   
    for word in words:
        if word[0].lower() in start_letters:
            print(word.upper())


words = ["I", "hate", "these", "videos", "example"]
start_letters = {'h', 'v'}
print_upper_words(words, start_letters)