import random
import numpy as np
import matplotlib.pyplot as plt
import copy
import random

class discrete():
    
    starting_index=0
    stopping_index=1
    steps=1
    name = ""
    xlabel = "Time"
    ylabel = "Amplitude"
    is_descrete = True
    gridcolor = '0.8'
    gridlinestyle=':'
    linecolor = 'grey'
    titleloc = 'left'
    bg_color='papayawhip'
    enable_draw = True
    
    x = []
    t = []
    
    def __init__(self, signal, start=0,step=1,time = [None],name=chr(random.randint(ord('a'), ord('z')))):

        self.steps = step
        self.name=name

        self.x = np.array(signal)
        if time[0] != None:
            self.t = time
        else:
            self.t = np.arange(start,start+len(signal),step)
        self.starting_index=self.t[0]
        self.stopping_index=self.t[-1]

    def extend_time(self,n):

        if(type(self.t) == np.ndarray):
            self.t=list(self.t)
        
        for i in range(n):
            self.t.append(self.t[-1]+self.steps)
    
    def __name__(self):
        oname=""
        for objname,oid in globals().items(): 
            if id(oid)==id(self):
                oname=objname
                break
        return oname

    def __add__(self,n):

        if type(n) == int or type(n) == float:

            new=[]
            for i in self.x:
                new.append(i+n)
            change = copy.deepcopy(self)
            change.x = new
            change.name = self.name+"+"+str(n)
            return change

        elif type(n) == list or type(n) == np.ndarray:
            
            new=[]
            change = copy.deepcopy(self)

            if(type(n) == np.ndarray):
                n=list(n)
            if(type(change.x)==np.ndarray):
                change.x=list(change.x)

            if(len(change.x)>len(n)):
                diff=len(change.x)-len(n)
                n=n+[0]*diff
            else:
                diff=len(n)-len(change.x)
                change.x=change.x+[0]*diff
                change.extend_time(diff)

            j=0
            for i in change.x:
                new.append(i+n[j])
                j=j+1
            change.x = new
            change.name = self.name+"+"+str(n)
            return change
        
        else:

            newt = []
            newx = []
            led=True

            if(self.t[0]>n.t[0]):
                t1 = self.t
                x1 = self.x
                t2 = n.t
                x2 = n.x
            else:
                t1 = n.t
                x1 = n.x
                t2 = self.t
                x2 = self.x
                led=False

            for i in range(len(t2)):
                if(t2[i]<t1[0]):
                    if led == False:
                        newx.append(x2[i]+0)
                    else:
                        newx.append(0+x2[i])

                    newt.append(t2[i])

            for i in range(len(t1)-1):
                
                c=0
                for j in range(len(t2)):
                    if(t2[j]==t1[i]):
                        if led == False:
                            newx.append(x2[j]+x1[i])
                        else:
                            newx.append(x1[i]+x2[j])
                        newt.append(t2[j])
                        c=c+1
                if(c==0):
                    if led == False:
                        newx.append(0+x1[i])
                    else:
                        newx.append(x1[i]+0)
                    newt.append(t1[i])

                for j in range(len(t2)):
                    if(t2[j]>t1[i] and t2[j]<t1[i+1]):
                        if led == False:
                            newx.append(x2[j]+0)
                        else:
                            newx.append(0+x2[j])
                        newt.append(t2[j])
            
            c=0
            for i in range(len(t2)):
                if(t2[i]==t1[-1]):
                    if led == False:
                        newx.append(x2[i]+x1[-1])
                    else:
                        newx.append(x1[-1]+x2[i])
                    newt.append(t2[i])
                    c=c+1
            if(c==0):
                if led == False:
                    newx.append(0+x1[-1])
                else:
                    newx.append(x1[-1]+0)
                newt.append(t1[-1])
                

            if(self.t[-1]>n.t[-1]):
                if(led==False):
                    led=True
                t1 = self.t
                x1 = self.x
                t2 = n.t
                x2 = n.x
            else:
                led=False
                t1 = n.t
                x1 = n.x
                t2 = self.t
                x2 = self.x

            for i in range(len(t1)):
                if(t2[-1]<t1[i]):
                    if led == False:
                        newx.append(0+x1[i])
                    else:
                        newx.append(x1[i]+0)
                    newt.append(t1[i])


            change = copy.deepcopy(self)
            change.x = newx
            change.t = newt
            change.name = self.name+"+"+n.name
            return change                 

    def __radd__(self,n):

        if type(n) == int or type(n) == float:
            new=[]
            for i in self.x:
                new.append(n+i)
            change = copy.deepcopy(self)
            change.x = new
            change.name = str(n)+"+"+self.name
            return change

        elif type(n) == list or type(n) == np.ndarray:
            
            new=[]
            change = copy.deepcopy(self)

            if(type(n) == np.ndarray):
                n=list(n)
            if(type(change.x)==np.ndarray):
                change.x=list(change.x)

            if(len(change.x)>len(n)):
                diff=len(change.x)-len(n)
                n=n+[0]*diff
            else:
                diff=len(n)-len(change.x)
                change.x=change.x+[0]*diff
                change.extend_time(diff)

            j=0
            for i in change.x:
                new.append(n[j]+i)
                j=j+1
            change.x = new
            change.name = str(n)+"+"+self.name
            return change

    def __pow__(self,n):

        if type(n) == int or type(n) == float:

            new=[]
            for i in self.x:
                new.append(i**n)
            change = copy.deepcopy(self)
            change.x = new
            change.name = self.name+"^"+str(n)
            return change

        elif type(n) == list or type(n) == np.ndarray:
            
            new=[]
            change = copy.deepcopy(self)

            if(type(n) == np.ndarray):
                n=list(n)
            if(type(change.x)==np.ndarray):
                change.x=list(change.x)

            if(len(change.x)>len(n)):
                diff=len(change.x)-len(n)
                n=n+[0]*diff
            else:
                diff=len(n)-len(change.x)
                change.x=change.x+[0]*diff
                change.extend_time(diff)

            j=0
            for i in change.x:
                new.append(i**n[j])
                j=j+1
            change.x = new
            change.name = self.name+"^"+str(n)
            return change

        else:

            newt = []
            newx = []
            led=True

            if(self.t[0]>n.t[0]):
                t1 = self.t
                x1 = self.x
                t2 = n.t
                x2 = n.x
            else:
                t1 = n.t
                x1 = n.x
                t2 = self.t
                x2 = self.x
                led=False

            for i in range(len(t2)):
                if(t2[i]<t1[0]):
                    if led == False:
                        newx.append(x2[i]**0)
                    else:
                        newx.append(0**x2[i])

                    newt.append(t2[i])

            for i in range(len(t1)**1):
                
                c=0
                for j in range(len(t2)):
                    if(t2[j]==t1[i]):
                        if led == False:
                            newx.append(x2[j]**x1[i])
                        else:
                            newx.append(x1[i]**x2[j])
                        newt.append(t2[j])
                        c=c+1
                if(c==0):
                    if led == False:
                        newx.append(0**x1[i])
                    else:
                        newx.append(x1[i]**0)
                    newt.append(t1[i])

                for j in range(len(t2)):
                    if(t2[j]>t1[i] and t2[j]<t1[i+1]):
                        if led == False:
                            newx.append(x2[j]**0)
                        else:
                            newx.append(0**x2[j])
                        newt.append(t2[j])
            
            c=0
            for i in range(len(t2)):
                if(t2[i]==t1[-1]):
                    if led == False:
                        newx.append(x2[i]**x1[-1])
                    else:
                        newx.append(x1[-1]**x2[i])
                    newt.append(t2[i])
                    c=c+1
            if(c==0):
                if led == False:
                    newx.append(0**x1[-1])
                else:
                    newx.append(x1[-1]**0)
                newt.append(t1[-1])
                

            if(self.t[-1]>n.t[-1]):
                if(led==False):
                    led=True
                t1 = self.t
                x1 = self.x
                t2 = n.t
                x2 = n.x
            else:
                led=False
                t1 = n.t
                x1 = n.x
                t2 = self.t
                x2 = self.x

            for i in range(len(t1)):
                if(t2[-1]<t1[i]):
                    if led == False:
                        newx.append(0**x1[i])
                    else:
                        newx.append(x1[i]**0)
                    newt.append(t1[i])


            change = copy.deepcopy(self)
            change.x = newx
            change.t = newt
            change.name = self.name+"^"+n.name
            return change       

    def __rpow__(self,n):

        if type(n) == int or type(n) == float:
            new=[]
            for i in self.x:
                new.append(n**i)
            change = copy.deepcopy(self)
            change.x = new
            change.name = str(n)+"^"+self.name
            return change

        elif type(n) == list or type(n) == np.ndarray:
            
            new=[]
            change = copy.deepcopy(self)

            if(type(n) == np.ndarray):
                n=list(n)
            if(type(change.x)==np.ndarray):
                change.x=list(change.x)

            if(len(change.x)>len(n)):
                diff=len(change.x)-len(n)
                n=n+[0]*diff
            else:
                diff=len(n)-len(change.x)
                change.x=change.x+[0]*diff
                change.extend_time(diff)

            j=0
            for i in change.x:
                new.append(n[j]**i)
                j=j+1
            change.x = new
            change.name = str(n)+"^"+self.name
            return change

    def __sub__(self,n):

        if type(n) == int or type(n) == float:

            new=[]
            for i in self.x:
                new.append(i-n)
            change = copy.deepcopy(self)
            change.x = new
            change.name = self.name+"-"+str(n)
            return change

        elif type(n) == list or type(n) == np.ndarray:
            
            new=[]
            change = copy.deepcopy(self)

            if(type(n) == np.ndarray):
                n=list(n)
            if(type(change.x)==np.ndarray):
                change.x=list(change.x)

            if(len(change.x)>len(n)):
                diff=len(change.x)-len(n)
                n=n+[0]*diff
            else:
                diff=len(n)-len(change.x)
                change.x=change.x+[0]*diff
                change.extend_time(diff)

            j=0
            for i in change.x:
                new.append(i-n[j])
                j=j+1
            change.x = new
            change.name = self.name+"-"+str(n)
            return change

        else:

            newt = []
            newx = []
            led=True

            if(self.t[0]>n.t[0]):
                t1 = self.t
                x1 = self.x
                t2 = n.t
                x2 = n.x
            else:
                t1 = n.t
                x1 = n.x
                t2 = self.t
                x2 = self.x
                led=False

            for i in range(len(t2)):
                if(t2[i]<t1[0]):
                    if led == False:
                        newx.append(x2[i]-0)
                    else:
                        newx.append(0-x2[i])

                    newt.append(t2[i])

            for i in range(len(t1)-1):
                
                c=0
                for j in range(len(t2)):
                    if(t2[j]==t1[i]):
                        if led == False:
                            newx.append(x2[j]-x1[i])
                        else:
                            newx.append(x1[i]-x2[j])
                        newt.append(t2[j])
                        c=c+1
                if(c==0):
                    if led == False:
                        newx.append(0-x1[i])
                    else:
                        newx.append(x1[i]-0)
                    newt.append(t1[i])

                for j in range(len(t2)):
                    if(t2[j]>t1[i] and t2[j]<t1[i+1]):
                        if led == False:
                            newx.append(x2[j]-0)
                        else:
                            newx.append(0-x2[j])
                        newt.append(t2[j])
            
            c=0
            for i in range(len(t2)):
                if(t2[i]==t1[-1]):
                    if led == False:
                        newx.append(x2[i]-x1[-1])
                    else:
                        newx.append(x1[-1]-x2[i])
                    newt.append(t2[i])
                    c=c+1
            if(c==0):
                if led == False:
                    newx.append(0-x1[-1])
                else:
                    newx.append(x1[-1]-0)
                newt.append(t1[-1])
                

            if(self.t[-1]>n.t[-1]):
                if(led==False):
                    led=True
                t1 = self.t
                x1 = self.x
                t2 = n.t
                x2 = n.x
            else:
                led=False
                t1 = n.t
                x1 = n.x
                t2 = self.t
                x2 = self.x

            for i in range(len(t1)):
                if(t2[-1]<t1[i]):
                    if led == False:
                        newx.append(0-x1[i])
                    else:
                        newx.append(x1[i]-0)
                    newt.append(t1[i])


            change = copy.deepcopy(self)
            change.x = newx
            change.t = newt
            change.name = self.name+"-"+n.name
            return change       

    def __rsub__(self,n):

        if type(n) == int or type(n) == float:
            new=[]
            for i in self.x:
                new.append(n-i)
            change = copy.deepcopy(self)
            change.x = new
            change.name = str(n)+"-"+self.name
            return change

        elif type(n) == list or type(n) == np.ndarray:
            
            new=[]
            change = copy.deepcopy(self)

            if(type(n) == np.ndarray):
                n=list(n)
            if(type(change.x)==np.ndarray):
                change.x=list(change.x)

            if(len(change.x)>len(n)):
                diff=len(change.x)-len(n)
                n=n+[0]*diff
            else:
                diff=len(n)-len(change.x)
                change.x=change.x+[0]*diff
                change.extend_time(diff)

            j=0
            for i in change.x:
                new.append(n[j]-i)
                j=j+1
            change.x = new
            change.name = str(n)+"-"+self.name
            return change

    def __mul__(self,n):

        if type(n) == int or type(n) == float:

            new=[]
            for i in self.x:
                new.append(i*n)
            change = copy.deepcopy(self)
            change.x = new
            change.name = self.name+"."+str(n)
            return change

        elif type(n) == list or type(n) == np.ndarray:
            
            new=[]
            change = copy.deepcopy(self)

            if(type(n) == np.ndarray):
                n=list(n)
            if(type(change.x)==np.ndarray):
                change.x=list(change.x)

            if(len(change.x)>len(n)):
                diff=len(change.x)-len(n)
                n=n+[0]*diff
            else:
                diff=len(n)-len(change.x)
                change.x=change.x+[0]*diff
                change.extend_time(diff)

            j=0
            for i in change.x:
                new.append(i*n[j])
                j=j+1
            change.x = new
            change.name = self.name+"."+str(n)
            return change

        else:

            newt = []
            newx = []
            led=True

            if(self.t[0]>n.t[0]):
                t1 = self.t
                x1 = self.x
                t2 = n.t
                x2 = n.x
            else:
                t1 = n.t
                x1 = n.x
                t2 = self.t
                x2 = self.x
                led=False

            for i in range(len(t2)):
                if(t2[i]<t1[0]):
                    if led == False:
                        newx.append(x2[i]*0)
                    else:
                        newx.append(0*x2[i])

                    newt.append(t2[i])

            for i in range(len(t1)-1):
                
                c=0
                for j in range(len(t2)):
                    if(t2[j]==t1[i]):
                        if led == False:
                            newx.append(x2[j]*x1[i])
                        else:
                            newx.append(x1[i]*x2[j])
                        newt.append(t2[j])
                        c=c+1
                if(c==0):
                    if led == False:
                        newx.append(0*x1[i])
                    else:
                        newx.append(x1[i]*0)
                    newt.append(t1[i])

                for j in range(len(t2)):
                    if(t2[j]>t1[i] and t2[j]<t1[i+1]):
                        if led == False:
                            newx.append(x2[j]*0)
                        else:
                            newx.append(0*x2[j])
                        newt.append(t2[j])
            
            c=0
            for i in range(len(t2)):
                if(t2[i]==t1[-1]):
                    if led == False:
                        newx.append(x2[i]*x1[-1])
                    else:
                        newx.append(x1[-1]*x2[i])
                    newt.append(t2[i])
                    c=c+1
            if(c==0):
                if led == False:
                    newx.append(0*x1[-1])
                else:
                    newx.append(x1[-1]*0)
                newt.append(t1[-1])
                

            if(self.t[-1]>n.t[-1]):
                if(led==False):
                    led=True
                t1 = self.t
                x1 = self.x
                t2 = n.t
                x2 = n.x
            else:
                led=False
                t1 = n.t
                x1 = n.x
                t2 = self.t
                x2 = self.x

            for i in range(len(t1)):
                if(t2[-1]<t1[i]):
                    if led == False:
                        newx.append(0*x1[i])
                    else:
                        newx.append(x1[i]*0)
                    newt.append(t1[i])


            change = copy.deepcopy(self)
            change.x = newx
            change.t = newt
            change.name = self.name+"."+n.name
            return change      

    def __rmul__(self,n):

        if type(n) == int or type(n) == float:
            new=[]
            for i in self.x:
                new.append(n*i)
            change = copy.deepcopy(self)
            change.x = new
            change.name = str(n)+"."+self.name
            return change

        elif type(n) == list or type(n) == np.ndarray:
            
            new=[]
            change = copy.deepcopy(self)

            if(type(n) == np.ndarray):
                n=list(n)
            if(type(change.x)==np.ndarray):
                change.x=list(change.x)

            if(len(change.x)>len(n)):
                diff=len(change.x)-len(n)
                n=n+[0]*diff
            else:
                diff=len(n)-len(change.x)
                change.x=change.x+[0]*diff
                change.extend_time(diff)

            j=0
            for i in change.x:
                new.append(n[j]*i)
                j=j+1
            change.x = new
            change.name = str(n)+"."+self.name
            return change

    def __truediv__(self,n):

        if type(n) == int or type(n) == float:

            new=[]
            for i in self.x:
                new.append(i/n)
            change = copy.deepcopy(self)
            change.x = new
            change.name = self.name+"/"+str(n)
            return change

        elif type(n) == list or type(n) == np.ndarray:
            
            new=[]
            change = copy.deepcopy(self)

            if(type(n) == np.ndarray):
                n=list(n)
            if(type(change.x)==np.ndarray):
                change.x=list(change.x)

            if(len(change.x)>len(n)):
                diff=len(change.x)-len(n)
                n=n+[0]*diff
            else:
                diff=len(n)-len(change.x)
                change.x=change.x+[0]*diff
                change.extend_time(diff)

            j=0
            for i in change.x:
                new.append(i/n[j])
                j=j+1
            change.x = new
            change.name = self.name+"/"+str(n)
            return change
        
        else:

            newt = []
            newx = []
            led=True

            if(self.t[0]>n.t[0]):
                t1 = self.t
                x1 = self.x
                t2 = n.t
                x2 = n.x
            else:
                t1 = n.t
                x1 = n.x
                t2 = self.t
                x2 = self.x
                led=False

            for i in range(len(t2)):
                if(t2[i]<t1[0]):
                    if led == False:
                        newx.append(x2[i]/0)
                    else:
                        newx.append(0/x2[i])

                    newt.append(t2[i])

            for i in range(len(t1)-1):
                
                c=0
                for j in range(len(t2)):
                    if(t2[j]==t1[i]):
                        if led == False:
                            newx.append(x2[j]/x1[i])
                        else:
                            newx.append(x1[i]/x2[j])
                        newt.append(t2[j])
                        c=c+1
                if(c==0):
                    if led == False:
                        newx.append(0/x1[i])
                    else:
                        newx.append(x1[i]/0)
                    newt.append(t1[i])

                for j in range(len(t2)):
                    if(t2[j]>t1[i] and t2[j]<t1[i+1]):
                        if led == False:
                            newx.append(x2[j]/0)
                        else:
                            newx.append(0/x2[j])
                        newt.append(t2[j])
            
            c=0
            for i in range(len(t2)):
                if(t2[i]==t1[-1]):
                    if led == False:
                        newx.append(x2[i]/x1[-1])
                    else:
                        newx.append(x1[-1]/x2[i])
                    newt.append(t2[i])
                    c=c+1
            if(c==0):
                if led == False:
                    newx.append(0/x1[-1])
                else:
                    newx.append(x1[-1]/0)
                newt.append(t1[-1])
                

            if(self.t[-1]>n.t[-1]):
                if(led==False):
                    led=True
                t1 = self.t
                x1 = self.x
                t2 = n.t
                x2 = n.x
            else:
                led=False
                t1 = n.t
                x1 = n.x
                t2 = self.t
                x2 = self.x

            for i in range(len(t1)):
                if(t2[-1]<t1[i]):
                    if led == False:
                        newx.append(0/x1[i])
                    else:
                        newx.append(x1[i]/0)
                    newt.append(t1[i])


            change = copy.deepcopy(self)
            change.x = newx
            change.t = newt
            change.name = self.name+"/"+n.name
            return change    

    def __rtruediv__(self,n):

        if type(n) == int or type(n) == float:
            new=[]
            for i in self.x:
                new.append(n/i)
            change = copy.deepcopy(self)
            change.x = new
            change.name = str(n)+"/"+self.name
            return change

        elif type(n) == list or type(n) == np.ndarray:
            
            new=[]
            change = copy.deepcopy(self)

            if(type(n) == np.ndarray):
                n=list(n)
            if(type(change.x)==np.ndarray):
                change.x=list(change.x)

            if(len(change.x)>len(n)):
                diff=len(change.x)-len(n)
                n=n+[0]*diff
            else:
                diff=len(n)-len(change.x)
                change.x=change.x+[0]*diff
                change.extend_time(diff)

            j=0
            for i in change.x:
                new.append(n[j]/i)
                j=j+1
            change.x = new
            change.name = str(n)+"/"+self.name
            return change

    def update_stopping_index(self):
        self.stopping_index=self.x[-1]
        return self.x[-1]
    
    def update_starting_index(self):
        self.stopping_index=self.x[0]
        return self.x[0]

    def get_stopping_index(self):
        return self.x[-1]
    
    def get_starting_index(self):
        return self.x[0]

    def update_steps(self):
        if len(self.t)==1:
            return self.steps
        else:
            self.steps=self.t[1]-self.t[0]
            return self.t[1]-self.t[0]

    def get_steps(self):
        if len(self.t)==1:
            return self.steps
        else:
            return self.t[1]-self.t[0]

    def draw(self,xx,tt,obj=None):

        if self.enable_draw==True:
            tempname = ""
            if obj == None:
               tempname = self.name
            else:
                tempname = obj.name

            print('\033[91m'+tempname+'\033[0m')

            print("[ ",end="\t")
            for i in xx:
                print(i,end="\t")
            print(" ]")  
        
            print("  ",end="\t")        
            for i in tt:
                if i==0:
                    print('\033[93m'+"🠕"+'\033[0m',end="")
                else:
                    print(" ",end="")
                
                print("\t",end="")  
              
            print("")
        
    def show(self):
        
        self.draw(self.x,self.t)

        plt.figure(facecolor=self.bg_color)
        plt.title(self.name,loc=self.titleloc)
        plt.ylabel(self.ylabel)
        plt.xlabel(self.xlabel)
        plt.grid(color=self.gridcolor,linestyle=self.gridlinestyle)

        if self.is_descrete == True:
            plt.stem(self.t,self.x,linefmt=self.linecolor)
        else:
            plt.plot(self.t,self.x)

        plt.show() 
    
    def compare(self,obj,obj1=None,obj2=None,obj3=None,obj4=None,spacing=None):
        
        tmp = [obj1,obj2,obj3,obj4]
        c = 2

        plt.figure(facecolor=self.bg_color)

        for i in tmp:
            if i!=None:
                c = c+1

        if spacing !=None:
            plt.subplots_adjust(hspace= spacing)
        else:
            plt.subplots_adjust(hspace= 0.3)

        self.draw(self.x, self.t)
        self.draw(obj.x, obj.t,obj)
        
        plt.subplot(c, 1, 1)
        plt.title(self.name,loc=self.titleloc)
        plt.ylabel(self.ylabel)
        plt.xlabel(self.xlabel)
        plt.grid(color=self.gridcolor,linestyle=self.gridlinestyle)

        if self.is_descrete == True:
            plt.stem(self.t,self.x,linefmt=self.linecolor)
        else:
            plt.plot(self.t,self.x)
        
        plt.subplot(c, 1, 2)
        plt.title(obj.name,loc=self.titleloc)
        plt.ylabel(obj.ylabel)
        plt.xlabel(obj.xlabel)
        plt.grid(color=self.gridcolor,linestyle=self.gridlinestyle)

        if obj.is_descrete == True:
            plt.stem(obj.t,obj.x,linefmt=self.linecolor)
        else:
            plt.plot(obj.t,obj.x)
        
        if obj1 != None:

            self.draw(obj1.x, obj1.t,obj1)

            plt.subplot(c, 1, 3)
            plt.title(obj1.name,loc=self.titleloc)
            plt.ylabel(obj1.ylabel)
            plt.xlabel(obj1.xlabel)
            plt.grid(color=self.gridcolor,linestyle=self.gridlinestyle)

            if obj1.is_descrete == True:
                plt.stem(obj1.t,obj1.x,linefmt=self.linecolor)
            else:
                plt.plot(obj1.t,obj1.x)
        
        if obj2 != None:

            self.draw(obj2.x, obj2.t,obj2)
            print("works")
            plt.subplot(c, 1, 4)
            plt.title(obj2.name,loc=self.titleloc)
            plt.ylabel(obj2.ylabel)
            plt.xlabel(obj2.xlabel)
            plt.grid(color=self.gridcolor,linestyle=self.gridlinestyle)

            if obj2.is_descrete == True:
                plt.stem(obj2.t,obj2.x,linefmt=self.linecolor)
            else:
                plt.plot(obj2.t,obj2.x)

        if obj3 != None:

            self.draw(obj3.x, obj3.t,obj3)

            plt.subplot(c, 1, 5)
            plt.title(obj3.name,loc=self.titleloc)
            plt.ylabel(obj3.ylabel)
            plt.xlabel(obj3.xlabel)
            plt.grid(color=self.gridcolor,linestyle=self.gridlinestyle)

            if obj3.is_descrete == True:
                plt.stem(obj3.t,obj3.x,linefmt=self.linecolor)
            else:
                plt.plot(obj3.t,obj3.x)

        if obj4 != None:

            self.draw(obj4.x, obj4.t,obj4)

            plt.subplot(c, 1, 6)
            plt.title(obj4.name,loc=self.titleloc)
            plt.ylabel(obj4.ylabel)
            plt.xlabel(obj4.xlabel)
            plt.grid(color=self.gridcolor,linestyle=self.gridlinestyle)

            if obj4.is_descrete == True:
                plt.stem(obj4.t,obj4.x,linefmt=self.linecolor)
            else:
                plt.plot(obj4.t,obj4.x)

        plt.show()
  
    def operate(self,slope=1,intercept=0,):
        change = copy.deepcopy(self)


        if self.is_descrete == False:
            if(intercept==0):
                change.name = self.name+"("+str(slope)+"t)"
            elif(slope==1):
                change.name = self.name+"(t+"+str(intercept)+")"
            else:
                change.name = self.name+"("+str(slope)+"t+"+str(intercept)+")"
        else:
            if(intercept==0):
                change.name = self.name+"["+str(slope)+"n]"
            elif(slope==1):
                change.name = self.name+"[n+"+str(intercept)+"]"
            else:
                change.name = self.name+"["+str(slope)+"n+"+str(intercept)+"]"
        
        if(slope<0):
           
            hh=[]
            for i in change.t:
                hh.append(i*-1)
            change.t=np.array(hh)
            n=len(change.t)
            
            for i in range(n-1):
                for j in range(0,n-i-1):
                    if(change.t[j]>change.t[j+1]):
                        change.t[j],change.t[j+1]=change.t[j+1],change.t[j]
                        change.x[j],change.x[j+1]=change.x[j+1],change.x[j]

            slope=(-1)*slope
        change.t = (change.t/slope)-intercept
        return change

    def TimeShift(self,intersept):
        return self.operate(1,intersept)

    def TimeScale(self,slope):
        return self.operate(slope,0)
    
    def convolve(self,n):       
        conv_signal = np.convolve(self.x,n.x)
        change = copy.deepcopy(self)
        new_starting_index=self.starting_index+n.starting_index
        new_steps=min(self.steps,n.steps)
        change.__init__(conv_signal,new_starting_index,new_steps)
        change.name = self.name+"*"+n.name
        return change

    def even_component(self):
        return (self+self.operate(-1))/2

    def odd_component(self):
        return (self-self.operate(-1))/2

    def to_continuous(self,enable_draw=True):
        self.enable_draw=enable_draw
        self.is_descrete=False

    def append(self,n):
        self.x=list(self.x)
        self.t=list(self.t)
        self.x.append(n)
        self.t.append(self.t[-1]+self.get_steps())

    #Trims zero elements from the start and end of the signal to beautify the plot
    def trim(self):

        self.x=list(self.x)
        self.t=list(self.t)

        for i in range(0,len(self.x)):
            if(self.x[i]==0):
                self.x.pop(i)
                self.t.pop(i)
            else:
                break
        
        for i in range(len(self.x)-1,-1,-1):
            if(self.x[i]==0):
                self.x.pop(i)
                self.t.pop(i)
            else:
                break

class unit_impulse(discrete):

    def __init__(self):
        super().__init__([1],0)

class unit_step(discrete):

    def __init__(self,size=20):
        arr=[]
        for i in range (size):
            arr.append(1)
        super().__init__(arr,0)

class continuous(discrete):

    def __init__(self,func=None,signal=None, start=0,stop=1,step=0.001, time=[None], name=chr(random.randint(ord('a'), ord('z')))):
        
        self.is_descrete=False
        self.enable_draw=False
        if time[0]==None and signal !=None:
            time = np.arange(start,start+len(signal),step)
        elif time[0]==None:
            time = np.arange(start,stop,step)
        
        temp=[]
        if func==None and signal==None:
            print('\033[91m'+'Error: Either refer to a function or supply a signal !'+'\033[0m')
        elif func!=None and signal==None:
            for i in time:
                temp.append(func(i))
            signal=temp

        super().__init__(signal, start, step, time, name)

class array(discrete):
    def __init__(self, signal, start=0, step=1, time=[None], name="arr"+str(random.randint(0,100))):
        super().__init__(list(signal), start, step, time, name)

class darray(array):
    def __init__(self, signal, start=0, step=1, time=[None], name="arr" + str(random.randint(0, 100))):
        super().__init__(signal, start, step, time, name)

class carray(continuous):
    
    def __init__(self,signal=None, start=0, stop=1, step=0.001, time=[None],func=None,name="arr" + str(random.randint(0, 100))):
        super().__init__(func, list(signal), start, stop, step, time, name)

