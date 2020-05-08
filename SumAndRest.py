import time

cache_keys = [1]
cache_values = [45]


def sum_dif_rev(n):
    # your code here
    def reverse_number(n):
        r = 0
        while n > 0:
            r *= 10
            r += n % 10
            n //= 10
        return r

    if n in cache_keys:
        return cache_values[cache_keys.index(n)]
    found = cache_keys[-1]
    num = cache_values[-1]

    while n > found:
        num += 1
        sum1 = num + reverse_number(num)
        sum2 = abs(num - reverse_number(num))
        if sum2 != 0:
            if sum1 % sum2 == 0:
                found += 1
                cache_keys.append(found)
                cache_values.append(num)
            if found == n:
                return num

    return False


t = time.time()
print(sum_dif_rev(52))
print(cache_keys, cache_values)
print(time.time() - t)
