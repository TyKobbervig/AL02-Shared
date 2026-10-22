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

6. ## Best-Case and Worst-Case Behavior

A request for **B1** stops sooner because B1 is the first record in the catalog. The search finds the match immediately and returns without checking any other records.

A request for **B4** requires examining several records before finding a match. An absent ID requires checking every record before determining that the book is not present.

- **Best case:** The requested ID is the first record (B1), so the search stops immediately.
- **Worst case:** The requested ID is the last record (B4) or is not in the catalog, so every record must be checked.
- **Average case:** The requested ID is somewhere in the middle, so only some of the records are examined before a match is found.

## Test Coverage

The tests verify:

- Repeated requests return

$ Thursday Tasks: $ 

1. Recommend an approach for a patron’s one B1 lookup when the catalog list is already available and no index has been built. Give a short reason.

2. Recommend an approach for a circulation desk’s many repeated catalog-ID requests when it can retain an index. Give a short reason.

3. Explain the work to build that index, its additional storage, and why reusing it differs from rebuilding it for every request. No new feature is required.

4. Verify the final application and focused tests. Check that both lookup paths still return the same book details or the same absent result.

5. Each partner copies the complete agreed solution and supplied modules into their own class repository, adds personal README notes, and tests the copy.

6. Commit and push the personal copy, then submit your own repository URL and folder path. This is one final submission, not three separate daily apps.

Thursday Observations:

1. One Patron Lookup (B1)

Recommended approach: Scan lookup

Reason: If the catalog list is already available and only one lookup is needed, scanning the list is simpler because no index needs to be built first. For a single request, the overhead of building an index is unnecessary.

## Many Repeated Catalog-ID Requests

**Recommendation:** Indexed Lookup

**Reason:** When many requests are expected, building an index once allows the same index to be reused for future lookups. This avoids repeatedly scanning the entire catalog.

---

## Index Building, Storage, and Reuse

Building the index requires one pass through all catalog records, which is O(n) work.

The index uses additional storage because it stores a dictionary entry for each book ID and its associated record.

Reusing an existing index differs from rebuilding it each time because the setup work is performed only once. After the index has been created, many lookups can use the same index. Rebuilding the index for every request would repeat the same O(n) setup cost over and over again.
