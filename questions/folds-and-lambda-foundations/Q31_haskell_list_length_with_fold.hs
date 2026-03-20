-- QUESTION:
-- Compute the length of a list using `foldl`.
--
-- CONCEPT:
-- Folds, counting through accumulation.
--
-- DIFFICULTY:
-- Beginner
--
-- APPROACH:
-- Ignore the current element and increment the counter on each step.
--
-- EXAMPLE RUN:
-- lengthWithFold [1,2,3] == 3

lengthWithFold :: [Int] -> Int
lengthWithFold = foldl (\acc _ -> acc + 1) 0

main :: IO ()
main = print (lengthWithFold [1, 2, 3])
