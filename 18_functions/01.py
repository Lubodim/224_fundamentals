b = float(input())

def grade(ocenka):
    if ocenka >= 5.5:
        a = 'excellent'
    elif 4.50 <= ocenka < 5.50:
        a = "Very good"
    elif 3.50 <= ocenka < 4.50:
        a = 'Good'
    elif 2.99 < ocenka < 3.50:
        a = 'Poor'
    else:
        a = 'fail'
    return a
print(grade(b))
