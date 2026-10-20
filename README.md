# AL02-Shared
Monday T.K:
Worst-case scan lookup: O(n) because the algorithm may need to examine every book record before finding the matching ID or determining the ID is absent.
Index construction: O(n) because each book record must be processed once to build the dictionary.
One lookup in an existing index: O(1) average case because a dictionary can directly access a record by its ID without scanning the entire catalog.

$ Monday Tasks: $

6. Briefly identify worst-case scan growth, index-build growth, and the expected average-case growth of one lookup in an existing index.

Worst-Case Scan Growth: 

Index-Build Growth: 

Expected Average-Case Growth: 

$ Tuesday Tasks: $

1. Inspect first_id, all_ids, ordered_pairs, and halving_sizes in growth_examples.py. Use the catalog records for the first three; the halving example takes a size.

    first_id: B1
    all_ids: ['B1', 'B2', 'B3', 'B4']
    ordered_pairs: [('B1', 'B1'), ('B1', 'B2'), ('B1', 'B3'), ('B1', 'B4'), ('B2', 'B1'), ('B2', 'B2'), ('B2', 'B3'), ('B2', 'B4'), ('B3', 'B1'), ('B3', 'B2'), ('B3', 'B3'), ('B3', 'B4'), ('B4', 'B1'), ('B4', 'B2'), ('B4', 'B3'), ('B4', 'B4')]
    halving_sizes(8): [8, 4, 2, 1]

2. For each, record a Big-O label and one short reason in your README.

    First ID: O(1) constant
    Reason: Returns the first record directly without scanning the catalog.

    All IDs: O(n) linear
    Reason: Visits each record once to collect all IDs. 

    Ordered Pairs: O(n^2) quadratic
    Reason: Uses nested loops to create ordered pairs.

    Halving Sizes: O(log n)
    Reason: Repeatedly halves at every step.

3. Explain why a request for B1 stops sooner than a request for B4 or an absent ID in this catalog order. Connect that observation to best/worst cases.

    B1 is at the top of the catalog, and our functions naturally draw from the beginning of said catalog. 

4. Finish focused tests for repeated requests, retained request order, unchanged records, and rejection of duplicate IDs by the supplied precheck.

5. Run the application and tests, correct mismatches, and commit progress.