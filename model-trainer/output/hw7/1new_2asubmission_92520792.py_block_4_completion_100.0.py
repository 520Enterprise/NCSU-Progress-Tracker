def alphabetical(sentence):
    sentence = sentence.strip()
    sentence_list = sentence.split(" ")
    sentence_list.sort()
    return(sentence_list)
def main():
    print (alphabetical("This is a sentence."))
if __name__ == '__main__':
    main()
