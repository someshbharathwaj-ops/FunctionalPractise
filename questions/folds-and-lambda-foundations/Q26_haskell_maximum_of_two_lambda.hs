-- QUESTION:
-- Return the larger of two integers using a lambda expression.
--
-- CONCEPT:
-- Lambdas, conditional selection.
--
-- DIFFICULTY:
-- Beginner
--
-- APPROACH:
-- Compare the two values inside the lambda and return the greater one.
--
-- EXAMPLE RUN:
-- maximumOfTwo 10 20 == 20

maximumOfTwo :: Int -> Int -> Int
maximumOfTwo = \x y -> if x > y then x else y

main :: IO ()
main = print (maximumOfTwo 10 20)
