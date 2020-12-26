#!/usr/bin/python3

def answered_by_anyone(answers):
    return len(answers)

def answered_by_everyone(answers, group_size):
    return len( { (k,v) for (k,v) in answers.items() if v == group_size } )

if __name__ == '__main__':
    n_answered_once = 0
    n_answered_by_all = 0
    group_answers = {}
    group_size = 0

    with open('input') as f:
        for line in f:
            line = line.rstrip()
            if line == '':
                n_answered_once += answered_by_anyone(group_answers)
                n_answered_by_all += answered_by_everyone(group_answers, group_size)
                group_answers = {}
                group_size = 0
                continue

            group_size += 1
            for c in line:
                group_answers[c] = group_answers.get(c,0) + 1
        n_answered_once += answered_by_anyone(group_answers)
        n_answered_by_all += answered_by_everyone(group_answers, group_size)

    print("Total questions answered once: {}".format(n_answered_once))
    print("Total questions answered by all: {}".format(n_answered_by_all))
