from itertools import permutations;c=list(permutations([str(k) for k in range(8)],8));i=8**46077
while any([''.join(j) not in oct(i).replace('o','') for j in c]):i+=1
print(''.join([str(int(i)+1) for i in oct(i).replace('o','')]))
