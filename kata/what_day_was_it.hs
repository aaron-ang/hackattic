import Data.Time (DayOfWeek (..), dayOfWeek)
import Data.Time.Calendar (Day, addDays, fromGregorian)

epochDate :: Day
epochDate = fromGregorian 1970 1 1

dayOfWeekName :: DayOfWeek -> String
dayOfWeekName day = case day of
  Sunday -> "Sunday"
  Monday -> "Monday"
  Tuesday -> "Tuesday"
  Wednesday -> "Wednesday"
  Thursday -> "Thursday"
  Friday -> "Friday"
  Saturday -> "Saturday"

getDay :: String -> String
getDay line =
  let days = read line :: Integer
      targetDate = addDays days epochDate
   in dayOfWeekName $ dayOfWeek targetDate

main :: IO ()
main = do
  contents <- getContents
  let linesOfInput = lines contents
      results = map getDay linesOfInput
  mapM_ putStrLn results