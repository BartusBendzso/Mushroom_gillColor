import pickle

def predict(data, model):
    clf = pickle.load(open(model,'rb'))
    return clf.predict(data)
