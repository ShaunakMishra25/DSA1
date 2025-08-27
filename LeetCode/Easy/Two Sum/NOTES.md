
          # Two Sum

          **Summary:** This algorithm uses a hash map (dictionary in Python) to efficiently find two numbers in a list that add up to a target value. It iterates through the input list `nums`. For each number, it calculates the complement needed to reach the target. It then checks if the complement exists as a key in the hash map. If found, it means the pair is found, and their indices are returned. Otherwise, the number and its index are added to the hash map and the iteration continues.

          - Time Complexity: O(n) because the algorithm iterates through the input list once. Hash map lookups and insertions take O(1) on average.
          - Space Complexity: O(n) because in the worst case, the hash map may store all the numbers from the input list.
          