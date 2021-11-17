import plotly.graph_objects as go

# d is the number of characters in the input alphabet
d = 256


def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    pat = pat.replace(" ", "")
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = pow(d, M-1)

    result = False
    if M > N:
        return result
    else:
        # preprocessing
        for i in range(M):
            p = (d * p + ord(pat[i].lower())) % q
            t = (d * t + ord(txt[i].lower())) % q
        for s in range(N - M + 1):  # note the +1
            if p == t:  # check character by character
                match = True
                for i in range(M):
                    if pat[i].lower() != txt[s + i].lower():
                        match = False
                        break
                if match:
                    result = True
            if s < N - M:
                t = (t - h * ord(txt[s].lower())) % q  # remove letter s
                t = (t * d + ord(txt[s + M].lower())) % q  # add letter s+m
                t = (t + q) % q  # make sure that t >= 0
        return result


def rabin_karp_matcher(pattern, text):
    return search(pattern, text, 2207)


# txt = "GEEKS FOR GEEKS"
# pat = "geek"
# q = 101  # A prime number
# print(rabin_karp_matcher(pat, txt))
stopwords = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and',
             'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being',
             'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did',
             "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few',
             'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having',
             'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him',
             'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into',
             'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't",
             'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other',
             'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd",
             "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's",
             'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they',
             "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under',
             'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't",
             'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why',
             "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've",
             'your', 'yours', 'yourself', 'yourselves']



jakartaIO = open('News/jakarta.txt', 'r', encoding='utf-8-sig')
jakarta_text = jakartaIO.read().lower()
jakarta_text = jakarta_text.replace("\n", " ")
jakartaIO.close()

bangkokIO = open('News/bangkok.txt', 'r', encoding='utf-8-sig')
bangkok_text = bangkokIO.read().lower()
bangkok_text = bangkok_text.replace("\n", " ")
bangkokIO.close()

taipeiIO = open('News/taipei.txt', 'r', encoding='utf-8-sig')
taipei_text = taipeiIO.read().lower()
taipei_text = taipei_text.replace("\n", " ")
taipeiIO.close()

hongkongIO = open('News/hongkong.txt', 'r', encoding='utf-8-sig')
hongkong_text = hongkongIO.read().lower()
hongkong_text = hongkong_text.replace("\n", " ")
hongkongIO.close()

tokyoIO = open('News/tokyo.txt', 'r', encoding='utf-8-sig')
tokyo_text = tokyoIO.read().lower()
tokyo_text = tokyo_text.replace("\n", " ")
tokyoIO.close()

beijingIO = open('News/beijing.txt', 'r', encoding='utf-8-sig')
beijing_text = beijingIO.read().lower()
beijing_text = beijing_text.replace("\n", " ")
beijingIO.close()

seoulIO = open('News/seoul.txt', 'r', encoding='utf-8-sig')
seoul_text = seoulIO.read().lower()
seoul_text = seoul_text.replace("\n", " ")
seoulIO.close()


# get frequency of words in a text
def frequency(text, city):
    list_of_words = text.split()
    freq = {}
    for word in list_of_words:
        freq[word] = freq.get(word, 0) + 1
    keys = freq.keys()

    print("Frequencies of word for " + city + "'s article:\n\n" + str(freq) + "\n")


# print frequency of each word in text for every cities' article

frequency(jakarta_text, 'Jakarta')
frequency(bangkok_text, 'Bangkok')
frequency(taipei_text, 'Taipei')
frequency(hongkong_text, 'HongKong')
frequency(tokyo_text, 'Tokyo')
frequency(beijing_text, 'Beijing')
frequency(seoul_text, 'Seoul')

def word_count(text):
    stop_count = 0
    list_of_words = text.split()
    for word in stopwords:
        if rabin_karp_matcher(word, text):
            stop_count = stop_count + 1
            # delete stop words
            text = text.lower().replace(word, "", 1)

    return [stop_count, len(list_of_words,)]


jakarta_stop_count, jakarta_total_words = word_count(jakarta_text)
bangkok_stop_count, bangkok_total_words = word_count(bangkok_text)
taipei_stop_count, taipei_total_words = word_count(taipei_text)
hongkong_stop_count, hongkong_total_words = word_count(hongkong_text)
tokyo_stop_count, tokyo_total_words = word_count(tokyo_text)
beijing_stop_count, beijing_total_words = word_count(beijing_text)
seoul_stop_count, seoul_total_words = word_count(seoul_text)

#print(tokyo1_stop_count)
#print(tokyo1_total_words)
#print(tokyo1_text)



x = ["Jakarta", "bangkok","taipei","hongkong","Tokyo ","beijing","seoul"]
stop_counts = [ jakarta_stop_count,bangkok_stop_count,taipei_stop_count,hongkong_stop_count,tokyo_stop_count,beijing_stop_count,seoul_stop_count]
total_words = [ jakarta_total_words,bangkok_total_words,taipei_total_words,hongkong_total_words,tokyo_total_words,beijing_total_words,seoul_total_words]

data = [
    go.Histogram(
        histfunc="sum",
        y=stop_counts,
        x=x,
        name="Stop words"
    ),
    go.Histogram(
        histfunc="sum",
        y=total_words,
        x=x,
        name="Total words"
    )
]
layout = go.Layout(
    title=go.layout.Title(
        text="Stop Words & Total Words",
        xref='paper',
        x=0
    )
)
fig = go.Figure(data=data, layout=layout)
fig.show()




jakartaIO = open('News/jakarta.txt', 'r', encoding='utf-8-sig')
jakarta_text = jakartaIO.read().lower()

jakartaIO.close()

bangkokIO = open('News/bangkok.txt', 'r', encoding='utf-8-sig')
bangkok_text = bangkokIO.read().lower()

bangkokIO.close()

taipeiIO = open('News/taipei.txt', 'r', encoding='utf-8-sig')
taipei_text = taipeiIO.read().lower()

taipeiIO.close()

hongkongIO = open('News/hongkong.txt', 'r', encoding='utf-8-sig')
hongkong_text = hongkongIO.read().lower()

hongkongIO.close()

tokyoIO = open('News/tokyo.txt', 'r', encoding='utf-8-sig')
tokyo_text = tokyoIO.read().lower()

tokyoIO.close()

beijingIO = open('News/beijing.txt', 'r', encoding='utf-8-sig')
beijing_text = beijingIO.read().lower()

beijingIO.close()

seoulIO = open('News/seoul.txt', 'r', encoding='utf-8-sig')
seoul_text = seoulIO.read().lower()

seoulIO.close()


positive_word = open('Words/positivewords.txt', 'r', encoding='utf-8-sig')
positive_text = positive_word.read().lower().split('\n')

negative_word = open('Words/negativewords.txt', 'r', encoding='utf-8-sig')
negative_text = negative_word.read().lower().split('\n')


# getting the frequency of positive, negative and neutral words in a text
def wordcount(text):
    total_length = len(text.split())
    count = 0
    positive = 0
    negative = 0

    for pat in positive_text:
        pat = pat.replace(" ", "")
        if rabin_karp_matcher(pat, text):
            positive = positive + 1
            count = count + 1
    for pat in negative_text:
        pat = pat.replace(" ", "")
        if rabin_karp_matcher(pat, text):
            negative = negative + 1
            count = count + 1
    # neutral word is equal to the total words in text minus the total count
    # of words that is positive or negative
    neutral = total_length - count
    return positive, negative, neutral


# getting the no. of positive, negative and neutral words in the text
jakarta_pos, jakarta_neg, jakarta_neutral = wordcount(jakarta_text)
bangkok_pos, bangkok_neg, bangkok_neutral = wordcount(bangkok_text)
taipei_pos, taipei_neg, taipei_neutral = wordcount(taipei_text)
hongkong_pos, hongkong_neg, hongkong_neutral = wordcount(hongkong_text)
tokyo_pos, tokyo_neg, tokyo_neutral = wordcount(tokyo_text)
beijing_pos, beijing_neg, beijing_neutral = wordcount(beijing_text)
seoul_pos, seoul_neg, seoul_neutral = wordcount(seoul_text)


print("\nJakarta's article word count")
print("Positive word: " + str(jakarta_pos) + " word(s)")
print("Negative word: " + str(jakarta_neg) + " word(s)")
print("Neutral word: " + str(jakarta_neutral) + " word(s)")

print("\nBangkok's article word count")
print("Positive word: " + str(bangkok_pos) + " word(s)")
print("Negative word: " + str(bangkok_neg) + " word(s)")
print("Neutral word: " + str(bangkok_neutral) + " word(s)")

print("\nTaipei's article word count")
print("Positive word: " + str(taipei_pos) + " word(s)")
print("Negative word: " + str(taipei_neg) + " word(s)")
print("Neutral word: " + str(taipei_neutral) + " word(s)")

print("\nHong Kong's article word count")
print("Positive word: " + str(hongkong_pos) + " word(s)")
print("Negative word: " + str(hongkong_neg) + " word(s)")
print("Neutral word: " + str(hongkong_neutral) + " word(s)")

print("\nTokyo's article word count")
print("Positive word: " + str(tokyo_pos) + " word(s)")
print("Negative word: " + str(tokyo_neg) + " word(s)")
print("Neutral word: " + str(tokyo_neutral) + " word(s)")

print("\nBeijing's article word count")
print("Positive word: " + str(beijing_pos) + " word(s)")
print("Negative word: " + str(beijing_neg) + " word(s)")
print("Neutral word: " + str(beijing_neutral) + " word(s)")

print("\nSeoul's article word count")
print("Positive word: " + str(seoul_pos) + " word(s)")
print("Negative word: " + str(seoul_neg) + " word(s)")
print("Neutral word: " + str(seoul_neutral) + " word(s)")

x = ["Jakarta", "Bangkok", "Taipei", "Hong Kong", "Tokyo", "Beijing", "Seoul"]
positive_y = [jakarta_pos, bangkok_pos, taipei_pos, hongkong_pos, tokyo_pos, beijing_pos, seoul_pos]
negative_y = [jakarta_neg, bangkok_neg, taipei_neg, hongkong_neg, tokyo_neg, beijing_neg, seoul_neg]
neutral_y = [jakarta_neutral, bangkok_neutral, taipei_neutral, hongkong_neutral, tokyo_neutral,
             beijing_neutral, seoul_neutral]

################
#    Graph     #
################
data = [
    go.Histogram(
        histfunc="sum",
        y=positive_y,
        x=x,
        name="Positive words"
    ),
    go.Histogram(
        histfunc="sum",
        y=negative_y,
        x=x,
        name="Negative words"
    ),
    go.Histogram(
        histfunc="sum",
        y=neutral_y,
        x=x,
        name="Neutral words"
     )
]
layout = go.Layout(
    title=go.layout.Title(
        text="Positive, Negative & Neutral Words",
        xref='paper',
        x=0
    )
)
fig = go.Figure(data=data, layout=layout)
fig.show()
#  Sentiment & Conclusion  #
def sentiment(positive_frequency, negative_frequency, city):
    print("\n" + city.upper())
    if positive_frequency > negative_frequency:
        x = positive_frequency/negative_frequency
        print('The articles are giving positive sentiment')
        print('So the country has positive economic/financial situation of a ratio ')
        print(value(positive_frequency, negative_frequency))
    elif negative_frequency > positive_frequency:
        x = positive_frequency/negative_frequency
        print('The articles are giving negative sentiment')
        print('So the country has negative economic/financial situation of a ratio ')
        print(value(positive_frequency, negative_frequency))
    else:
        x = positive_frequency / negative_frequency
        print('The articles are giving neutral sentiment')
        print('So the country has neutral economic/financial situation of a ratio ')
        print(value(positive_frequency, negative_frequency))

def value(positive, negative):
    e = positive/negative
    return e

print("\n Concluding the cities' economic/fjnancial situation")
sentiment(jakarta_pos, jakarta_neg, "Jakarta")
sentiment(bangkok_pos, bangkok_neg, "Bangkok")
sentiment(taipei_pos, taipei_neg, "Taipei")
sentiment(hongkong_pos, hongkong_neg, "Hong Kong")
sentiment(tokyo_pos, tokyo_neg, "Tokyo")
sentiment(beijing_pos, beijing_neg, "Beijing")
sentiment(seoul_pos, seoul_neg, "Seoul")

