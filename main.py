from utils import fac, is_prime, is_lucky, nsd


def main():
    n = 3
    print(f"Факторіал числа {n} дорівнює {fac(n)}")


print(is_prime(1))
print(is_lucky(37))
print(is_lucky(33))
print(nsd(23, 43))

if __name__ == "__main__":
    main()
