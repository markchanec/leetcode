class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        if total_length > 1:
            median = int(total_length/2)
            avg_flag = False
            if total_length%2 == 0:
                avg_flag =True
            else:
                median += 1
            # print("median", median)

            nums1count = 0
            nums2count = 0
            element = 0
            temp_element = 0

            for i in range(1,median+2):
                if nums1count < len(nums1) and nums2count < len(nums2):
            #         print("a")
                    if nums1[nums1count] <= nums2[nums2count]:
                        element = nums1[nums1count]
                        nums1count += 1
                    else:
                        element = nums2[nums2count]
                        nums2count += 1
                elif nums1count >= len(nums1):
            #         print("b")
                    element = nums2[nums2count]
                    nums2count += 1
                elif nums2count >= len(nums2):
            #         print("c")
                    element = nums1[nums1count]
                    nums1count += 1
            #     else:
            #         print("error", nums1count, nums2count)

            #     print("ele", element)

                if i == median:
                    if avg_flag:
            #             print("avg")
                        temp_element = element
                        avg_flag = False
                    else:
                        return(float(element))
                        break
                if i == median + 1:
            #         print("add")
                    return((temp_element + element)/2)
                    break
        elif total_length == 1:
            if len(nums1) == 1:
                return(float(nums1[0]))
            elif len(nums2) == 1:
                return(float(nums2[0]))
