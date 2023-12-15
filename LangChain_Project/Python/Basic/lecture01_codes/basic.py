import copy
#range(start, stop, step)
# start and step are optional
# stop is exclusive
for i in range(1,10,3):
	print(i)

original = [["I","am","the","original","one"],[1,2,3,4,5]]

shallow = copy.copy(original)
 
print(shallow)

shallow[0][0] = "You"
shallow[0][1] = "are"

print(original)