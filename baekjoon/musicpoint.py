import sys

def main():
    music_list = list(map(int,sys.stdin.readline().split()))
    #증가할경우 1,감소할경우 -1
    find = 0
    if music_list[0] > music_list[1]:
        find = -1
    else:
        find = 1

    index= 1
    while index < len(music_list)-1:
        if find == 1:
            if music_list[index] < music_list[index+1]:
                index+=1
            else:
                print('mixed')
                break
        else:
            if music_list[index] > music_list[index+1]:
                index+=1
            else:
                print('mixed')
                break
    
    if index == len(music_list)-1:
        if find == 1:
            print('ascending')
        else:
            print('descending')

   
        

       



if __name__ == '__main__':
    main()

