import itertools


#itertools
def permutation_itertools(list1):
    list2 = list(itertools.permutations(list1, len(list1)))
    return list(set(list2))


#DFS
def permutation_DFS(res, l, nums):
        if len(nums) == 0:
            res.append(list(l))
        pre = None
        for i in xrange(len(nums)):
            if nums[i] == pre:
                continue
            l.append(nums[i])
            permutation_DFS(res, l, nums[:i] + nums[i+1:])
            l.pop()
            pre = nums[i]
        return res

result = []
n = []
lists = [1, 1, 2]
lists = sorted(lists)

# lists = [1, 2, 3, 5]
# input_list = raw_input("please input a collection of numbers: ")
# lists = input_list.split(" ")

permutation_DFS(result, n, lists)
print result
print permutation_itertools(lists)
