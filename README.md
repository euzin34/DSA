# DSA
DSA problems
<br>
Q1 Minimum Operations to Reduce X to Zero
<br>
Explanation:You are given an integer array a of length n and an integer x.

In one operation, you can remove the leftmost or rightmost element from the array. The value of the removed element is then subtracted from x.

Your goal is to perform a minimum number of such operations so that x becomes exactly 0. If it's not possible, print −1.

Note: The removed elements no longer appear in the array for future operations.
Input Format:The first line contains two integers n and x(1 ≤ n ≤ 10^5 , 1 ≤ x ≤ 10^9 ) --- the size of the array and the target value.

The second line contains n integers a1,a2, …,an (1 ≤ ai ≤ 10^4 ) --- the elements of the array.
Output Format: Print a single integer --- the minimum number of operations to make x exactly zero, or −1
if it is not possible.
