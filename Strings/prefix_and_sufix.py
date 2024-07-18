def prefix_words(prefix, word): 
    if word.startswith(prefix):
        print("Starts with {}").format(prefix)
prefix="un"
word="unhappy"
prefix_words(prefix,word)