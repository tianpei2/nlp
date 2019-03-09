import sys
import copy

f1 = open(sys.argv[1], "r")
f0 = open(sys.argv[2], "r")
f2 = open(sys.argv[3], "r")
words = []
pos = []

arc = {}
emit = {}

'''training data preprocessing'''
for line in f1.readlines():
    str = line.split()
    c = 0
    if (str == []):
        words.append(" ")
        pos.append(" ")
    for i in str:
        if (c % 2 == 0):
            words.append(i)
        else:
            pos.append(i)
        c = c + 1
f1.close

for line in f0.readlines():
    str = line.split()
    c = 0
    if (str == []):
        words.append(" ")
        pos.append(" ")
    for i in str:
        if (c % 2 == 0):
            words.append(i)
        else:
            pos.append(i)
        c = c + 1
f0.close

'''
caluculating the arc and emit dictionary
arc: transition probabilities
emit: emission probabilities
'''
arc["start"] = {}
arc["start"][pos[0]] = 1
for i in range(len(words)-1):
    if pos[i] not in arc.keys():
        arc[pos[i]] = {}
    if pos[i] == " ":
        if "end" not in arc[pos[i-1]].keys():
            arc[pos[i-1]]["end"] = 1
        else:
            arc[pos[i-1]]["end"] += + 1
        if pos[i+1] not in arc["start"].keys():
            arc["start"][pos[i+1]] = 1
        else:
            arc["start"][pos[i+1]] += 1
    else:
        if pos[i+1] == " ":
            continue
        else:
            if pos[i+1] not in arc[pos[i]].keys():
                arc[pos[i]][pos[i+1]] = 1
            else:
                arc[pos[i]][pos[i+1]] += 1

emit["start"] = {}
emit["end"] = {}
for i in range(len(words)):
    if words[i] != " ":
        if pos[i] not in emit.keys():
            emit[pos[i]] = {}
        if words[i] not in emit[pos[i]].keys():
            emit[pos[i]][words[i]] = 1
        else:
            emit[pos[i]][words[i]] += 1

for i in arc.keys():
    arc_sum = 0
    for j in arc[i].keys():
        arc_sum += arc[i][j]
    for j in arc[i].keys():
        arc[i][j] = arc[i][j] / arc_sum

for i in emit.keys():
    emit_sum = 0
    for j in emit[i].keys():
        emit_sum += emit[i][j]
    for j in emit[i].keys():
        emit[i][j] = emit[i][j] / emit_sum

f3 = open("output.pos", "w")

'''
def r_arc (pos, arc):
    ret = []
    for i in arc.keys():
        if pos in arc[i].keys():
            ret.append(i)
    return ret

def poss (sent, states, arc, emit):
    possi = 1.0
    l = len(states)-1
    if len(states) < len(sent):
        return 0

    for i in range(l):
        possi = possi * arc[states[i]][states[i+1]] * emit[states[i]][sent[i]]
    possi = possi * emit[states[l]][sent[l]]

    return possi

＃Viterbi algorithm returns the best route(set of states) to the final state

def Viterbi(sent, arc, emit, state):
    max_poss = 0
    max_states = []
    if len(sent) == 1:
        return state
    for j in r_arc(state, arc):
        s = copy.copy(sent)
        s.remove(sent[len(sent)-1])
        if s[len(s)-1] in emit[j].keys():
            posi = Viterbi(s, arc, emit, j)
            temp_poss = poss(s, posi, arc, emit) * arc[j][state]
            if max_poss < temp_poss:
                max_poss = temp_poss
                max_states = copy.copy(posi)
                max_states.append(state)

    return max_states

'''

f3 = open("output.pos", "w")
prev = "start"
posibility = 1.0
pre_posibility = 1.0
#open the test file and produce the output
for line in f2.readlines():
    if line == "\n" or line == "\t":
        f3.write("\n")
        prev = "start"
        posibility = 1.0
        pre_posibility = 1.0
    else:
        for i in line.split():
            word = i
        signal = 0
        temp_prob = 0
        cnt = 0
        for i in arc[prev].keys():
            if i != "end" and word in emit[i].keys():
                cnt = cnt + 1
                prob = posibility * arc[prev][i] * emit[i][word]
                if temp_prob < prob:
                    signal = 1
                    temp_prob = prob
                    posi_ret = i

        '''signal = 0 for UNKNOWN words'''
        if signal == 0:
            for i in emit.keys():
                if i != "end" and word in emit[i].keys():
                    prob = pre_posibility * posibility * emit[i][word]
                    if temp_prob < prob:
                        temp_prob = prob
                        posi_ret = i
                        signal = 1
        if signal == 0:
            for i in arc[prev].keys():
                if i != "end":
                    prob = pre_posibility * posibility * arc[prev][i]
                    if temp_prob < prob:
                        temp_prob = prob
                        posi_ret = i
                        signal = 1
        f3.write(word + "\t" + posi_ret + "\n")
        pre_posibility = posibility
        posibility = temp_prob
        prev = posi_ret
