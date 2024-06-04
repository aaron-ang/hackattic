almostBinary :: String -> Int
almostBinary binaryStr = go (reverse binaryStr) 0 0 -- reverse the string, start with pos = 0, accumulator = 0
  where
    go [] _ acc = acc -- base case: empty string
    go ('.' : xs) pos acc = go xs (pos + 1) acc -- skip dot
    go ('#' : xs) pos acc = go xs (pos + 1) (acc + 2 ^ pos) -- add 2 ^ pos to the accumulator
    go _ _ _ = error "invalid input"

main :: IO ()
main = do
  contents <- getContents
  let linesOfInput = lines contents
      results = map almostBinary linesOfInput
  mapM_ print results