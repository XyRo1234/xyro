from os import walk

## 폴더내의 파일명을 리스트로 만들기
filename = []                       # 파일명 리스트                     
for (dirpath, dirnames, filenames) in walk(r"D:\\Program Files\\Workspace\\UK"):   #정리할 파일 위치
    filename.extend(filenames)
    break
print(filename)

## 파일명리스트(filename)에서 txt or srt파일 골라내기.
srtfile = []                       # 골라낸 파일 리스트
for i in filename:
    if 'srt' in i:              # 'txt' or 'srt'가 포함되어있는 리스트 골라내기
        srtfile.append(i)



# for TXTSSML in srtfile:
#     file= open(r"D:\\Program Files\\Workspace\\UK\\" + TXTSSML, encoding='UTF8')
#     # data = file.read()



for TEXTSRT in srtfile:
    lines = []
    index_nums = []                     # 빈줄이 아닌 리스트 index값들 목록 리스트
    lines2 = []                         # 빈줄제외 및 불필요줄제외한 값들을 리스트

    file= open(r"D:\\Program Files\\Workspace\\UK\\" + TEXTSRT, encoding='UTF8')

    lines = file.readlines()            # 알아서 한줄한줄 리스트로 만들어줌
    print(lines)
    i = 0
    for line in lines:          # index_nums 제작, 리스트화
        if len(line) > 1:       # 빈줄은 길이가 1
            index_nums.append(i)
        i = i+1
    i = 0

    for number in index_nums:   # lines2 제작, 리스트화
        if len(lines[number]) == 2 or len(lines[number]) == 3 or len(lines[number]) == 30:   # len이 2거나 3이거나 30
            print(len(lines[number]))
        else:
            lines2.append(lines[number])        # lines2 리스트에 추가

    for line_data in lines2:    # 파일 생성 및 데이터 쓰기
        file = open("D:\\Program Files\\Workspace\\UK\\new_" + TEXTSRT, 'a', encoding='UTF8')   # "a" append    #(파일위치 및 파일생성)
        file.write(line_data)
    


file.close()