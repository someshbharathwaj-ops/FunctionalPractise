-- QUESTION:
-- Increase every integer in a list by 1 using `map`.
--
-- CONCEPT:
-- Higher-order functions, mapping.
--
-- DIFFICULTY:
-- Beginner
--
-- APPROACH:
-- Map a simple increment lambda across the list.
--
-- EXAMPLE RUN:
-- incrementList [1,2,3] == [2,3,4]

incrementList :: [Int] -> [Int]
incrementList = map (\x -> x + 1)

main :: IO ()
main = print (incrementList [1, 2, 3])
