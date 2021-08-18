def dfs(num):
    if num == n+1:
        for i in range(1, n+1):
            if result_arr[i] != 0:
                print(result_arr[i], end=' ')
        print()
    else:
        result_arr[num] = ch[num-1]
        dfs(num+1)
        result_arr[num] = 0
        dfs(num+1)


if __name__=='__main__':
    n = 7
    ch = ['1', '2', 'a', 'b', 'c', 'd', 'e']
    result_arr = [0]*(n+1)
    dfs(1)
