from wiggles import signals as sp

#making a test signal
x = sp.discrete([-1,8,-3,4],0)
x.name="x"

#Finding the component and displaying the result
component = x.even_component()
component.name = "Even Component"
x.compare(component)
