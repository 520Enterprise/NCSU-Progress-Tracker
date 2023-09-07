def alphabetical(sentence):
    sentence = sentence.strip()
    sentence_list = sentence.split(" ")
    sentence_list.sort()
    return(sentence_list)
