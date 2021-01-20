
def insertion_sort(items):
	list_items=items
	
	for i in range(0,len(list_items)):
		
		if i == list_items.index(list_items[-1]):
			break

		elif list_items[i] > list_items[i+1]:

			counter = i

			while counter != 0 :
				
				if list_items[i+1] > list_items[counter-1]:
					list_items.insert(counter,list_items[i+1])
					list_items.pop(i+2)
					break

				else :
					counter = counter - 1

			if counter == 0:
				list_items.insert(0,list_items[i+1])
				list_items.pop(i+2)

	return list_items




mylist=[9,8,0,5,3,2,8]

print(insertion_sort(mylist))








