fizzBuzz :: Int -> String
fizzBuzz n
  | n `mod` 15 == 0 = "FizzBuzz"
  | n `mod` 3 == 0 = "Fizz"
  | n `mod` 5 == 0 = "Buzz"
  | otherwise = show n

main :: IO ()
main = do
  input <- getLine
  let [n, m] = map read (words input) :: [Int] -- words splits a string on whitespace and newline
  mapM_ (putStrLn . fizzBuzz) [n .. m]