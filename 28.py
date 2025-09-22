names=[]
english=[]
toppers_eng=[]
maths=[]
toppers_math=[]
physics=[]
toppers_phy=[]
chemistry=[]
toppers_chem=[]
biology=[]
toppers_bio=[]
f1=open("marks.txt","r")
for i in range(0,26,1):

    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])
    list2=list1[3].split(":")
    english.append(list2[1])
    list2=list1[4].split(":")
    maths.append(list2[1])
    list2=list1[5].split(":")
    physics.append(list2[1])
    list2=list1[6].split(":")
    chemistry.append(list2[1])
    list2=list1[7].split(":")
    biology.append(list2[1])
    list2=list1[7].split(";")
print(names)
print(english)
print(maths)
print(physics)
print(chemistry)
print(biology)

maxEng=max(english)
print(maxEng)
for i in range(0,26,1):
    if english[i]==maxEng:
        toppers_eng.append(names[i])
print(toppers_eng)

maxMat=max(maths)
print(maxMat)
for i in range(0,26,1):
    if maths[i]==maxMat:
        toppers_math.append(names[i])
print(toppers_math)

maxPhy=max(physics)
print(maxPhy)
for i in range(0,26,1):
    if physics[i]==maxPhy:
        toppers_phy.append(names[i])
print(toppers_phy)

maxChem=max(chemistry)
print(maxChem)
for i in range(0,26,1):
    if chemistry[i]==maxChem:
        toppers_chem.append(names[i])
print(toppers_chem)

maxBio=max(biology)
print(maxBio)
for i in range(0,26,1):
    if biology[i]==maxBio:
        toppers_bio.append(names[i])
print(toppers_bio)

















































































































































































































































