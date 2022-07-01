# while and for loops are in it

# While loop
x=0
while(x<10):
    print(x)
    x=x+1



# For loop
for x in range(12,23):
    print(x)


# Fuctions in loop
days=["mon","tue",'wed',"thrus","fri","sat","sun"]
for d in days:
    if d=="fri":break      #Break is used for stop
    elif d=="tue":continue #continue is use for skip
    print(d)