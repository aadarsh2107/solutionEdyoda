string=input()
stack=[]
first_unmatched=0
for i in range(len(string)):
    if string[i]=="{" or string[i]=="(" or string[i]=="[":
        stack.append(string[i])
    elif string[i]=="}" and stack[-1]=="{":
        stack.pop()
    elif string[i]==")" and stack[-1]=="(":
        stack.pop()
    elif string[i]=="]" and stack[-1]=="[":
        stack.pop()
    elif string[i]=="}" or string[i]=="]" or string[i]==")":
        first_unmatched=i
if stack==[]:
    print("success")
else:
    print(first_unmatched+1)