# coding: utf-8

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.


def removeDuplicates(listofElements):
    # Create an empty list to store unique elements
    uniqueList = []

    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)

    # Return the list of unique elements
    return uniqueList

# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
#
def q_1():
    import csv
    import collections
    #counts = collections.defaultdict(int)
    results=[]
    with open("data.csv", encoding="utf-8") as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            results.append(row['nationality'])
            # counts[row['nationality']] += 1

    nacionalidades =removeDuplicates(results)

    totalNacionalidades = len(nacionalidades)
    return totalNacionalidades


# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    import csv
    import collections
    #counts = collections.defaultdict(int)
    results=[]
    with open("data.csv", encoding="utf-8") as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            results.append(row['club'])
            #counts[row['club']] += 1


    clubs = removeDuplicates(results)

    totalClubs = len(clubs)
    return totalClubs

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    import csv
    import operator
    results=[]
    from itertools import islice
    with open('data.csv', encoding="utf-8") as myFile:
        reader = csv.DictReader(myFile)
        #sort =(reader, key=operator.itemgetter('full_name')
        for eachline in reader:
            print(eachline['full_name'])
            results.append(eachline['full_name'])
    print(results[0:20])
    return results[0:20]


# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    import csv
    import operator
    results=[]
    from itertools import islice
    with open('data.csv', encoding="utf-8") as myFile:
        reader = csv.DictReader(myFile)
        #sort = sorted(reader, key=operator.itemgetter('eur_wage'))
        sort = sorted(reader, key=lambda x: float(x['eur_wage']), reverse=True)
        for eachline in islice(sort, 10):
            #print(eachline['full_name'] + ' - ' + eachline['eur_wage'] + '\n')
            results.append(eachline['full_name'])

    print(results)
    return results

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    import csv
    import operator
    results=[]
    from itertools import islice
    with open('data.csv', encoding="utf-8") as myFile:
        reader = csv.DictReader(myFile)
        sort = sorted(reader, key=operator.itemgetter('age'), reverse=True)
        for eachline in islice(sort, 10):
            print(eachline['full_name'] + ' - ' + eachline['age'] + '\n')
            results.append(eachline['full_name'])

    return results


# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    import csv
    import collections
    import operator
    results=[]
    counts = collections.defaultdict(int)
    with open("data.csv", encoding="utf-8") as csvFile:
        reader = csv.DictReader(csvFile)
        sort = sorted(reader, key=operator.itemgetter('age'), reverse=False)
        for row in sort:
            counts[int(row['age'])] += 1

    results.append(dict(counts))

    print(dict(counts))

    return dict(counts)

