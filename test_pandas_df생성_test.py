import pandas as pd

Topic_No_list = ['00069924', '00069925', '00069926', '00069927']
Topic_Title_list = ['Choosing', 'the', 'Proper', 'Installation']
Region_list = ['GLOBAL', 'GLOBAL', 'GLOBAL', 'GLOBAL']


# Data = [{'No':Topic_No_list, 'Topic Title':Topic_Title_list,'Region':Region_list}]
# df = pd.DataFrame(Data)
# print(df)




Data = [Topic_No_list,Topic_Title_list,Region_list]
df = pd.DataFrame.from_records(Data)
df = df.transpose()
print(df.head())

line = 'test'
path = "00_Default\\"

with open(f'{path}New.txt', 'a', encoding='utf8') as fl:
    fl.write(line.strip())