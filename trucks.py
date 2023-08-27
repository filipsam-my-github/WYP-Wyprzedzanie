to_int = lambda strings: [int(string) for string in strings]
with open("trucks.txt","r") as file:
    datas=[]
    for line in file:
        datas.append(to_int(line.split()))
        
    file.close()
#print(datas)

car=[[-datas[0][1],0,datas[0][1]],datas[0][2]/datas[0][3]]
#print(car)

trucks=[]
copy_datas=datas.copy()
copy_datas.pop(0)

for truck in copy_datas:
    trucks.append([[truck[0]-truck[1],0,truck[1]],truck[2]/truck[3]])

min_speed=float("inf")
for truck in trucks:
    if truck[1]<min_speed:
        min_speed=truck[1]
        
for truck in trucks:
    truck[1]-=min_speed
car[1]-=min_speed

#print(min_speed,"///")
#print(trucks)
trucks=sorted(trucks,key=lambda truck: truck[0][0])
#print(trucks,"cd",car)
min_dt=float("inf")

def chck_colision(rect,rects):
    a=lambda trucks: [truck[0] for truck in trucks]
    rects=a(rects)
    #print(rects)
    for i_rect in rects:
        if i_rect[0]<=rect[0]<i_rect[0]+i_rect[2]:
            return True,i_rect
        elif i_rect[0]<=rect[0]+rect[2]<i_rect[0]+i_rect[2]:
            return True,i_rect
    return False,None

def more_cose_rect(rect,rects):
    crect_cord=[[[float("inf")]]]
    for number,i_rect in enumerate(rects):
        #print(crect_cord[0][0][0]>i_rect[0][0]+i_rect[0][2]>rect[0][0])
        #print(crect_cord[0][0][0],i_rect[0][0]+i_rect[0][2],rect[0][0])
        if crect_cord[0][0][0]>i_rect[0][0]+i_rect[0][2]>rect[0][0]:
            crect_cord=[i_rect,number]
    return crect_cord
#print(trucks,"cd",car)

# for number_truck in range(len(trucks)-1):
#     if trucks[number_truck][1]==0:
#         continue
#     if min_dt>((trucks[number_truck+1][0][0]-trucks[number_truck][0][2])/trucks[number_truck][1])-trucks[number_truck][0][0]:
#         #print(((trucks[number_truck+1][0][0]-trucks[number_truck][0][2]-trucks[number_truck][0][0])/(trucks[number_truck][1]-trucks[number_truck+1][1])))
#         min_dt=((trucks[number_truck+1][0][0]-trucks[number_truck][0][2]-trucks[number_truck][0][0])/(trucks[number_truck][1]-trucks[number_truck+1][1]))
# if chck_colision(car[0],trucks)[0] and min_dt>((trucks[0][0][0]-car[0][2])/(car[1]-trucks[0][1])):
#     min_dt=((trucks[0][0][0]-car[0][2])/(car[1]-trucks[0][1]))
# elif min_dt>((trucks[0][0][0]-car[0][2]-car[0][0])/(car[1]-trucks[0][1])):
#     #print(trucks[0][0][0],car[0][2],car[0][0],trucks[0][0][0]-car[0][2]-car[0][0],trucks[0][1],car[1],(car[1]-trucks[0][0][0]))
#     min_dt=((trucks[0][0][0]-car[0][2]-car[0][0])/(car[1]-trucks[0][1]))
# dt=min_dt

    
# for truck in trucks:
#     truck[0][0]+=dt*truck[1]
# car[0][0]+=car[1]*dt
# #if car[0][0]+car[0][2]>sorted(trucks,key=lambda truck: truck[0][0])
# car[0][1]=0
# if chck_colision(car[0],trucks)[0]:
#     car[0][1]=1
# print(dt)
#print(trucks,"cd",car)

left=[0,0]
while more_cose_rect(car,trucks) != [[[float("inf")]]]:
    if 1==car[0][1]!=left[1]:
        left[0]+=1
    
    left[1]=car[0][1]
    min_dt=float("inf")
    for number_truck in range(len(trucks)-1):
        if trucks[number_truck][1]==0:
            continue
        if ((trucks[number_truck+1][0][0]-trucks[number_truck][0][2])/trucks[number_truck][1])-trucks[number_truck][0][0]==0:
            pass
        if min_dt>((trucks[number_truck+1][0][0]-trucks[number_truck][0][2])/trucks[number_truck][1])-trucks[number_truck][0][0]:
            #print(((trucks[number_truck+1][0][0]-trucks[number_truck][0][2]-trucks[number_truck][0][0])/(trucks[number_truck][1]-trucks[number_truck+1][1])))
            if ((trucks[number_truck+1][0][0]-trucks[number_truck][0][2]-trucks[number_truck][0][0])/(trucks[number_truck][1]-trucks[number_truck+1][1]))==0:
                trucks[number_truck][1]=trucks[number_truck+1][0][1]
            else:
                min_dt=((trucks[number_truck+1][0][0]-trucks[number_truck][0][2]-trucks[number_truck][0][0])/(trucks[number_truck][1]-trucks[number_truck+1][1]))
    ctrucks=more_cose_rect(car,trucks)
    #print(ctrucks,"????????",min_dt,(trucks[ctrucks[1]][0][0]+trucks[ctrucks[1]][0][2]-car[0][0]-car[0][2]))
    pass
    if chck_colision(car[0],trucks)[0] and min_dt>((trucks[ctrucks[1]][0][0]+trucks[ctrucks[1]][0][2]-car[0][0]-car[0][2])/(car[1]-trucks[ctrucks[1]][1])):
        min_dt=((trucks[ctrucks[1]][0][0]+trucks[ctrucks[1]][0][2]-car[0][0])/(car[1]-trucks[ctrucks[1]][1]))
    elif min_dt>((trucks[ctrucks[1]][0][0]-car[0][2]-car[0][0])/(car[1]-trucks[ctrucks[1]][1])) and not chck_colision(car[0],trucks)[0]:
        #print(trucks[0][0][0],car[0][2],car[0][0],trucks[0][0][0]-car[0][2]-car[0][0],trucks[0][1],car[1],(car[1]-trucks[0][0][0]))
        min_dt=((trucks[ctrucks[1]][0][0]-car[0][2]-car[0][0])/(car[1]-trucks[ctrucks[1]][1]))
    dt=min_dt

        
    for truck in trucks:
        truck[0][0]+=dt*truck[1]
    car[0][0]+=car[1]*dt
    #if car[0][0]+car[0][2]>sorted(trucks,key=lambda truck: truck[0][0])
    car[0][1]=0
    if chck_colision(car[0],trucks)[0]:
        car[0][1]=1
        

    #print(trucks,"cd",car)
    #while car[0][0][1]==0 and car[0][0][0]<trucks[-1][0][0]:
print(left[0])


