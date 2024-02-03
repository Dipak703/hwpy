import time as t
def display(a):    
    lis=['q','w','r','e','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','m','n','b',"v","c","x","z"," "]
    if __name__=="__main__":
        print("hi")
    for i in range(len(a)):
        for j in range(26):
            t.sleep(0.03)
            x=lis[j]
            print(a[0:i]+x)
            if a[i]==x:
                break
            elif a[i]!=x and j ==25:
                print(a[0:i+1])
display('helllo world')