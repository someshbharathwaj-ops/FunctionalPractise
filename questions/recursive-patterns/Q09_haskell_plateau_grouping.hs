-- QUESTION:
-- Split a list of integers into sublists whenever the value changes. Each sublist must contain one
-- maximal run of equal consecutive values.
--
-- CONCEPT:
-- Structural recursion, grouping runs, pattern matching.
--
-- DIFFICULTY:
-- Intermediate
--
-- APPROACH:
-- Recursively group the tail, then compare the current element with the first element of the next
-- plateau. If they match, extend that plateau; otherwise start a new one.
--
-- EXAMPLE RUN:
-- allPlateaus [3,3,3,2,2,5] == [[3,3,3],[2,2],[5]]
--
-- NOTES:
-- This formulation keeps the original recursive strategy but documents the grouping invariant.

allPlateaus :: [Int] -> [[Int]]
allPlateaus [] = []
allPlateaus [value] = [[value]]
allPlateaus (value : next : rest)
    | value == next = (value : head groupedTail) : tail groupedTail
    | otherwise = [value] : groupedTail
  where
    groupedTail = allPlateaus (next : rest)

main :: IO ()
main = print (allPlateaus [3, 3, 3, 2, 2, 5])
