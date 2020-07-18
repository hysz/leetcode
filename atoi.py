class Solution:
    def myAtoi(self, s: str) -> int:
        min_ascii = ord("0")
        max_ascii = ord("9")
        

        sign = None
        decoded_number = 0
        did_decode_number = False
        for c in s:
            c_in_ascii = ord(c)

            if not min_ascii <= c_in_ascii <= max_ascii:
                if not did_decode_number:
                    sign = c
                    continue
                break
            
            did_decode_number = True
            decoded_number = decoded_number * 10 + (c_in_ascii - min_ascii)

        if sign == '-':
            decoded_number *= -1

        return decoded_number

print(Solution().myAtoi("0"))
print(Solution().myAtoi("10"))
print(Solution().myAtoi("123"))
print(Solution().myAtoi("-123"))
print(Solution().myAtoi("+123"))
print(Solution().myAtoi("      asdadsas +123"))
print(Solution().myAtoi("      asdadsas 123 asdjhahdjh 12"))
