# AL02-Shared
Monday T.K:
Worst-case scan lookup: O(n) because the algorithm may need to examine every book record before finding the matching ID or determining the ID is absent.
Index construction: O(n) because each book record must be processed once to build the dictionary.
One lookup in an existing index: O(1) average case because a dictionary can directly access a record by its ID without scanning the entire catalog.
