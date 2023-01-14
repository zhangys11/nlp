from sklearn.feature_extraction.text import CountVectorizer
from tqdm import tqdm
import jieba

# get DTM for Chinese. The special treatment is add space between Chinese words. 
# The returned corpus can be used by sklearn  TfidfVectorizer, CountVectorizer
def DTM_CHN(texts, addwrdlst = [], stpwrdlst = []):    

    for w in addwrdlst:
        jieba.add_word(w)    

    newcorpus = []

    for text in tqdm(texts):    
        words = list(jieba.cut(text, cut_all = False))    
        filtered = [item for item in words if item not in stpwrdlst]
        newtext = " ".join(filtered)
        newcorpus.append(newtext)

    # newcorpus = [" ".join(list(jieba.cut(t, cut_all = False))) for t in corpus]
    # print(newcorpus[0])

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(newcorpus)
    vocab = vectorizer.get_feature_names()
    
    return newcorpus, X, vocab