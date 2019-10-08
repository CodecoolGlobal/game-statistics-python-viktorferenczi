import time


#ask Judy and simply print the outcome


def MyMaximum(list):
    max = 0
    for i in list:
        if i > max:
            max = i
        else:
            pass
    return max

def get_most_played(file_name):         #question 1.
        mylist = []
        dic = {}
        keys = []
        with open(file_name, "r") as file:
            x = file.readlines()
            for lines in x:
                lines.split('\t')
                mylist.append(lines.split('\t')[:-1])
            for sublist in mylist:
                dic.update({float(sublist[1]):sublist[0]})
            for elem in dic.keys():
                keys.append(float(elem))
            maximum_sold = MyMaximum(keys)
            return dic[maximum_sold]
print('What is the title of the most played game?')
print(get_most_played('game_stat.txt'))
print()
time.sleep(1.6)




def sum_sold(file_name):            #question 2.
    mylist =[]
    sold = []
    with open(file_name, "r") as file:
        x = file.readlines()
        for lines in x:
            lines.split('\t')
            mylist.append(lines.split('\t')[:-1])
        for sublist in mylist:
            sold.append(float(sublist[1]))
        return sum(sold)
print("How many copies have been sold total?")
print(sum_sold('game_stat.txt'))
print()
time.sleep(1.6)







#created avg calculator for get the average
def MyAvgCalculator(list):
    num = 0
    list_lenght = len(list)
    for elem in list:
        num += elem
    result = num / list_lenght
    return result

def get_selling_avg(file_name):             #question 3.
    mylist = []
    selling = []
    with open(file_name, "r") as file:
        x = file.readlines()
        for lines in x:
            lines.split('\t')
            mylist.append(lines.split('\t')[:-1])
        for sublist in mylist:
            selling.append(float(sublist[1]))
        return MyAvgCalculator(selling)
print("What is the average selling?")
print(get_selling_avg('game_stat.txt'))
print()
time.sleep(1.6)







def count_longest_title(file_name):             #question 4.
    mylist = []
    titles_list = []
    titleslenght_list = []
    with open(file_name, "r") as file:
        x = file.readlines()
        for lines in x:
            lines.split('\t')
            mylist.append(lines.split('\t')[:-1])
        for sublist in mylist:
            titles_list.append(sublist[0])
        for titles in titles_list:
            titleslenght_list.append(len(titles))
        return max(titleslenght_list)
print("How many characters long is the longest title?")
print(count_longest_title("game_stat.txt"))
print()
time.sleep(1.6)



#used avg calculator from question 3.
def get_date_avg(file_name):                        #question 5.
    mylist = []
    date = []
    with open(file_name, "r") as file:
        x = file.readlines()
        for lines in x:
            lines.split('\t')
            mylist.append(lines.split('\t')[:-1])
        for sublist in mylist:
            date.append(float(sublist[2]))
        return round(MyAvgCalculator(date))
print("What is the average of the release dates?")
print(get_date_avg("game_stat.txt"))
print()
time.sleep(1.6)




def get_game(file_name, title):                 #question 6.
    mylist = []
    dic = {}
    with open(file_name, "r") as file:
        x = file.readlines()
        for lines in x:
            lines.split('\t')
            mylist.append(lines.split('\t'))
        for sublist in mylist:
            sublist[4] = sublist[4][:-1]
            dic.update({sublist[0]:[sublist[0],float(sublist[1]),int(sublist[2]),sublist[3],sublist[4]]})
        return dic[title]
print("What properties has your chosen game? ")
game = input("Enter game: ")
print(get_game("game_stat.txt",game))
print()
