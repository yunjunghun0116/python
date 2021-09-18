import sys


def solve_n_queens(N):
    def is_available(current_candidate,current_col):
        current_row = len(current_candidate)
        for queen_row in range(current_row):
            if current_candidate[queen_row] == current_col : 
                return False
            elif abs(current_candidate[queen_row]-current_col) == current_row-queen_row:
                return False
        return True


    
    def dfs(N,current_row,current_candidate,final_result):
        if current_row == N:
            result = current_candidate[:]
            final_result.append(result)
            return
        for candidate_col in range(N):
            if is_available(current_candidate,candidate_col):
                current_candidate.append(candidate_col)
                dfs(N,current_row+1,current_candidate,final_result)
                current_candidate.pop()

    final_result = []
    dfs(N,0,[],final_result)
    return len(final_result)

def main():
    n = int(sys.stdin.readline())
    print(solve_n_queens(n))

if __name__ == '__main__':
    main()




