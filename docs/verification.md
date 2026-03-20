# Verification Notes

The refactor was validated locally with both Python and GHC tooling.

## Python commands run

```powershell
python .\questions\inventory-and-sales\Q02_python_inventory_updates.py
python .\questions\inventory-and-sales\Q04_python_sales_revenue.py
python .\questions\inventory-and-sales\Q06_python_stock_trend_pipeline.py
python .\questions\recursive-patterns\Q10_python_organization_budget.py
python .\questions\validation-and-analytics\Q11_python_bmi_pipeline.py
python .\questions\validation-and-analytics\Q13_python_product_review_filter.py
python .\questions\comprehensions-and-generators\Q17_python_employee_performance_classification.py
python .\questions\comprehensions-and-generators\Q18_python_sensor_data_transform.py
python .\questions\comprehensions-and-generators\Q19_python_city_population_filter.py
python .\questions\comprehensions-and-generators\Q20_python_prime_sum_pairs.py
python .\questions\comprehensions-and-generators\Q21_python_pascal_triangle.py
python .\questions\string-and-number-patterns\Q32_python_reduce_operations.py
python .\questions\string-and-number-patterns\Q33_python_reverse_string_recursively.py
python .\questions\string-and-number-patterns\Q34_python_count_upper_and_lowercase.py
python .\questions\string-and-number-patterns\Q35_python_unique_elements_preserve_order.py
python .\questions\string-and-number-patterns\Q36_python_classify_numbers_by_properties.py
python .\questions\string-and-number-patterns\Q37_python_perfect_number_check.py
python .\questions\string-and-number-patterns\Q38_python_palindrome_phrase_check.py
python .\questions\string-and-number-patterns\Q39_python_pangram_check.py
```

## Haskell commands run

```powershell
ghc -fno-code .\questions\inventory-and-sales\Q01_haskell_inventory_updates.hs
ghc -fno-code .\questions\inventory-and-sales\Q03_haskell_sales_revenue.hs
ghc -fno-code .\questions\inventory-and-sales\Q05_haskell_library_fine.hs
ghc -fno-code .\questions\recursive-patterns\Q07_haskell_magic_growth.hs
ghc -fno-code .\questions\recursive-patterns\Q08_haskell_polynomial_derivative.hs
ghc -fno-code .\questions\recursive-patterns\Q09_haskell_plateau_grouping.hs
ghc -fno-code .\questions\validation-and-analytics\Q12_haskell_student_mark_scaling.hs
ghc -fno-code .\questions\folds-and-lambda-foundations\Q14_haskell_count_even_with_fold.hs
ghc -fno-code .\questions\folds-and-lambda-foundations\Q15_haskell_reverse_with_fold.hs
ghc -fno-code .\questions\folds-and-lambda-foundations\Q16_haskell_map_via_fold.hs
ghc -fno-code .\questions\folds-and-lambda-foundations\Q22_haskell_add_two_numbers_with_lambda.hs
ghc -fno-code .\questions\folds-and-lambda-foundations\Q23_haskell_square_with_lambda.hs
ghc -fno-code .\questions\folds-and-lambda-foundations\Q24_haskell_even_odd_label.hs
ghc -fno-code .\questions\folds-and-lambda-foundations\Q25_haskell_absolute_value_lambda.hs
ghc -fno-code .\questions\folds-and-lambda-foundations\Q26_haskell_maximum_of_two_lambda.hs
ghc -fno-code .\questions\folds-and-lambda-foundations\Q27_haskell_increment_list_with_map.hs
ghc -fno-code .\questions\folds-and-lambda-foundations\Q28_haskell_square_list_with_map.hs
ghc -fno-code .\questions\folds-and-lambda-foundations\Q29_haskell_filter_even_numbers.hs
ghc -fno-code .\questions\folds-and-lambda-foundations\Q30_haskell_sum_list_with_fold.hs
ghc -fno-code .\questions\folds-and-lambda-foundations\Q31_haskell_list_length_with_fold.hs
```

## Outcome

- All listed Python files executed successfully.
- All listed Haskell files passed `ghc -fno-code` compilation checks successfully.
- Parallel `runghc` validation initially timed out, so syntax validation was used for a more reliable batch check.
- The later expansion batch also validated the new Python string and number pattern files through direct execution.
