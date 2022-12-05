# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 16:11:24 2022

@author: Usuario
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



pm_df = pd.read_csv(r"/Users/montserrattrullsjuanola/Downloads/datosSO2.csv",
                          index_col=0, header=0)

pm_df["hmean"]=pm_df[['h01', 'h02', 'h03', 'h04', 'h05', 'h06','h07', 'h08','h09', 
                         'h11','h12', 'h13','h14','h15', 'h16', 'h17','h18', 
                         'h19','h20','h21', 'h22','h23','h24']].mean(axis=1)
pm_df["hmean"] = pm_df["hmean"].fillna(value=0)





meanhebron=[]
hebron_df = pm_df.loc[pm_df['altitud'] == 136]
hebronn=np.array(hebron_df["hmean"])
        
aa=np.fft.fft(hebronn)
temps=np.linspace(0,1409,1409)
plt.plot(temps,aa)
plt.xlabel('t (dies)')
plt.title('Transformada de Fourier de les concentracions', y=1.1)
plt.show()




any2019hebron = hebron_df.iloc[1045:,:]
hebron2019 = np.array(any2019hebron["hmean"])
meanhebron2019=np.mean(hebron2019)
meanhebron.append(meanhebron2019)


any2020hebron = hebron_df.iloc[679:1045,:]
hebron2020 = np.array(any2020hebron["hmean"])
meanhebron2020=np.mean(hebron2020)
meanhebron.append(meanhebron2020)

any2021hebron = hebron_df.iloc[314:679,:]
hebron2021 = np.array(any2021hebron["hmean"])
meanhebron2021=np.mean(hebron2021)
meanhebron.append(meanhebron2021)

any2022hebron = hebron_df.iloc[:314,:]
hebron2022 = np.array(any2022hebron["hmean"])
meanhebron2022=np.mean(hebron2022)
meanhebron.append(meanhebron2022)


meaneixample=[]
eixample_df = pm_df.loc[pm_df['altitud'] == 26]

any2019eixample = eixample_df.iloc[1045:,:]
eixample2019 = np.array(any2019eixample["hmean"])
meaneixample2019=np.mean(eixample2019)
meaneixample.append(meaneixample2019)
eixample2019rev=list(reversed(eixample2019))
Meanrev2=[]


for i in range(0,360,30):
    eixample2019rev1=eixample2019rev[i:i+30]
    meanrev2=np.mean(eixample2019rev1)
    Meanrev2.append(meanrev2)



any2020eixample = eixample_df.iloc[679:1045,:]
eixample2020 = np.array(any2020eixample["hmean"])
meaneixample2020=np.mean(eixample2020)
meaneixample.append(meaneixample2020)
eixample2020rev=list(reversed(eixample2020))
Meanrev=[]


for i in range(0,360,30):
    eixample2020rev1=eixample2020rev[i:i+30]
    meanrev=np.mean(eixample2020rev1)
    Meanrev.append(meanrev)
    







any2021eixample = eixample_df.iloc[314:679,:]
eixample2021 = np.array(any2021eixample["hmean"])
meaneixample2021=np.mean(eixample2021)
meaneixample.append(meaneixample2021)
eixample2021rev=list(reversed(eixample2021))
Meanrev3=[]

for i in range(0,360,30):
    eixample2021rev1=eixample2021rev[i:i+30]
    meanrev3=np.mean(eixample2021rev1)
    Meanrev3.append(meanrev3)
    






any2022eixample = eixample_df.iloc[:314,:]
eixample2022 = np.array(any2022eixample["hmean"])
meaneixample2022=np.mean(eixample2022)
meaneixample.append(meaneixample2022)
eixample2022rev=list(reversed(eixample2022))
Meanrev4=[]


for i in range(0,330,30):
    eixample2022rev1=eixample2022rev[i:i+30]
    meanrev4=np.mean(eixample2022rev1)
    Meanrev4.append(meanrev4)
    



mesos=np.linspace(0,12,12)
labels=['Gen','Feb','Mar','Abr','Mai','Jun','Jul','Ago','Set','Oct','Nov','Des']
#plt.bar(mesos, Meanrev4, width=0.125, )
#plt.bar(mesos,Meanrev3, width=0.125)
plt.bar(mesos,Meanrev2, label=2019)
plt.bar(mesos,Meanrev, label=2020)
plt.xticks(mesos,labels)
plt.ylabel(r'SO2 ($\mu$g/m3)')
plt.xlabel('mes')
plt.legend()
plt.ylim(0,3)
plt.show()





meangracia=[]
gracia_df = pm_df.loc[pm_df['altitud'] == 57]

any2019gracia = gracia_df.iloc[1045:,:]
gracia2019 = np.array(any2019gracia["hmean"])
meangracia2019=np.mean(gracia2019)
meangracia.append(meangracia2019)

any2020gracia = gracia_df.iloc[679:1045,:]
gracia2020 = np.array(any2020gracia["hmean"])
meangracia2020=np.mean(gracia2020)
meangracia.append(meangracia2020)

any2021gracia = gracia_df.iloc[314:679,:]
gracia2021 = np.array(any2021gracia["hmean"])
meangracia2021=np.mean(gracia2021)
meangracia.append(meangracia2021)


any2022gracia = gracia_df.iloc[:314,:]
gracia2022 = np.array(any2022gracia["hmean"])
meangracia2022=np.mean(gracia2022)
meangracia.append(meangracia2022)


meanbesos=[]
besos_df = pm_df.loc[pm_df['altitud'] == 7]


any2019besos = besos_df.iloc[1045:,:]
besos2019 = np.array(any2019besos["hmean"])
meanbesos2019=np.mean(besos2019)
meanbesos.append(meanbesos2019)

any2020besos = besos_df.iloc[679:1045,:]
besos2020 = np.array(any2020besos["hmean"])
meanbesos2020=np.mean(besos2020)
meanbesos.append(meanbesos2020)

any2021besos = besos_df.iloc[314:679,:]
besos2021 = np.array(any2021besos["hmean"])
meanbesos2021=np.mean(besos2021)
meanbesos.append(meanbesos2021)


any2022besos = besos_df.iloc[:314,:]
besos2022 = np.array(any2022besos["hmean"])
meanbesos2022=np.mean(besos2022)
meanbesos.append(meanbesos2022)


meanpalau=[]
palau_pm10_df = pm_df.loc[pm_df['altitud'] == 81]

any2019palau = palau_pm10_df.iloc[1045:,:]
palau2019 = np.array(any2019palau["hmean"])
meanpalau2019=np.mean(palau2019)
meanpalau.append(meanpalau2019)

any2020palau = palau_pm10_df.iloc[679:1045,:]
palau2020 = np.array(any2020palau["hmean"])
meanpalau2020=np.mean(palau2020)
meanpalau.append(meanpalau2020)

any2021palau = palau_pm10_df.iloc[314:679,:]
palau2021 = np.array(any2021palau["hmean"])
meanpalau2021=np.mean(palau2021)
meanpalau.append(meanpalau2021)


any2022palau = palau_pm10_df.iloc[:314,:]
palau2022 = np.array(any2022palau["hmean"])
meanpalau2022=np.mean(palau2022)
meanpalau.append(meanpalau2022)


    



a=np.linspace(0,4,4)
labels=[2019,2020,2021,2022]
plt.bar(a-0.25,meanhebron, width=0.125, label='Parc Vall d\'Hebron')
plt.bar(a-0.125,meangracia, width=0.125, label='Gràcia')
plt.bar(a,meanbesos, width=0.125, label='Besòs')
plt.bar(a+0.125,meaneixample, width=0.125, label='Eixample')
plt.bar(a+0.25,meanpalau, width=0.125, label='Palau Reial')
plt.xticks(a,labels)
plt.ylabel(r'SO2 ($\mu$g/m3)')
plt.xlabel('year')
plt.legend(bbox_to_anchor = (1.05, 0.6))
plt.ylim(0,2.5)







