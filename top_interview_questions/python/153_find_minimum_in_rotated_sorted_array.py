#!/usr/bin/env python
# encoding: utf-8
'''
@author: Fizz Cao 
@time: 7/08/2022 01:00 am
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums)-1
        
        if nums[left] < nums[right]:
            return nums[left]
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1