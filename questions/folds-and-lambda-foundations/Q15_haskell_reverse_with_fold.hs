-- QUESTION:
-- Reverse a list of integers using a fold instead of explicit recursion.
--
-- CONCEPT:
-- Left folds, accumulator construction, list reversal.
--
-- DIFFICULTY:
-- Beginner
--
-- APPROACH:
-- Build the reversed list by inserting each new value at the front of the accumulator.
--
-- EXAMPLE RUN:
-- reverseWithFold [1,2,3,4] == [4,3,2,1]
--
-- NOTES:
-- This is a cleaned version of the `reverselist` practice exercise.

reverseWithFold :: [Int] -> [Int]
reverseWithFold = foldl (flip (:)) []

main :: IO ()
main = print (reverseWithFold [1, 2, 3, 4])
