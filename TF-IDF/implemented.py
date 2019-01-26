from sklearn.feature_extraction.text import TfidfVectorizer

docA = "The car is driven on the road"
docB = "The truck is driven on the highway"
docC = "The duck was driven on the road"

tfidf = TfidfVectorizer()

response = tfidf.fit_transform([docA, docB, docC])

feature_names = tfidf.get_feature_names()
for col in response.nonzero()[1]:
    print (feature_names[col], ' - ', response[0, col])

    #scrubbing grammar / regex 
    #stop words
    #todo, processing the data