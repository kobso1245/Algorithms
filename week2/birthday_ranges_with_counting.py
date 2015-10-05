class Birthday:

    def __init__(self, arr):
        self.res = [0 for x in range(366)]
        self.birtdays = [0 for x in range(366)]
        for elem in arr:
            self.birtdays[elem] += 1
        self.curr_birt_count = 0
        for i in range(366):
            self.curr_birt_count += self.birtdays[i]
            self.res[i] = self.curr_birt_count

    def add(self, day, cnt):
        self.birtdays[day] += cnt
        if day > 1:
            self.curr_birt_count = self.res[day - 1]
        else:
            self.curr_birt_count = 0
        for i in range(day, 366):
            self.curr_birt_count += self.birtdays[i]
            self.res[i] = self.curr_birt_count

    def remove(self, day, cnt):
        if self.birtdays[day] - cnt < 0:
            self.birtdays[day] = 0
        else:
            self.birtdays[day] -= cnt
        if day > 1:
            self.curr_birt_count = self.res[day - 1]
        else:
            self.curr_birt_count = 0
        for i in range(day, 366):
            self.curr_birt_count += self.birtdays[i]
            self.res[i] = self.curr_birt_count

    def count(self, ranges):

        result = []
        for curr_range in ranges:
            if curr_range[1] == 365 and curr_range[0] == 0:
                result.append(self.curr_birt_count)
            elif curr_range[1] == 365:
                result.append(
                    self.curr_birt_count -
                    self.res[
                        curr_range[0] -
                        1])
            elif curr_range[0] == 0:
                result.append(self.res[curr_range[1] + 1])
            elif curr_range[0] > 0 and curr_range[1] < 365:
                result.append(
                    self.res[
                        curr_range[1]] -
                    self.res[
                        curr_range[0] -
                        1])
            else:
                result.append("Out of range!")

        return result


def main():
    inp = input().split(' ')
    elems = input().split(' ')
    arr = [int(x) for x in elems]

    bday = Birthday(arr)
    for i in range(int(inp[1])):
        command = input().split(' ')
        if command[0] == 'add':
            bday.add(int(command[1]), int(command[2]))
        elif command[0] == 'remove':
            bday.remove(int(command[1]), int(command[2]))
        else:
            ranges = [(int(command[1]), int(command[2]))]
            cnt = bday.count(ranges)
            print(cnt[0])


if __name__ == '__main__':
    main()
