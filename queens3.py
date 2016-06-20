#!/usr/bin/env python

import sys

class NQueens(object):
    def __init__(self):
        self.possible = []
        pass

    def solveNQueens(self, n):
        self.BackTrack([], n, 0, None)
        for i in self.possible:
            self.prettyPrint(n, i)
        print "Total Possible Solutions for {} Queens {}".format(n, len(self.possible))

    def makeState(self, n, state):
        """LeetCode question Format"""
        row = ['.' for __ in range(n)]
        staterino = []
        for s in state:
            new_row = list(row)
            if s != -1:
                new_row[s] = 'Q'
                staterino.append("".join(new_row))
        return staterino

    def prettyPrint(self, n, state):
        default = ['_'] * n
        for s in state:
            d = list(default)
            d[s] = 'Q'
            print "|".join(d)
        print '\n'

    def BackTrack(self, state, n, curr, attack_vector):
        if attack_vector == None:
            available_domains = [i for i in range(n)]
            prev_attack_vector = [[False]*3]*n
        else:
            prev_attack_vector, available_domains = self.updateAttackVector(n, attack_vector)
        if curr == n - 1 and available_domains:
            for i in available_domains:
                state_copy = list(state)
                state_copy.append(i)
                self.possible.append(state_copy)
        else:
            for i in available_domains:
                state_copy = list(state)
                state_copy.append(i)
                new_attack_vector = list(prev_attack_vector)
                new_attack_vector[i] = [True] * 3
                self.BackTrack(state_copy, n, curr + 1, new_attack_vector)

    def updateAttackVector(self, n, attack_vector):
        new_attack_vector = []
        available = []
        for i in range(n):
            # 0 : Attack Going Down
            # 1 : Attack Going Diagonally Left
            # 2 : Attack Going Diagonally Right
            curr_attack = [False] * 3
            no_attacks = True
            if attack_vector[i][0]:
                curr_attack[0] = True
                no_attacks = False
            if i + 1 < n and attack_vector[i + 1][1]:
                curr_attack[1] = True
                no_attacks = False
            if i - 1 >= 0 and attack_vector[i-1][2]:
                curr_attack[2] = True
                no_attacks = False
            new_attack_vector.append(curr_attack)
            if no_attacks:
                available.append(i)
        return new_attack_vector, available

def main():
    nq = NQueens()
    try:
        num = 8 if len(sys.argv) != 2 else int(sys.argv[1])
    except:
        num = 8
    if num < 0:
        num = 8
    nq.solveNQueens(num)

if __name__ == "__main__":
    main()
