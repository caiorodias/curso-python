T = int(input())

while T > 0:
    T -= 1
    N, K = input().split() # Ele vai receber o input e vai separar com o split
    N = int(N)
    K = int(K)
    total = int(int(N % K) + int(N / K))
  