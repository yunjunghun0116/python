import sys

def is_anagram(s1,s2):
    #알파벳 a-z의 개수 26만큼 배열을 만들어놓고
    c1 = [0]*26
    c2 = [0]*26
    #c1에 s1을,c2에 s2를 입력해주는데 만약 a가 나오면 ord['a']를 통해 아스키코드값을 받고
    #문자열중 가장 작게나올수있는 a의 값을 빼줌으로써 a : 0,b : 1 ...의 인덱스를 갖게 저장한다.
    #그리고 해당 인덱스에 +=1을 통해 개수를 저장해준다.
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')   
        c1[pos] +=1 
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')   
        c2[pos] +=1 
    #그리고 두개의 문자열이 애너그램인지 판별하는것인데,
    isAnagram = True
    j = 0
    #while문을 통해 아나그램인지 체크한다.
    #여기서 걸러지는 조건은 c1,c2의 배열(문자열이 저장된 배열)이 애너그램일경우 같고(문자의 구성이 같고)
    #아니면 바로 isAnagram을 통해 멈춘다.
    while j < 26 and isAnagram:
        if c1[j] != c2[j]:
            isAnagram = False
        j+=1
    return isAnagram
    
def main():
    #입력받은 문자열이 대/소문자구분안하기때문에 lower()이나
    m,n = map(str,sys.stdin.readline().lower().strip().split())
    print(is_anagram(m,n))

if __name__ == '__main__':
    main()
