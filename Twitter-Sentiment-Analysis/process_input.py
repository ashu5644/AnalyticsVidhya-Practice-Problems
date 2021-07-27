import re
import nltk
import pickle
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def map_func(text):
    text = text.replace("@user"," ")
    text = re.sub("[^a-zA-Z0-9#']+", " ",text)
    re.sub(' +',' ',text)
    text = text.lower().strip()
    text = [w for w in text.split(" ") if w not in stop_words]
    text = " ".join(text)
    return text

model = pickle.load(open('model.pkl','rb'))
tfidf_vect = pickle.load(open('tfidf_vector.pkl','rb'))

def func(sent):
    sent = map_func(sent)
    x = tfidf_vect.transform([sent])
    y = model.predict(x)
    return str(y[0])


