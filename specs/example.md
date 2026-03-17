# Example Specification: Parse a Names CSV

> This shows what a strong spec looks like. Your specs should have this level of detail.

## Overview

Read a CSV file of names and return them as a sorted list, deduplicated.

## Inputs

| Parameter | Type | Description |
|-----------|------|-------------|
| `filepath` | `str` | Absolute or relative path to a CSV file |

**File format:**
- Single column with header `"name"` in row 1
- Each subsequent row: one name string (may have leading/trailing whitespace)
- Encoding: UTF-8

## Outputs

Returns `list[str]` — all unique names, sorted case-insensitively, preserving original capitalisation of first occurrence.

Example: if the file contains `"alice"` and `"Alice"`, return `["Alice"]` (first occurrence is `"alice"` → returns that... actually: return the first occurrence's capitalisation).

Wait — define clearly: "sort is case-insensitive; when two names differ only by case, keep the capitalisation of whichever appears first in the file."

## Rules

1. Header row (`"name"`) is not included in output
2. Names are trimmed of leading/trailing whitespace before processing
3. Empty strings (after trimming) are ignored
4. Duplicate names (case-insensitive match) are deduplicated — first occurrence wins
5. Output is sorted case-insensitively (A before B, a before b, A and a adjacent)
6. File not found raises `FileNotFoundError` with message: `"File not found: {filepath}"`

## Acceptance Criteria

- **AC1**: Given a file with `["Alice", "Bob", "carol"]`, returns `["Alice", "Bob", "carol"]`
- **AC2**: Given a file with `["Bob", "Alice"]`, returns `["Alice", "Bob"]` (sorted)
- **AC3**: Given a file with `["Alice", "ALICE"]`, returns `["Alice"]` (deduplicated, first wins)
- **AC4**: Given a file with only the header row, returns `[]`
- **AC5**: Given a non-existent path, raises `FileNotFoundError`
- **AC6**: Given `["  Alice  ", "Bob"]`, returns `["Alice", "Bob"]` (whitespace trimmed)

## Test Cases

```python
def test_basic_sort():
    result = parse_names("names.csv")  # contains Alice, Bob, carol
    assert result == ["Alice", "Bob", "carol"]

def test_deduplication():
    result = parse_names("dupes.csv")  # contains Alice, ALICE
    assert result == ["Alice"]

def test_empty_file():
    result = parse_names("empty.csv")  # only header
    assert result == []

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        parse_names("does_not_exist.csv")
```

## Edge Cases

| Case | Input | Expected |
|------|-------|----------|
| All-whitespace name | `"   "` | Ignored |
| Single name | `["Alice"]` | `["Alice"]` |
| Names with numbers | `["Alice2", "Alice1"]` | `["Alice1", "Alice2"]` |
| Unicode | `["André", "Alice"]` | `["Alice", "André"]` |

## Engineering Notes

- Use `csv.DictReader` — handles quoting edge cases better than splitting on commas
- Do NOT load entire file into memory for very large files — iterate rows
- The sort key should be `str.casefold()`, not `str.lower()` (handles more Unicode cases correctly)
