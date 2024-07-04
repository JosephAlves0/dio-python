T = int(input());

for i in range(T):

    V = input();
    N = int(V.split()[0]);
    K = int(V.split()[1]);
    print(N)
    print(K)
    print(int((N % K) + (N / K)));