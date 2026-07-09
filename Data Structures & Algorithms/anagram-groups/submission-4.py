class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # This is the main function.
        # It takes a list of strings (strs) and returns a list of lists,
        # where each inner list contains strings that are anagrams of each other.

        res = defaultdict(list)
        # Create a special dictionary called 'res'.
        # Unlike a normal dict, defaultdict(list) automatically creates
        # an empty list [] as the value whenever we access a key
        # that doesn't exist yet — so we never get a KeyError.

        for s in strs:
            # Loop through every string 's' in the input list 'strs'.

            sortedS = ''.join(sorted(s))
            # sorted(s) breaks the string into characters and sorts them
            # alphabetically, returning a LIST of characters.
            # Example: sorted("eat") -> ['a', 'e', 't']
            #
            # ''.join(...) then glues that list of characters back
            # into a single string with no separator.
            # Example: ''.join(['a', 'e', 't']) -> "aet"
            #
            # So sortedS becomes a "signature" for the word —
            # all anagrams of the same word produce the SAME sortedS.
            # "eat", "tea", "ate" all become "aet".

            res[sortedS].append(s)
            # Use sortedS as the dictionary key.
            # Append the ORIGINAL string 's' (not the sorted version)
            # to the list stored under that key.
            # Because res is a defaultdict, if this key doesn't exist yet,
            # Python automatically creates res[sortedS] = [] first,
            # then appends 's' to it.

        return list(res.values())
        # res.values() gives us just the lists of grouped anagrams,
        # ignoring the sortedS keys (we don't need them anymore).
        # list(...) converts that into an actual list of lists,
        # which is the final expected output format.