names=[]
subjects=[]
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
total=[]
gold_medalist=[]
f1=open("marks.txt","r")
for i in range(0,26,1):

    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])
    list2=list1[3].split(":")
    print(list2)
    subjects.append(list2[0])
    english.append(int(list2[1]))
    list2=list1[4].split(":")
    maths.append(int(list2[1]))
    list2=list1[5].split(":")
    physics.append(int(list2[1]))
    list2=list1[6].split(":")
    chemistry.append(int(list2[1]))
    list2=list1[7].split(":")
    biology.append(int(list2[1]))
    list2=list1[7].split(";")
    total.append(english[i]+maths[i]+physics[i]+chemistry[i]+biology[i])
print(names)
print(english)
print(maths)
print(physics)
print(chemistry)
print(biology)
print(total)

maxEng=max(english)
for i in range(0,26,1):
    if english[i]==maxEng:
        toppers_eng.append(names[i])
print(toppers_eng,"is the topper in",subjects[0],"with marks",maxEng)

maxMat=max(maths)
for i in range(0,26,1):
    if maths[i]==maxMat:
        toppers_math.append(names[i])
print(toppers_math,"is the topper in Maths with marks",maxMat)

maxPhy=max(physics)
for i in range(0,26,1):
    if physics[i]==maxPhy:
        toppers_phy.append(names[i])
print(toppers_phy,"is the topper in physics with marks",maxPhy)

maxChem=max(chemistry)
for i in range(0,26,1):
    if chemistry[i]==maxChem:
        toppers_chem.append(names[i])
print(toppers_chem,"is the topper in chemistry with marks",maxChem)

maxBio=max(biology)
for i in range(0,26,1):
    if biology[i]==maxBio:
        toppers_bio.append(names[i])
print(toppers_bio,"are the toppers in biology with marks",maxBio)

maxTotal=max(total)
for i in range(0,26,1):
    if total[i]==maxTotal:
        gold_medalist.append(names[i])
print(gold_medalist,"is the Gold Medalist with marks",maxTotal)

















































































































































































































































