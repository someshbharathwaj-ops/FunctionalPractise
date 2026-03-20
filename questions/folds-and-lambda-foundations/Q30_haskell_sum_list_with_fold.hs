-- QUESTION:
-- Sum all integers in a list using `foldl`.
--
-- CONCEPT:
-- Folds, accumulators.
--
-- DIFFICULTY:
-- Beginner
--
-- APPROACH:
-- Start from 0 and add each new element into the accumulator.
--
-- EXAMPLE RUN:
-- sumWithFold [1,2,3] == 6
--
-- NOTES:
-- The source practice function started from 6; this curated version states the conventional summation problem explicitly.

sumWithFold :: [Int] -> Int
sumWithFold = foldl (\acc x -> acc + x) 0

main :: IO ()
main = print (sumWithFold [1, 2, 3])
