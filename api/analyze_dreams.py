import nltk
# nltk.download()
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud

DREAM_TITLES = ['REVOLUTIONS', 'HACK_BEAN_TATTOOS']

DREAMS = {
    'REVOLUTIONS': "I was waiting for you to come visit and was w my mom running errands and so were you and then eventually I drove down to either somewhere downtown SD or to work to meet you and I was with Saif I think and maybe someone else and we had talked before you came to figure out the plan. It was some big day occurring (I think having to do w the stock market so the plan - also all of a sudden we were in NYC - was to grab food then walk down Wall Street since that’s what everyone was doing. There was a sort of serious overtone to the day despite the day representing some sort of exciting thing. We had some friends on the corner of Wall Street selling like lemonade or something bright and colorful and wanted to meet up w them when we started. I also looked at the world from some sort of satellite view and Russia was red while the rest was green and that’s bc there were people all standing in protest but then there were army members littered all over the streets watching for any revolutions (it might’ve been called Revolution day) and ready to strike back. (Kinda like in the hunger games) Because there were so many ppl Russia appeared red from such a high up view. This revolution day was supposedly happening in other countries all around the world too so pretty big day. You came and were dressed in a white burka I think and had a really grown out your beard and saif was also dressed up I think as someone and we asked who you were and you were like I’m the....Muslim Man (everyone said the Muslim man part together except for me because everyone knew who that was except for me - apparently some important historical character.) We were all sitting in some stagecoach at the time and I don’t think we ever got out to go walk around cuz I woke up. ",
    'HACK_BEAN_TATTOOS': "I went out for dinner with Raquel and Willa to parish cafe but it looked pretty different. Willa was blonde and looked like 100% different and when she entered someone was pointing out the differences and I kinda forgot what the real Willa looked like until much later. We all ordered drinks and food and the waitress was annoyed cuz I didn’t know what I wanted even tho she never gave me a menu so I used the one she was holding just for show. After we ordered the other waitress came around with an assortment of branded goodies such as shot glasses, temp tattoos, straws etc. and I decided to take a pink and purple sparkly tattoo that I would put near my rib cage which literally said the name of the restaurant I think. No one else took stuff and then eventually somehow I remembered what Willa looked like and I think she might’ve transformed back to her normal looking self. "
}

def tokenize_dreams():
    tokenized_dreams = []
    for title in DREAM_TITLES:
        tokenized_dreams.append(word_tokenize(DREAMS[title]))
    # print("tokenized dreams: ", tokenized_dreams[0])
    return tokenized_dreams

def clean_stop_words_from_dreams():
    stop_words = set(stopwords.words( 'english' ))
    dreams = tokenize_dreams()
    filtered_sentences = []
    for dream in dreams:
        filtered_sentence = [word for word in dream if not word in stop_words or word == "you"]
        filtered_sentences.append(filtered_sentence)
    # print("filtered sentences: ", filtered_sentences[0])
    return filtered_sentences

def get_word_frequency(dreams):
    for sent in clean_stop_words_from_dreams():
        freq = nltk.FreqDist(sent)
        for key,val in freq.items():
            print(str(key),':', str(val))
        freq.plot(20, cumulative=False)

def analyze_sentiment():
    pass

# WORD CLOUDS:
#  - sentiments 
#  - most frequently used words
clean_stop_words_from_dreams()
wordcloud = WordCloud().generate(DREAMS['REVOLUTIONS'])
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

if __name__ == "__main__":
    get_word_frequency(clean_stop_words_from_dreams)
