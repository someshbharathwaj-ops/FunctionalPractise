-- QUESTION:
-- Label an integer as `EVEN` or `ODD` using a lambda expression.
--
-- CONCEPT:
-- Lambdas, conditional expressions, parity testing.
--
-- DIFFICULTY:
-- Beginner
--
-- APPROACH:
-- Check the remainder modulo 2 inside the lambda and return the matching label.
--
-- EXAMPLE RUN:
-- parityLabel 7 == "ODD"

parityLabel :: Int -> String
parityLabel = \x -> if even x then "EVEN" else "ODD"

main :: IO ()
main = print (parityLabel 7)
