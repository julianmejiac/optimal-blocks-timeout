from scipy.stats import poisson


def find_mu(k, epsilon=0.01):
    low, high = 0, k*5
    for _ in range(20):
        mid = (low + high) / 2
        if poisson.cdf(k - 1, mid) > epsilon:
            low = mid
        else:
            high = mid
    return (low + high) / 2
N=int(input("N, el numero total de votos (por nodo): "))
h=1440
lamb=N/h
k=int(input("k, el cantidad de votos por bloque: "))
mu=find_mu(k)
T=mu/lamb
print(T)
eps=poisson.cdf(k - 1, mu)
print(f'Para bloques de tamano k={k},lambda={lamb} votos/min, tenemos que en  T={T} minutos se va a llenar el bloque con una probabilidad de {1-eps}')