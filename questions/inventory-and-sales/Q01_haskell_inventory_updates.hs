-- QUESTION:
-- Model an inventory as a list of (product, quantity) pairs. Write pure functions to add stock,
-- remove stock safely, update the inventory through a higher-order function, and use a fold to
-- identify the product with the highest quantity.
--
-- CONCEPT:
-- Higher-order functions, tuple processing, recursion, folds, immutable state updates.
--
-- DIFFICULTY:
-- Intermediate
--
-- APPROACH:
-- Traverse the association list recursively for updates, preserving order and replacing only the
-- matching product. Removal rejects impossible updates with an Either value instead of using
-- sentinel tuples. The highest-stock product is computed with foldl.
--
-- EXAMPLE RUN:
-- Added inventory: [("apple",15),("banana",8),("pear",11)]
-- Reduced inventory: [("apple",10),("banana",8),("pear",11)]
-- Highest stock: Just ("pear",11)
--
-- NOTES:
-- The original code already suggested a higher-order update function. This version keeps that idea
-- and makes stock changes total, explicit, and purely functional.

type Product = String
type Quantity = Int
type Inventory = [(Product, Quantity)]
type StockUpdate = Inventory -> (Product, Quantity) -> Either String Inventory

addStock :: Inventory -> (Product, Quantity) -> Either String Inventory
addStock inventory (product, quantity)
    | quantity <= 0 = Left "Quantity to add must be positive."
    | otherwise = Right (go inventory)
  where
    go [] = [(product, quantity)]
    go ((name, available) : rest)
        | name == product = (name, available + quantity) : rest
        | otherwise = (name, available) : go rest

removeStock :: Inventory -> (Product, Quantity) -> Either String Inventory
removeStock inventory (product, quantity)
    | quantity <= 0 = Left "Quantity to remove must be positive."
    | otherwise = go inventory
  where
    go [] = Left "No products left with the requested name."
    go ((name, available) : rest)
        | name /= product = ((name, available) :) <$> go rest
        | available < quantity = Left "Insufficient stock for the requested removal."
        | available == quantity = Right rest
        | otherwise = Right ((name, available - quantity) : rest)

updateStock :: StockUpdate -> Inventory -> (Product, Quantity) -> Either String Inventory
updateStock updater inventory item = updater inventory item

highestQuantity :: Inventory -> Maybe (Product, Quantity)
highestQuantity [] = Nothing
highestQuantity (entry : rest) =
    Just (foldl chooseHigher entry rest)
  where
    chooseHigher current@(_, currentQty) candidate@(_, candidateQty)
        | candidateQty > currentQty = candidate
        | otherwise = current

main :: IO ()
main = do
    let baseInventory = [("apple", 10), ("banana", 8), ("pear", 11)]
    case updateStock addStock baseInventory ("apple", 5) of
        Left err -> putStrLn err
        Right expandedInventory -> do
            putStrLn ("Added inventory: " ++ show expandedInventory)
            case updateStock removeStock expandedInventory ("apple", 5) of
                Left removalErr -> putStrLn removalErr
                Right reducedInventory -> do
                    putStrLn ("Reduced inventory: " ++ show reducedInventory)
                    putStrLn ("Highest stock: " ++ show (highestQuantity reducedInventory))
