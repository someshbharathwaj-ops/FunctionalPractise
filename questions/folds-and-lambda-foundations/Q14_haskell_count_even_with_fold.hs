-- QUESTION:
-- Count how many even numbers appear in a list using a fold.
--
-- CONCEPT:
-- Folds, accumulator design, parity predicates.
--
-- DIFFICULTY:
-- Beginner
--
-- APPROACH:
-- Traverse the list with `foldl`, increasing the accumulator only when the current element is even.
--
-- EXAMPLE RUN:
-- countEven [1,2,3,4,6,9] == 3
--
-- NOTES:
-- This problem is curated from the `queone` fold exercise in the Haskell practice set.

countEven :: [Int] -> Int
countEven = foldl (\acc value -> if even value then acc + 1 else acc) 0

main :: IO ()
main = print (countEven [1, 2, 3, 4, 6, 9])
