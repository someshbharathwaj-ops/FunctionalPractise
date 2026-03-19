-- QUESTION:
-- Implement `map` for integer lists using folds, and compare a `foldl`-based version with a
-- `foldr`-based version.
--
-- CONCEPT:
-- Higher-order functions, folds, order preservation.
--
-- DIFFICULTY:
-- Intermediate
--
-- APPROACH:
-- `foldr` naturally preserves left-to-right order when rebuilding the list. The `foldl` version
-- first builds a reversed mapped list and then reverses it to restore the original order.
--
-- EXAMPLE RUN:
-- mapWithFoldL (+1) [1,2,3] == [2,3,4]
-- mapWithFoldR (^2) [1,2,3] == [1,4,9]
--
-- NOTES:
-- The source material contained both `foldl` and `foldr` variants; this version makes the
-- difference in order handling explicit.

mapWithFoldL :: (Int -> Int) -> [Int] -> [Int]
mapWithFoldL transform values =
    reverse (foldl (\acc value -> transform value : acc) [] values)

mapWithFoldR :: (Int -> Int) -> [Int] -> [Int]
mapWithFoldR transform = foldr (\value acc -> transform value : acc) []

main :: IO ()
main = do
    print (mapWithFoldL (+ 1) [1, 2, 3])
    print (mapWithFoldR (^ (2 :: Int)) [1, 2, 3])
