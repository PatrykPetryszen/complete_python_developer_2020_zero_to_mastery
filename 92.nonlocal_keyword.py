# def outer():
#     x = 'local'
#     def inner():
#         nonlocal x # it changes previously defined x to 'nonlocal' string, Try not to use this
#         x = 'nonlocal'
#         print('innter:', x)
#
#     inner()
#     print('outer', x)
#
# outer()

#We use local variables to don't waste CPU of the hypervisor. Once the function is done the python interpreter puts all the used variables to the bin.

x = "Hello"[0]

print(x)
