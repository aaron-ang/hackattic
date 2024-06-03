import Data.List

solveOpenParens :: String -> String
solveOpenParens = go 0
  where
    go 0 [] = "yes" -- empty string
    go _ [] = "no" -- no more input
    go n (x : xs) -- n is the number of open parentheses, x is the current character, xs is the rest of the input
      | n < 0 = "no"
      | x == '(' = go (n + 1) xs
      | x == ')' = go (n - 1) xs
      | otherwise = go n xs -- ignore other characters

main :: IO ()
main = do
  contents <- getContents
  let linesOfInput = lines contents
      results = map solveOpenParens linesOfInput
  mapM_ putStrLn results
