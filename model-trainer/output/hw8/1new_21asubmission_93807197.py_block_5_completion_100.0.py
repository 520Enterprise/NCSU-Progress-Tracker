def sum_lists(lists):
    total = 0
    for i in lists:
        product = 1
        for n in i:
            product *= n
        total += product
    return total
def main():
print(sum_lists([[1,2],[3,4],[5,6]]))
print(sum_lists([[3,0.1],[0.04,0.001]]))
print(sum_lists([[0,7,9,-4],[13,21,9,-2]]))
if __name__ == '__main__':
    main()
