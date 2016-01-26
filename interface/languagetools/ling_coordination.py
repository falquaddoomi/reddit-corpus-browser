import liwc

liwc_index = liwc.LIWC_Index()


# categories from LIWC2007 dictionary that are assumedly used in the echoes of power/mark my words ling. accomm. papers
def get_matches(txt):
    liwc_matches = liwc_index.category_matches(txt, [
        "Article",
        "Certain",
        "Conj",
        "Discrep",
        "Excl",
        "Incl",
        "Ipron",
        "Negate",
        "Prep",
        "Quant",
        "Tentat",
        "I",
        "We",
        "You"
    ])

    return liwc_matches


if __name__ == '__main__':
    regulatedConflict = 'I am really angry about this. When you came to the meeting without the chart, I thought that' \
                        ' was really disrespectful of what we all had agreed upon. Ok. So. Let me tell you why I didnt ' \
                        'do it Saturday! That sounds like an excuse to me and I dont think thats helpful right now. ' \
                        'Im sorry, I thought it would be helpful for this discussion. Well, if he if he wants to tell ' \
                        'us. Ok, how about we discuss what happened there and then figure out what we can do better?'
    nonregulatedConflict = 'I really think you not having done the chart is just an example and its indicative of your ' \
                           'carelessness in general. Ok. So. Let me tell you why I didnt do it Saturday! I already know.' \
                           ' I dont think excuses are a good idea, period. I feel it would be helpful for this discussion.' \
                           ' Well, if he if he wants to tell us. I dont. You remember what I said to you last week? ' \
                           'Reasons are bullshit!'

    # positivity_count = liwc_matches['Negemo']
    # anxiety_count = liwc_matches['Anx']
    # anger_count = liwc_matches['Anger']

    print "* Non-regulated conflict: %s\n%s\n" % (nonregulatedConflict, get_matches(nonregulatedConflict))
    print "* Regulated conflict: %s\n%s\n" % (regulatedConflict, get_matches(regulatedConflict))
