"""You are given two lists, one containing key and the other containing values. Write a Python 
function that creates a dictionary from the two lists. (keys = ['name', 'age', 'city'] values = 
['Alice', 25, 'New York'])"""
def dictionary(list1,list2):
    return dict(zip(list1,list2))
keys_list=['name', 'age', 'city']
values_list=['Alice', 25, 'New York']
result=dictionary(keys_list,values_list) 
print(result)   
