'''
Linear correlation program
'''
def find_corr_x_y(x,y):
    
    if len(x) != len(y):
        print('The two sets of numbers are of  unequal size')
        return None
    n = len(x)

    # find the sum of the products
    prod = [xi*yi for xi, yi in zip(x, y)]
    sum_prod_x_y = sum(prod)

    # sum of the numbers in x
    sum_x = sum(x)
    # sum of the numbers in y
    sum_y = sum(y)

    # square of the sum if the numbers in x
    squared_sum_x = sum_x**2
    # square of the sum if the numbers in y
    squared_sum_y = sum_y**2

    # find the squares of numbers in x and the sum of the squares
    x_square = [xi**2 for xi in x]
    x_square_sum = sum(x_square)

    # find the squares of numbers in y and the sum of the squares
    y_square = [yi**2 for yi in y]
    y_square_sum = sum(y_square)

    # numerator
    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    denominator = (denominator_term1*denominator_term2)**0.5
    correlation = numerator/denominator

    return correlation
    
    corr = find_corr_x_y(x,y)
    if not corr:
        print('Correlation could not be calculated')
    else:
        print('The correlation coefficient between x and y is {0}'.format(corr))