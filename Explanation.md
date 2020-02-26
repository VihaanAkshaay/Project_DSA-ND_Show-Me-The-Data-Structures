# Project_DSA-ND_Show-Me-The-Data-Structures
The explanation for all the files can be found below-

## problem_1.py
For the __LRU_Cache__ problem, it is satisfactory to use __OrderedDict()__, specifically the use of the _method_ __.popitem(last=False)__ as it allows us to do basic operations in constant time __O(1)__ as well as keep entry of the order of input ( since it is asn ordered dictionary ). The space complexity here is __O(n)__ as it has to store all n entries.

## problem_2.py
Here the application of __Recursive process__ would be how searching in a generalised folder, we look for the files in the folder and do the same process for the folders inside the current folder. the time complexity is dependant on the number of iterations that are launched. Being in this case dependent on __depth__ and __width__ of folders, resulting in a __O(d*w)__. As for the space complexity, in this case, it is directly dependent on the number of returns the function does, hence, the number of found files __f__, __O(f)__.

## problem_3.py
the data was encoded by first counting the frequency of each charachter, then building a heapafied tree where the leaf nodes were the charachters the depth of each charachter in the tree is determined by their frequency in the data. The time complexity for encoding and decoding is __O(n^2)__  since in the worst case we'll have to traverse throught the entries twice to find the two least values, and while decoding, n is the length of the encoded data for building the string, loops over all charachters in the encoded data, and for each match with the reverse_code dictionary, it bulds a new string __O(n)__. - Space Complexity:
 O(u*log(u)) from the tree for encoding and for decoding O(n) where n is the length of the string.
 
## problem_4.py: Windows Active Directory
__preorder DFS__ is used to traverse the active directory structure and find the user that matches the one we are looking for.Each group search for the user in the users list, and if it's not there, it is looped through all subgroups and searched for the user in them recursevly .Time complexity for a tree of n nodes (here groups) is __O(n)__ and for each node there is a list of users of length l that we need to search for a user so the time complexity is __O(n*l)__. the space complexity is __O(b*m)__ where m is the longest path and b is the number of sibling nodes along the path.

## problem_5.py: Blockchain
A linked list where each node has block and a next pointer, and everytime data was appended, a new block was created with a time stamp a the prevoius nodes hash, and  information was hashed and appended to the new block to the chain. Time Complexity for appending new data is __O(n)__ (because even if we assume that the hash function takes constant time we are concatonating the data and timestamp and previous_hash before hashing them wich takes O(n) because python strings are immutable), for iterationg over the block chain it is also O(n). Space Complexity is __O(n)__ as the hash needed to concatinate all the data in a string and encode it and then hash it, and stored in size n.

## problem_6.py: Union and Intersection
Python's built-in set class was used to perform the intersection and union. In the case of Union,values form both the set were obtained, then iterated over and then added to a linked list. In the case of Intersection, the values are added from each list to a set,then intersected, then iterated over the resulting set and the values are added to a linked list. Time Complexity for         union is O(s1+s2) where s1 is the number of elements in the first set and s2 is the number of elements in the second set or O(n) where n is the size of the input and that of intersection is O(n) where n is the longer of the 2 lists. Space Complexity union and intersection is O(n) where n is the size of the input (llist_1 + llist_2).

