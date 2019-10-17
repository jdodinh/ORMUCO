# Question A:
# Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns
# whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
#
# By: Jeremi Do Dinh


def main():
    l_1 = (1, 1)
    l_2 = (2, 6)
    if (l_1[0] <= l_2[0] <= l_1[1]) or (l_1[0] <= l_2[1] <= l_1[1]) or (l_2[0] <= l_1[0] <= l_2[1]) or (l_2[0] <= l_1[1] <= l_2[1]):
        print("The lines overlap")
    else:
        print("The lines don't overlap")


if __name__ == "__main__":
    main()
