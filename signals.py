import numpy as np
import matplotlib.pyplot as plt
import copy
import random
import sympy.core.numbers as symnum
import sympy.functions as symfun

#Class to build discrete signals
class discrete():
    
    #Class variables used for different visual and operational settings
    starting_index=0
    stopping_index=1
    steps=1
    name = ""
    xlabel = "Time"
    ylabel = "Amplitude"
    is_descrete = True
    color1 = 'red'
    color2='grey'
    titleloc = 'left'
    bg_color=None#'papayawhip'
    enable_draw = True
    style='Solarize_Light2'
    stem_opacity=0.1
    domain = 'time'
    
    x = []
    t = []
    
    #Gets invoked on object creation
    def __init__(self, signal, start=0,step=1,time = [None],name=chr(random.randint(ord('a'), ord('z')))):

        #Storing the supplied variables for later use
        self.steps = step
        self.name=name

        #Converting and Handling the given data
        self.x = np.array(signal) 
        if time[0] != None:
            self.t = time
        else:
            #Generating the time array if not received
            self.t = np.arange(start,start+(len(signal))*step,step)

        #Storing the index values for later use
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

    #Operator overloading, adding two wiggle signals
    def __add__(self,n):

        #Adding a scalar value with self
        if type(n) == int or type(n) == float:

            new=[]
            for i in self.x:
                new.append(i+n)
            change = copy.deepcopy(self)
            change.x = new
            change.name = self.name+"+"+str(n)
            return change

        #Adding a list with self
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
        
        #Adding a wiggle type signal value with self
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

            change.fix_index()
            return change                 

    #To fix index errors after operation
    def fix_index(self):

        self.x=list(self.x)
        self.t=list(self.t)

        for i in range(1,len(self.t)):
            if(self.t[i]<=self.t[(i-1)]):
                for j in range(i,len(self.t)):
                    self.x.pop(i)
                    self.t.pop(i)
                break

    #To handle addition in reverse
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
            change.fix_index()
            return change

    #Operator overloading, to handle powers
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
            change.fix_index()
            return change       

    #Operator overloading, to handle powers in reveerse
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
            change.fix_index()
            return change

    #Operator overloading, subtracting two wiggle signals
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
            change.fix_index()
            return change       

    #To handle subtract in reverse
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
            change.fix_index()
            return change

    #Operator overloading, multiplying two wiggle signals
    def __mul__(self,n):

        #Multiplying a scalar value with self
        if type(n) == int or type(n) == float:

            new=[]
            for i in self.x:
                new.append(i*n)
            change = copy.deepcopy(self)
            change.x = new
            change.name = self.name+"."+str(n)
            return change

        #Multiplying a list with self
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

        #Multiplying a wiggle type signal value with self
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
            change.fix_index()
            return change      

    #To handle multiplication in reverse
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
            change.fix_index()
            return change

    #Operator overloading, dividing two wiggle signals
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
            change.fix_index()
            return change    

    #To handle division in reverse
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
            change.fix_index()
            return change

    #To enable the object to be treated like arrays ; easily get items in the signal
    def __getitem__(self,key):
        time = list(self.t)
        amp = list(self.x)

        index = 0
        found = 0
        for i in time:
            if i == key:
                found = found + 1
                break
            else:
                index = index +1
        
        if found == 1:
            return amp[index]
        else:
            return 0

    #To enable the object to be treated like arrays ; easily set value in the signal
    def __setitem__(self,key,newval):
        time = list(self.t)
        amp = list(self.x)

        index = 0
        found = 0
        for i in time:
            if i == key:
                found = found + 1
                break
            else:
                index = index +1
        
        if found == 1:
            amp[index] = newval
        else:
            amp[key] = newval

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
        
    #used to draw the plot and display the graph    
    def show(self):
        
        #printing the curve in book notation
        self.draw(self.x,self.t)

        #Setting up visual config for the graph
        CB91_Blue = '#2CBDFE'
        CB91_Green = '#47DBCD'
        CB91_Pink = '#F3A0F2'
        CB91_Purple = '#9D2EC5'
        CB91_Violet = '#661D98'
        CB91_Amber = '#F5B14C'
        color_list = [CB91_Blue, CB91_Pink, CB91_Green, CB91_Amber,CB91_Purple, CB91_Violet]
        plt.style.use(self.style)
        plt.rcParams['font.size'] = 10
        plt.rcParams['axes.labelsize'] = 10
        plt.rcParams['axes.labelweight'] = 'bold'
        plt.rcParams['xtick.labelsize'] = 8
        plt.rcParams['ytick.labelsize'] = 8
        plt.rcParams['legend.fontsize'] = 10
        plt.rcParams['figure.titlesize'] = 12
        plt.figure(facecolor=self.bg_color)

        #Setting up the tittles and x,y lables
        plt.title(self.name,loc=self.titleloc,fontsize=10.3,fontstyle='italic', fontweight='bold')
        plt.ylabel(self.ylabel)
        plt.xlabel(self.xlabel)

        #plotting the signal
        if self.is_descrete == True:
            markerline, stemlines, baseline = plt.stem(self.t,self.x)
            plt.setp(stemlines, linewidth=5, color=self.color2, alpha=self.stem_opacity)     
            plt.setp(markerline, markeredgecolor=self.color1, markerfacecolor=self.color2)  
            plt.setp(baseline,linewidth=1, color=self.color2, alpha=0.6)               
        else:
            plt.plot(self.t,self.x,color=self.color1)  
        
        #Changing color and rendering the image
        plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)
        plt.show() 
    
    def __repr__(self):
        self.show()

    def __str__(self):
        self.show()
        return ""

    def compare(self,obj,obj1=None,obj2=None,obj3=None,obj4=None,spacing=None):
        
        tmp = [obj1,obj2,obj3,obj4]
        c = 2

        CB91_Blue = '#2CBDFE'
        CB91_Green = '#47DBCD'
        CB91_Pink = '#F3A0F2'
        CB91_Purple = '#9D2EC5'
        CB91_Violet = '#661D98'
        CB91_Amber = '#F5B14C'
        color_list = [CB91_Blue, CB91_Pink, CB91_Green, CB91_Amber,CB91_Purple, CB91_Violet]
        plt.style.use(self.style)
        plt.rcParams['font.size'] = 10
        plt.rcParams['axes.labelsize'] = 10
        plt.rcParams['axes.labelweight'] = 'bold'
        plt.rcParams['xtick.labelsize'] = 8
        plt.rcParams['ytick.labelsize'] = 8
        plt.rcParams['legend.fontsize'] = 10
        plt.rcParams['figure.titlesize'] = 12
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
        plt.title(self.name,loc=self.titleloc, fontsize=10.3,fontstyle='italic', fontweight='bold')
        plt.ylabel(self.ylabel)
        plt.xlabel(self.xlabel)
        #plt.grid(color=self.gridcolor,linestyle=self.gridlinestyle)

        if self.is_descrete == True:
            markerline, stemlines, baseline=plt.stem(self.t,self.x)
            plt.setp(stemlines, linewidth=5, color=self.color2, alpha=self.stem_opacity)     
            plt.setp(markerline, markeredgecolor=self.color1, markerfacecolor=self.color2)  
            plt.setp(baseline,linewidth=1, color=self.color2, alpha=0.6) 
        else:
            plt.plot(self.t,self.x,color=self.color1)
        
        plt.subplot(c, 1, 2)
        plt.title(obj.name,loc=self.titleloc, fontsize=10.3,fontstyle='italic', fontweight='bold')
        plt.ylabel(obj.ylabel)
        plt.xlabel(obj.xlabel)
        #plt.grid(color=self.gridcolor,linestyle=self.gridlinestyle)

        if obj.is_descrete == True:
            markerline, stemlines, baseline=plt.stem(obj.t,obj.x)
            plt.setp(stemlines, linewidth=5, color=self.color2, alpha=self.stem_opacity)     
            plt.setp(markerline, markeredgecolor=self.color1, markerfacecolor=self.color2)  
            plt.setp(baseline,linewidth=1, color=self.color2, alpha=0.6) 
        else:
            plt.plot(obj.t,obj.x,color=self.color1)
        
        if obj1 != None:

            self.draw(obj1.x, obj1.t,obj1)

            plt.subplot(c, 1, 3)
            plt.title(obj1.name,loc=self.titleloc, fontsize=10.3,fontstyle='italic', fontweight='bold')
            plt.ylabel(obj1.ylabel)
            plt.xlabel(obj1.xlabel)
            #plt.grid(color=self.gridcolor,linestyle=self.gridlinestyle)

            if obj1.is_descrete == True:
                markerline, stemlines, baseline=plt.stem(obj1.t,obj1.x)
                plt.setp(stemlines, linewidth=5, color=self.color2, alpha=self.stem_opacity)     
                plt.setp(markerline, markeredgecolor=self.color1, markerfacecolor=self.color2)  
                plt.setp(baseline,linewidth=1, color=self.color2, alpha=0.6) 
            else:
                plt.plot(obj1.t,obj1.x,color=self.color1)
        
        if obj2 != None:

            self.draw(obj2.x, obj2.t,obj2)
            plt.subplot(c, 1, 4)
            plt.title(obj2.name,loc=self.titleloc, fontsize=10.3,fontstyle='italic', fontweight='bold')
            plt.ylabel(obj2.ylabel)
            plt.xlabel(obj2.xlabel)
            #plt.grid(color=self.gridcolor,linestyle=self.gridlinestyle)

            if obj2.is_descrete == True:
                markerline, stemlines, baseline=plt.stem(obj2.t,obj2.x)
                plt.setp(stemlines, linewidth=5, color=self.color2, alpha=self.stem_opacity)     
                plt.setp(markerline, markeredgecolor=self.color1, markerfacecolor=self.color2)  
                plt.setp(baseline,linewidth=1, color=self.color2, alpha=0.6) 
            else:
                plt.plot(obj2.t,obj2.x,color=self.color1)

        if obj3 != None:

            self.draw(obj3.x, obj3.t,obj3)

            plt.subplot(c, 1, 5)
            plt.title(obj3.name,loc=self.titleloc, fontsize=10.3,fontstyle='italic', fontweight='bold')
            plt.ylabel(obj3.ylabel)
            plt.xlabel(obj3.xlabel)
            #plt.grid(color=self.gridcolor,linestyle=self.gridlinestyle)

            if obj3.is_descrete == True:
                markerline, stemlines, baseline=plt.stem(obj3.t,obj3.x)
                plt.setp(stemlines, linewidth=5, color=self.color2, alpha=self.stem_opacity)     
                plt.setp(markerline, markeredgecolor=self.color1, markerfacecolor=self.color2)  
                plt.setp(baseline,linewidth=1, color=self.color2, alpha=0.6) 

            else:
                plt.plot(obj3.t,obj3.x,color=self.color1)

        if obj4 != None:

            self.draw(obj4.x, obj4.t,obj4)

            plt.subplot(c, 1, 6)
            plt.title(obj4.name,loc=self.titleloc, fontsize=10.3,fontstyle='italic', fontweight='bold')
            plt.ylabel(obj4.ylabel)
            plt.xlabel(obj4.xlabel)
            #plt.grid(color=self.gridcolor,linestyle=self.gridlinestyle)

            if obj4.is_descrete == True:
                markerline, stemlines, baseline=plt.stem(obj4.t,obj4.x)
                plt.setp(stemlines, linewidth=5, color=self.color2, alpha=self.stem_opacity)     
                plt.setp(markerline, markeredgecolor=self.color1, markerfacecolor=self.color2)  
                plt.setp(baseline,linewidth=1, color=self.color2, alpha=0.6) 
            else:
                plt.plot(obj4.t,obj4.x,color=self.color1)

        plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)
        plt.show()
  
    #To shift and scale a function
    def operate(self,slope=1,intercept=0,):
        
        #Creates a deep copy of the signal(itself) 
        change = copy.deepcopy(self)

        #To change the name and to give the correct notation in the result
        if self.is_descrete == False: 
            #different representation for continuous signal
            if self.domain == 'time':
                if(intercept==0):
                    change.name = self.name+"("+str(slope)+"t)"
                elif(slope==1):
                    change.name = self.name+"(t+"+str(intercept)+")"
                else:
                    change.name = self.name+"("+str(slope)+"t+"+str(intercept)+")"
            else:
                if(intercept==0):
                    change.name = self.name+"("+str(slope)+"s)"
                elif(slope==1):
                    change.name = self.name+"(s+"+str(intercept)+")"
                else:
                    change.name = self.name+"("+str(slope)+"s+"+str(intercept)+")"
        else:
            #different representation for discrete signal
            if self.domain == 'time':
                if(intercept==0):
                    change.name = self.name+"["+str(slope)+"n]"
                elif(slope==1):
                    change.name = self.name+"[n+"+str(intercept)+"]"
                else:
                    change.name = self.name+"["+str(slope)+"n+"+str(intercept)+"]"
            else:
                if(intercept==0):
                    change.name = self.name+"["+str(slope)+"s]"
                elif(slope==1):
                    change.name = self.name+"[s+"+str(intercept)+"]"
                else:
                    change.name = self.name+"["+str(slope)+"s+"+str(intercept)+"]"
        
        #Scaling cannot be negetive, We reverse the signal instead
        if(slope<0):
           
           #reversing the signal
            hh=[]
            for i in change.t:
                hh.append(i*-1)
            change.t=np.array(hh)
            n=len(change.t)
            
            #sorting to recreate the ascending time array
            for i in range(n-1):
                for j in range(0,n-i-1):
                    if(change.t[j]>change.t[j+1]):
                        change.t[j],change.t[j+1]=change.t[j+1],change.t[j]
                        change.x[j],change.x[j+1]=change.x[j+1],change.x[j]

            #extractng the absolute value
            slope=(-1)*slope
        
        #scling or shifting based on the input
        change.t = (change.t/slope)-intercept

        #returning  the new signal
        return change

    #To shift a signal.
    def TimeShift(self,intersept):
        #Calls the operate function and passes on the value
        return self.operate(1,intersept)

    #To scale a signal
    def TimeScale(self,slope):
        #Calls the operate function and passes on the value
        return self.operate(slope,0)

    #To reverse a signal.
    def reverse(self):
        #Calls the operate function and passes on the value
        return self.operate(-1,0)
    
    #To concolve a wiggles type signal with itself
    def convolve(self,n):  

        #To preserve the properties, we copy self
        change = copy.deepcopy(self)
        n = copy.deepcopy(n)

        #Trimming the signal to prevent index calculation error
        change.trim()
        n.trim()

        #perform convolution with self and store it     
        conv_signal = np.convolve(change.x,n.x)

        #Making sure the stating index of both the signals are updated
        self.update_starting_index()
        n.update_starting_index()

        #Modifying the starting indexes
        new_starting_index=self.starting_index+n.starting_index

        #Dealing with unmatching step value and overriding the current signal status
        #By calling the constructor
        new_steps=min(self.steps,n.steps)
        change.__init__(conv_signal,new_starting_index,new_steps)

        #Changing the name to the correct notation and returning the changed waves
        change.name = self.name+"*"+n.name
        return change

    #To compute the even component of a signal
    def even_component(self):
        return (self+self.operate(-1))/2

    #To compute the odd component of a signal
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
            if(self.x[0]==0):
                self.x.pop(0)
                self.t.pop(0)
            else:
                break
        
        for i in range(len(self.x)-1,0,-1):
            if(self.x[-1]==0):
                self.x.pop(-1)
                self.t.pop(-1)
            else:
                break

#Create unit impulse signals easily
class unit_impulse(discrete):

    def __init__(self,length=20,length2=None,step=1):

        #converting everything to positive
        length=abs(length)
        if(length2!=None):
            length2=abs(length2)

        #checking if the positive length is given
        if(length2==None):
            #if not given, the signal is symetrical
            len2=length
        else:
            #else, we override with the given length
            len2=length2

        #building amplitude data for unit impulse
        y=([0]*length)+[1]+([0]*len2)

        #making signal using the amplitude data 'y' using the inherited discrete class
        super().__init__(y,-length*step,step)

#Create unit step signals easily
class unit_step(discrete):

    def __init__(self,length=20,length2=None,step=1):

        #converting everything to positive
        length=abs(length)
        if(length2!=None):
            length2=abs(length2)

        #checking if the positive length is given
        if(length2==None):
            #if not given, the signal is symetrical
            len2=length
        else:
            #else, we override with the given length
            len2=length2

        #building amplitude data for unit step
        y=([0]*length)+([1]*length)

        #making signal using the amplitude data 'y' using the inherited discrete class
        super().__init__(y,-length*step,step)

#Create unit ramp signals easily
class ramp(discrete):

    def __init__(self,length=20,time_step=1,ramp_step=1):
        y=[]
        for i in range(0,length,ramp_step):
            y.append(i)

        super().__init__(y,-length*time_step,time_step)

#Class to build continuous signals
class continuous(discrete):

    #Gets invoked on object creation
    def __init__(self,func=None,signal=None, start=0,stop=1,step=0.001, time=[None], name=chr(random.randint(ord('a'), ord('z')))):
        
        #Changing up the parent class config
        self.is_descrete=False
        self.enable_draw=False

        #Handling the given data and contructing the time array
        if time[0]==None and signal !=None:
            time = np.arange(start,start+len(signal),step)
        elif time[0]==None:
            time = np.arange(start,stop,step)
        
        #Generating wave from the supplied function
        temp=[]
        if func==None and signal==None:
            print('\033[91m'+'Error: Either refer to a function or supply a signal !'+'\033[0m')
        elif func!=None and signal==None:
            for i in time:
                out = func(i)

                if type(out) in [symnum.Infinity,symnum.ComplexInfinity,symnum.NegativeInfinity]:
                    out = np.inf
                elif type(out) in [symfun.DiracDelta]:
                    out = 1
                try:
                    out = float(out)
                except:
                    out = np.nan

                temp.append(out)
            signal=temp

        #Calling the parent class to construct the signal
        super().__init__(signal, start, step, time, name)

#Class to build continuous signals in frequency domain
class continuous_fdomain(discrete):

    #Gets invoked on object creation
    def __init__(self,func=None,signal=None, start=0,stop=1,step=0.001, time=[None], name=chr(random.randint(ord('a'), ord('z')))):
        
        #Changing up the parent class config
        self.is_descrete=False
        self.enable_draw=False
        self.domain = 'frequency'

        #Handling the given data and contructing the time array
        if time[0]==None and signal !=None:
            time = np.arange(start,start+len(signal),step)
        elif time[0]==None:
            time = np.arange(start,stop,step)
        
        #Generating wave from the supplied function
        temp=[]
        if func==None and signal==None:
            print('\033[91m'+'Error: Either refer to a function or supply a signal !'+'\033[0m')
        elif func!=None and signal==None:
            for i in time:
                out = func(i)
                if type(out) in [symnum.Infinity,symnum.ComplexInfinity,symnum.NegativeInfinity]:
                    out = np.inf
                elif out == symfun.DiracDelta(0):
                    out = 1
                try:
                    out = float(out)
                except:
                    out = np.nan

                temp.append(out)
            signal=temp

        #Calling the parent class to construct the signal
        super().__init__(signal, start, step, time, name)

#Class to build discrete signals in frequency domain
class discrete_fdomain(discrete):

    def __init__(self, signal, start=0, step=1, time=[None], name=chr(random.randint(ord('a'), ord('z')))):
        self.domain='frequency'
        super().__init__(signal, start, step, time, name)

#Class to create a wiggles type array, can be evaluated with wiggles type signals
class array(discrete):
    def __init__(self, signal, start=0, step=1, time=[None], name="arr"+str(random.randint(0,100))):
        super().__init__(list(signal), start, step, time, name)

#Class to create a wiggles type discrete array, can be evaluated with wiggles type signals
class darray(array):
    def __init__(self, signal, start=0, step=1, time=[None], name="arr" + str(random.randint(0, 100))):
        super().__init__(signal, start, step, time, name)

#Class to create a wiggles type continuous array, can be evaluated with wiggles type signals
class carray(continuous):
    
    def __init__(self,signal=None, start=0, stop=1, step=0.001, time=[None],func=None,name="arr" + str(random.randint(0, 100))):
        super().__init__(func, list(signal), start, stop, step, time, name)

