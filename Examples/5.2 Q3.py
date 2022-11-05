import wiggles.signals as sp

#Generating wiggles wave using the given amplitude data
x=sp.discrete([1,2,3,4,5,6,7,6,5,4,3,2,1],-2)
x.name="x"

#Operation 1
x1=(2*x.TimeShift(-5))-(3*x.TimeShift(4))
x1.name="operation 1"

#Operation 2
x2=x.operate(-1,3)+(x*x.TimeShift(-2))
x2.name="operation 2"

#Displaying the result
x.compare(x1,x2)


