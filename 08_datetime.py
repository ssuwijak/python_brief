import datetime
import my_module as mm


def now():
    return datetime.datetime.now()


def calPoint(ops) -> int:
    scores = []
    sum = 0

    debugMode = True

    if debugMode:
        print("0) initilize\n")

    for idx, x in enumerate(ops):

        x = x.strip()
        score_count = len(scores)

        flagSkip = True

        if int_tryparse(x):  # x.isdigit():
            flagSkip = False
            scores.append(int(x))
            if debugMode:
                print("{}) add {} .. {}".format(idx+1, x, scores))
        elif x == '+':
            if score_count >= 2:
                flagSkip = False
                sum = int(scores[-1])+int(scores[-2])
                scores.append(sum)

                if debugMode:
                    print("{}) add sum of last 2 scores .. {}".format(
                        idx+1, scores))
        elif x == 'D':
            if score_count >= 1:
                flagSkip = False
                sum = int(scores[-1]) * 2
                scores.append(sum)
                if debugMode:
                    print("{}) add double of last score .. {}".format(
                        idx+1, scores))
        elif x == 'C':
            if score_count >= 1:
                flagSkip = False
                scores.pop(score_count-1)
                if debugMode:
                    print("{}) remove last score .. {}".format(idx+1, scores))
        else:
            pass

        if flagSkip:
            if debugMode:
                print("{}) ignore and skip for '{}'".format(idx+1, x))

    sum = 0
    for x in scores:
        sum += int(x)

    if debugMode:
        print("\nraw score is {}".format(ops))
        print("total score of {} is {}".format(scores, sum))

    return sum


def int_tryparse(value):
    ret = False
    try:
        i = int(value)
        ret = True
    except:
        i = -1

    return ret


def mprint(idx, msg):
    print("{}) {}".format(idx+1, msg))


if __name__ == "__main__":
    # mm.PrintLn("get Now()")
    # mm.PrintVar(now())

    line = "+ 5 -2 4 zz c d 9 + +"
    ops = line.strip().upper().split()
    calPoint(ops)
