current_movies = {"Mia Khalifa": "11:00am",
                  "Lana Rhodes": "1:00pm",
                  "Nicole Aniston": "3:00pm",
                  "August Tyler": "5:00pm"}
print("We're showing the following movies:")
for key in current_movies:
    print(key)
# Make it print all the keys
movie = input("What movie would you like the showtime for?\n")
#Ask what movie you wanna see
showtime = current_movies.get(movie)
#Showtime is used to get the data for the movie key, provided from asking the user. Use this to display the showtime
if showtime ==None:
    print("Requested movie is not showing")
else:
    print(movie, "is playing at", showtime)