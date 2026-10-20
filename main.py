def first_record(records):
    """Return the first record directly, or None for empty input."""
    if not records:
        return None
    return records[0]


def scan_lookup(records, queries):
    """Find the first match for each query and count inspected records."""
    results = []
    inspected = 0

    for query in queries:
        found = None

        for record in records:
            inspected += 1

            if record["id"] == query:
                found = record
                break

        results.append(found)

    return results, inspected


def indexed_lookup(records, queries):
    """Build an ID index and return ordered answers plus setup/query counts."""
    index = {}

    for record in records:
        index[record["id"]] = record

    results = []

    for query in queries:
        if query in index:
            results.append(index[query])
        else:
            results.append(None)

    return results, len(records), len(queries)


def halving_trace(size):
    """Show repeated rounded-up halving."""
    trace = []

    while size > 1:
        trace.append(size)
        size = (size + 1) // 2

    return trace + [size]


def make_records(size):
    """Create synthetic records with unique IDs."""
    records = []

    for value in range(size):
        records.append({"id": value})

    return records


def run_demo():
    print("First record:")
    print(first_record(make_records(4)))

    print("\nHalving trace:")
    print(halving_trace(16))

    rows = make_records(4)
    queries = [0, 3, -1]

    print("\nScan lookup:")
    print(scan_lookup(rows, queries))

    print("\nIndexed lookup:")
    print(indexed_lookup(rows, queries))


def main():
    run_demo()


if __name__ == "__main__":
    main()
