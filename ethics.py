__doc__ = """
My goal is to create a sentient AI that knows what is good and bad. I am using a file with all the
basic life lessons in it. My goal is to use those life lessons, measure them against decisions,
and calculate which decision is the best to make. Overall, I want to add this to Benji's final form,
to give him the power of reasonable decision-making.

Here's the plan:
-   First, I will simplify every choice to the simplest word form, using a combination of synonyms and
    lemmatizing.
-   Then, I will use a "compare_strings" method to compare the strings to the life lessons.
-   Finally, I will use a sentiment analysis classifier (either TextBlob or Vader) to calculate 
    which decisions are the best and which are less optimal.
-   Then I will output the results to Benji, who will say them out loud.
"""

import nltk
from nltk.corpus import wordnet
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from speech import pytts

import re
import time

STOP_WORDS = stopwords.words("english")

def compare_strings(stra, strb):
    if type(stra) == str:
        syns1 = wordnet.synsets(stra)[0]
    elif type(stra) == nltk.corpus.reader.wordnet.Synset:
        syns1 = stra
    else:
        raise TypeError
    if type(strb) == str:
        syns2 = wordnet.synsets(strb)[0]
    elif type(strb) == nltk.corpus.reader.wordnet.Synset:
        syns2 = strb
    else:
        raise TypeError
    correlation = syns1.wup_similarity(syns2)
    if correlation == None:
        return 0
    else:
        return correlation

def simplify_sentence(sentence):

    def convert_pos_tag(nltk_tag):
        if nltk_tag.startswith('J'):
            return wordnet.ADJ
        elif nltk_tag.startswith('V'):
            return wordnet.VERB
        elif nltk_tag.startswith('N'):
            return wordnet.NOUN
        elif nltk_tag.startswith('R'):
            return wordnet.ADV
        else:
            return None

    def lemmatize_sentence(sentence):
        lemmatizer = WordNetLemmatizer()

        nltk_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
        wn_tagged = map(lambda x: (x[0], convert_pos_tag(x[1])), nltk_tagged)
        res_words = []
        for word, tag in wn_tagged:
            if tag is None:
                res_words.append(word)
            else:
                res_words.append(lemmatizer.lemmatize(word, tag))
        return " ".join(res_words)

    synss = []
    sentence = re.sub(r'[^\w\s]', '', (sentence.lower()))
    sentence = lemmatize_sentence(sentence)
    pos_lst = nltk.pos_tag(word_tokenize(sentence))

    template = "{}.{}.01"
    for word, pos in pos_lst:
        if word.lower() not in STOP_WORDS:
            try:
                xsyns = wordnet.synset(template.format(word, convert_pos_tag(pos)))
            except nltk.corpus.reader.wordnet.WordNetError:
                try:
                    xsyns = wordnet.synsets(word)[0]
                except IndexError:
                    synss.append(word)
                    continue
            synss.append(xsyns)
        else:
            synss.append(word)

    synss = list(synss)
    new_synss = []
    for word in synss:
        if str(word) not in STOP_WORDS:
            new_synss.append(word)

    return new_synss

def applies(choice):

    with open("data\\lessons.txt", "r") as f:
        pure_lessons = f.readlines()

    METRIC = 0.5

    lessons = [lesson.strip() for lesson in pure_lessons]

    lessons = [simplify_sentence(lesson) for lesson in lessons]
    choice = simplify_sentence(choice)
    good_lessons = []
    for lesson in lessons:
        total_correlation = 0
        for idx, word in enumerate(lesson):
            try:
                choice_word = choice[idx]
                correlation = compare_strings(word, choice_word)
                total_correlation += correlation
            except IndexError:
                break
        if total_correlation > METRIC:
            good_lessons.append((total_correlation, lesson))
    max_cor = 0
    best_lesson = None
    for cor, lesson in good_lessons:
        if cor > max_cor:
            best_lesson = lesson
            max_cor = cor
    if not best_lesson:
        return [False, None]
    else:
        return [True, pure_lessons[lessons.index(best_lesson)].strip()]

def make_decision():
    pytts("I see you have a problem.")
    num_options = None
    while not num_options:
        try:
            num_options = int(input("How many options do you have?"))
        except ValueError:
            num_options = None
            pytts("Invalid number, please try again!")

    pytts("Great! Now, please list your options to solve the problem, and keep them as generic as possible!")
    options = []
    for _ in range(num_options):
        option = input("Complete the sentence: I can...")
        options.append(option)
        del option

    for option in options:
        condition, lesson = applies(option)
        if condition:
            pytts("I believe that you should {}".format(lesson))
            break
        else:
            pytts("I believe that none of these are the best solution. Please look again and see if you can find anything else you can do.")
    time.sleep(1)
    pytts("Thank you for considering my advice!")

