"""
Ada's Stats Module

A collection of functions for doing some basic statistics on your data.
This is an INDIVIDUAL project. Do not consult with others or share code.
Refer to the instructions on Canvas for more information.
"""

# 0) Question and Results
QUESTION = "How many days did you work out last week?"
ANSWERS = [0,0,0,1,2,2,3,3,3,4,5,5,5,5,7,7]
# 1) count
def count(numbers):
    count=0
    for i in numbers:
        count+=1
    return(count)

# 2) summate
def summate(numbers):
    sum=0
    for i in numbers:
        sum+=i
    return(sum)

# 3) mean
def mean(numbers):
    sum=0
    sum=summate(numbers)
    countboi=count(numbers)
    if countboi==0:
        return None
    average=sum/countboi
    return round(average,2)

# 4) square
def square(numbers):
    squaredbois=[]
    for i in numbers:
        ok=i*i
        squaredbois.append(ok)
    return squaredbois

# 5) standard_deviation
def standard_deviation(numbers):
    length= count(numbers)
    if length<2:
        return None
    total=summate(numbers)
    total_squared=square(numbers)
    sum_squared=summate(total_squared)
    divided_by_count=sum_squared/length
    diff=sum_squared-divided_by_count
    return (((sum_squared)-((total)*(total))/(length))/(length-1))**.5

    # use n instead of (n-1) if want to compute the exact variance of the given data
    # use (n-1) if data are samples of a larger population
#return variance
# 6) main function
# The following code can be used to try out your functions.
# Uncomment each line as you implement the functions to try them out.
# When you have implemented each function, copy the output from the
#   console into a comment below.
def main(question, results):
    print("We asked", count(results), "people the following question.")
    print(' "'+question+'"')
    print("Here are the statistical results:")
    print("\tSum:", summate(results))
    print("\tMean:", mean(results))
    print("\tStandard Deviation:", standard_deviation(results))


if __name__ == "__main__":
    main(QUESTION, ANSWERS)
