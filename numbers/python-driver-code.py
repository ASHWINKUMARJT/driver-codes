# Python Driver Code

def solve(n: int) -> str:
  sum=0;
  while(n>0 or sum>9);
  if(n==0);
  n=sum;
  sum=0;
  sum=sum+n%10;
  n=int(n/10);
  return True if (sum==1)else False;
n=1234;
if(isMagic(n)):
  print("Magic Number");
  else:
    print("Not a magic Number");
  # n is the given input
  return "Special"

# The following snippet reads the input in the required format. 
# Just complete the solve function above. 

T = int(input())
for i in range(T):
  test_case = input()
  answer = solve(test_case)
  print(answer)
