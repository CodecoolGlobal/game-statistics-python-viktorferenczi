#Created maximum calculator for get the most played games
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
        print(titles_list)
        for titles in titles_list:
            titleslenght_list.append(len(titles))
        return max(titleslenght_list)





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






#bonus questions:






def count_grouped_by_genre(file_name):              #bonus question 1.
    mylist = []
    genre = []
    dic = {}

    rpg_counter = 0
    survival_counter = 0
    action_counter = 0
    shooter_counter = 0
    simulation_counter = 0
    strategy_counter = 0
    sandbox_counter = 0

    with open(file_name, "r") as file:
        x = file.readlines()
        for lines in x:
            lines.split('\t')
            mylist.append(lines.split('\t')[:-1])
        for sublist in mylist:
            genre.append(sublist[3])


        for item in genre:                  #and here comes the if train
            if item == "Survival game":
                survival_counter +=1
            elif item == "RPG":
                rpg_counter+=1
            elif item == "Action-adventure":
                action_counter+=1
            elif item == "Simulation":
                simulation_counter+=1
            elif item == "First-person shooter":
                shooter_counter+=1
            elif item == "Real-time strategy":
                strategy_counter+=1
            elif item == "Sandbox":
                sandbox_counter+=1

        dic.update(
            {"Survival game":survival_counter,
             "RPG":rpg_counter,
             "Action-adventure":action_counter,
             "First-person shooter":shooter_counter,
             "Simulation":simulation_counter,
             "Real-time strategy":strategy_counter,
             "Sandbox": sandbox_counter}
        )
        return dic









#creating an ordering function for numbers
def MyOrder(list):
    new_list = []

    while list:
        minimum = list[0]
        for number in list:
            if number > minimum:
                minimum = number
        new_list.append(minimum)
        list.remove(minimum)
    return new_list

def get_date_ordered(file_name):            #bonus question 2.
    mylist = []
    dic = {}
    datelist = []
    result = []
    with open(file_name, "r") as file:
        x = file.readlines()
        for lines in x:
            lines.split('\t')
            mylist.append(lines.split('\t'))
        for sublist in mylist:
            dic.update({int(sublist[2]): sublist[0]})
        for date in dic.keys():
            datelist.append(date)
        OrderedDatelist = MyOrder(datelist)
        for dates in OrderedDatelist:
           result.append(dic[dates])
        return result



