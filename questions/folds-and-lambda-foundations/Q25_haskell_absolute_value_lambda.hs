-- QUESTION:
-- Compute the absolute value of an integer with a lambda.
--
-- CONCEPT:
-- Lambdas, numeric normalization.
--
-- DIFFICULTY:
-- Beginner
--
-- APPROACH:
-- Apply `abs` through a lambda-based definition.
--
-- EXAMPLE RUN:
-- absoluteWithLambda (-5) == 5

absoluteWithLambda :: Int -> Int
absoluteWithLambda = \x -> abs x

main :: IO ()
main = print (absoluteWithLambda (-5))
