-- QUESTION:
-- Square an integer using a lambda expression.
--
-- CONCEPT:
-- Lambdas, unary numeric transformation.
--
-- DIFFICULTY:
-- Beginner
--
-- APPROACH:
-- Use a one-parameter lambda that multiplies the value by itself.
--
-- EXAMPLE RUN:
-- squareWithLambda 4 == 16

squareWithLambda :: Int -> Int
squareWithLambda = \x -> x * x

main :: IO ()
main = print (squareWithLambda 4)
