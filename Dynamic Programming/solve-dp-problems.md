# Steps to solve DP Problems:
- Find the recurrence relation 
    - A recurrence relation describes the answer to our problem in terms of answers to the same problem with smaller inputs
- Identity base cases
    - Think empty or small here: empty strings, empty arrays, 0, or 1. Another way of thinking about dp(0) for our problem is: "how much treasure can we collect if the treasure array is empty?"
- Write the recursive solution 
- Convert to "Bottom up" DP
- Further Optimization 

# General Tips for Identifying Optimial Structure:
- Assume you already know the answer r a smaller version of the input. Then see if you can se that information to solve the problem for a larger input.
- If the input is an array, assume you have the answer  the first few elements in the array. If the input is a string, assume you have the answer for the first few characters.
if the input is a number, assume, you have an answer for a smaller number etc.


# Recurrence Relation:
- 