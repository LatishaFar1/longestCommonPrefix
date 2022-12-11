# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string.

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# // -------------------------------------------------------

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    longestPref = strs[0]
    for string in strs:
        for index in range(0, len(longestPref)):
            if (index >= len(string) or longestPref[index] != string[index]):
                longestPref = longestPref[0:index]
                break
    return longestPref


print(longestCommonPrefix(["flower","flow","flight"]))