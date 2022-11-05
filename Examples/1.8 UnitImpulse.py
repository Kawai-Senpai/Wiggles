from wiggles import signals as sp

#building amplitude data for unit impulse
length = 20
y=([0]*length)+[1]+([0]*length)

#making signal using the amplitude data 'y' using wiggles and displaying
unitimpulse=sp.discrete(y,-length)
unitimpulse.name="Unit Impulse"
unitimpulse.show()
