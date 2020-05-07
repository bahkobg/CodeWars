import time

cache_keys = []
cache_values = []


def sum_dif_rev(n):
    # your code here
    def reverse_number(n):
        r = 0
        while n > 0:
            r *= 10
            r += n % 10
            n //= 10
        return r

    found = 0
    num = 45
    if cache_keys:
        found = cache_keys[-1]
        num = cache_values[-1]
    while n > found:
        sum1 = num + reverse_number(num)
        sum2 = abs(num - reverse_number(num))
        if sum2 != 0:
            if sum1 % sum2 == 0:
                found += 1
                cache_keys.append(found)
                cache_values.append(num)
            if found == n:
                return num
        num += 1
    return False


t = time.time()
print(sum_dif_rev(4))
print(sum_dif_rev(5))
print(time.time() - t)
