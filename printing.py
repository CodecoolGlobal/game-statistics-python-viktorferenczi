import time

#ask Judy and simply print the outcome



def count_games(file_name):     # Question 1.
    file = open(file_name, "r")
    x = file.readlines()
    counter = 0
    for lines in x:
        counter += 1
    file.close()
    return counter
print("How many games are in the file?")
print(count_games('game_stat.txt'))
print()
time.sleep(1)

def decide(file_name, year):        # Question 2.
    with open(file_name, "r") as file:
       x = file.read()
       if str(year) in x:
           return True
       else:
           return False
print("Is there a game from a given year?")
year = input("Enter year: ")
print(decide('game_stat.txt',year))
print()
time.sleep(1)



def get_latest(file_name):      # Question 3.
    dic = {}
    with open(file_name, "r") as file:
        x = file.readlines()
        for lines in x:
           z = lines.split('\t')
           dic.update({z[0]:z[2]})
    last_game = max(dic, key=(lambda key: dic[key]))
    return last_game

print("Which was the latest game?")
print(get_latest('game_stat.txt'))
print()
time.sleep(1)

def count_by_genre(file_name, genre):       # Question 4.
    counter = 0
    with open(file_name, 'r') as file:
        x = file.readlines()
        for lines in x:
            if genre in lines:
                counter += 1
        return counter

print('How many games do we have by genre?')
genre = input("Enter genre: ")
print(count_by_genre('game_stat.txt',genre))
print()
time.sleep(1)


def get_line_number_by_title(file_name, title):     # Question 5.
    counter = 0
    mylist = []
    with open(file_name, 'r') as file:
        x = file.readlines()
        for lines in x:

            y = mylist.append(lines.split('\n')[:-1])
        for sublist in mylist:
            counter += 1
            sublist.append(counter)

        for sublist in mylist:
            if title in sublist[0]:
               return sublist[1]


print('What is the line number of the given game (by title)?')
title = input("Enter the title: ")
print(get_line_number_by_title('game_stat.txt',title))
