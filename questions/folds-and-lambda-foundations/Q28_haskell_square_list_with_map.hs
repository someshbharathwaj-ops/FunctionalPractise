-- QUESTION:
-- Square every integer in a list using `map`.
--
-- CONCEPT:
-- Higher-order functions, list transformation.
--
-- DIFFICULTY:
-- Beginner
--
-- APPROACH:
-- Apply a squaring lambda to every element in the list.
--
-- EXAMPLE RUN:
-- squareList [1,2,3] == [1,4,9]

squareList :: [Int] -> [Int]
squareList = map (\x -> x * x)

main :: IO ()
main = print (squareList [1, 2, 3])
