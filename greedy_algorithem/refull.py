def greedy():
    n = 100
    k = 5
    d = [50, 80, 39, 60, 40, 32]
    selected = [0] * len(d)
    # elements in d indicates the distance between gas stations
    num = 0
    # num indicates refueling times
    for i in range(k):
        if d[i] > n:
            print('no solution')
            # If any value in the distance is greater than n, it cannot be calculated
            return

    i, s = 0, 0

    while i <= k:
        s += d[i]
        if s >= n:
         # if the the mileage the car has traveled since the last time it was filled with gas add the distance from the current gas station to the next gas station is longer than n
            print('you are at the number', i+1, 'gas station,',
                  'you have ran', s-d[i], 'km, the next trip is', d[i], 'km, you need to refuel the gas',)
            s = d[i]
            # refuel number +1

            num += 1
            selected[i] = 1
        i += 1
    print('the location where u refueled your gas is ', selected)
    print('the number of time that you have refueled your gas is', num)


if __name__ == '__main__':
    greedy()
