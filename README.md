# Functional Programming Question Bank

This repository curates a mixed Haskell and Python practice folder into a structured question bank focused on functional programming ideas. The structure was derived from the actual codebase and now covers inventory and sales processing, recursive patterns, validation-driven analytics, fold/lambda foundations, comprehension-driven generators, and string/number patterns.

## Repository usage

- Browse questions by theme under `questions/`.
- Open any question file to find:
  - `QUESTION`
  - `CONCEPT`
  - `DIFFICULTY`
  - `APPROACH`
  - `IMPLEMENTATION`
  - `EXAMPLE RUN`
  - `NOTES`
- Use [`docs/question-index.md`](docs/question-index.md) as the master lookup table.

## Functional paradigm focus

- Haskell questions emphasize recursion, pattern matching, folds, and decomposition into pure helper functions.
- Python questions are written in a functional style using `map`, `filter`, `reduce`, comprehensions, immutable transformations, and recursive decomposition where appropriate.
- The repository avoids unnecessary global mutation and keeps each question authentic to its original learning goal.

## Topic coverage

- Inventory updates and stock management
- Sales cleaning and revenue analytics
- Rule-based fine calculation
- Recursive recurrence relations
- Symbolic differentiation
- Plateau grouping
- Recursive organization-budget analysis
- BMI filtering pipelines
- Student mark scaling
- Product review validation
- Fold-based counting and reversing
- Implementing `map` with `foldl` and `foldr`
- Employee performance classification
- Sensor-data cleaning and transformation
- City-population filtering
- Prime-sum pair generation
- Pascal triangle construction
- Recursive string reversal
- Case counting and pangram detection
- Perfect-number and palindrome checks
- Stable deduplication with reduction

## Running the questions

### Python

Run any Python question directly:

```powershell
python .\questions\inventory-and-sales\Q04_python_sales_revenue.py
```

### Haskell

Interpret a Haskell question:

```powershell
runghc .\questions\recursive-patterns\Q09_haskell_plateau_grouping.hs
```

Or perform a syntax-only validation:

```powershell
ghc -fno-code .\questions\recursive-patterns\Q09_haskell_plateau_grouping.hs
```

## Documentation

- [`docs/structure-analysis.md`](docs/structure-analysis.md) explains the inferred organization.
- [`docs/question-index.md`](docs/question-index.md) lists all questions.
- [`docs/topic-coverage.md`](docs/topic-coverage.md) summarizes the academic grouping.
- [`docs/verification.md`](docs/verification.md) records the validation commands used during the refactor.
