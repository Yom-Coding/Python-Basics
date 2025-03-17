# Write a program to build a school curriculum, consisting of subjects, languages, sports and year
# Hint : Use random library, and pick 10 items for languages, 10 items for sports and 10 items for subjects

import random

subjects_list = ["Math", "Science", "History", "Geography", "Art", "Music", "Technology", "Physics", "Chemistry", "Biology", 
                 "Drama", "Economics", "Philosophy"]
languages_list = ["English", "French", "Spanish", "German", "Chinese", "Japanese", "Arabic", "Hindi", "Russian", "Portuguese", 
                  "Italian", "Korean"]
sports_list = ["Football", "Basketball", "Tennis", "Swimming", "Cricket", "Baseball", "Volleyball", "Athletics", "Gymnastics", 
               "Hockey", "Rugby", "Badminton"]

subjects = random.sample(subjects_list, 4)
languages = random.sample(languages_list, 2)
sports = random.sample(sports_list, 2)

year = random.randint(8, 12)

print("Your ideal school curriculum for year {} is : {}{}{}".format(year, subjects, languages, sports))
