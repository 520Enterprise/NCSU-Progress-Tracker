def alphabetical(sentence):
    sentence = sentence.split(" ")
    sentence.sort()
    return sentence
def main():
    a = ['turtle', 'potato', 'bagel']
    a[1].title()
    print(a)
if __name__ == '__main__':
    main()
