-- QUESTION:
-- Add two integers using a lambda-based function.
--
-- CONCEPT:
-- Lambdas, anonymous functions.
--
-- DIFFICULTY:
-- Beginner
--
-- APPROACH:
-- Define the function directly with a two-argument lambda.
--
-- EXAMPLE RUN:
-- addWithLambda 3 5 == 8
--
-- NOTES:
-- Curated from the `addusinglambda` exercise in the practice Haskell file.

addWithLambda :: Int -> Int -> Int
addWithLambda = \x y -> x + y

main :: IO ()
main = print (addWithLambda 3 5)
