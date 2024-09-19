
s = input("Enter a roman number: ")
romToInt = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
lon = len(s)
result = 0
a = 0
while (a < lon):
    if (a < lon - 1) and (romToInt[s[a]] < romToInt[s[a + 1]]):
        result += (romToInt[s[a + 1]] - romToInt[s[a]])
        a += 2
        print(result)
    else:
        result += romToInt[s[a]]
        a += 1
        print(result)
