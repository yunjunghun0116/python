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