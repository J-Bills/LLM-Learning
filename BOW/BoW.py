from BOW.preprocessing import preprocess_text


#we want to take a sentence of words and have them be output as a dictionary that keeps counts of the their frequency

#define text_to_bow() below:
def text_to_bow(some_text):
    bow_dictionary = dict()
    #we are taking the words and putting them into our method to be processed
    #this ensures that words that differ in small ways are counted the same ex: 'game' and 'Games'
    tokens = preprocess_text(some_text)
    for token in tokens:
        bow_dictionary[token] = bow_dictionary.get(token,0) + 1
    return bow_dictionary



def main():
    print(text_to_bow("I love fantastic flying fish. These flying fish are just ok, so maybe I will find another few fantastic fish..."))

if __name__ == "__main__":
    main()
    