from wiggles import signals as sp

#building amplitude data for Ramp
length = 20
y=[]
for i in range(length):
    y.append(i)

#making signal using the amplitude data 'y' using wiggles and displaying it
unitimpulse=sp.discrete(y)
unitimpulse.name="Ramp"
unitimpulse.show()
