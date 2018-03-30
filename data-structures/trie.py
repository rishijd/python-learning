'''
This is a Python trie implementation following the Java code for:
Data Structures: Solve 'Contacts' Using Tries
https://www.hackerrank.com/challenges/ctci-contacts/editorial
https://www.youtube.com/watch?time_continue=2&v=vlYZb68kAY0
The video is a part of HackerRank's Cracking The Coding Interview Tutorial
with Gayle Laakmann McDowell.
'''
class Node:

    def __init__(self):
        NO_OF_CHARS = 26
        self.children = [None] * NO_OF_CHARS # will hold actual Nodes when set
        self.size = 0 # size of each node, see findCount below or watch Gayle video
                      # near end where she discusses findCount
        self.leafnode = False

    # helper function to get the int index of char c
    def helper_get_char_index(self, c: chr):
        return ord(c) - ord('a')

    def getNode(self, c: chr):
        return self.children[self.helper_get_char_index(c)]

    def setNode(self, c: chr, node: 'Node'):
        self.children[self.helper_get_char_index(c)] = node

    def add(self, s: str, index: int = 0):
        # recursive, goes through until a new node is added
        self.size += 1 # increment as this node's size just increased
        print('Size', self.size)
        if (index == len(s)):
            self.leafnode = True
            print(self.size, 'leaf')
            return # we are done here if we reach the end of the string, it means nothing else to add

        current_chr = s[index]
        childnode = self.getNode(current_chr)
        if (not childnode): # null, so set the new node
            childnode = Node()
            self.setNode(current_chr, childnode)
            print('just added', current_chr)

        # now add the rest to the child Node (not this current (parent) node)
        childnode.add(s, index+1)


    def findCount(self, s: str, index: int = 0) -> int:
        # recursive, walk through the nodes for each character of s. If no next child, return 0 (no substr found)
        # or reach end of s - then return the current count
        # so keep the current count in each node - which is the size variable above

        if (index == len(s)): return self.size

        childnode = self.getNode(s[index])
        if (not childnode): # null, so the complete string is not found in the trie
            return 0

        return childnode.findCount(s, index+1)

    def findCountList(self, s: str, index: int = 0, matchlist: list = []) -> list:
        # Similar to findCount, but I added a new function to get a list of all matching names in the trie

        if (index == len(s)):
            # now we have to generate a list of all the children here
            print('-------- Finding Count List for', s)
            retlist = [s + l for l in self.getChildList()] # e.g. "ga" is s, and getChildList() yields ['yle', 'ry', 'reth']
            return (self.size, retlist)

        childnode = self.getNode(s[index])
        if (not childnode): # null, so the complete string is not found in the trie
            return (0, [])

        return childnode.findCountList(s, index+1)

    def getChildList(self):

        if self.leafnode:
            # print('this is a leaf node')
            return

        print(self.size, 'size (children)')
        stack = [('', self.children)] # DFS

        while (stack):
            parent_char, children = stack.pop()

            for index, childnode in enumerate(children):
                if childnode is not None:
                    char = chr(index + ord('a'))
                    print('char', char)
                    if childnode.leafnode:
                        # end of this path
                        yield parent_char + char

                    else:
                        # print('append', parent_char, childnode.size, char)
                        stack.append((parent_char + char, childnode.children))


if __name__ == "__main__":
    # set up a trie and test
    n = Node()
    n.add('gary')
    n.add('aloa')
    n.add('aria')
    n.add('genna')
    n.add('gayle')
    n.add('gareth')
    print('### The trie is set up.')
    print('### Find gayle')
    print(n.findCount('gayle'))
    print('### Find jeff')
    print(n.findCount('jeff'))
    print('### Find ga') # 3 possibilities here
    print(n.findCount('ga'))

    print(n.findCountList('ga')) # should return tuple with list of 3 names
    print(n.findCountList('jeff')) # should return (0, [])
