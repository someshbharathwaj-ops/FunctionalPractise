# Migration Notes

This document records how the original unstructured files were curated into the question bank.

## Legacy-to-curated mapping

| Legacy file | Curated question |
| --- | --- |
| `QUE$.hs` | `questions/inventory-and-sales/Q01_haskell_inventory_updates.hs` |
| `QUE$.py` | `questions/inventory-and-sales/Q02_python_inventory_updates.py` |
| `QUE&.py` | `questions/recursive-patterns/Q10_python_organization_budget.py` |
| `QUE(.py` | `questions/inventory-and-sales/Q04_python_sales_revenue.py` |
| `QUE!).hs` | `questions/inventory-and-sales/Q05_haskell_library_fine.hs` |
| `QUE!!.py` | `questions/inventory-and-sales/Q06_python_stock_trend_pipeline.py` |
| `QUE!.hs` | `questions/recursive-patterns/Q07_haskell_magic_growth.hs` |
| `QUE#.hs` | `questions/recursive-patterns/Q08_haskell_polynomial_derivative.hs` |
| `QUE).hs` | `questions/recursive-patterns/Q09_haskell_plateau_grouping.hs` |
| `QUE8.py` | `questions/validation-and-analytics/Q11_python_bmi_pipeline.py` |
| `QUE@.hs` | `questions/validation-and-analytics/Q12_haskell_student_mark_scaling.hs` |
| `QUE^.py` | `questions/validation-and-analytics/Q13_python_product_review_filter.py` |

## Consolidation decisions

- Inventory and sales questions were grouped together because they share tuple-based updates, data cleaning, and reporting workflows.
- Recursive questions were separated where recursion is the primary conceptual goal.
- Validation-driven analytics questions were grouped for their emphasis on safe filtering before computation.

## Cleanup summary

- Symbol-heavy legacy filenames were removed from the working tree after their logic was migrated.
- The editor-specific `.vscode` folder was removed so the repository stays focused on teaching material.
