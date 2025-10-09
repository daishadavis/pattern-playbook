# Problem: Decode ways 

**Pattern / Category:1-DP**

**Notes:**
- The goal of this problem is to count how many ways we can decode a string 
- dfs(i) means how many ways can we decode the substring start at index i 
- We have two choices at position i we can take one digit only if its between 1 and 9 and not 0 or take two if the digit is greater than 10 but less than 26 (recurrence relation )
- 


**Mini-Template (Core logic):
```

```

**Complexity:**
 - Time: O(n)
 - Space: O(n)