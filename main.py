# import command to import json
# import datetime function to incorporate system time into the python project

import json
from datetime import datetime

# turning the json file into an open command variable
# open command to open the separate json data list
# naming variable 'songs' to load the data in the json file named 'songs'

# indented in a loop so the code becomes repeatable
while True:
    with open('/Users/isabellatruong/Downloads/PythonProject/songs.json') as json_file :
        data = json.load(json_file)
        songs = data["songs"]

    # define time of day function
    # define variable current_hour to grab the current time
    def get_time_of_day():
        current_hour = datetime.now().hour

    # Time Algorithm
    # if the current time is between 4am-11am, it is considered morning
    # between 11am-2pm is considered midday
    # between 2pm-6pm is considered afternoon
    # Then, anything "else" is considered night time

        if 4 <= current_hour < 11:
            return "morning"
        elif 11 <= current_hour < 14:
            return "midday"
        elif 14 <= current_hour < 18:
            return "afternoon"
        else:
            return "night"

    # I tried to use a weights approach below. However, this did not work in the way I wanted
    # I wanted for more inputs that match to increase exponentially rather than adding 1.

    # weights = dict(weather=3, time=2, month=1)
    # if song["weather"] == weather:
    #     score += weights["weather"]
    #
    # if song["time"] == time:
    #     score += weights["time"]
    #
    # if song["month"] == birthday:
    #     score += weights["month"]


    # defines scoring system for recommender
    # all songs start as 0, if input matches, add 1
    # if more inputs match, the score is exponentially increased by 3


    def recommend_songs(birthday, weather, time):
        scored_songs = []

        for song in songs:
            matches = 0

            if song["weather"] == weather:
                matches += 1

            if song["time"] == time:
                matches += 1

            if song["month"] == birthday:
                matches += 1

            # Exponential scoring algorithm (includes -1 to make baseline 0 if no songs match.)
            score = 3 ** matches - 1

            scored_songs.append((score, song))

    # sorts the scores and assigns songs
    # define function and python calls getitem
        def function(x):
            return x[0]

    # key=function runs through the list and is prompted to sort
    # reverse=true puts the highest output first in a list
        scored_songs.sort(key=function,
                          reverse=True)

    # returns list up to 5 items
        return scored_songs[:5]

    print("\033[1mDAYLIST BIRTHDAY PLAYLIST\033[0m")
    print("Welcome to your personalised birthday daylist! Please answer the prompts below to find your personalised recommendations of Seventeen and wave to earth songs.")
    print("========================")

    # prompts user for inputs with function to disregard typing in lower or uppercase
    birthday = input("What month were you born? ").lower()
    weather = input("What's the weather like? (sunny, cloudy, rainy) ").lower()

    # get time from system time
    time = get_time_of_day()

    # display what their inputs are
    # \n prints on a new line

    print("\n\033[1mYour answers:\033[0m")
    print("\033[1mBirthday:\033[0m", birthday)
    print("\033[1mWeather:\033[0m", weather)
    print("\033[1mTime:\033[0m", time)

    print("\n\033[1mRecommendations:\033[0m")

    # print score list and recommendations in order
    recommendations = recommend_songs(birthday,weather,time)

    # print total score - title of song - artist of song
    for score, song in recommendations:
        print(score, "-", song["title"], "-", song["artist"])

# prompt user to either continue or terminate the code
    exit_code = input("Continue? (y/n)").lower()
    if exit_code == "n":
        print("Goodbye!")
        break
