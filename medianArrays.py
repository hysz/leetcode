import collections
from recordclass import recordclass
import statistics

class N:
    l = 0
    m = 0
    h = 0
    primary = False

    def __init__(self, l,m,h,primary):
        self.l = l
        self.m = m
        self.h = h

    def __repr__(self):
        return "{%d, %d, %d}"%(self.l, self.m, self.h)

MedianRange = recordclass('MedianRange', ['l', 'm', 'h', 'primary'])

def findMedianSortedArrays(nums1, nums2):
    n1 = MedianRange(l = 0, m = int((len(nums1) - 1) / 2), h = len(nums1) - 1, primary = False)
    n2 = MedianRange(l = 0, m = int((len(nums2) - 1) / 2), h = len(nums2) - 1, primary = False)

    print(n1)
    print(n2)
    print("----")

    total = len(nums1) + len(nums2)
    left = 0
    right = 0
    

    while n1.l < n1.h and n2.l < n2.h:
        if nums1[n1.m] < nums2[n2.m]:
            print("#1")
            # Update <n1>
            n1.l = n1.m + 1
            n1.m = int((n1.l + n1.h) / 2)
            
            # Update <n2>
            n2.h = n2.m
            n2.m = int((n2.l + n2.h) / 2)
            
            n1.primary = True
            n2.primary = False
        else:
            print("#2")
            # Update <n1>
            n1.h = n1.m
            n1.m = int((n1.l + n1.h) / 2)
            
            # Update <n2>
            n2.l = n2.m + 1
            n2.m = int((n2.l + n2.h) / 2)

            n1.primary = False
            n2.primary = True

        left = n1.m + 1 + n2.m - 1
        right = total - left - 1

        print(n1)
        print(n2)
        print("----")
            
    median = -99999999999
    if n1.primary:
        median = nums1[n1.m]
    else:
        median = nums2[n2.m]


    print("left: ", left)
    print("right: ", right)

        
    '''
    if n1.l < n1.h:
        if nums1[n1.m] < nums2[n2.m]:
            n1.l = n1.m = n1.h
        else:
            n1.h = n1.m = n1.l

    if n2.l < n2.h:
        n2.l = n2.h = n2.m
    '''


    merged = sorted(nums1 + nums2)
    print(merged)
    print("----")
    print(nums1)
    print(nums2)
    
    print("----")
    print(n1)
    print(n2)
    print("----")
    print(list(map(lambda i: nums1[i], n1)))
    print(list(map(lambda i: nums2[i], n2)))
    print("...")
    print("EXPECTED = ", statistics.median(merged))
    print("ACTUAL = ", median)








findMedianSortedArrays([2,4,6,8], [1,3,5,9,11])

# findMedianSortedArrays([1,2,3,4,5,6], [6,7,8,9,10])


# WORKS - findMedianSortedArrays([2, 10], [1,3,5,9,11])



# FAILS - findMedianSortedArrays([2], [1,11])

