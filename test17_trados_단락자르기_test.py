from collections import namedtuple
import re

content = 'Do not place. Iam apple. You are a girl. You are a boy. ects(such candles, lamps, etc.), or heating devices(such as stoves, heaters, etc.) on the appliance.'
content2 = 'Не размещте. тялые или. хруп предметы. контейнеры, зап. едметы (такие как свечи, лампы и т.д) или приборы (такие как печи, обогреватели и т.д.) на прибор.'

contenta = 'Do not use a multi socket outlet which is not properly grounded(portable). In case of using a properly-grounded multi socket outlet (portable), use the multi socket outlet with the current capacity of the power code rating or higher and use the multi socket outlet only for the appliance. Failure to do so may result in electric shock or fire due to the heat of multi socket outlet. The power may be shut off when the circuit breaker is operated.'
content2a = 'Не используйте неправильно заземленные портативные розетки-разветвители. Правильно заземленная портативная розетка-разветвитель должна иметь допустимую нагрузку по току, соответствующую номинальной или превышающую ее. Используйте розетку-разветвитель только для данного устройства. Несоблюдение этих инструкций может привести к поражению электрическим током или пожару из-за нагревания розетки-разветвителя. При срабатывании автоматического выключателя питание может быть отключено.'

contentb = 'If needed. loosen the mounting fasteners b that connect the refrigerator door and handle using a 1/4 in. Allen wrench fasteners.'
content2b = 'Au besoin. desserrez les fixations de montage b qui se vissent à la porte et à la poignée du réfrigérateur à l’aide d’une clé Allen de 1/4 po, puis retirez les fixations de montage.'



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

sentence_cut(contentb)





def sentence_cut(content,content2):
    m = re.findall("..\. ", content)
    # print(m)
    n = re.split("..\. ", content)
    # print(n)

    m2 =  re.findall("..\. ", content2)
    n2 = re.split("..\. ", content2)

    for index,value in enumerate(n):
        try:
            # print(len(n))
            # print(index)
            n.insert(index,(value+m[index]).strip())
            # print(n)
            n.remove(n[index+1])
            # print(n)
        except IndexError:
            break

    for index,value in enumerate(n2):
        try:
            # print(len(n2))
            # print(index)
            n2.insert(index,(value+m2[index]).strip())
            # print(n2)
            n2.remove(n2[index+1])
            # print(n2)
        except IndexError:
            break
    return list(n), list(n2)
n, n2 = sentence_cut(contenta, content2a)

# print(len(n))
# print(len(n2))

