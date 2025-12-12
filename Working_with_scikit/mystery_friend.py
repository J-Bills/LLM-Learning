from goldman_emma_raw import goldman_docs
from henson_matthew_raw import henson_docs
from wu_tingfang_raw import wu_docs
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#combining the docs of my friends so that I can analyze them
friends_docs = goldman_docs + henson_docs + wu_docs

bow_vectorizer = CountVectorizer()
friends_vectors = bow_vectorizer.fit_transform(friends_docs)

#creating labels for the data that we have from our friends
friends_labels = [0] * len(goldman_docs) + [1] * len(henson_docs) + [2] * len(wu_docs)

print(wu_docs[44])
print('_'*50)
print(goldman_docs[44])
print('_'*50)
print(henson_docs[44])
print('_'*50)

mystery_postcard = """
My friend,
From the 10th of July to the 13th, a fierce storm raged, clouds of
freeing spray broke over the ship, incasing her in a coat of icy mail,
and the tempest forced all of the ice out of the lower end of the
channel and beyond as far as the eye could see, but the _Roosevelt_
still remained surrounded by ice.
Hope to see you soon.
"""

mystery_vector = bow_vectorizer.transform([mystery_postcard])

friends_classifier = MultinomialNB()
friends_classifier.fit(friends_vectors, friends_labels)

predicitons = ["None Yet"]

predictions = friends_classifier.predict(mystery_vector)

mystery_friend = predictions[0] if predictions[0] else "someone else"

print("The postcard was from {}!".format(mystery_friend))



""" Running this returned 1, so that means the person who sent the letter was goldman"""