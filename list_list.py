

def list_list(input_list, elements_per_inner_list):
    # Check if the input list can be evenly divided into inner lists
    if len(input_list) % elements_per_inner_list != 0:
        raise ValueError("Input list length is not divisible by elements_per_inner_list")
    
    # Create a list of lists
    list_of_lists = []
    for i in range(0, len(input_list), elements_per_inner_list):
        inner_list = input_list[i:i + elements_per_inner_list]
        list_of_lists.append(inner_list)
    
    return list_of_lists


