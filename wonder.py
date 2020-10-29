import pickled as s

list_no = ['good movie', 'this movies is bullshit',
           'what a pathetic  movie', 'must watched movie',  'worst best']

polarity = 0
positive_tweet = 0
negative_tweet = 0
# rating = 0
for i in list_no:
    ef = s.sentiment(i)
    print(f'{i}   : your confidence = {ef}')
    # positive_tweet = 0
    if ef[0] == 'pos':
        positive_tweet += 1
    elif ef[0] == 'neg':
        negative_tweet += 1

print(positive_tweet)
print(negative_tweet)

rating = (positive_tweet/len(list_no)) * 10
print(f'Rating for your movie is {rating}')


'''test run
    succesful 2020.10.30 
    trying to get sentiment for given input'''