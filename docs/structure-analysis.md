# Structure Discovery Notes

The repository structure was inferred from the source material rather than imposed externally.

## Observed patterns

- Several questions appeared in both Haskell and Python, especially around inventory updates and sales-style data processing.
- A second cluster focused on recursive reasoning in Haskell, with one Python tree-recursion question aligned to the same theme.
- A third cluster centered on validation-heavy analytics pipelines, especially in Python, with one Haskell list-processing exercise that fit the same assessment style.

## Resulting organization

- `questions/inventory-and-sales`
  - Questions about inventory mutation, sales cleaning, pricing, fines, and stock trend analytics.
- `questions/recursive-patterns`
  - Questions whose main teaching goal is structural recursion or recursive decomposition.
- `questions/validation-and-analytics`
  - Questions emphasizing filtering, derived metrics, and safe transformation of partially valid datasets.

## Naming strategy

- Each file uses a stable `QNN_...` prefix to preserve a numbering system across the repository.
- File names highlight language, concept, and task so the question bank stays browsable without opening every file.

## Preservation policy

- No original question logic was removed.
- Missing question statements were reconstructed from the code behavior and converted into academic prompts.
- Duplicate themes across languages were retained because they represent useful cross-language practice.
