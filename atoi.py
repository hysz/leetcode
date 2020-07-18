class Solution:
    def myAtoi(self, s: str) -> int:
        min_ascii = ord("0")
        max_ascii = ord("9")
        
        # Eat whitespace
        i = 0
        while i < len(s):
            if not s[i].isspace():
                break
            i += 1

        # We done?
        if i == len(s):
            return 0

        # Return zero if next value is not +/-/numeric
        if not min_ascii <= ord(s[i]) <= max_ascii and not s[i] in ['+', '-']:
            return 0

        # Decode +/- numeric value, stopping once we encounter a non-numeric value.
        sign = None
        decoded_number = 0
        did_decode_number = False
        while i < len(s):
            # read next char
            c = s[i]
            i += 1

            # get ascii and validate
            c_in_ascii = ord(c)
            if not min_ascii <= c_in_ascii <= max_ascii:
                if not did_decode_number:
                    if sign:
                        # cannot find the sign twice
                        return 0
                    sign = c
                    continue
                break
            
            did_decode_number = True
            decoded_number = decoded_number * 10 + (c_in_ascii - min_ascii)

        # adjust sign and range check [MIN_INT, MAX_INT]
        min_int32 = -pow(2,31)
        max_int32 = pow(2,31) - 1
        if sign == '-':
            decoded_number *= -1
            if decoded_number < min_int32:
                return min_int32
        else:
            if decoded_number > max_int32:
                return max_int32
        
        return decoded_number


print(Solution().myAtoi("0"))
print(Solution().myAtoi("       "))
print(Solution().myAtoi("10"))
print(Solution().myAtoi("123"))
print(Solution().myAtoi("-123"))
print(Solution().myAtoi("+123"))
print(Solution().myAtoi("      asdadsas +123"))
print(Solution().myAtoi("      asdadsas 123 asdjhahdjh 12"))
print(Solution().myAtoi("       123 asdjhahdjh 12"))
print(Solution().myAtoi("       -123 asdjhahdjh 12"))
print(Solution().myAtoi("       -123 asdjhahdjh 12"))
print(Solution().myAtoi("       2147483648"))
print(Solution().myAtoi("       2147483647"))
print(Solution().myAtoi("       -2147483649"))
print(Solution().myAtoi("       -2147483648"))
print(Solution().myAtoi("+-123"))
