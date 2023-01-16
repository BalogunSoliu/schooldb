import numpy as np
import pandas as pd

def getrooms(rooms,courses):


     realarrag = {}
     objvalue =np.inf

     for i in range(100):
         
         assignment={}

         arrag=np.random.choice(len(rooms),len(courses),replace=False)
         Ro=list(rooms.keys())
         Cou = list(courses.keys())
         noStudentWithnoseat = 0
         for c in range(len(Cou)):

             d=arrag[c]
             assignment[Cou[c]]=Ro[d]

             noStudentWithnoseat = max(0,courses[Cou[c]] - rooms[Ro[d]])
     
         if  noStudentWithnoseat <objvalue :
             realarrag=assignment
             objvalue=noStudentWithnoseat
             
         print('Objective Value at iteration %d = %d' %(i,objvalue))

     courses2 = list(realarrag.keys())
     rooms2 =[]
     capacity2=[]
     studentno=[]

     for c in courses2:
        r=realarrag[c]
        rooms2.append(r)
        capacity2.append(rooms[r])
        studentno.append(courses[c])

     df=pd.DataFrame({'Courses':courses2,'Number of Students':studentno,
                      'Room':rooms2,'Number of Seat':capacity2})
     
     return df




rooms ={'100':10,'200':50,'400':10}
courses = {'101a':22,'202b':54,'202a':34}


df=getrooms(rooms,courses)

print(df)


    
