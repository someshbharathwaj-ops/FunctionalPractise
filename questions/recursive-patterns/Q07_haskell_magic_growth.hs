-- QUESTION:
-- Define a recursive function that starts from a base value `h` and applies `n` growth steps. For
-- each odd step multiply the recursive result by 3; for each even step add 1.
--
-- CONCEPT:
-- Primitive recursion, parity-based guards.
--
-- DIFFICULTY:
-- Beginner
--
-- APPROACH:
-- The base case returns the seed value. Each recursive call reduces the step count by one and then
-- applies the parity rule for the current step.
--
-- EXAMPLE RUN:
-- magicGrowth 2 5 == 23
--
-- NOTES:
-- The original function name was preserved in spirit but renamed for readability.

magicGrowth :: Int -> Int -> Int
magicGrowth seed 0 = seed
magicGrowth seed steps
    | odd steps = 3 * magicGrowth seed (steps - 1)
    | otherwise = 1 + magicGrowth seed (steps - 1)

main :: IO ()
main = print (magicGrowth 2 5)
