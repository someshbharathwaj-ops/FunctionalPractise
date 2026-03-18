-- QUESTION:
-- Compute a library fine from the number of delayed days, member type, reference-book status, and
-- reminder status. The result combines a daily rate with additional rule-based penalties.
--
-- CONCEPT:
-- Guards, decomposition into helper functions, rule-based functional design.
--
-- DIFFICULTY:
-- Beginner
--
-- APPROACH:
-- Break the calculation into independent pure functions for the daily rate and each surcharge. This
-- keeps the business rules readable and makes the total composition explicit.
--
-- EXAMPLE RUN:
-- Student fine: 165
-- Faculty fine: 380
--
-- NOTES:
-- The original file had text/encoding issues around the reminder rule. This version assumes a
-- penalty is added when a digital reminder was not sent.

data MemberType = Student | Faculty deriving (Eq, Show)

fineCalculator :: Int -> MemberType -> Bool -> Bool -> Int
fineCalculator 0 _ _ _ = 0
fineCalculator delayedDays memberType isReferenceBook reminderSent =
    baseFine delayedDays memberType
        + referenceCharge isReferenceBook
        + reminderCharge reminderSent
        + longDelayCharge delayedDays

baseFine :: Int -> MemberType -> Int
baseFine delayedDays Student = 5 * delayedDays
baseFine delayedDays Faculty = 10 * delayedDays

referenceCharge :: Bool -> Int
referenceCharge True = 100
referenceCharge False = 0

reminderCharge :: Bool -> Int
reminderCharge True = 0
reminderCharge False = 50

longDelayCharge :: Int -> Int
longDelayCharge delayedDays
    | delayedDays > 15 = 200
    | otherwise = 0

main :: IO ()
main = do
    putStrLn ("Student fine: " ++ show (fineCalculator 3 Student True False))
    putStrLn ("Faculty fine: " ++ show (fineCalculator 18 Faculty False True))
