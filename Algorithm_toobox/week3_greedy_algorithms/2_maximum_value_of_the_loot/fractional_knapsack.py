# Uses python3
import sys
def get_unit_value(weights, values):

    unit_values = []

    for i in range(len(weights)):
        unit_values.append(values[i]/weights[i])
    return unit_values


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    weights_i = weights.copy()
    unit_values = get_unit_value(weights, values)
    while capacity > 0 and len(weights_i) > 0:

        choose = unit_values.index(max(unit_values))
        a = min(capacity, weights_i[choose])
        capacity = capacity - a
        value = value + a*unit_values[choose]
        weights_i[choose] = weights_i[choose] - a
        unit_values.remove(max(unit_values))
        weights_i.remove(weights_i[choose])
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


# print(get_optimal_value(50, [20, 50, 30], [60, 100, 120]))
#
# print(get_optimal_value(10, [30], [500]))
#
# print(get_optimal_value(1000, [30], [500]))