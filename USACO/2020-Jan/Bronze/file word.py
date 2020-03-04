"""
ID: ZGW
LANG: PYTHON3
TASK: XXX
"""
fin = open ('file word.in', 'r')
lines = fin.readlines()
N = int(lines[0].split(" ")[0])
K = int(lines[0].split(" ")[1])
words = lines[1].strip().split(" ")

def Solve():
    new_lines = [words[0]]
    for i in range(1,len(words)):
        if len(new_lines[-1].replace(" ","")) + len(words[i]) <= K:
            new_lines[-1] = new_lines[-1]+ " " +words[i]
        else:
            new_lines.append(words[i])
    return new_lines

results = Solve()

fout = open ('file word.out', 'w')
for r in range(len(results)-1):
    fout.write (str(results[r]) + '\n')
fout.write (str(results[len(results)-1]))
# fout.write(result)
fout.close()