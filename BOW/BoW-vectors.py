""" Sometimes a dictionary is not enough. Most modelling applications use vectors or Feature Vectors. 
    A feature vector is a numeric representation of an item's most important features. Each item has it's own column.
    If a feature exists for the item, you could represent that with a 1
    
    For the bag of words example we would have documents and the features would be the different words. And we would want to know how many times each word occurred.
    This process is called vectorization
    
    To know which vector index corresponds to each word we create features dictionary of all the vocab in out training data mapped to indices."""
from BOW.preprocessing import preprocess_text

def create_features_dictionary(documents):
    """This will be the list of string documents that will be passed in"""
    features_dictionary = dict()
    # features_dictionary is where we will map all of the terms to index numbers
    merged = " ".join(documents)
    # merging the documents together so that we can process them
    tokens = preprocess_text(merged)
    # this index corresponds to the the word's first vector index.
    index = 0
    for token in tokens:
        if token not in features_dictionary:
            features_dictionary[token] = index
            index += 1
    return features_dictionary, tokens

training_documents = ["Five fantastic fish flew off to find faraway functions.", "Maybe find another five fantastic fish?", "Find my fish with a function please!"]

# We've created a feature dictionary that we can use to make vectors
feature_dictionary = create_features_dictionary(training_documents)[0]

def text_to_bow_vector(some_text, features_dictionary):
    # bow_vector = [0 for _ in range(len(features_dictionary))]
    bow_vector = [0] * len(features_dictionary)
    tokens = preprocess_text(some_text)
    
    for token in tokens:
        feature_index = features_dictionary[token]
        bow_vector[feature_index] += 1
    return bow_vector, tokens
    
features_dictionary = {'function': 8, 'please': 14, 'find': 6, 'five': 0, 'with': 12, 'fantastic': 1, 'my': 11, 'another': 10, 'a': 13, 'maybe': 9, 'to': 5, 'off': 4, 'faraway': 7, 'fish': 2, 'fly': 3}

text = "Another five fish find another faraway fish."
print(text_to_bow_vector(text, feature_dictionary)[0])