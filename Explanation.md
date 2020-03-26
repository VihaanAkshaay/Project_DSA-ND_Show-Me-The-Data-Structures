# Project_DSA-ND_Show-Me-The-Data-Structures
The explanation for all the files can be found below-

## problem_1.py
For the __LRU_Cache__ problem, it is satisfactory to use __OrderedDict()__, specifically the use of the _method_ __.popitem(last=False)__ as it allows us to do basic operations in constant time __O(1)__ as well as keep entry of the order of input ( since it is asn ordered dictionary ). The space complexity here is __O(n)__ as it has to store all n entries.

## problem_2.py
Here the application of __Recursive process__ would be how searching in a generalised folder, we look for the files in the folder and do the same process for the folders inside the current folder. the time complexity is dependant on the number of iterations that are launched. Being in this case dependent on __depth__ and __width__ of folders, resulting in a __O(d*w)__. As for the space complexity, in this case, it is directly dependent on the number of returns the function does, hence, the number of found files __f__, __O(f)__.

## problem_3.py
The implementation of the Huffmann Algorithm, has consisted as pseudo code tasks were resolved, in the construction of several classes,namely Node,Queue,Tree and HuffmanEncoder. In respects to the study of the time complexity, would be **O(Ln)**, being L the maximum length of a codeword. If I had not used a built in function for sorting, the input would take O(nlog(n)), ending up **the time complexity being O(nlog(n))**. Comparing the size of data structures used, it is directly related to the size of the employed alphabet, in this case k, resulting in a **space complexity of O(k)**.


 
## problem_4.py: Windows Active Directory
__preorder DFS__ is used to traverse the active directory structure and find the user that matches the one we are looking for.Each group search for the user in the users list, and if it's not there, it is looped through all subgroups and searched for the user in them recursevly .Time complexity for a tree of n nodes (here groups) is __O(n)__ and for each node there is a list of users of length l that we need to search for a user so the time complexity is __O(n*l)__. the space complexity is __O(b*m)__ where m is the longest path and b is the number of sibling nodes along the path.

## problem_5.py: Blockchain
A linked list where each node has block and a next pointer, and everytime data was appended, a new block was created with a time stamp a the prevoius nodes hash, and  information was hashed and appended to the new block to the chain. Time Complexity for appending new data is __O(n)__ (because even if we assume that the hash function takes constant time we are concatonating the data and timestamp and previous_hash before hashing them wich takes O(n) because python strings are immutable), for iterationg over the block chain it is also O(n). Space Complexity is __O(n)__ as the hash needed to concatinate all the data in a string and encode it and then hash it, and stored in size n.

## problem_6.py: Union and Intersection
For the union and intersection problem, the approach has been to transform the linked lists, a format which is harder to work with, on something much simpler as is a list. Once the transformation has been done, the combination with the handy object sets, has done all the work. For the **time complexity** , **Union** needs to create a nwe array resulting in **O(n)**. Meanwhile **Intersection** requires a double loop for the creation of a final array, resulting in **O(n^2)**. Considering space consumed, we have created 3 lists which results in a **space complexity of O(n)**
