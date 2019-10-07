from printing import  year,genre,title

#ask Judy, print it and store it in a single text file with all the answers she needs



def count_games(file_name):     # Question 1.
    file = open(file_name, "r")
    x = file.readlines()
    counter = 0
    for lines in x:
        counter += 1
    file.close()
    with open("answers.txt",'a') as file:
        file.writelines(str(counter)+'\n')



def decide(file_name, year):        # Question 2.
    with open(file_name, "r") as file:
       x = file.read()
       with open("answers.txt", 'a') as file:
           if str(year) in x:
               file.writelines('True'+'\n')
           else:
               file.writelines('False'+'\n')




def get_latest(file_name):      # Question 3.
    dic = {}
    with open(file_name, "r") as file:
        x = file.readlines()
        for lines in x:
           z = lines.split('\t')
           dic.update({z[0]:z[2]})
    last_game = max(dic, key=(lambda key: dic[key]))
    with open("answers.txt", 'a') as file:
        file.writelines(str(last_game)+'\n')





def count_by_genre(file_name, genre):       # Question 4.
    counter = 0
    with open(file_name, 'r') as file:
        x = file.readlines()
        for lines in x:
            if genre in lines:
                counter += 1
        with open("answers.txt", 'a') as file:
            file.writelines(str(counter)+'\n')





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
                file = open("answers.txt", 'a')
                file.writelines(str(sublist[1])+'\n')


count_games('game_stat.txt')
decide('game_stat.txt',year)
get_latest('game_stat.txt')
count_by_genre('game_stat.txt',genre)
get_line_number_by_title('game_stat.txt',title)
