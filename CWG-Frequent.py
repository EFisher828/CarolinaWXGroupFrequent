import numpy as np
import math
import urllib.request
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import matplotlib.patches as patches
from matplotlib.patches import PathPatch
from matplotlib.collections import LineCollection
from matplotlib import cm
from bs4 import BeautifulSoup
import shapefile as shp
import datetime
from datetime import datetime as dt

def wnctemp():

    names = ('South Asheville 2060ft','Boone 2980ft', 'Bearwallow Mtn 4200ft', 'Mt Jefferson 4600ft','Grandfather Mtn 5280ft','Mt Mitchell 6200ft')#'Valle Crucis 2670ft',,'Mt Mitchell #1 6600ft 'Linville 3650ft', 'Seven Devils 3940ft', ,'Sugar Mtn 5000ft', 'Valle Crucis 2670ft'
    
    barnames = []
    Temperature = []
    Elevation = []
    i = 0

    
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=FLET'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("FLET missing")
        i = i + 1

    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=ktnb'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KTNB missing")
        i = i + 1

    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=BEAR'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("BEAR missing")
        i = i + 1
        
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=JEFF'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("JEFF missing")
        i = i + 1
        
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=grandfathr'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        Temp = eval(Temp_8)
        print("MITC - " + str(Temp))
        if Temp > (-20):
            Temperature.append(Temp)
            barnames.append(names[i])
            i = i + 1
        else:
            print("Grandfathr data issues")
            i = i + 1

    except:
        print("Grandfathr missing")
        i = i + 1

        
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=MITC'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        Temp = eval(Temp_8)
        print("MITC - " + str(Temp))
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("MITC missing")
        i = i + 1

    print(Temperature)

    fig = plt.figure()
    fig.patch.set_facecolor('grey')
    ax = plt.axes()
    ax.set_facecolor('grey')
    
    #data and bar names
    height = Temperature
    bars = barnames
    y_pos = np.arange(len(bars))

    #max/mins & fonts
    if len(height) > 0:
        maximum = max(height)+5
        minimum = min(height)-5
        font = {'size':16,'color':'white'}
        font2 = {'size':22,'color':'white'}

    #color
        color_1 = np.array(height)
        color_2 = cm.cool(1-(color_1 / float(max(color_1))))
        ax.xaxis.label.set_color('white')
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white') 
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
 
    #horizontal bars
        plt.barh(y_pos, height, color = color_2)
 
    #y-axis names
        plt.yticks(y_pos, bars, **font)

    #x-axis
        plt.xlim(minimum,maximum)

    #x label
        plt.xlabel('Temperature (°F)',**font)

        for i, v in enumerate(height):
            temp_height = height[i]
            len_finder = len(str(temp_height))
            if temp_height >= 0:
                plt.text(v , i-0.1, str(v), color='white', fontsize='13')
            elif temp_height < 0 and len_finder < 5:
                plt.text(v-2.1 , i-0.1, str(v), color='white', fontsize='13')
            elif temp_height < 0 and len_finder >= 5:
                plt.text(v-2.8 , i-0.1, str(v), color='white', fontsize='13')
        plt.title('Northern/Central Mountains, NC\nVertical Temperature Profile', **font2)

        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        plt.text(-0.27,-0.12,"Source: NCSCO",color='white',size=16,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
        plt.text(-0.27,1.05,"Valid: " + current_time,color='white',size=16,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
        plt.figtext(0.5,-0.2,"CarolinaWeatherGroup.com",color='white',size=10,horizontalalignment='center',transform = ax.transAxes)
        #show/save graphic
        plt.savefig("output/WNC-Temp.png",bbox_inches='tight', facecolor=fig.get_facecolor())
    elif len(height) == 0:
        fig = plt.figure()
        fig.patch.set_facecolor('grey')
        ax = plt.axes()
        ax.set_facecolor('grey')
        plt.text(0.5,0.5,"All Stations Down",color='white',size=22,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
        plt.savefig("output/WNC-Temp.png",bbox_inches='tight', facecolor=fig.get_facecolor())

wnctemp()

def wnchumidity():

    names = ('South Asheville 2060ft','Boone 2980ft', 'Bearwallow Mtn 4200ft', 'West Jefferson 4600ft','Grandfather Mtn 5280ft','Mt Mitchell 6200ft')#'Valle Crucis 2670ft',,'Mt Mitchell #1 6600ft 'Linville 3650ft', 'Seven Devils 3940ft', ,'Sugar Mtn 5000ft'
    
    barnames = []
    Temperature = []
    Elevation = []
    i = 0

    
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=FLET'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Dew_1 = str(Tr[5])
        Dew_2 = Dew_1.split('<')
        Dew_3 = str(Dew_2[11])
        Dew_4 = Dew_3.split('>')
        Dew_5 = str(Dew_4[1])
        Dew_6 = Dew_5.split('%')
        Dew_7 = str(Dew_6[0])
        Dew_8 = Dew_7.split(' ')
        Dew_9 = str(Dew_8[1])
        Dewpoint = eval(Dew_9)
        Temperature.append(Dewpoint)
        barnames.append(names[i])
        i = i + 1

    except:
        print("FLET missing")
        i = i + 1


    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=ktnb'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Dew_1 = str(Tr[5])
        Dew_2 = Dew_1.split('<')
        Dew_3 = str(Dew_2[11])
        Dew_4 = Dew_3.split('>')
        Dew_5 = str(Dew_4[1])
        Dew_6 = Dew_5.split('%')
        Dew_7 = str(Dew_6[0])
        Dew_8 = Dew_7.split(' ')
        Dew_9 = str(Dew_8[1])
        Dewpoint = eval(Dew_9)
        Temperature.append(Dewpoint)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KTNB missing")
        i = i + 1

    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=BEAR'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Dew_1 = str(Tr[5])
        Dew_2 = Dew_1.split('<')
        Dew_3 = str(Dew_2[11])
        Dew_4 = Dew_3.split('>')
        Dew_5 = str(Dew_4[1])
        Dew_6 = Dew_5.split('%')
        Dew_7 = str(Dew_6[0])
        Dew_8 = Dew_7.split(' ')
        Dew_9 = str(Dew_8[1])
        Dewpoint = eval(Dew_9)
        Temperature.append(Dewpoint)
        barnames.append(names[i])
        i = i + 1

    except:
        print("BEAR missing")
        i = i + 1
        
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=JEFF'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Dew_1 = str(Tr[5])
        Dew_2 = Dew_1.split('<')
        Dew_3 = str(Dew_2[11])
        Dew_4 = Dew_3.split('>')
        Dew_5 = str(Dew_4[1])
        Dew_6 = Dew_5.split('%')
        Dew_7 = str(Dew_6[0])
        Dew_8 = Dew_7.split(' ')
        Dew_9 = str(Dew_8[1])
        Dewpoint = eval(Dew_9)
        Temperature.append(Dewpoint)
        barnames.append(names[i])
        i = i + 1

    except:
        print("JEFF missing")
        i = i + 1
        
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=grandfathr'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Dew_1 = str(Tr[5])
        Dew_2 = Dew_1.split('<')
        Dew_3 = str(Dew_2[11])
        Dew_4 = Dew_3.split('>')
        Dew_5 = str(Dew_4[1])
        Dew_6 = Dew_5.split('%')
        Dew_7 = str(Dew_6[0])
        Dew_8 = Dew_7.split(' ')
        Dew_9 = str(Dew_8[1])
        Dewpoint = eval(Dew_9)
        if Dewpoint > 2:
            Temperature.append(Dewpoint)
            barnames.append(names[i])
        i = i + 1

    except:
        print("Grandfathr missing")
        i = i + 1

        
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=MITC'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Dew_1 = str(Tr[5])
        Dew_2 = Dew_1.split('<')
        Dew_3 = str(Dew_2[11])
        Dew_4 = Dew_3.split('>')
        Dew_5 = str(Dew_4[1])
        Dew_6 = Dew_5.split('%')
        Dew_7 = str(Dew_6[0])
        Dew_8 = Dew_7.split(' ')
        Dew_9 = str(Dew_8[1])
        Dewpoint = eval(Dew_9)
        Temperature.append(Dewpoint)
        barnames.append(names[i])
        i = i + 1

    except:
        print("MITC missing")
        i = i + 1
    print(Temperature)

    fig = plt.figure()
    fig.patch.set_facecolor('grey')
    ax = plt.axes()
    ax.set_facecolor('grey')
    
    #data and bar names
    height = Temperature
    bars = barnames
    y_pos = np.arange(len(bars))

    #max/mins & fonts
    if len(height) > 0:
        maximum = 110
        minimum = 0
        font = {'size':16,'color':'white'}
        font2 = {'size':22,'color':'white'}

    #color
        color_1 = np.array(height)
        color_2 = cm.YlGn((color_1 / 100))
        ax.xaxis.label.set_color('white')
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white') 
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
 
    #horizontal bars
        plt.barh(y_pos, height, color = color_2)
 
    #y-axis names
        plt.yticks(y_pos, bars, **font)

    #x-axis
        plt.xlim(minimum,maximum)

    #x label
        plt.xlabel('Relative Humidity (%)',**font)

        for i, v in enumerate(height):
            temp_height = height[i]
            len_finder = len(str(temp_height))
            if temp_height >= 0:
                plt.text(v , i-0.1, str(v), color='white', fontsize='13')
            elif temp_height < 0 and len_finder < 5:
                plt.text(v-2.1 , i-0.1, str(v), color='white', fontsize='13')
            elif temp_height < 0 and len_finder >= 5:
                plt.text(v-2.8 , i-0.1, str(v), color='white', fontsize='13')
        plt.title('Northern/Central Mountains, NC\nVertical Relative Humidity Profile', **font2)

        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        #plt.text(0.87,0.94,current_time,color='white',size=18,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
        plt.text(-0.27,-0.12,"Source: NCSCO",color='white',size=16,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
        plt.text(-0.27,1.05,"Valid: " + current_time,color='white',size=16,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
        plt.figtext(0.5,-0.2,"CarolinaWeatherGroup.com",color='white',size=10,horizontalalignment='center',transform = ax.transAxes)
        #show/save graphic
        plt.savefig("output/WNC-Humidity.png",bbox_inches='tight', facecolor=fig.get_facecolor())
        #plt.show()
    elif len(height) == 0:
        fig = plt.figure()
        fig.patch.set_facecolor('grey')
        ax = plt.axes()
        ax.set_facecolor('grey')
        plt.text(0.5,0.5,"All Stations Down",color='white',size=22,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
        plt.savefig("output/WNC-Humidity.png",bbox_inches='tight', facecolor=fig.get_facecolor())

wnchumidity()

def swnctemp():

    names = ('Andrews 1697ft','Franklin 2020ft', 'Waynesville 2755ft', 'Bearwallow Mtn 4219ft','Frying Pan Mtn 5320ft','Wayah Bald 5469ft')#'Valle Crucis 2670ft',,'Mt Mitchell #1 6600ft 'Linville 3650ft', 'Seven Devils 3940ft', ,'Sugar Mtn 5000ft'
    
    barnames = []
    Temperature = []
    Elevation = []
    i = 0

    
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KRHP'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("FLET missing")
        i = i + 1


    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=K1A5'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KTNB missing")
        i = i + 1

    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=WAYN'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("BEAR missing")
        i = i + 1
        
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=BEAR'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("JEFF missing")
        i = i + 1
        
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=FRYI'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("Grandfathr missing")
        i = i + 1

        
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=WINE'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("MITC missing")
        i = i + 1
    print(Temperature)

    fig = plt.figure()
    fig.patch.set_facecolor('grey')
    ax = plt.axes()
    ax.set_facecolor('grey')
    
    #data and bar names
    height = Temperature
    bars = barnames
    y_pos = np.arange(len(bars))

    #max/mins & fonts
    if len(height) > 0:
        maximum = max(height)+5
        minimum = min(height)-5
        font = {'size':16,'color':'white'}
        font2 = {'size':22,'color':'white'}

    #color
        color_1 = np.array(height)
        color_2 = cm.cool_r((color_1 / float(max(color_1))))
        ax.xaxis.label.set_color('white')
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white') 
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
 
    #horizontal bars
        plt.barh(y_pos, height, color = color_2)
 
    #y-axis names
        plt.yticks(y_pos, bars, **font)

    #x-axis
        plt.xlim(minimum,maximum)

    #x label
        plt.xlabel('Temperature (°F)',**font)

        for i, v in enumerate(height):
            temp_height = height[i]
            len_finder = len(str(temp_height))
            if temp_height >= 0:
                plt.text(v , i-0.1, str(v), color='white', fontsize='13')
            elif temp_height < 0 and len_finder < 5:
                plt.text(v-2.1 , i-0.1, str(v), color='white', fontsize='13')
            elif temp_height < 0 and len_finder >= 5:
                plt.text(v-2.8 , i-0.1, str(v), color='white', fontsize='13')
        plt.title('Southwestern Mountains, NC\nVertical Relative Humidity Profile', **font2)

        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        #plt.text(0.87,0.94,current_time,color='white',size=18,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
        plt.text(-0.27,-0.12,"Source: NCSCO",color='white',size=16,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
        plt.text(-0.27,1.05,"Valid: " + current_time,color='white',size=16,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
        plt.figtext(0.5,-0.2,"CarolinaWeatherGroup.com",color='white',size=10,horizontalalignment='center',transform = ax.transAxes)
        #show/save graphic
        plt.savefig("output/SWNC-Temp.png",bbox_inches='tight', facecolor=fig.get_facecolor())
        #plt.show()
    elif len(height) == 0:
        fig = plt.figure()
        fig.patch.set_facecolor('grey')
        ax = plt.axes()
        ax.set_facecolor('grey')
        plt.text(0.5,0.5,"All Stations Down",color='white',size=22,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
        plt.savefig("output/SWNC-Temp.png",bbox_inches='tight', facecolor=fig.get_facecolor())

swnctemp()

def swnchumidity():

    names = ('Andrews 1697ft','Franklin 2020ft', 'Waynesville 2755ft', 'Bearwallow Mtn 4219ft','Frying Pan Mtn 5320ft','Wayah Bald 5469ft')#'Valle Crucis 2670ft',,'Mt Mitchell #1 6600ft 'Linville 3650ft', 'Seven Devils 3940ft', ,'Sugar Mtn 5000ft'
    
    barnames = []
    Temperature = []
    Elevation = []
    i = 0

    
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KRHP'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Dew_1 = str(Tr[5])
        Dew_2 = Dew_1.split('<')
        Dew_3 = str(Dew_2[11])
        Dew_4 = Dew_3.split('>')
        Dew_5 = str(Dew_4[1])
        Dew_6 = Dew_5.split('%')
        Dew_7 = str(Dew_6[0])
        Dew_8 = Dew_7.split(' ')
        Dew_9 = str(Dew_8[1])
        Dewpoint = eval(Dew_9)
        Temperature.append(Dewpoint)
        barnames.append(names[i])
        i = i + 1

    except:
        print("FLET missing")
        i = i + 1


    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=K1A5'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Dew_1 = str(Tr[5])
        Dew_2 = Dew_1.split('<')
        Dew_3 = str(Dew_2[11])
        Dew_4 = Dew_3.split('>')
        Dew_5 = str(Dew_4[1])
        Dew_6 = Dew_5.split('%')
        Dew_7 = str(Dew_6[0])
        Dew_8 = Dew_7.split(' ')
        Dew_9 = str(Dew_8[1])
        Dewpoint = eval(Dew_9)
        Temperature.append(Dewpoint)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KTNB missing")
        i = i + 1

    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=WAYN'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Dew_1 = str(Tr[5])
        Dew_2 = Dew_1.split('<')
        Dew_3 = str(Dew_2[11])
        Dew_4 = Dew_3.split('>')
        Dew_5 = str(Dew_4[1])
        Dew_6 = Dew_5.split('%')
        Dew_7 = str(Dew_6[0])
        Dew_8 = Dew_7.split(' ')
        Dew_9 = str(Dew_8[1])
        Dewpoint = eval(Dew_9)
        Temperature.append(Dewpoint)
        barnames.append(names[i])
        i = i + 1

    except:
        print("BEAR missing")
        i = i + 1
        
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=BEAR'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Dew_1 = str(Tr[5])
        Dew_2 = Dew_1.split('<')
        Dew_3 = str(Dew_2[11])
        Dew_4 = Dew_3.split('>')
        Dew_5 = str(Dew_4[1])
        Dew_6 = Dew_5.split('%')
        Dew_7 = str(Dew_6[0])
        Dew_8 = Dew_7.split(' ')
        Dew_9 = str(Dew_8[1])
        Dewpoint = eval(Dew_9)
        Temperature.append(Dewpoint)
        barnames.append(names[i])
        i = i + 1

    except:
        print("JEFF missing")
        i = i + 1
        
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=FRYI'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Dew_1 = str(Tr[5])
        Dew_2 = Dew_1.split('<')
        Dew_3 = str(Dew_2[11])
        Dew_4 = Dew_3.split('>')
        Dew_5 = str(Dew_4[1])
        Dew_6 = Dew_5.split('%')
        Dew_7 = str(Dew_6[0])
        Dew_8 = Dew_7.split(' ')
        Dew_9 = str(Dew_8[1])
        Dewpoint = eval(Dew_9)
        Temperature.append(Dewpoint)
        barnames.append(names[i])
        i = i + 1

    except:
        print("Grandfathr missing")
        i = i + 1

        
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=WINE'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Dew_1 = str(Tr[5])
        Dew_2 = Dew_1.split('<')
        Dew_3 = str(Dew_2[11])
        Dew_4 = Dew_3.split('>')
        Dew_5 = str(Dew_4[1])
        Dew_6 = Dew_5.split('%')
        Dew_7 = str(Dew_6[0])
        Dew_8 = Dew_7.split(' ')
        Dew_9 = str(Dew_8[1])
        Dewpoint = eval(Dew_9)
        Temperature.append(Dewpoint)
        barnames.append(names[i])
        i = i + 1

    except:
        print("MITC missing")
        i = i + 1
    print(Temperature)

    fig = plt.figure()
    fig.patch.set_facecolor('grey')
    ax = plt.axes()
    ax.set_facecolor('grey')
    
    #data and bar names
    height = Temperature
    bars = barnames
    y_pos = np.arange(len(bars))

    #max/mins & fonts
    if len(height) > 0:
        maximum = 110
        minimum = 0
        font = {'size':16,'color':'white'}
        font2 = {'size':22,'color':'white'}

    #color
        color_1 = np.array(height)
        color_2 = cm.YlGn((color_1 / 100))
        ax.xaxis.label.set_color('white')
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white') 
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
 
    #horizontal bars
        plt.barh(y_pos, height, color = color_2)
 
    #y-axis names
        plt.yticks(y_pos, bars, **font)

    #x-axis
        plt.xlim(minimum,maximum)

    #x label
        plt.xlabel('Relative Humidity (%)',**font)

        for i, v in enumerate(height):
            temp_height = height[i]
            len_finder = len(str(temp_height))
            if temp_height >= 0:
                plt.text(v , i-0.1, str(v), color='white', fontsize='13')
            elif temp_height < 0 and len_finder < 5:
                plt.text(v-2.1 , i-0.1, str(v), color='white', fontsize='13')
            elif temp_height < 0 and len_finder >= 5:
                plt.text(v-2.8 , i-0.1, str(v), color='white', fontsize='13')
        plt.title('Southwestern Mountains, NC\nVertical Relative Humidity Profile', **font2)

        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        #plt.text(0.87,0.94,current_time,color='white',size=18,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
        plt.text(-0.27,-0.12,"Source: NCSCO",color='white',size=16,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
        plt.text(-0.27,1.05,"Valid: " + current_time,color='white',size=16,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
        plt.figtext(0.5,-0.25,"CarolinaWeatherGroup.com",color='white',size=10,horizontalalignment='center',transform = ax.transAxes)
        #show/save graphic
        plt.savefig("output/SwNcHumidityPlot.png",bbox_inches='tight', facecolor=fig.get_facecolor())
        #plt.show()
    elif len(height) == 0:
        fig = plt.figure()
        fig.patch.set_facecolor('grey')
        ax = plt.axes()
        ax.set_facecolor('grey')
        plt.text(0.5,0.5,"All Stations Down",color='white',size=22,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
        plt.savefig("output/SwNcHumidityPlot.png",bbox_inches='tight', facecolor=fig.get_facecolor())

swnchumidity()

def ncscmap():
    SCOfile = open('stations.txt')
    print('Collecting Data...\n\n')

    time = datetime.datetime.now()
    polished = dt.strftime(time,"%I:%M %p")

    Wind = []
    plotdata = []
    plotdew = []
    Latitude = []
    Longitude = []
    u = []
    v = []
    x = []
    y = []
    q = 0
    p = 0
    invest = 0

    for line in SCOfile:
        url = line
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html,features='html.parser')
        try:

            #A bunch of nonsense to isolate the temperature within the webpage's html
            
            Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
            Tr = Table.split(',')

            length = len(Wind)
            lengthlat = len(Latitude)

            Wind_1 = str(Tr[6])
            Wind_2 = Wind_1.split('<')
            Wind_3 = str(Wind_2[9])
            Wind_4 = Wind_3.split('>')
            Wind_5 = str(Wind_4[1])
            Wind_Sum = Wind_5[1:]
            Wind.append(Wind_5)
            #print(Wind_Sum)

            if len(Wind) == length + 1:
                try:
                    #A bunch of nonsense to isolate the temperature within the webpage's html   
                    Table = str(soup.find('table', {"class":"StationDetails"}).find_all('tr'))
                    Tr = Table.split(',')

                    cord_1 = str(Tr[15])
                    #print(cord_1)
                    cord_2 = cord_1.split('</strong>')
                    lat_1 = str(cord_2[1])
                    lat_2 = lat_1.split('°')
                    lon_1 = str(cord_2[2])
                    lon_2 = lon_1.split('°')
                    lat = eval(lat_2[0])
                    lon = eval(lon_2[0])
                    #print(url[-5:])
                    #print(lat)
                    #print(lon)
                    Latitude.append(lat)
                    Longitude.append(lon)
                except:
                    try:
                        #A bunch of nonsense to isolate the temperature within the webpage's html   
                        Table = str(soup.find('table', {"class":"StationDetails"}).find_all('tr'))
                        Tr = Table.split(',')                
                        cord_1 = str(Tr[11])
                        #print(cord_1)
                        cord_2 = cord_1.split('</strong>')
                        lat_1 = str(cord_2[1])
                        lat_2 = lat_1.split('°')
                        lon_1 = str(cord_2[2])
                        lon_2 = lon_1.split('°')
                        lat = eval(lat_2[0])
                        lon = eval(lon_2[0])
                        #print(url[-5:])
                        #print(lat)
                        #print(lon)
                        Latitude.append(lat)
                        Longitude.append(lon)

                    except:
                        try:
                            #A bunch of nonsense to isolate the temperature within the webpage's html   
                            Table = str(soup.find('table', {"class":"StationDetails"}).find_all('tr'))
                            Tr = Table.split(',')                
                            cord_1 = str(Tr[12])
                            #print(cord_1)
                            cord_2 = cord_1.split('</strong>')
                            lat_1 = str(cord_2[1])
                            lat_2 = lat_1.split('°')
                            lon_1 = str(cord_2[2])
                            lon_2 = lon_1.split('°')
                            lat = eval(lat_2[0])
                            lon = eval(lon_2[0])
                            #print(url[-5:])
                            #print(lat)
                            #print(lon)
                            Latitude.append(lat)
                            Longitude.append(lon)
                        except:
                            print("Abandon all hope for "+url[-5:])
            if len(Wind) == length + 1:
                try:
                    Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
                    Tr = Table.split(',')

                    Temp_1 = str(Tr[4])
                    Temp_2 = Temp_1.split('<')
                    Temp_3 = str(Temp_2[9])
                    Temp_4 = Temp_3.split('>')
                    Temp_5 = str(Temp_4[1])
                    Temp_6 = Temp_5.split('°')
                    Temp_7 = str(Temp_6[0])
                    Temp_8 = Temp_7.strip(' ')
                    Temperature1 = eval(Temp_8)
                    Temperature = round(Temperature1)
                    plotdata.append(Temperature)
                except:
                    Temperature = 'M'
                    plotdata.append(Temperature)
                    #print(url + " temp missing")
                try:
                    Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
                    Tr = Table.split(',')

                    Dew_1 = str(Tr[5])
                    Dew_2 = Dew_1.split('<')
                    Dew_3 = str(Dew_2[9])
                    Dew_4 = Dew_3.split('>')
                    Dew_5 = str(Dew_4[1])
                    Dew_6 = Dew_5.split('calculated at ')
                    Dew_7 = str(Dew_6[1])
                    Dew_8 = Dew_7.split('°')
                    Dew_9 = str(Dew_8[0])
                    Dewpoint1 = eval(Dew_9)
                    Dewpoint = round(Dewpoint1)
                    plotdew.append(Dewpoint)
                except:
                    try:
                        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
                        Tr = Table.split(',')

                        Dew_1 = str(Tr[5])
                        Dew_2 = Dew_1.split('size="-1"> ')
                        Dew_3 = str(Dew_2[1])
                        Dew_4 = Dew_3.split(' °F')
                        Dew_5 = str(Dew_4[0])
                        Dewpoint1 = eval(Dew_5)
                        Dewpoint = round(Dewpoint1)
                        plotdew.append(Dewpoint)
                    except:
                        Dewpoint = 'M'
                        plotdew.append(Dewpoint)
                    
        except:
            print(" missing and very broken")
        #print(url[-4:] + Wind_Sum + ' ' + str(lat) + ' ' + str(lon) + ' ' + str(Temperature) + ' ' + str(Dewpoint))
        #print(len(Latitude))
        #print(len(plotdata))

    for i in Wind:
        temp_wind = str(Wind[q])
        if temp_wind[:4] == ' not':
            print("in not available with " + temp_wind)
            u.append(1)
            v.append(1)
            x.append(Longitude[q])
            y.append(Latitude[q])
            #print(u)
            #print(v)
            q = q + 1
        elif temp_wind[:5] == ' Calm':
            print("in Calm with " + temp_wind)
            u.append(1)
            v.append(1)
            x.append(Longitude[q])
            y.append(Latitude[q])
            #print(u)
            #print(v)
            q = q + 1

        elif temp_wind[:9] == ' Variable':
            print("in Variable with " + temp_wind)
            u.append(1)
            v.append(1)
            x.append(Longitude[q])
            y.append(Latitude[q])
            #print(u)
            #print(v)
            q = q + 1

        elif temp_wind[6:8] == '°F':
            print("Somehow got temp with " + temp_wind)
            u.append(1)
            v.append(1)
            x.append(Longitude[q])
            y.append(Latitude[q])
            q = q + 1

        elif temp_wind[:11] == ' calculated':
            print("Somehow got temp with " + temp_wind)
            u.append(1)
            v.append(1)
            x.append(Longitude[q])
            y.append(Latitude[q])
            q = q + 1
            
        elif temp_wind[4:6] == '°F':
            print("Somehow got temp with " + temp_wind)
            u.append(1)
            v.append(1)
            x.append(Longitude[q])
            y.append(Latitude[q])
            q = q + 1

        else:
            print("in not calm with " + temp_wind)
            Dir_1 = Wind[q].split('(')
            Dir_2 = str(Dir_1[1])
            Dir_3 = Dir_2.split('°')
            Dir_4 = eval(Dir_3[0])
            #print(Dir_4)
            Speed_1 = Wind[q].split('at ')
            Speed_2 = str(Speed_1[1])
            Speed_3 = Speed_2.split(' mph')
            Speed_4 = eval(Speed_3[0])

            if Dir_4 < 90:
                offset = 90 - Dir_4
                deg_direction = Dir_4 + 90 + 2*offset
            else:
                offset = 90 - Dir_4
                
            deg_direction = Dir_4 + 90 + 2*offset
            rad_direction = math.radians(deg_direction)
            speed = Speed_4
            u.append(speed*math.cos(rad_direction))
            v.append(speed*math.sin(rad_direction))
            x.append(Longitude[q])
            y.append(Latitude[q])
            #print(u)
            #print(v)
            q = q + 1
        
    print(x)
    print(y)
    fig = plt.figure(figsize=(13,8))
    ax = plt.axes()
    ax.axis('off')
    ax.barbs(x,y,u,v, length=6,color='black')
    uf = len(plotdata)
    df = len(plotdew)
    hf = len(x)
    jf = len(y)
    print("Length plotdata " + str(df))
    print("Length plotdew " + str(uf))
    print("Length x " + str(hf))
    print("Length y " + str(jf))
    for b in x:
        plt.text((x[p])-0.2,(y[p])+0.1,plotdata[p],color='red',size=8)
        print("Temp " + str(p))
        plt.text((x[p])-0.2,(y[p])-0.1,plotdew[p],color='green',size=8)
        p = p + 1
    ax.set(xlim=(-84.6, -75.2), ylim=(31.82, 37))
    plt.xlim(-84.6, -75.2)
    plt.ylim(31.82, 37)

    sf = shp.Reader("GT NC & SC Counties.shp")

    for shape in sf.shapeRecords():
        for i in range(len(shape.shape.parts)):
            i_start = shape.shape.parts[i]
            if i==len(shape.shape.parts)-1:
                i_end = len(shape.shape.points)
            else:
                i_end = shape.shape.parts[i+1]
            e = [i[0] for i in shape.shape.points[i_start:i_end]]
            f = [i[1] for i in shape.shape.points[i_start:i_end]]
            plt.plot(e,f, color='grey', linewidth=0.2)

    fig.text(0.5,0.9,f"Valid {polished}",color='black',size=15,ha='center')
    plt.savefig("output/NcScMap.png",bbox_inches='tight',dpi=200)

ncscmap()
