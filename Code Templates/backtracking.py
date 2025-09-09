def backtrack(curr, OTHER_ARGUMENTS...):
    # Step 3: Check for a Solution (Base Case)
    if (BASE_CASE):
        # modify the answer (save or count a solution)
        return
    
    ans = 0
    # Step 5: Try Next Option
    for (ITERATE_OVER_INPUT):
        # Step 1: Choose
        # modify the current state (make a choice)

        # Step 2: Explore
        ans += backtrack(curr, OTHER_ARGUMENTS...)

        # Step 4: Un-choose (Backtrack)
        # undo the modification of the current state
    
    return ans




