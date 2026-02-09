# AI Code Review Assignment (Python)

## Candidate
- Name: Meryem Sakin
- Approximate time spent: ~60 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- **Incorrect count calculation**: The function uses `count = len(orders)` which includes all orders in the denominator, but only non-cancelled orders are added to the total. This results in an incorrect average.
- **ZeroDivisionError**: When an empty list is passed, `len(orders)` returns 0, causing a division by zero error.

### Edge cases & risks
- If all orders are cancelled, `total = 0` but `count > 0`, returning 0 as average even though there are no valid orders to average.
- Missing key handling: If an order dictionary doesn't have "status" or "amount" keys, the function will raise a KeyError.

### Code quality / design issues
- The variable name `count` is misleading since it doesn't represent the count of non-cancelled orders.
- No input validation or error handling.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Changed to count only non-cancelled orders (`valid_count`)
- Added empty list check at the beginning
- Added check for when all orders are cancelled (returns 0.0)
- **Malformed orders are now skipped**: Orders missing `status` or with non-numeric `amount` are excluded to avoid masking data quality issues
- Used `.get()` method with try-except for safer dictionary access and numeric conversion

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

1. **Empty list**: Verify it returns 0.0 without crashing
2. **All cancelled orders**: Should return 0.0, not raise an error
3. **Mixed orders**: Verify only non-cancelled amounts are averaged
4. **Single valid order**: Edge case for division logic
5. **Missing keys**: Test with malformed order dictionaries

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- **Misleading claim**: States it "correctly excludes cancelled orders" but the count includes ALL orders, making the denominator incorrect.
- **Omits critical bug**: The explanation doesn't mention the division uses total order count, not valid order count.
- **No edge case mention**: Doesn't address empty list or all-cancelled scenarios.

### Rewritten explanation
- This function calculates the average order value by summing amounts of non-cancelled orders and dividing by the count of non-cancelled orders only. It safely handles empty lists and scenarios where all orders are cancelled by returning 0.0. The function uses safe dictionary access to prevent KeyError exceptions.

## 4) Final Judgment
- **Original Code Decision**: Request Changes
- **After Fix Decision**: Approve
- Justification: The original code has a critical bug in the denominator calculation that produces incorrect averages. The corrected version properly counts only valid orders and skips malformed data.
- Confidence & unknowns: High confidence in the identified bugs and fixes.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- **Insufficient email validation**: Only checking for `@` character is not adequate for email validation. Invalid formats like `"@"`, `"user@"`, `"@domain.com"`, or `"user@@domain.com"` would be counted as valid.

### Edge cases & risks
- **TypeError on None values**: If a None value is in the list, `"@" in None` will raise a TypeError.
- **Non-string inputs**: Numbers or other types in the list will cause errors.
- **Whitespace**: Emails with leading/trailing spaces (e.g., `" user@domain.com "`) are not properly handled.
- **Multiple @ symbols**: `"user@@domain.com"` would be counted as valid.

### Code quality / design issues
- No type checking for input elements.
- No documentation about what constitutes a "valid" email.
- The validation logic is too simplistic for real-world use.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Implemented regex-based email validation with pattern: `^[^@\s]+@[^@\s]+\.[^@\s]+$`
- Added type checking to skip non-string values
- Added whitespace stripping before validation
- Added empty list handling

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

1. **Valid emails**: Standard formats like `user@example.com`
2. **Invalid formats**: `"@"`, `"user@"`, `"@domain"`, `"user.domain.com"`
3. **Edge strings**: Empty string `""`, whitespace only `"   "`
4. **Non-string values**: None, integers, lists in the input
5. **Whitespace handling**: Emails with extra spaces
6. **Multiple @ symbols**: `"user@@domain.com"`

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- **Overstates validation**: Claims to count "valid email addresses" but only checks for `@` presence.
- **False claim about safety**: Says it "safely ignores invalid entries" but will crash on None values.
- **Incorrect about empty handling**: The function does handle empty lists correctly (returns 0), but this is incidental.

### Rewritten explanation
- This function counts email addresses that match a basic pattern validation (contains one @ symbol, has content before and after @, and includes a domain with a dot). It safely handles non-string values by skipping them and strips whitespace before validation. For production use, consider using a more comprehensive email validation library.

## 4) Final Judgment
- **Original Code Decision**: Request Changes
- **After Fix Decision**: Approve
- Justification: The original email validation is too simplistic and has type safety issues. The corrected version uses a basic but reasonable regex pattern.
- Confidence & unknowns: High confidence. The regex is intentionally basic; production systems may want a dedicated email validation library.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- **Incorrect count calculation**: Same issue as Task 1 — `count = len(values)` includes all values (including None) in the denominator, but only non-None values are summed. This produces incorrect averages.
- **ZeroDivisionError**: Empty list causes division by zero.

### Edge cases & risks
- **All None values**: If all values are None, total = 0 but count > 0, giving incorrect result.
- **ValueError on float conversion**: If a value like `"abc"` is passed, `float(v)` will raise ValueError.
- **Non-numeric types**: Complex objects that can't be converted to float will crash the function.

### Code quality / design issues
- No exception handling for conversion errors.
- The variable name `count` doesn't reflect that it includes invalid values.
- No input validation.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Changed to count only successfully converted values (`valid_count`)
- Added empty list check returning 0.0
- Added try-except block to handle ValueError and TypeError on float conversion
- **Added NaN/Inf filtering**: Values like `float('nan')` or `float('inf')` are now excluded to ensure meaningful averages
- Returns 0.0 when no valid measurements exist

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

1. **Empty list**: Should return 0.0
2. **All None values**: Should return 0.0
3. **Mixed valid/None**: Verify correct average of valid values only
4. **Non-convertible strings**: `["abc", "123"]` — should skip "abc", average "123"
5. **Numeric strings**: `["1.5", "2.5"]` — should work correctly
6. **Mixed types**: Integers, floats, strings together

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- **Incorrect average claim**: The denominator uses total count, not valid count, so the average is inaccurate.
- **False safety claim**: Says it "safely handles mixed input types" but will crash on non-numeric strings.
- **Overstates accuracy**: Claims "accurate average" but the calculation is fundamentally wrong.

### Rewritten explanation
- This function calculates the average of valid measurements by filtering out None values and values that cannot be converted to float. It divides the sum by the count of successfully converted values only, ensuring an accurate average. Empty lists or lists with no valid values return 0.0.

## 4) Final Judgment
- **Original Code Decision**: Request Changes
- **After Fix Decision**: Approve
- Justification: The original function has the same critical bug as Task 1 (incorrect denominator) and lacks error handling. The corrected version properly handles edge cases including NaN/Inf values.
- Confidence & unknowns: High confidence in the fixes. The choice to return 0.0 for no valid values is a design decision documented in NOTES.md.
