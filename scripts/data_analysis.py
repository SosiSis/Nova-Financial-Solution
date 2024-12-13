from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def sentement_analysis(data_frame):
    data_frame['sentiment'] = data_frame['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    data_frame['sentiment_category'] = data_frame['sentiment'].apply(
        lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'neutral'
    )
    print(data_frame['sentiment_category'].value_counts())


def topic_modeling(data_frame):
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(data_frame['headline'])

    lda = LatentDirichletAllocation(n_components=5, random_state=42)
    lda.fit(X)

    for idx, topic in enumerate(lda.components_):
        print(f"Topic {idx}:")
        print([vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]])
     

     