x = 2020 
y = x //1000 
y1 = (x - y*1000)//100 
y2 = (x - y*1000 - y1*100)//10 
y3 = x - y*1000 - y1*100 - y2*10 

print(y+y1+y2+y3) 