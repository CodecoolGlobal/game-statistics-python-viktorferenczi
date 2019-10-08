from printing2 import game

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
            with open("answers2.txt", 'a') as file:
                file.write(dic[maximum_sold]+'\n')






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
        with open("answers2.txt", 'a') as file:
            file.write(str(sum(sold))+'\n')








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
        with open("answers2.txt", 'a') as file:
            file.write(str(MyAvgCalculator(selling))+'\n')








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
        with open("answers2.txt", 'a') as file:
            file.write(str(max(titleslenght_list))+'\n')





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
        with open("answers2.txt", 'a') as file:
            file.write(str(round(MyAvgCalculator(date)))+'\n')







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
        with open("answers2.txt", 'a') as file:
            file.write(str(dic[title]))


get_most_played("game_stat.txt")
sum_sold("game_stat.txt")
get_selling_avg("game_stat.txt")
count_longest_title("game_stat.txt")
get_date_avg("game_stat.txt")
get_game("game_stat.txt",game)
