# Notes

## Assumptions

1. **Task 1 & 3**: Returning `0.0` when no valid data exists was chosen as a safe default. An alternative would be returning `None` or raising an exception to signal "undefined average."

2. **Task 2**: The email regex `^[^@\s]+@[^@\s]+\.[^@\s]+$` is intentionally basic. For production systems, a more comprehensive solution like the `email-validator` library would be recommended.

## Design Decisions

- **Error Handling Strategy**: Invalid values are **skipped** rather than causing crashes or being defaulted to 0. This avoids masking data quality issues.

- **Task 1 - Malformed Orders**: Orders missing `status` or with non-numeric `amount` are skipped entirely. This is stricter than defaulting missing amounts to 0, which could silently distort averages.

- **Task 3 - NaN/Inf Filtering**: Values like `float('nan')` or `float('inf')` are filtered out to ensure the resulting average is a meaningful finite number.

- **Return Value for Empty/Invalid Input**: All three functions return `0.0` (or `0`) for edge cases like empty lists or all-invalid data. This ensures consistent behavior and prevents crashes in downstream calculations.

## Alternative Approaches Considered

- **Task 2**: Considered using Python's `email.utils.parseaddr()` but it's too permissive for validation purposes. A strict regex approach was chosen for clarity and predictability.

- **Task 3**: Considered raising `ValueError` when encountering non-convertible values instead of silently skipping them. The silent skip approach was chosen because it better matches the function's stated purpose of "aggregating valid measurements" — implying invalid ones should be filtered out rather than causing errors.

## Verification

All corrected functions were tested locally with various edge cases:
- Empty inputs
- All-invalid data (all cancelled orders, all None values)
- Mixed valid/invalid values
- Type conversion errors (non-numeric strings)
- Whitespace handling (for emails)
- NaN/Inf values (for Task 3)

All tests passed successfully.

## Final Note

Thank you for the opportunity. I enjoyed working on this assignment.
