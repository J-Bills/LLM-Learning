import pickle

training_spam_docs, training_doc_tokens, training_labels, test_labels, test_spam_docs, raw_test_clean, raw_training_clean = pickle.load(open("spam_data.p", "rb"))

data = (
    training_spam_docs,
    training_doc_tokens,
    training_labels,
    test_labels,
    test_spam_docs,
    raw_test_clean,
    raw_training_clean
)

with open("spam_data.p", "wb") as f:
    pickle.dump(data, f)
    
training_docs = [doc[1] for doc in raw_training_clean]
test_docs = [doc[1] for doc in raw_test_clean]