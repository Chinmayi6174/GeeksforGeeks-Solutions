class Solution:
    def findPages(self, arr, k):
        # If students are more than books, allocation is impossible
        if len(arr) < k:
            return -1
        def canAssign(limit):
            students = 1
            pages = 0
            for book in arr:
                if pages + book <= limit:
                    pages += book
                else:
                    students += 1
                    pages = book

                    if students > k:
                        return False
            return True
        low = max(arr)      # At least one book must be assigned
        high = sum(arr)     # One student gets all books
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if canAssign(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
