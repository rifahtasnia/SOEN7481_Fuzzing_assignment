def oldtax(ta):
    total = 0
    n = 0
    while ta > 0:
        if n == 1:
            if ta >= 250000:
                total = total + 250000 * 5 / 100
            else:
                total = total + ta * 5 / 100
        elif n == 2 or n == 3:
            if ta >= 250000:
                total = total + 250000 * 20 / 100
            else:
                total = total + ta * 20 / 100
        elif n == 4:
            total = total + ta * 30 / 100
            break
        else:
            total = 0
        ta = ta - 250000
        n = n + 1
    cess = total * 4 / 100
    return total + cess

def newtax(ta):
    total = 0
    n = 0
    while ta > 0:
        if n == 1:
            if ta >= 250000:
                total = total + 250000 * 5 / 100
            else:
                total = total + ta * 5 / 100
        elif n == 2:
            if ta >= 250000:
                total = total + 250000 * 10 / 100
            else:
                total = total + ta * 10 / 100
        elif n == 3:
            if ta >= 250000:
                total = total + 250000 * 15 / 100
            else:
                total = total + ta * 15 / 100
        elif n == 4:
            if ta >= 250000:
                total = total + 250000 * 20 / 100
            else:
                total = total + ta * 20 / 100
        elif n == 5:
            if ta >= 250000:
                total = total + 250000 * 25 / 100
            else:
                total = total + ta * 25 / 100
        elif n == 6:
            total = total + ta * 30 / 100
            break
        else:
            total = 0
        ta = ta - 250000
        n = n + 1
    cess = total * 4 / 100
    return total + cess
