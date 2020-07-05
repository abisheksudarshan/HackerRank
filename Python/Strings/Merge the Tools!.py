def merge_the_tools(string, k):
    # your code goes here
    s=[]
    for i in range(0,len(string),k):
        temp=[]
        for j in range(0,k):
            if string[i+j] not in set(temp):
                temp.append(string[i+j])
        s.append(temp)
    print('\n'.join([''.join(t) for t in s]))

   
if __name__ == '__main__':
