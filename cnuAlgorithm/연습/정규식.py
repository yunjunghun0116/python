import re


def main():
    # 정규식은 대부분 db에 자주 쓰인다.

    # \d의 의미는 숫자를 의미.\D는 문자를 의미(한글 영문 공백 특수기호등)
    # \w의 의미는 워드를 의미
    # \s는 공백을 의미
    
    # (\d+)([SDT])([*#]?) 숫자,SDT중 하나,*#일수도있고 없을수도있음
    # ?를 통해 있을수도없을수도있음을 알게해줌
    # p = re.compile('^\d{2}.\d{2}.\d{2}')처럼 12.23.34 와같은부분만 찾을 수 있다
    p = re.compile('(\d+)([SDT])([*|#]?)')
    lists = p.findall('hahahaha123S*6D#8T')
    print(lists)
    p2 = re.compile('(^who)(who\$$)')
    list2 = p2.findall('whowho$')
    print(list2)
    # a*은 0개이상반복, a+는 1개이상반복
    p3 = re.compile('ca+t')
    list3 = p3.findall('cat')
    print(list3)
    # a{k}는 a가k번 반복되는 용어만 가져온다. 
    # ?는 {0,1}과 같은의미로써 하나가 있거나 아예 없거나
    p4 = re.compile('ca?t')
    list4 = p4.findall('ct')
    print(list4)
    # []는 한 글자로 분리하는작업을 한다.
    p5 = re.compile('[a-zA-Z]')
    list5 = p5.findall('123caaaaaat')
    print(list5)
    search_test = p5.search('123caaaaaat')
    print(search_test)

if __name__ == '__main__':
    main()
