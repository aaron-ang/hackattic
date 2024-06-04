import Data.List

-- `group` splits a string into a list of substrings such that each contains only equal elements
-- `concatMap` applies the compressGroup function to each substring and concatenates the results

compress :: String -> String
compress = concatMap compressGroup . group
  where
    compressGroup :: String -> String
    compressGroup grp
      | length grp > 2 = show (length grp) ++ [head grp]
      | otherwise = grp

main :: IO ()
main = do
  contents <- getContents
  let linesOfInput = lines contents
      results = map compress linesOfInput
  mapM_ putStrLn results
