
class State:
    letter = ''
    count = 0
    next_state = None
    
    def __init__(self, letter, count, next_state):
        self.letter = letter
        self.count = count
        self.next_state = next_state
        
    def match(self, s: str) -> bool:
        # Match local state
        has_matched = True if self.count == -1 else False
        
        # Base case - empty string
        if not s:
            return has_matched and self.next_state == None
        
        # Check what letter we're matching
        # print("letter: %s"%(self.letter))
        # print("has_matched: %s"%(has_matched))
        
        # Perform matching
        matched_letters = ""
        while s:
            c = s[:1]
            if c != self.letter and self.letter != '.':
                # print("%s != %s"%(c, self.letter))
                if not has_matched:
                    # print("done")
                    return False
                else:
                    break
            
            matched_letters += s[0]
            s = s[1:]
            has_matched = True
            # Only need one, lets dip
            if self.count == 1:
                break

        # print("done loop")

        # Check next
        if not self.next_state:
            return len(s) == 0
        
        # Iterate
        next_matched = self.next_state.match(s[:])
        if next_matched:
            # print("next matched!")
            return True

        # if we did not match but this is a 0..many state, then try putting
        # matched letters back in and iterate.
        if not next_matched and self.count == -1:
            # print("matched letters: ", matched_letters)
            for i in range(0, len(matched_letters)):
                # print("Trying '%s'"%(matched_letters[-(i+1):] + s[:]))
                next_matched = self.next_state.match(matched_letters[-(i+1):] + s[:])
                if next_matched:
                    return True

        return False

    def __repr__(self):
        return "[%s, %d, %s]"%(self.letter, self.count, self.next_state)

class StateMachine:
    def create(s: str) -> State:
        # create reversed, for fun.
        state = None
        count = 1
        for c in reversed(s):
            if c == '*':
                count = -1
            else:
                state = State(c, count, state)
                count = 1
        return state

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        state_machine = StateMachine.create(p)
        if not p:
            return not s
        # print(state_machine)
        return state_machine.match(s)
    

'''
# print(Solution().isMatch("a", "a"))
# print(Solution().isMatch("b", "a"))
# print(Solution().isMatch("aa", "a"))
# print(Solution().isMatch("aa", "a*"))
# print(Solution().isMatch("aab", "a*"))

# print("FInal: " , Solution().isMatch("aa", "a*b"))
# print("FInal: " , Solution().isMatch("aab", "a*b"))
'''

## print("FInal: " , Solution().isMatch("aatb", "aa..*b"))
## print("FInal: " , Solution().isMatch("aatbbbcd", "aa..*bbcd"))


## print("FInal: " , Solution().isMatch("a", "ab*a"))


## print("FInal: " , Solution().isMatch("ab", ".*"))


# print("FInal: " , Solution().isMatch("bbbba", ".*a*a"))


#print("FInal: " , Solution().isMatch("a", ""))
#print("FInal: " , Solution().isMatch("", ""))

print("FInal: " , Solution().isMatch("", ""))