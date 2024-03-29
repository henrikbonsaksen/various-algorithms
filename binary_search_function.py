
def binarySearch(alist, item):
	    first = 0
	    last = len(alist)-1
	    found = False
	
	    while first<=last and not found:
	        midpoint = (first + last)//2
	        if alist[midpoint] == item:
	            found = True
	        else:
	            if item < alist[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1
	
	    return found

testlist = [2000, 1996, 1994, 1989, 1969, 1952, 1945]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))