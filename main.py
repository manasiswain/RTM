import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import time
# Prepare table
def redraw_figure():
    plt.draw()
    plt.pause(0.00001)
plt.rcParams["figure.autolayout"] = True
columns = ('chanel/sub-chanel', '0' , '1' , '2', '3', '4', '5', '6', '7')
rows = ["0", "1","2","3","4","5","6","7","8"]
plt.ion()
figure, ax = plt.subplots(figsize=(15,10))
f = open("/Users/manasiswain/Desktop/demofile.txt","r")
cell_text = [["0","","","","","","","",""],["1","","","","","","","",""],\
             ["2","","","","","","","",""],["3","","","","","","","",""],\
             ["4","","","","","","","",""],["5","","","","","","","",""],\
             ["6","","","","","","","",""],["7","","","","","","","",""]]
# Add a table at the bottom of the axes
colors = [["w","w","w","w","w","w","w","w","w"],["w","w","w","w","w","w","w","w","w"],\
          ["w","w","w","w","w","w","w","w","w"],["w","w","w","w","w","w","w","w","w"],\
          ["w","w","w","w","w","w","w","w","w"],["w","w","w","w","w","w","w","w","w"],\
          ["w","w","w","w","w","w","w","w","w"],["w","w","w","w","w","w","w","w","w"]]
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=cell_text,cellColours=colors,
                     colLabels=columns,loc='center')
the_table.auto_set_font_size(False)
the_table.set_fontsize(8)
the_table.scale(1.7, 1.7)
figure.canvas.draw()
SumRxLevSubDL=[]
SumRxLevelFullDL=[]
NumTimesRxQualSubIs0to2DL=[]
NumMeasurementsDL=[]
SumRxLevSubUL=[]
SumRxLevelFullUL=[]
NumTimesRxQualSubIs0to2UL=[]
NumMeasurementsUL=[]
for i in range(0,9):
    SumRxLevSubDL.append([])
    SumRxLevelFullDL.append([])
    NumTimesRxQualSubIs0to2DL.append([])
    NumMeasurementsDL.append([])
    SumRxLevSubUL.append([])
    SumRxLevelFullUL.append([])
    NumTimesRxQualSubIs0to2UL.append([])
    NumMeasurementsUL.append([])
    for j in range(0,9):
        SumRxLevSubDL[-1].append(0)
        SumRxLevelFullDL[-1].append(0)
        NumTimesRxQualSubIs0to2DL[-1].append(0)
        NumMeasurementsDL[-1].append(0)
        SumRxLevSubUL[-1].append(0)
        SumRxLevelFullUL[-1].append(0)
        NumTimesRxQualSubIs0to2UL[-1].append(0)
        NumMeasurementsUL[-1].append(0)
textstr ="EMPTY"
txt="Active Sdcch:"
txt1="Active TCH:"
props = dict(boxstyle='round', facecolor='purple', alpha=0.5)
t1=ax.text(0,0.85,textstr, transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)
t2=ax.text(0,0.95,textstr, transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)
t3=ax.text(0,1.05,textstr, transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)
t4=ax.text(0,1.15,txt, transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)
t5=ax.text(0,1.25,txt1, transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)
counter=0
counter1=0
while(1):
    for x in f:
        l = x.split(" ")
        print(l)
        if(l[0]=="Sdcch"):
            row=int(l[1])+1
            column=int(l[2])+1
            if(l[-1]=="up\n"):
                the_table[(row,column)].set_facecolor("b")
                the_table[(row, column)].get_text().set_color('white')
                the_table._cells[(row,column)]._text.set_text("Sdcch UP")
                counter += 1
                s=txt+str(counter)
                t4.set_text(s)

            elif(l[-1]=="down\n"):
                the_table[(row,column)].set_facecolor("g")
                the_table[(row, column)].get_text().set_color('white')
                the_table._cells[(row,column)]._text.set_text("Sdcch DOWN")
                counter-=1
                s = txt + str(counter)
                t4.set_text(s)
            figure.canvas.draw()
        elif(l[0]=="TCH"):
            row = int(l[1]) + 1
            column = int(l[2]) + 1
            if (l[-1] == "up\n"):
                the_table[(row,column)].set_facecolor("b")
                the_table[(row, column)].get_text().set_color('white')
                the_table._cells[(row,column)]._text.set_text("TCH UP")
                counter1 += 1
                s = txt1 + str(counter1)
                t5.set_text(s)

            elif (l[-1] == "down\n"):
                the_table[(row,column)].set_facecolor("g")
                the_table[(row, column)].get_text().set_color('white')
                the_table._cells[(row,column)]._text.set_text("TCH DOWN")
                counter1 -= 1
                s = txt1 + str(counter1)
                t5.set_text(s)
            figure.canvas.draw()
        else:
            if(l[0]=="EQ"):
                t1.set_text(x)
            elif(l[0]=="TX"):
                t2.set_text(x)
            elif(l[0]=="RX"):
                t3.set_text(x)
            elif(l[0]=="Meas(DL)"):
                row=int(l[3])+1
                column=int(l[6])+1
                if(NumMeasurementsDL[row][column]>=1):
                    st="DL:"+str(round(SumRxLevSubDL[row][column]/NumMeasurementsDL[row][column],2))+","+\
                       str(round(SumRxLevelFullDL[row][column]/NumMeasurementsDL[row][column],2))+","+\
                       str(round((100*NumTimesRxQualSubIs0to2DL[row][column])/NumMeasurementsDL[row][column],2))+"\n"
                    if(NumMeasurementsUL[row][column]!=0):
                        st+="UL:"+str(round(SumRxLevSubUL[row][column]/NumMeasurementsUL[row][column],2))+\
                            ","+str(round(SumRxLevelFullUL[row][column]/NumMeasurementsUL[row][column],2))+\
                            ","+str(round((100*NumTimesRxQualSubIs0to2UL[row][column])/NumMeasurementsUL[row][column],2))
                    the_table._cells[(row,column)]._text.set_text(st)
                    redraw_figure()
                SumRxLevSubDL[row][column]+=int(l[9])
                SumRxLevelFullDL[row][column]+=int(l[15])
                if(int(l[12])>=0 and int(l[12])<=2):
                    NumTimesRxQualSubIs0to2DL[row][column]+=1
                NumMeasurementsDL[row][column]+=1
            elif (l[0] == "Meas(UL)"):
                row = int(l[5]) + 1
                column = int(l[8]) + 1
                if (NumMeasurementsUL[row][column]>= 1):
                    st="UL:" + str(round(SumRxLevSubUL[row][column]/ NumMeasurementsUL[row][column],2)) +\
                       "," + str(round(SumRxLevelFullUL[row][column]/ NumMeasurementsUL[row][column],2)) +\
                       "," + str(round((100 * NumTimesRxQualSubIs0to2UL[row][column])/NumMeasurementsUL[row][column],2))+ "\n"
                    if(NumMeasurementsDL[row][column]!=0):
                        st+="DL:" + str(round(SumRxLevSubDL[row][column]/ NumMeasurementsDL[row][column],2))+\
                            "," + str(round(SumRxLevelFullDL[row][column]/NumMeasurementsDL[row][column],2))+\
                            "," + str(round((100 * NumTimesRxQualSubIs0to2DL[row][column]) /NumMeasurementsDL[row][column],2))
                    the_table._cells[(row,column)]._text.set_text(st)
                    redraw_figure()
                SumRxLevSubUL[row][column] += int(l[17])
                SumRxLevelFullUL[row][column]+= int(l[11])
                if (int(l[20]) >= 0 and int(l[20]) <= 2):
                    NumTimesRxQualSubIs0to2UL[row][column]+= 1
                NumMeasurementsUL[row][column]+=1
            else:
                continue

        figure.canvas.flush_events()
        time.sleep(1)
