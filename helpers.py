def split_cell_type(x, mode):
    """ Split cell of dataframe which contains 
        Input:
            x: string, which contains type of cell
            mode: number, determines what value to return after processing 
        Output:
            string which contains type of cell or bin
    """
    list_x = x.split(":")
    if mode == 1:
        return list_x[0]
    else: 
        return list_x[1]
    
def define_undefferentiated(x):
    """ Determines if a cell is undifferentiated
        Input:
            x: string, which contains type of cell
        Output:
            True if type of cell contains substring "undifferentiated"
            False if type of cell doesn't contain substring "undifferentiated"
    """
    if x.split('_').count('undifferentiated') > 0:
        return True        
    else:
        return False 
    
def fill_zeros(key, value, mode, dictionary):
    """ Fill empy values of dictionary of timebins for particular cell type
        Input:
            key: key of dictionary which means not empty key
            value: the value to which the zeros in the dictionary should be replaced
            mode: number, determines in which direction should iterate dictionary 
            dictionary: dictionary of timebins
        Output:
            filled dictionary of timebins
    """
    if mode == 0:
        for k in dictionary:
            if k == key:
                break
            if dictionary[k] == 0.0:            
                dictionary[k] = value
    else:
        for k in reversed(dictionary):
            if k == key:
                break
            if dictionary[k] == 0.0:            
                dictionary[k] = value
    return dictionary