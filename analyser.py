def analyse(sentiment):
    if sentiment == 0:
        return "The sentiment is Neutral"
    elif sentiment > 0:
        return "The sentiment is Positive"
    else:
        return "The sentiment is Negative"
