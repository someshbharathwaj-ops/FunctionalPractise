-- QUESTION:
-- Given a list of sales entries as (product, quantity, unitPrice), remove invalid records, compute
-- total revenue, and identify the product with the highest price using functional transformations.
--
-- CONCEPT:
-- List comprehensions, folds, tuple decomposition, data cleaning.
--
-- DIFFICULTY:
-- Intermediate
--
-- APPROACH:
-- Filter out malformed entries first, then derive each report value from the cleaned dataset. The
-- total revenue uses a fold, while the highest-priced product is extracted with a fold over tuples.
--
-- EXAMPLE RUN:
-- Total Sales Revenue: 3750
-- Highest Price Product: ("Laptop",800)
--
-- NOTES:
-- Empty names and non-positive quantities are treated as invalid because they distort the analytics.

type Sale = (String, Int, Int)

cleanSales :: [Sale] -> [Sale]
cleanSales = filter isValidSale
  where
    isValidSale (product, quantity, _) = not (null product) && quantity > 0

totalRevenue :: [Sale] -> Int
totalRevenue = foldl (\revenue (_, quantity, unitPrice) -> revenue + quantity * unitPrice) 0

highestPricedProduct :: [Sale] -> Maybe (String, Int)
highestPricedProduct [] = Nothing
highestPricedProduct ((product, _, unitPrice) : rest) =
    Just (name, price)
  where
    (name, _, price) = foldl chooseHigher (product, 0, unitPrice) rest
    chooseHigher current@(_, _, currentPrice) candidate@(_, _, candidatePrice)
        | candidatePrice > currentPrice = candidate
        | otherwise = current

sampleSales :: [Sale]
sampleSales =
    [ ("Laptop", 2, 800)
    , ("Smartphone", 1, 500)
    , ("Headphones", 5, 50)
    , ("Laptop", 1, 800)
    , ("Smartwatch", 3, 150)
    , ("", 2, 100)
    , ("Tablet", -1, 400)
    , ("Headphones", 3, 50)
    ]

main :: IO ()
main = do
    let cleanedSales = cleanSales sampleSales
    putStrLn ("Total Sales Revenue: " ++ show (totalRevenue cleanedSales))
    putStrLn ("Highest Price Product: " ++ show (highestPricedProduct cleanedSales))
