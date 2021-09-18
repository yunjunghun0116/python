#제약조건만족문제에서 해를 찾기위한 전략으로서 백트래킹이 사용된다
#해를 찾기위해 후보군에 제약 조건을 점진적으로 체크하다 해당 후보군이 제약조건을 만족할 수 없다고
#판단되는 즉시 백트래킹(다시는 이 후보군을 체크하지 않을것)하고 다른 후보군으로 넘어가며 최적의 해를
#찾는 방식이다
#실제 구현시 고려할 수 있는 모든 경우의 수를 상태공간트리(자식노드가 여러개일수 있음)를 통해 표현
#각 후보군을 DFS방식으로 확인
#상태공간트리를 탐색하면서 제약이 맞지 않으면 해의 후보가 될만한곳으로 넘어가서 탐색
#1.promising - 해당 루트가 조건에 맞는지 검사
#2.pruning(가지치기) - 조건에 맞지 않으면 포기하고 다른 루트로 돌아서서 탐색 시간 절약하는 기법

#한 행에 두개의 퀸을 놓을수는 없기때문에 
#맨 윗줄부터 차례차례로 내려가되 더 내려갈 수 있는지 판단

#1.수직 체크 : 행이같거나 열이같거나
#2.대각선 체크 : i와 queen의 행의차와 열의차가 같을경우 대각선에있다.

#이 함수에서 수직체크/대각선체크 둘다 해줄것
def is_available(current_candidate,current_col):
    current_row = len(current_candidate)
    for queen_row in range(current_row):
        if current_candidate[queen_row] == current_col : 
            return False
        elif abs(current_candidate[queen_row]-current_col) == current_row-queen_row:
            return False
    return True
                
    


#current_candidate 지금까지 배치된 Queen의 정보를 갖고있음
#current_row 한 행씩 내려가며 dfs를 진행할것이기 때문에
def dfs(N,current_row,current_candidate,final_result):
    if current_row == N:
        #얕은 복사를 통해서 current_candidate를 넣어줄때 하단 코드를 보면 pop 이 진행되기때문에
        #일종의 동기화가 되는것이다. 그렇기때문에 current_candidate 자체를 넣어주는것이아닌
        #복사본을 통해서 넣어주어야 한다 -> 전체를 복사하는 :연산자를 통한 얇은복사를 진행한다.
        result = current_candidate[:]
        final_result.append(result)
        return
    for candidate_col in range(N):
        if is_available(current_candidate,candidate_col):
            #대부분의 dfs구조는 결국 append후 pop을 통해 제대로된 값을 찾아낼 수 있도록 하는것이 좋다.
            current_candidate.append(candidate_col)
            dfs(N,current_row+1,current_candidate,final_result)
            current_candidate.pop()


def solve_n_queens(N):
    final_result = []
    dfs(N,0,[],final_result)
    return final_result



