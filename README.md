# AL02-Shared
Monday T.K:
Worst-case scan lookup: O(n) because the algorithm may need to examine every book record before finding the matching ID or determining the ID is absent.
Index construction: O(n) because each book record must be processed once to build the dictionary.
One lookup in an existing index: O(1) average case because a dictionary can directly access a record by its ID without scanning the entire catalog.

Growth Pattern Observations

First_id
Big-0: 0(1)

Reason: Returns the first record directly without scanning the catalog.

all_ids
Big-0: O(n)

Reason: Visits each record once to collect all IDs.


