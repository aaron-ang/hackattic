import Data.Char

hungarianToSnakeCase :: String -> String
hungarianToSnakeCase = stripTrailingUnderscore . snakeCase . stripPrefix
  where
    stripPrefix :: String -> String
    stripPrefix xs
      | length prefix > 3 = xs
      | otherwise = drop (length prefix) xs
      where
        prefix = takeWhile (\c -> isLower c || isDigit c) xs
    snakeCase :: String -> String
    snakeCase [] = []
    snakeCase (x : xs)
      | isUpper x = '_' : toLower x : snakeCase xs
      | otherwise = x : snakeCase xs
    stripTrailingUnderscore :: String -> String
    stripTrailingUnderscore (x : xs)
      | x == '_' = stripTrailingUnderscore xs
      | otherwise = x : xs

main :: IO ()
main = do
  contents <- getContents
  let linesOfInput = lines contents
      results = map hungarianToSnakeCase linesOfInput
  mapM_ putStrLn results