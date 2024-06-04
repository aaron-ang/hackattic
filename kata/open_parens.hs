import Data.List

solveOpenParens :: String -> String
solveOpenParens = go 0 -- count of open parentheses
  where
    go 0 [] = "yes" -- empty string and no open parentheses
    go _ [] = "no" -- empty string with some open parentheses
    go n (x : xs) -- n = no. of open parentheses, x = current character, xs = rest of input
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
