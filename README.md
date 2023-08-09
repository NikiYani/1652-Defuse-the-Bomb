# 1652. Defuse the Bomb

You have a bomb to defuse, and your time is running out! Your informer will provide </br>
you with a circular array code of length of n and a key k. </br>

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously. </br>

If k > 0, replace the ith number with the sum of the next k numbers. </br>
If k < 0, replace the ith number with the sum of the previous k numbers. </br>
If k == 0, replace the ith number with 0. </br>
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1]. </br>

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb! </br>

## Example 1:

Input: code = [5,7,1,4], k = 3 </br>
Output: [12,10,16,13] </br>
Explanation: Each number is replaced by the sum of the next 3 numbers. </br>
The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around. </br>

## Example 2:

Input: code = [1,2,3,4], k = 0 </br>
Output: [0,0,0,0] </br>
Explanation: When k is zero, the numbers are replaced by 0. </br>

## Example 3:

Input: code = [2,4,9,3], k = -2 </br>
Output: [12,5,6,13] </br>
Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the </br>
numbers wrap around again. If k is negative, the sum is of the previous numbers. </br>

## Constraints:

n == code.length </br>
1 <= n <= 100 </br>
1 <= code[i] <= 100 </br>
-(n - 1) <= k <= n - 1 </br>
