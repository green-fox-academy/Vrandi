# -*- coding: utf-8 -*-
'''
Created on 2015 ápr. 25

@author: vrabely2
'''

class Clock(object):
    def __init__(self, h, m, sec):
        if h>23:
            h = 0
        self.hour = h
        if m>59:
            m = 0
        self.minute = m
        if sec>59:
            sec = 0
        self.second = sec
    
    def restart(self):
        '''
        Újra beállítja az osztály értékeit (óra, perc, másodperc) amiket a konzolról kér be.
        '''
        print("Állíts be az órát:")
        nh = input("Hány órára szeretnéd állítani? (0-23) ")
        nm = input("Hány perc? (0-59) ")
        ns = input("Hány másodperc? (0-59) ")
        newh = int(nh)
        newm = int(nm)
        newsec = int(ns) 
        if newh>23:
            newh = 0
        self.hour = newh
        if newm>59:
            newm = 0
        self.minute = newm
        if newsec>59:
            newsec = 0
        self.second = newsec
        
    def tikk(self):
        '''
        Másodpercenként növeli az osztály értékeit.
        '''
        if self.second < 59:
            self.second = self.second+1
        elif self.second == 59 and self.minute != 59:
            self.second = 0
            self.minute = self.minute + 1
        elif self.second == 59 and self.minute == 59:
            self.second = 0
            self.minute = 0
            self.hour = self.hour+1
            
    def printer(self):
        print("Az idő: ", self.hour, ':', self.minute, ':', self.second)
        
    def __str__(self):
        '''
        Egy stringet csinál az osztály értékeiből óra:perc:másodperc formátumban.
        '''
        string=''
        if self.hour < 10:
            string= string+'0'+str(self.hour)
        else:
            string= string+str(self.hour)
        
        string = string + ':'
        if self.minute < 10:
            string= string+'0'+str(self.minute)
        else:
            string= string+str(self.minute)
        
        string = string + ':'    
        if self.second < 10:
            string= string+'0'+str(self.second)
        else:
            string= string+str(self.second)
        return string
            
'''
Clock proba:
'''       
cl = Clock(12,35,45)
cl.restart()
cl.tikk()
cl.tikk()
cl.tikk()
cl.printer() 
print(cl.__str__())
           
            
class Calendar(object):
    def __init__(self, y, mon, day):
        harminc = [4,6,9,11]
        harmincegy = [1,3,5,7,8,10,12]
        self.year = y
        if mon > 12:
            mon = 12
        elif mon == 0:
            mon = 1
        self.month = mon 
        if self.month == 2:
            if day > 28:
                day = 28
            elif day == 0:
                day = 1
        elif self.month in harminc:
            if day > 30:
                day = 30
            elif day == 0:
                day = 1
        elif self.month in harmincegy:
            if day > 31:
                day = 31
            elif day == 0:
                day = 1
        self.day = day
    
    def setdate(self):
        '''
        Újra beállítja az osztály értékeit (év, hónap, nap) amiket a konzolról kér be.
        '''
        print("A naptár beállítása: ")
        ny = input("Add meg az évet (4 számjegy): ")
        nm = input("Add meg a hónapot (1-12): ")
        nd = input("Add meg a napot (1-28-30-31): ")
        newy = int(ny)
        newm = int(nm)
        newday = int(nd)
        harminc = [4,6,9,11]
        harmincegy = [1,3,5,7,8,10,12]
        self.year = newy
        if newm > 12:
            newm = 12
        elif newm == 0:
            newm = 1
        self.month = newm 
        if self.month == 2:
            if newday > 28:
                newday = 28
            elif newday == 0:
                newday = 1
        elif self.month in harminc:
            if newday > 30:
                newday = 30
            elif newday == 0:
                newday = 1
        elif self.month in harmincegy:
            if newday > 31:
                newday = 31
            elif newday == 0:
                newday = 1
        self.day = newday
    
    def get(self):
        '''
        Visszatér a példány értékeivel egy tuplebe rendezve.
        '''
        t = (self.year, self.month, self.day)
        return t
            
    def daybyday(self):
        '''
        Naponként növeli az osztály értékeit.
        '''
        harminc = [4,6,9,11]
        harmincegy = [1,3,5,7,8,10]
        if self.month == 2:
            if self.day == 28:
                self.day = 1
                self.month = self.month + 1
            elif self.day < 28:
                self.day = self.day + 1
        
        elif self.month in harminc:
            if self.day == 30:
                self.day = 1
                self.month = self.month + 1
            elif self.day < 30:
                self.day = self.day + 1
        
        elif self.month in harmincegy:
            if self.day == 31:
                self.day = 1
                self.month = self.month + 1
            elif self.day < 31:
                self.day = self.day + 1
                
        elif self.month == 12:
            if self.day == 31:
                self.day = 0
                self.month = 1
                self.year = self.year + 1
            elif self.day < 31:
                self.day = self.day + 1
                
    def __str__(self):
        '''
        Egy stringet csinál az osztály értékeiből év.hónap.nap formátumban.
        '''
        string=''
        string = string+str(self.year)
        string = string + '.'
        if self.month < 10:
            string= string+'0'+str(self.month)
        else:
            string= string+str(self.month)
        
        string = string + '.'
            
        if self.day < 10:
            string= string+'0'+str(self.day)
        else:
            string= string+str(self.day)
        string = string + '.'
        return string

'''
Calendar proba:
'''
d = Calendar(2015,2,30)
d.daybyday()
d.setdate()
d.daybyday()
d.daybyday()
print(d.__str__())
        
class Calendarclock(Clock, Calendar):
    
    def __init__(self, y, mon, day, h, m, sec):
        '''
        Átadja a superclassok értékeit.
        '''
        Calendar.__init__(self, y, mon, day)
        Clock.__init__(self, h, m, sec)
    
    def __str__(self):
        '''
        Egy sztringben összefogja az értékeket 
        '''
        string=''
        string = string+str(self.year)
        string = string + '.'
        if self.month < 10:
            string= string+'0'+str(self.month)
        else:
            string= string+str(self.month)
        
        string = string + '.'
            
        if self.day < 10:
            string= string+'0'+str(self.day)
        else:
            string= string+str(self.day)
        string = string + '.'+'\t'
        
        if self.hour < 10:
            string= string+'0'+str(self.hour)
        else:
            string= string+str(self.hour)
        
        string = string + ':'
        if self.minute < 10:
            string= string+'0'+str(self.minute)
        else:
            string= string+str(self.minute)
        
        string = string + ':'    
        if self.second < 10:
            string= string+'0'+str(self.second)
        else:
            string= string+str(self.second)
            
        return string
    
    
       
'''
Calendarclock proba:
'''
ido = Calendarclock(2001,11,15,12,35,15)
print(ido.__str__())
    


    
            
        