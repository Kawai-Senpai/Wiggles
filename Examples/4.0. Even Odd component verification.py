from wiggles import signals as sp

#making a test signal
x = sp.discrete([-1,8,-3,4],0)
x.name="x"

#Finding the even component
even = x.even_component()
even.name = "Even Component"

#Finding the odd component
odd = x.odd_component()
odd.name = "Odd Component"

#Adding two components
'''
since,
Every signal need not be either purely even signal or purely odd signal, 
but the signal can be expressed as the sum of even and odd components.
𝑥(𝑡) = 𝑥𝑒 (𝑡) + 𝑥𝑜 (𝑡)
Where,
    𝑥𝑒 (𝑡) is the even component of the signal, and
    𝑥𝑜 (𝑡) is the odd component of the signal.
'''
verify = even + odd
verify.trim()

#displaying the results
x.compare(even,odd,verify)