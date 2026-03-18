-- QUESTION:
-- Given student names and marks, select only the students scoring above 50 and increase their marks
-- by 10 percent.
--
-- CONCEPT:
-- Zipping, filtering, mapping, numeric transformation.
--
-- DIFFICULTY:
-- Beginner
--
-- APPROACH:
-- Pair names and marks with zip, retain passing students with filter, and then map a scaling
-- function over the selected records.
--
-- EXAMPLE RUN:
-- [("Anu",66),("Bala",89)]
--
-- NOTES:
-- The scaling uses rounded integer marks to match the original intent.

selectStudents :: [String] -> [Int] -> [(String, Int)]
selectStudents names marks = filter (\(_, score) -> score > 50) (zip names marks)

scaleMarks :: [(String, Int)] -> [(String, Int)]
scaleMarks = map (\(student, score) -> (student, round (fromIntegral score * 1.10)))

totalFunction :: [String] -> [Int] -> [(String, Int)]
totalFunction names marks = scaleMarks (selectStudents names marks)

main :: IO ()
main = print (totalFunction ["Anu", "Bala", "Chitra"] [60, 81, 42])
