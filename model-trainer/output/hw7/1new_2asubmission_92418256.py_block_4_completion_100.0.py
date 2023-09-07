def alphabetical(sentence):
    sentence = sentence.split(' ')
    sentence.sort()
    return sentence
def main():
    print(alphabetical("I do not like to code this class sucks"))
if __name__ == '__main__':
    main()
