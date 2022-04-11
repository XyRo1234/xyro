
import re

path1 = "D:\\Program Files\\Workspace\\00_Default\\m.t_00053275_r2.xml"
path2 = "D:\\Program Files\\Workspace\\00_Default\\file1.txt"
path3 = "D:\\Program Files\\Workspace\\00_Default\\file2.txt"

def extract_string(target):
    return re.sub('<[^>]*>','',target)

list = []

# with open(path1, "r", encoding='utf-8') as file:
#     content = file.read()
#     list = content.split('2D Text')
#     data = str(list[0])
#     TwoD = str(list[1])

with open(path1, "r", encoding='utf-8') as file:
    content = file.read()
    data = content
    TwoD = content

r1 = data.split('>')
r2 = TwoD.split('>')
r3 = []
r4 = []
for line in r1:
    r3.append(f'{line}>')

for line in r2:
    r4.append(f'{line}>')

for i in r3:
    file1 = extract_string(str(i))
    with open(path2, 'a', encoding='utf8') as fl:
                        fl.write(file1.strip())
                        fl.write('\n')

for i in r4:
    file2 = extract_string(str(i))
    with open(path3, 'a', encoding='utf8') as fl:
                        fl.write(file2.strip())
                        fl.write('\n')