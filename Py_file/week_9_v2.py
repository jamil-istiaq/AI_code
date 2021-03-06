# -*- coding: utf-8 -*-
"""18-37918-2-week-9-v2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w1t4yqeo-AqgS66-zw8YSoklL22lu3m3

# Name: Md. Jamil Istiaq
# Id: 18-37918-2

###### To solve a puzzle, you are given an initial state and a goal state.
###### Target is to reach goal state from initial state using puzzle rules.
######  We can move blank tile only on left, right, up, and down
![Capture.JPG](attachment:Capture.JPG)

# Generate an intial state of NPuzzle
"""

import numpy as np
import random
def get_state(N):    
    state = [item for item in range(N*N)]
    random.shuffle(state)
    tmp = np.array(state)
    print(tmp.reshape(N,N))
    return state

get_state(4)

"""# Calculate inversion

Inversion is a pair of tiles that are in the reverse order from where they ought to be. In our case, the bigger number is in front of the smaller one.

![Capture.JPG](attachment:Capture.JPG)
"""

def count_inversion(arr):
    arr = [i for i in arr if i !=0]
    #print(arr)
    inversion = []
    for i in range(len(arr)):    
        count = 0
        for j in arr[i+1:]:        
            if(arr[i]>j): count = count + 1
        inversion.append(count)
    print(inversion)
    return sum(inversion)

s = get_state(4)
count_inversion(s)

"""# Solvability Rules"""

N = 4
S = get_state(N)
I = count_inversion(S)

# find row position of the blank tile
# apply the rules to decide solvability

def get_row(S):
        blank_position = 0
        for i in range(N*N):
            if (S[i] == 0):
                blank_position = i
        return blank_position

def isSolvable(N,R,I):
    if ((N*N)%2)==0 and (I%2)!=0:
        print('Solvable')
    elif ((N*N%2)!=0) and (R%2)!=0 and (I%2)==0:
        print('Solvable')
    elif ((N*N)%2)==0 and (R%2)==0 and (I%2)!=0:
        print('Solvable')
    else:
        print('Not Solvable')

N = 4
S = get_state(N)
I = count_inversion(S)
R = get_row(S)
isSolvable(N, R, I)