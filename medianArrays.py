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
    median = -99999999

    primary = 0

    while n1.l < n1.h and n2.l < n2.h:
        if nums1[n1.m] < nums2[n2.m]:
            if left <= right:
                n1.l = n1.m + 1
                median = nums2[n2.m]
            else:
                n2.h = n2.m - 1
                median = nums1[n1.m]
        else:
            if left <= right:
                n2.l = n2.m + 1
                median = nums1[n1.m]
            else:
                n1.h = n1.m - 1
                median = nums2[n2.m]
            
        
        left = n1.m+1 + n2.m+1 - 1
        right = total - left - 1
        if left == right:
            print("Breaking")
            break
        n1.m = int((n1.l + n1.h) / 2)
        n2.m = int((n2.l + n2.h) / 2)
        
        
        # if left == right:
            # break
     
    '''
    if total % 2 == 0:
        # raise Exception('not sure here')
        median = (nums1[n1.m] + nums2[n2.m]) / 2
    else:
        median = min(nums1[n1.m], nums2[n2.m])
    '''


    print("left: ", left)
    print("right: ", right)


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








# findMedianSortedArrays([2,4,6,8], [1,3,5,9,11])

# findMedianSortedArrays([1,2,3,4,5,6], [6,7,8,9,10])


# findMedianSortedArrays([2, 10], [1,3,5,9,11])



findMedianSortedArrays([1, 11], [9, 12, 13, 19, 100, 110, 120])

