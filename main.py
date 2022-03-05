''' docstring
never eat pears
'''
def main():
    print("Hello World!")
    def gcd (m, n):
        if m<1 or n<1:
            return 0
        p, q = m, n
        if m<n:
            p, q = n, m
        while ((p%q) != 0):
            r = p % q
            p, q = q, r
        return q
    print(gcd(77, 21)) #7



if __name__ == "__main__":
    main()
