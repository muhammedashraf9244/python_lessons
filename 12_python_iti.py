'''
Learn:
    - sum() , round() ,range()
    - change pritn output 
    - abs() , pow() , min() , max() , slice()
'''

'''
sum(iterable,start) if not start reurtn sum iterable else return sum iterable + start
round(n, ndigits) return the nearer number of n and ndigit the number of numbers after float point
range(start,end,step) make range number from start to end-1 and defalut step is 1 
'''
# sum(iterable, start)
a =[1,2,3]
print(sum(a,50))
b=253.564
print(round(b,2))
# range
print(list(range(10,2)))  # number from 0 to 9 and setp is 2

'''
change print out 
print(str,sep=sep_char) separtor is defalut space
print(str,end=end_char) defalut of print is \n to change git end with value 
'''
print('Hello' ,'world', 'in' ,'python',sep="_")  # print as snake_case
print('First line',end=" ")  # change defalut print 
print('Second line')
print('_'*50)
# abs(number) Return the absolute value of the argument. 
print(f" abs 100 => {abs(100)}")
print(f" abs -100 => {abs(-100)}")
# pow(base,exp,mod) == **
print(pow(2,4)) # 2 * 2 *2 *2 == 2**4
print(pow(2,4,10)) # 2 * 2 * 2 * 2 = 16#10 = 6
# min (item,item or iterator)
l =[0,20,10]
print(min(1,2,3))
print(min(l))
# max (iteam , item iterator )
print(max(1,2,3))
print(max(l))

# slice(start,stop,step)  must be pass stop 
A = ["A","B","C","D","E"]
print(A[:4]) 
print(A[slice(4)])