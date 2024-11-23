from string import *
# text="Hello Iam: amir Hallajian yers= old 24 where Are You From?"
text = input("Text:")
text = text.replace(" ","").replace("\t","")
symbols=":?!@#$%&*+=,"
numbers="0123456789"
lower_str=ascii_lowercase
upper_str=ascii_uppercase

#=================================================

# for i in range(0,len(text)):
#     if text[i] in numbers:
#         print((text[i]),end="")

# for i in range(0,len(text)):
#     if text[i] in symbols:
#         print(text[i],end="")
        
# for i in range(0,len(text)):
#     if text[i] in upper_str:
#         print(text[i],end="")
        
# for i in range(0,len(text)):
#     if text[i] in lower_str:
#         print(text[i],end="")

#=================================================
i = 0
while len(text) > i:
    if text[i] in numbers:
        print(text[i],end="")
    i += 1  
    
j =0
while len(text) > j:
    if text[j] in symbols:
        print(text[j],end="")
    j += 1

h=0
while len(text) > h:
    if text[h] in lower_str:
        print(text[h],end="")
    h += 1
u = 0
while len(text) > u:
    if text[u] in upper_str:
        print(text[u],end="")
    u += 1   