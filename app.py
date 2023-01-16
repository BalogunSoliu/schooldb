from flask import Flask, render_template, redirect,request
import pandas as pd
from optimize import getrooms

app = Flask(__name__)

@app.route('/')
def index():

    Cou=pd.read_excel('database.xlsx','Course')
    Rom=pd.read_excel('database.xlsx','room')

    Rms = list(Rom['Rooms'])
    Cap = list(Rom['Capacity'])

    courses ={}
    
    rooms ={}
    for r in range(len(Rms)):
        rr=str(Rms[r])
        rooms[rr]=Cap[r]

    stu = Cou['noStudent']
    Cou2 = Cou['Courses']
    for c in range(len(Cou)):
        cc=str(Cap[c])
        courses[cc]=stu[c]
        

    
    df=getrooms(rooms,courses)

    
    return render_template('index.html',tables=[df.to_html(classes='data')])


@app.route('/database',methods=['POST','GET'])
def database():
    print('here')
    df=pd.read_excel('database.xlsx','Course')
    df_list=df.values.tolist()
    dd=[]
    
    for d in range(len(df_list)):
        r={}
        r['course']=df_list[d][0]
        r['capacity']=df_list[d][1]
        r['nostudent']=df_list[d][2]

        dd.append(r)
          
    return render_template('database.html',data=dd)


@app.route('/database_room',methods=['POST','GET'])
def database_room():
    print('here')
    df=pd.read_excel('database.xlsx','room')
    df_list=df.values.tolist()
    dd=[]
    
    for d in range(len(df_list)):
        r={}
        r['idx']=df_list[d][0]
        r['course']=df_list[d][1]
        r['Type']=df_list[d][2]
        r['capacity']=df_list[d][3]
        

        dd.append(r)
    print(dd)
    return render_template('database_room.html',data=dd)

@app.route('/edit_room',methods=['POST','GET'])
def edit_room():

    if request.method =='GET':
        
        room=int(request.args.get('idx'))

        df=pd.read_excel('database.xlsx','room')
        
        df2=df[df['Room ID']==room]
        print(df2)
      

        return render_template('edit.html',room=str(df2.iloc[0,1]),
                               typeid=df2.iloc[0,2],capacity=df2.iloc[0,3])


    
    if request.method == 'POST':

        try:
            roomid = int(request.form["roomid"])
        except:
            roomid = request.form["roomid"]
        typeid = request.form["typeid"]
        capacity = request.form["capacityid"]

        df=pd.read_excel('database.xlsx','room')
        df2=df[df['Rooms']==roomid]
        df3=df2[df2['Type']==typeid]

        df3.capacity=capacity

        df.iloc[df3.index[0],3]=capacity

        room=pd.read_excel('database.xlsx','room')
        course=pd.read_excel('database.xlsx','Course')

        writer=pd.ExcelWriter('database.xlsx')

        room.to_excel(writer,sheet_name='room',index=False)
        course.to_excel(writer,sheet_name='Course',index=False)

        writer.save()

        return render_template('edit.html',room=roomid,
                               typeid=typeid,capacity=capacity)

        
if __name__=="__main__":
    app.run(debug=True)
