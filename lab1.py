
def max_list_iter(int_list):  # must use iteration not recursion
    if int_list == []:
        return None
    if int_list == None:
        raise ValueError      # empty list raises value error
    max_int = int_list[0]     # default value of maximum is the first item in the list
    for i in int_list:        # iterating through list
        if i > max_int:       # checking if value is greater than current max value 
            max_int = i
    return max_int            
   
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    

def reverse_rec(int_list):   # must use recursion
    if int_list == None:
        raise ValueError     # None list raises value error
    if len(int_list) == 0:     
        return []            # when fully reversed, an empty list is returned
    return [int_list[-1]] + reverse_rec(int_list[:-1]) # takes the last value in the list, then adds it to the reverse function of the rest of the list
       
   
   
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    

def bin_search(target, low, high, int_list):  # must use recursion
   
    if int_list == []:
        return None                # empty list raises value error
    if low > high:
        raise ValueError           # if low > high, is illogical and raises value error
    if int_list == None:
        raise ValueError
    m = (low + high) / 2           # sets midpoint/floor of the list
    if int_list[int(m)] == target: # if target is found, returns index
        return m
    if int_list[int(m)] > target:  # if target is less than midpoint value, recursion restarts search in 2nd half of given list
        bin_search(target, low, high / 2, int_list)
    if int_list[int(m)] < target:  # if target is greater than midpoint value, recursion restarts search in 2nd half of given list
        bin_search(target, low + high / 2, high, int_list)
    
   
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    
