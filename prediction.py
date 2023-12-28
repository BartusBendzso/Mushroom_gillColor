import pickle

def predict_homemade(data, model):
    clf = pickle.load(open(model,'rb'))
    return clf.predict(data)
