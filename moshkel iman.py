
#====================================================================
while True:
    tedad_emthan=int(input("Emthanat:"))
    z = 0
    n = 0
    while tedad_emthan >= 1:
        nomre=float(input("Nomre:"))
        zarib= int(input("Zarib:"))
        n += nomre*zarib
        z += zarib
        tedad_emthan -= 1

    s = n//z
    if s <=20 and s >=15:
        print(s,"A")
        # break
    elif s <15 and s>=10:
        print(s,"B")
        # break
    elif s <10 and s >=5:
        print(s,"C")
        # break
    elif s < 5 and s>=0:
        print(s,"D")
        # break
    contin=input("Do you continue?(Y/N):")
    if "n" in contin.lower():
        break
        
