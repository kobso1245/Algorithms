def checker(points, curr_path, curr_node, poseteni):
    poseteni.append(curr_node)
    curr_path.append(curr_node)

    for next_elem in range(len(points[curr_node])):
        if points[curr_node][next_elem] == 2: #file, go up
            poseteni.append(next_elem)
        elif points[curr_node][next_elem] == 1: #folder, continue with new recursion tree
            if next_elem in curr_path:
                return False
            if next_elem not in poseteni:
                res = checker(points, curr_path, next_elem, poseteni)
                if not res:
                    return False

    curr_path.pop()
    return True

def test():
    row_num = int(input())
    points = []
    for i in range(row_num):
        row = input().split(' ')
        row = [int(x) for x in row]
        points.append(row)

    curr_path = []
    poseteni = []

    res = checker(points, curr_path, 0, poseteni) 
    if res:
        print('true')
    else:
        print('true')

test()
