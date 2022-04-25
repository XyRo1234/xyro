import re
import os



file_fullname = r"D:\test\ru-RU_test.tmx"
filename=os.path.basename(file_fullname)
file_path = os.path.dirname(file_fullname)

lang1 = 'en-GB'
lang2 = 'ru-RU'

def sentence_cut(content):
    m = re.findall("..\. ", content)
    n = re.split("..\. ", content)
    for index,value in enumerate(n):
        try:
            n.insert(index,(value+m[index]).strip())
            n.remove(n[index+1])
        except IndexError:
            break
    return list(n)

# <tu  ~  </tu> : '(?<=\<tu)(.*?)(?=<\/tu>)'
# "(?<=\<seg>)(.*?)(?=<\/seg>)"

# def extract_string(target):
#     return re.sub('<[^>]*>','',target)


with open(file_fullname, "r", encoding='utf-8') as file:           # r : read
        content = str(file.read())
        content = content.replace('\n',' ')
        # w = ''
        # for a in content:
        #     print(w)
        #     w = w + " " + str(a)

        p = re.compile("(?<=\<seg>)(.*?)(?=<\/seg>)")    # re.compile('..-[a-zA-Z]{2}')
        m = p.findall(content)                  # <re.Match object; span=(0, 5), match='ar-AE'>
        # print(m)

        en = []
        ru = []
        en_execpt = []
        ru_execpt = []

        for index, value in enumerate(m):
                value = re.sub('<[^>]*>','',value)      # <>특수기호용 꺽세내용 제거
                if(index%2==0):
                    # print(index,"짝수입니다.")
                    en_list = sentence_cut(value)                    
                    en_len = len(en_list)
                    # print(index,"짝수입니다.")
                else:
                    # print("홀수입니다.")
                    ru_list = sentence_cut(value)
                    ru_len = len(ru_list)
                    if en_len == ru_len:
                        for en_val in en_list:
                            en.append(en_val)
                        for ru_val in ru_list:
                            ru.append(ru_val)
                    else:                           # 예외항목 별도 저장
                        w=''
                        q=''
                        for i in en_list: w = w +' '+ i
                        en_execpt.append(w)
                        en_list
                        for i in ru_list: q = q +' '+ i
                        ru_execpt.append(q)

        # print(en)
        # print(ru)
        print(len(en))
        print(len(ru))


with open(f'{file_path}\\test.tmx', "w", encoding='utf-8') as file:
    file.write(f'<?xml version="1.0" encoding="utf-8"?><tmx version="1.4"><header creationtool="SDL Language Platform" creationtoolversion="8.1" o-tmf="SDL TM8 Format" datatype="xml" segtype="sentence" adminlang="{lang1}" srclang="{lang1}" creationdate="20180711T065553Z" creationid="trados2015-PC\trados2015"><prop type="x-Comment:MultipleString"></prop><prop type="x-Recognizers">RecognizeNumbers, RecognizeAcronyms, RecognizeVariables, RecognizeMeasurements, RecognizeAlphaNumeric</prop><prop type="x-IncludesContextContent">True</prop><prop type="x-TMName">{lang2}</prop><prop type="x-TokenizerFlags">DefaultFlags</prop><prop type="x-WordCountFlags">DefaultFlags</prop></header><body>')
    file.write('\n')

    for index,value in enumerate(en):
        file.write(f'<tu creationdate="20220415T{100001+index}Z" creationid="LGE\ws.jung" changedate="20220415T{100001+index}Z" changeid="LGE\ws.jung" lastusagedate="20220415T{100001+index}Z">')
        file.write('\n')
        file.write('  <prop type="x-LastUsedBy">LGE\ws.jung</prop>')
        file.write('\n')
        file.write('  <prop type="x-Context">0, 0</prop>')
        file.write('\n')
        file.write('  <prop type="x-Origin">TM</prop>')
        file.write('\n')
        file.write('  <prop type="x-ConfirmationLevel">Translated</prop>')
        file.write('\n')
        file.write(f'  <tuv xml:lang="{lang1}">')
        file.write('\n')
        file.write(f'    <seg>{en[index]}</seg>')
        file.write('\n')
        file.write('  </tuv>')
        file.write('\n')
        file.write(f'  <tuv xml:lang="{lang2}">')
        file.write('\n')
        file.write(f'    <seg>{ru[index]}</seg>')
        file.write('\n')
        file.write('  </tuv>')
        file.write('\n')
        file.write('</tu>')
        file.write('\n')

    for index,value in enumerate(en_execpt):    # 예외항목 저장
        file.write(f'<tu creationdate="20220415T{100001+index}Z" creationid="LGE\ws.jung" changedate="20220415T{100001+index}Z" changeid="LGE\ws.jung" lastusagedate="20220415T{100001+index}Z">')
        file.write('\n')
        file.write('  <prop type="x-LastUsedBy">LGE\ws.jung</prop>')
        file.write('\n')
        file.write('  <prop type="x-Context">0, 0</prop>')
        file.write('\n')
        file.write('  <prop type="x-Origin">TM</prop>')
        file.write('\n')
        file.write('  <prop type="x-ConfirmationLevel">Translated</prop>')
        file.write('\n')
        file.write(f'  <tuv xml:lang="{lang1}">')
        file.write('\n')
        file.write(f'    <seg>{en_execpt[index]}</seg>')
        file.write('\n')
        file.write('  </tuv>')
        file.write('\n')
        file.write(f'  <tuv xml:lang="{lang2}">')
        file.write('\n')
        file.write(f'    <seg>{ru_execpt[index]}</seg>')
        file.write('\n')
        file.write('  </tuv>')
        file.write('\n')
        file.write('</tu>')
        file.write('\n')

    file.write('  </body>')
    file.write('\n')
    file.write('</tmx>')


print(f'예외항목 : {en_execpt}')

with open(f'{file_path}\\{filename}.txt', "w", encoding='utf-8') as file:
    for index,i in enumerate(en_execpt):
        file.write('\n')
        if index==0: file.write(str(len(en_execpt)))
        file.write(str(index+1)+'\n')
        file.write(i)
    file.write('\n')    # en, ru구분을 위한 줄바꿈
    file.write('\n')    #
    file.write('\n')    #
    for index,i in enumerate(ru_execpt):
        file.write('\n')
        if index==0: file.write(str(len(ru_execpt)))
        file.write(str(index+1)+'\n')
        file.write(i)
