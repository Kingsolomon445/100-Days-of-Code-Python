facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0
# TODO: Catch the exception and make sure the code runs without crashing.
for post in facebook_posts:
    try:
        likes = post['Likes']
    except KeyError:
        likes = 0
    finally:
        total_likes += likes

print(total_likes)
