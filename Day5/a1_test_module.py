# output `a1_test module` if run from a2_index, output __main__ if run directly `python a1_test_module`
print(__name__)


def square(num):
    return num * num


if __name__ == "__main__":
    # output the result ONLY if it run directly `python a1_test_module`
    print(square(3))
