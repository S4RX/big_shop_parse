hryvnias_list = [['8'], ['28'], ['4'], ['10'], ['31'], ['19'], ['15'], ['14'], ['15'], ['22'], ['149'], ['279'], ['119'], ['99'], ['279'], ['35'], ['7'], ['7'], ['6'], ['9'], ['50'], ['200'], ['100'], ['500'], ['49'], ['79'], ['38'], ['10'], ['7'], ['28'], ['37'], ['669'], ['449']]
kopecks_list = [['00'], ['89'], ['10'], ['00'], ['99'], ['69'], ['99'], ['69'], ['89'], ['19'], ['00'], ['00'], ['00'], ['00'], ['00'], ['99'], ['00'], ['50'], ['59'], ['49'], ['00'], ['00'], ['00'], ['00'], ['99'], ['99'], ['49'], ['49'], ['89'], ['99'], ['29'], ['00'], ['00']]
price = []
for hryvnia in hryvnias_list:
        for kopeck in kopecks_list:
            if hryvnias_list.index(hryvnia) == kopecks_list.index(kopeck): 
                price.append((hryvnia, kopeck))
print(price)