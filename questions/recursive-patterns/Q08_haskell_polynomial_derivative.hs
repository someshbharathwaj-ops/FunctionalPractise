-- QUESTION:
-- Represent a polynomial as a flat list of coefficient-exponent pairs and compute its derivative.
-- For example, [3,2,5,1,4,0] represents 3x^2 + 5x + 4.
--
-- CONCEPT:
-- Recursive list processing, pattern matching, symbolic differentiation.
--
-- DIFFICULTY:
-- Intermediate
--
-- APPROACH:
-- Consume the list two elements at a time. Constant terms disappear, while each non-constant term
-- contributes coefficient * exponent followed by exponent - 1.
--
-- EXAMPLE RUN:
-- derivative [3,2,5,1,4,0] == [6,1,5,0]
--
-- NOTES:
-- The input is assumed to be well-formed with an even number of integers.

derivative :: [Int] -> [Int]
derivative [] = []
derivative [coefficient] = [coefficient]
derivative (coefficient : exponent : rest)
    | exponent == 0 = derivative rest
    | otherwise = coefficient * exponent : exponent - 1 : derivative rest

main :: IO ()
main = print (derivative [3, 2, 5, 1, 4, 0])
