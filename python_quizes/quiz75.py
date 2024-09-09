import matplotlib.pyplot as plt

def find_k(n):
    k = 0
    while 2**k < n + k + 1:
        k += 1
    return k

def plot(n):
    x = range(n)
    y = [find_k(i) for i in x]
    plt.plot(x, y)
    plt.show()

def plot_efficiency():
    x = range(1, 1000)
    y = [i/(find_k(i) +i) for i in x]
    plt.style.use('ggplot')
    plt.plot(x, y)
    plt.show()

print("find_k(3): ", find_k(3))
print("find_k(4): ", find_k(4))
print("find_k(5): ", find_k(5))
print("find_k(10): ", find_k(10))
print("find_k(20): ", find_k(20))
print("find_k(30): ", find_k(30))
print("find_k(40): ", find_k(40))

print("plotting efficiency for 0-1000")
plot_efficiency()

