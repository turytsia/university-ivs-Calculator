import cProfile
from ..math import ivs_math as math

def count(list):
    list_count = 0
    for _ in list:
        list_count = math.sum(list_count, 1)
    return list_count

def avg(list):
    sum = 0
    for item in list:
        sum = math.sum(sum, item)
    return (math.div(sum, count(list)))

def formule(list):
    list_count = count(list)
    average = avg(list)
    s = 0
    for item in list:
        s = math.sum(s, math.exp(item, 2))
    s = math.sub(s, math.mult(list_count, math.exp(average, 2)))
    s = math.div(s, math.sub(list_count, 1))
    s = math.square_root(s)
    return s



def main():
    input_numbers = list(map(int,input().split()))
    print("Average value is " + str(avg(input_numbers)))
    print("S = " + str(formule(input_numbers)))

if __name__ == '__main__':
    cProfile.run('main()', sort='time')