"""
Input: N = 6, Sum = 12
Output: 2.00
Divisors of N are {1, 2, 3, 6}
Sum of inverse of divisors is equal to (1/1 + 1/2 + 1/3 + 1/6) = 2.0
Input: N = 9, Sum = 13
Output: 1.44
-----------------------------------------------------------------------
def SumofInverseDivisors( N, Sum):

    # Calculating the answer
    ans = float(Sum)*1.0 /float(N);

    # Return the answer
    return round(ans,2);


# Driver code
N = 9;
Sum = 13;
print SumofInverseDivisors(N, Sum);

# This code is contributed by CrazyPro
"""
class sample():
    def add(self,x,y):
        return x+y


class Advanced(sample):
    def Inverse(self, x, y):
        return (1 / sample.add(self, x, y))

obj=sample()
sum=obj.add(2,3)
print(sum)
obj_=Advanced()
inverse=obj_.Inverse(2,3)
print(inverse)