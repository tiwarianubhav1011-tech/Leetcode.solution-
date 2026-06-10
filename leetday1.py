# problem title :  Reverse Integer (med)
'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x 
causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
Constraints:
-231 <= x <= 231 - 1'''
def reverse( x):
        """
        :type x: int
        :rtype: int
        """
        # 1. Handle the sign
        sign = -1 if x < 0 else 1
        
        # 2. Reverse the absolute value as a string
        string = str(abs(x))
        reversed_int = int(string[::-1]) 
        
        # 3. Manual 32-bit overflow check
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
            
        return (reversed_int*sign)
  
testcases = [123,-123,120,1560000000000000001]
outputs_expected= [321,-321,21,0]
output_came=[]
for testcase in testcases :
    out_put = reverse(testcase)
    output_came.append(out_put)
  
if output_came ==  outputs_expected :
     print("well done all test cases passed") 
else:
     print('recheck')  

# note :
# use both cde seperatly
# =========================
# question 2 problem name : String to Integer (atoi) (med)

'''Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
The algorithm for myAtoi(string s) is as follows:
Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
Example 1:
Input: s = "42"
Output: 42
Explanation:
The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
Step 2: "42" (no characters read because there is neither a '-' nor '+')
Step 3: "42" ("42" is read in)
Example 2:
Input: s = " -042"
Output: -42
Explanation:
Step 1: "   -042" (leading whitespace is read and ignored)
Step 2: "   -042" ('-' is read, so the result should be negative)
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
Example 3:
Input: s = "1337c0d3"
Output: 1337
Explanation:
Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+') ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)     ^
Example 4:
Input: s = "0-1"
Output: 0
Explanation:
Step 1: "0-1" (no characters read because there is no leading whitespace)
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit) ^
Example 5
Input: s = "words and 987"
Output: 0
Explanation:
Reading stops at the first non-digit character 'w'.
Constraints:
0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.'''

# solution
def myAtoi( s):
        """
        :type s: str
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        # 1. Get rid of leading whitespace instantly
        s = s.lstrip()
        # If the string becomes empty after stripping, return 0
        if not s:
            return 0
        i = 0
        n = len(s)
        sign = 1
        # 2. Handle sign
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        # 3. Convert digits
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Overflow check
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            res = res * 10 + digit
            i += 1
        return res * sign
testcases = [ "42"," -042", "1337c0d3", "0-1","words and 987"]
outputs_expected=[42,-42,1337,0,0]
output_came=[]
for testcase in testcases :
    out_put = myAtoi(testcase)
    output_came.append(out_put)
print(output_came)
if output_came ==  outputs_expected :
     print("well done all test cases passed") 
else:
     print('recheck')  



   