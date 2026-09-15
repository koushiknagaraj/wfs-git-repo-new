def merge(intervals: list[list[int]]) -> list[list[int]]:
    """
    LeetCode 56 - Merge Intervals (Medium)

    Given an array of intervals where intervals[i] = [start_i, end_i], merge
    all overlapping intervals, and return an array of the non-overlapping
    intervals that cover all the intervals in the input.

    Example:
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        -> [[1,6],[8,10],[15,18]]
        intervals = [[1,4],[4,5]]
        -> [[1,5]]

    Constraints:
        - 1 <= len(intervals) <= 10^4
        - intervals[i].length == 2

    Hint: sort intervals first using
        intervals.sort(key=lambda pair: pair[0])
    then sweep through with a loop, merging into the last interval in your
    result list when the current one overlaps it.
    """
    raise NotImplementedError
