#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


def LoadData():
    df=pd.read_csv("Project2Data - Copy.txt",header=None)
    df=df.rename(columns={0:"States",1:"Answer"})
    return df


# In[3]:


df=LoadData()


# In[116]:


def CreateTransitionProbs(df):
    trans_mat = {'sunny': [0, 0, 0], 'rainy': [0, 0, 0], 'foggy': [0, 0, 0]}
    mapping = {'sunny': 0, 'rainy': 1, 'foggy':2}
    first_flag = True

        
    for x in df["States"]:
        if first_flag:
            prev_state = x
            first_flag = False
            continue
        trans_mat[prev_state][mapping[x]] += 1
        prev_state=x
#     print("",trans_mat)
    for k,v in trans_mat.items():
#         print(sum(trans_mat[k]))
        trans_mat[k] = [round(x/sum(trans_mat[k]),3) for x in trans_mat[k]]
        
    print("\tsunny\trainy\tfoggy")
    # for i in len(trans_mat):
    #     print(trans_mat[i])
    for i in trans_mat.items():
        print(i[0],"\t",i[1])
    # trans_mat
    trans_prob=np.array([trans_mat['sunny'],trans_mat['rainy'],trans_mat['foggy']])
    return trans_prob


# In[117]:


trans_prob=CreateTransitionProbs(df)


# In[118]:


trans_prob


# In[99]:


def CreateEmitionProbs(df):
    states = ['sunny', 'rainy', 'foggy']
    observation= ['yes', 'no']
    emission_mat = {'yes': [0, 0,0], 'no': [0,0,0]}
#     print(emission_mat.keys())
    mapping = {'sunny': 0, 'rainy': 1, 'foggy':2}
#     map_yes_no={"yes":0,"no":1}
    sum_yes=df[df['Answer']=="yes"]["Answer"].count()
    sum_no=df[df["Answer"]=="no"]["Answer"].count()
#     print(sum_no)
#     print("SUM yes :\nSUm no: ",sum_yes,sum_no)
     
    temp=[]
    for i in range(df.shape[0]):
        emission_mat[df["Answer"][i]][mapping[df["States"][i]]]+=1
    for i in range(len(states)):
        s=emission_mat['yes'][i]+emission_mat['no'][i]
        temp.append([round(emission_mat['yes'][i]/s,3),round(emission_mat['no'][i]/s,3)])
#         print(temp)
    emission_prob = np.array([temp[0], temp[1], temp[2]])
    print("yes\tno")
    print(emission_prob)
    return emission_prob


# In[102]:


emission_prob=CreateEmitionProbs(df)


# In[121]:


pi = [1,0,0]
def viterbi(obs_seq):
        T = len(obs_seq)
        N = trans_prob.shape[0]
        delta = np.zeros((T, N))
        psi = np.zeros((T, N))
        delta[0] = pi*emission_prob[:,obs_seq[0]]
        for t in range(1, T):
            for j in range(N):
                delta[t,j] = np.max(delta[t-1]*trans_prob[:,j]) * emission_prob[j, obs_seq[t]]
                psi[t,j] = np.argmax(delta[t-1]*trans_prob[:,j])
        print(delta)
        # backtrack
        states = np.zeros(T, dtype=np.int32)
        states[T-1] = np.argmax(delta[T-1])
        for t in range(T-2, -1, -1):
            states[t] = psi[t+1, states[t+1]]
        return states


# In[55]:


['no', 'no', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'yes']


# In[122]:


print(viterbi([0,1,1,0,0,0,0,0,0,1]))

