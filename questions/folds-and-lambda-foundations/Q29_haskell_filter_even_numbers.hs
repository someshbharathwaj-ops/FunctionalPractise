-- QUESTION:
-- Extract only the even numbers from a list using `filter`.
--
-- CONCEPT:
-- Filtering, predicates.
--
-- DIFFICULTY:
-- Beginner
--
-- APPROACH:
-- Keep only the values that satisfy the `even` predicate.
--
-- EXAMPLE RUN:
-- filterEvenNumbers [1,2,3,4,5] == [2,4]

filterEvenNumbers :: [Int] -> [Int]
filterEvenNumbers = filter (\x -> even x)

main :: IO ()
main = print (filterEvenNumbers [1, 2, 3, 4, 5])
