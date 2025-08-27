1. Two Sum
Solved
Easy
Topics
Companies
Hint

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]


Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
18,529,535/33M
Acceptance Rate
56.2%
Topics
Array
Hash Table
Companies
Hint 1
A really brute force way would be to search for all possible pairs of numbers but that would be too slow. Again, it's best to try out brute force solutions just for completeness. It is from these brute force solutions that you can come up with optimizations.
Hint 2
So, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y which is value - x where value is the input parameter. Can we change our array somehow so that this search becomes faster?
Hint 3
The second train of thought is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?
Similar Questions
3Sum
Medium
4Sum
Medium
Two Sum II - Input Array Is Sorted
Medium
Two Sum III - Data structure design
Easy
Subarray Sum Equals K
Medium
Two Sum IV - Input is a BST
Easy
Two Sum Less Than K
Easy
Max Number of K-Sum Pairs
Medium
Count Good Meals
Medium
Count Number of Pairs With Absolute Difference K
Easy
Number of Pairs of Strings With Concatenation Equal to Target
Medium
Find All K-Distant Indices in an Array
Easy
First Letter to Appear Twice
Easy
Number of Excellent Pairs
Hard
Number of Arithmetic Triplets
Easy
Node With Highest Edge Score
Medium
Check Distances Between Same Letters
Easy
Find Subarrays With Equal Sum
Easy
Largest Positive Integer That Exists With Its Negative
Easy
Number of Distinct Averages
Easy
Count Pairs Whose Sum is Less than Target
Easy
Discussion (1.5K)
Choose a type
Comment
💡 Discussion Rules

1. Please don't post any solutions in this discussion.

2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.

3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.

Sort by:Best
Vinay Kumar pat
Apr 09, 2019

Hello all,

I'm new coding and noob in using classes. why no one is writing int main() in their codes. Definetly there will be different versions in the main() i.e taking input from STDIN, passing arguments to class etc.

 
839
Show 76 Replies
Reply
AlgoEngine
Apr 29, 2023

Video visualizing how a hash table can reduce the runtime from O(n^2) to O(n):

 
Read more
468
Show 12 Replies
Reply
winstonchi
Mar 10, 2016

In interview, I was asked what if duplicates exists.. How do we handle this?
My original thought is worst case nums = [1,1,1,1] target is 2
then the complexity if N^2... Is it true?
Is there any way to improve this?

 
277
Show 51 Replies
Reply
CafogarN4
May 24, 2024

Not that easy

 
198
Show 7 Replies
Reply
AlexTheGreat
Nov 04, 2014

Can't find a better place to ask this...
Every time I passed a problem, it's marked with a green check mark.
If I want to redo all the problems for the second round, is there a way to "reset" all the marks?

 
165
Show 17 Replies
Reply
Xu ZHANG
May 13, 2016

We can see a lot of HashMap solutions using a HashMap to store the number as the key and the index as the value.

Many people will come up the same questions that what if there have duplicate numbers in the array?

Well, it's not a problem at all. Because in the description, it says there is exactly one solution. I will prove it here:

Say we have three N1 in the array like this [N1, N2, N1, N3, N1], then N1 will not be part of the result with N2 or N3, since if N1 is part of the result, then we have three solutions which go against the description. N1 cannot be part of result with itself neither since then we have three solutions again. So in this case, we do not care duplicates at all.

So the only possible situation that the N1 can be the result is: N1 MUST only have two of them, and the target MUST be 2 * N1, then we have an array like this: [N1, N2, N1], and a target like this 2 * N1. In this case, after building up the map, N1's index will be the right most one which is 2. Then when we start from the first N1 at index 0, we do (target - N1) and get N1, and then query the N1's index in the array, which is 2, and then we can get the result which is [0, 2] with no problem.

 
Read more
141
Show 7 Replies
Reply
CodeBumblebee
Jun 11, 2024

this is easy? im cooked

 
Feedback
90
Show 2 Replies
Reply
Ming Yue
Jan 15, 2014

O(n^2) I got Time Limit Exceed. Does anyone got accept by O(n^2) ? I just use binary search and finally accept.

 
58
Show 24 Replies
Reply
shaguv
Feb 01, 2015

Sorry for the newbie question: is there any way to read the test cases for a given problem? Even after having validated it, I couldn't find how to access them.

PS: At the moment of posting this general question, I realize I need to assign it a particular problem as a category. So I guess this is the wrong place to ask. Could you redirect me to some "meta" forum?

 
78
Show 1 Replies
Reply
Mikhail Lachikhin
Nov 19, 2019

Hello there. This is my first time solving problems on leetcode and I ran into a problem. The output of my code is [0, 1], and the output expected is [0,1]. But yet, site says im wrong. Also I see my output in "stdout", not in the "Output" line. I used "print()" method for output. How should I do it instead? image

 
68
Show 17 Replies
Reply
1
2
3
4
5
6
153
Copyright © 2025 LeetCode. All rights reserved.