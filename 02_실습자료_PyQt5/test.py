print(len('흔들어 댄다. 여기 새들이 나무 위로 날아가는 것처럼 각양각색의 물고기가 나뭇가지 사이를 드나든다. 드넓은 바다'))

filepath = r'D:\01_SW_Reskilling\02.실습자료_배포용(V121)\흐\인어공주.txt'
all_lines = ''
cut_list = []
with open(filepath, 'r', encoding='utf-8') as fl:
        lines = fl.readlines()
        for line in lines:
            while line:
                cut_list.append(line[:62])
                line = line[62:]
        # for line in lines:
        #     all_lines += line
        # print(all_lines)
print(cut_list)

