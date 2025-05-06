def product_of_array_except_self(array):
    result = [1 for i in range(len(array))]
    prefix_product = 1
    for i in range(len(array)):
        result[i] = prefix_product
        prefix_product*=array[i]
    postfix_product = 1    
    for i in range(len(array)-1,-1,-1):
        result[i]*= postfix_product
        postfix_product *= array[i]
    return result    

print(product_of_array_except_self([-1,1,0,-3,3]))