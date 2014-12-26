import string

def get3plus():
	sum = 0
	i = 0
	for n in range (1000):
		while n == 3*i:
			sum = sum+n
			i = i+1
			print (sum)
	return sum
def get5plus():
	sum = 0
	i = 0
	for n in range (1000):
		while n == 5*i:
			sum = sum + n
			i = i+1
			print (sum)
	return sum
def get15plus():
        sum = 0
        i = 0
        for n in range (1000):
                while n == 15*i:
                        sum = sum + n
                        i = i + 1
                        print (sum)
        return sum

def Fibonacci(n):
        a,b = 1,2
        sum = 0
        while b < n:
                if b%2 == 0:
                        sum = sum + b
                a,b = b,a+b
                print (sum),
        return sum

def LargestPrimeFactor(n):
        i = 2
        while i*i <= n:
                if n % i == 0:
                        n = n/i
                        print (i,n)
                        i = 1
                i = i+1

def Palindrome(n):
        i,j,p = 1,1,0
        pstr = ''
        m = 0
        final = 0
        while i < n:
                while j < n:
                        p = i * j
                        j = j + 1
                        m = 0
                        pstr = str(p)
                        if len(pstr)%2 == 1:
                                continue
                        for k in range(len(pstr)/2):
                                if pstr[k] != pstr[len(pstr)-k-1]:
                                        m = 0
                                        continue
                                        
                                else:
                                        m = m + 1
                                        if m == len(pstr)/2:
                                                m = 0
                                                if final < p:
                                                        final = p
                                                        print (p,i,j-1)
                                                continue
                                        
                i = i + 1
                j = i

def SmallestMultiple(n):
        i,j = 1,2
        f = 1
        while i <= n:
                while j < i:
                        if f % i != 0:
                                f = f* i
                        if i%j == 0:
                                f = f / j
                                print (f)
                        j = j +1
                j = 2
                i = i + 1

def learnPy():
        for num in range(2,10):
                if num%2 ==0:
                        print ("Found an even number ", num)
                        continue
                print ("Find a number ", num)
        print 2 ** 6
        
if __name__ == "__main__":
	#a = get3plus()
	#b = get5plus()
	#c = get15plus()
        #d = Fibonacci(4000000)
	#print(a+b-c)
        #print (d)
        #LargestPrimeFactor(10)
        #Palindrome(1000)
	#SmallestMultiple(10)
        learnPy()

