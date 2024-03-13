### Q6 🥺
Consider the problem of given an integer n, generating all possible permutations of the numbers {1, 2, . . . , n}. Provide a <mark style="background: #FF5582A6;">recursive</mark> algorithm for this problem.

```Python
# current: the position of current manipulate element

l = [1,2,3,4 ......]

def helper(current, end):
	if current == end:
		print(l) 
	else:
		for i in range(current,end+1):
			l[current], l[end] = l[end], l[current]  
			helper(current,end)
			l[current], l[end] = l[end], l[current] 

helper(0, len(l)-1)  
```


### Q7 😅
Consider the problem of given an integer n, generating all possible permutations of the numbers {1, 2, . . . , n}. Provide a non-recursive algorithm for this problem using a <mark style="background: #FF5582A6;">stack</mark>.


Hint : <mark style="background: #FF5582A6;">push/pop</mark>  <=> <mark style="background: #FFF3A3A6;">invoke/return</mark>

```Python
def helper(n):
	stack.push("start",0,0)
	l = [1,2,3,4,5 ...... n]
	while stack:
		status,current,i = stack.pop()
		if status == "start":
			if current == n-1:
				print(l)
			else:
				l[current], l[i] = l[i], l[current] 
				
				stack.push("finish",current,i)
				
				# actually is a fuckin new invoke!!!!!
				stack.pop("start",current+1,i+1) 

				
		if status == "finish":
			l[current], l[i] = l[i], l[current] 
			if i < n-1:
				# actually next iteration
				stack.push("start",current,i+1)
		
```

