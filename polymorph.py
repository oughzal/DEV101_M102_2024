from multipledispatch import dispatch

@dispatch(int,int) 
def test(a,b): return f"int {a}, {b}"
@dispatch(float,float) 
def test(a,b): return f"float {a}, {b}"
@dispatch(str,str) 
def test(a,b): return f"str {a}, {b}"
@dispatch(object,object) 
def test(a,b): return f"autre {a}, {b}"

print(test(1,2))
print(test(1.0,2.0))
print(test("1.0","2.0"))
print(test(1,"2.0"))
