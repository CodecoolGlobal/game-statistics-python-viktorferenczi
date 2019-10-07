import sys
import os

#report files

def count_games(file_name):     # Question 1.
    file = open(file_name, "r")
    x = file.readlines()
    counter = 0
    for lines in x:
        counter += 1
    file.close()
    return counter




def decide(file_name, year):        # Question 2.
    with open(file_name, "r") as file:
       x = file.read()
       if str(year) in x:
           return True
       else:
           return False




def get_latest(file_name):      # Question 3.
    dic = {}
    with open(file_name, "r") as file:
        x = file.readlines()
        for lines in x:
           z = lines.split('\t')
           dic.update({z[0]:z[2]})
    last_game = max(dic, key=(lambda key: dic[key]))
    return last_game





def count_by_genre(file_name, genre):       # Question 4.
    counter = 0
    with open(file_name, 'r') as file:
        x = file.readlines()
        for lines in x:
            if genre in lines:
                counter += 1
        return counter





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
    if title not in x:
        raise ValueError






#bonus questions:






#created function to sort_alphabetical. For bonus question 1
def Sorting(list):
    lenght = len(list) -1
    unsorted = True

    while unsorted:
        unsorted = False
        for item in range(0,lenght):
            if list[item] > list[item +1]:
                x = list[item]
                list[item] = list[item + 1]
                list[item +1] = x
                unsorted = True
    return list

def sort_abc(file_name):        #bonus question 1.
    mylist = []
    with open(file_name, "r") as file:
        x = file.readlines()
        for lines in x:
            z = lines.split('\t')
            mylist.append(z[0])
        return Sorting(mylist)







#created function to get rid of duplicates. For bonus question 2.
def NoDuplicate(list):
    sortedlist =[]
    for item in list:
        if item not in sortedlist:
            sortedlist.append(item)
        else:
            pass
    return sortedlist

def get_genres(file_name):      # bonus question 2.
    result = []
    mylist = []
    with open(file_name, "r") as file:
        x = file.readlines()
        for lines in x:
           z = lines.split('\t')
           mylist.append(z[3])
        return NoDuplicate(Sorting(mylist))







#created a function to calculate maximum from a list. Reason for this: line 180. For bonus question 3.
def MyMaximum(list):
    max = 0
    for i in list:
        if i > max:
            max = i
        else:
            pass
    return max

def when_was_top_sold_fps(file_name):           #bonus question 3.
    mylist = []
    onlyshooterlist = []
    onlyshooterlist_final = []
    dic = {}
    keys = []
    shooter_check = open(file_name,"r")
    currentfile = shooter_check.read()
    shooter_genre_available = 'First-person shooter'
    if shooter_genre_available in currentfile:
        with open(file_name, "r") as file:
            x = file.readlines()
            for lines in x:
                lines.split('\n')
                mylist.append(lines.split('\n')[:-1])
            for sublist in mylist:
                shooter = 'First-person shooter'
                if shooter in sublist[0]:
                    onlyshooterlist.append(sublist)
            for elem in onlyshooterlist:
                onlyshooterlist_final.extend(elem)
            for line in onlyshooterlist_final:
                z = line.split('\t')
                dic.update({z[1]:z[2]})


            #top_sold = max(dic, key=(lambda key: dic[key]))

            #This one is not functioning in this situation somehow, I just have to find the maximum from the keys...
            #Don't know the reason so I created a maximum calculator function for myself



            for elem in dic.keys():
                keys.append(float(elem))
            maximum_sold = MyMaximum(keys)
            return int(dic[str(maximum_sold)])
    else:
        raise ValueError






