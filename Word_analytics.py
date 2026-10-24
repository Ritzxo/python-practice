def analyze_text(text):
    # Your solution here
    
    split_words = text.split()

    clean_words = map(lambda word: word.strip('.,!?:;"()').lower(), split_words)

    list_clean_words = list(clean_words)

    unique_word = len(set(list_clean_words))

    seen_words = []

    repeated_words = []

    for i in list_clean_words:
        if i in seen_words and i not in repeated_words:
            repeated_words.append(i)
        else:
            seen_words.append(i)

    sorted_rep_words = sorted(repeated_words)

    palindrome_words = sorted(set(filter(lambda word: word == word[::-1], list_clean_words)))

    
    final_dict = {'unique_count': unique_word, 'repeated_words': sorted_rep_words, 'palindromes': palindrome_words}

    return final_dict
    
    pass