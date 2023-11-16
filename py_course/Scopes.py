'''
GLOBAL VARIABLE     GLOBAL SPACE    LOCAL SPACE                       NON LOCAL SPACE

Initialization      possible        possible(Global keyword)          possible(Global keyword)   
Fetch               possible        possible                          possible
Reinitialization    possible        possible(Global keyword)          possible(Global keyword)
Delete              possible        possible(Global keyword)          possible(Global keyword)

def fact(n,factt=1):
    if n==0:
        return factt
    factt*=n
    # print(factt)
    return fact(n-1,factt)
fact(5)
'''
'''
print (globals())
x=10
print(x)
print(globals())
x=30
print(x)
print(globals())
del(x)
print(globals())'''
#---
x=10
print(globals())
def sample():
    #print(x)
    print(locals())
    x=20
    print(x)
    print(locals())
sample()
'''
LOCAL VARIABLES:
.These are the variables defined or created inside the function area/nested function area known as local variables.
.We can access,modfy,delete,create the local variables in that functon.
.When the control enters the function area/method area then it executes those statements.These variables will be created once the function call is done.
(Variables life scope will start the function execution and once after function execution is done then variable scope is deallocated).
These variables will be deleted once the control comes out of the function area/method area.
.We can access local variables inside child functions (nested functions) but it is not possible to modify modify local variables inside nested function
.To overcome the above problem,we make use of nonlocal keywords.
.By using nonlocal keyword, we can get permission from the non-local space to manipulate the non-local variable in local space.

SYNTAX:
def hello():
        var1,var2,var3,...varn=val1,val2,val3,...valn
           #all these variables are valled as local variable
hello()

.When the control reaches the function area. all statements are executed one by one.
 If in case any variables are present, that variables will be created inside the function space.
'''
'''

NON-LOCAL VARIABLES:

.If we want to access the local variables in nested function directly we can do and the nested function is allowed. But if we want to modify or delete it, then it will not allow.
.Still if we want to modify. delete the local variables in nested functons then we are using a NONLOCAL keyword.

SYNTAX:

def outer(args):
    var1,var2,var3,...varn=val1,val2,val3,...valn
    def inner(args):
        nonlocal var1,var2,...varn

    inner(args)
outer(args)

Note:
Once we specify the variable as a nonlocal then the modification and deletion of it will affect the local function area only.
'''
'''
LOCAL VARIABLE          GLOBAL SPACE        ENCLOSED/LOCAL SPACE        non-LOCAL SPACE

1.Initialization          Impossible          Possible                    Impossible
2.Fetch                   Impossible          Possible                    Possible
3.Reinitialization        Impossible          Possible                    Possible(nonlocal keyword)
4.Delete                  Impossible          Possible                    Possible(nonlocal keyword)

-------------------------------------------------------------------------------------------------------

LOCAL VARIABLE          GLOBAL SPACE        ENCLOSED/LOCAL SPACE         non-LOCAL SPACE

1.Initialization          Impossible          Impossible                    Possible
2.Fetch                   Impossible          Impossible                    Possible
3.Reinitialization        Impossible          Impossible                    Possible
4.Delete                  Impossible          Impossible                    Possible

'''
'''
NOTE:
If we want to carry to the local variable value from local space to Global space we have to use 'return' keyword

'''
'''
def sample():
    x=32 #local variable
    print(x)
    return x #carry the local variable value from local space to Global space
x=sample() #local value is initialize inside th global
print(x)

-----------------------
def outer():
    def inner():
        m=145 #local variable
        print(m)
        return m #carry the local variable value from  nested local space to global space
    inner()
outer()

-------------------
def outer():
    def inner():
        m=145 #local variable
        print(m)
        return m #carry the local variable value from  local space to enclosed space
    y=inner()
    print(y) #local vlaue is intialize inside the enclosed space
outer()

------------------------
def outer():
    def inner():
        m=145 #local variable
        print(m)
        return m #carry the local variable value from  nested local space to global space
    return inner()
    inner()
res=outer() #nested local value is intialize inside the global space
print(res)

'''