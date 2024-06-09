defmodule SumThings do
  def parse_and_sum(input) do
    input
    |> String.split(" ")
    |> Enum.map(&parse_component/1)
    |> Enum.sum()
  end

  defp parse_component(str) do
    cond do
      # hexadecimal
      String.starts_with?(str, "0x") ->
        {value, _} = Integer.parse(String.slice(str, 2..-1), 16)
        value

      # octal
      String.starts_with?(str, "0o") ->
        {value, _} = Integer.parse(String.slice(str, 2..-1), 8)
        value

      # binary
      String.starts_with?(str, "0b") ->
        {value, _} = Integer.parse(String.slice(str, 2..-1), 2)
        value

      # decimal
      Regex.match?(~r/^\d+$/, str) ->
        String.to_integer(str)

      # ascii character
      String.length(str) == 1 ->
        String.to_charlist(str) |> hd()

      true ->
        raise "Invalid input: #{str}"
    end
  end
end

inputs = IO.stream(:stdio, :line) |> Stream.map(&String.trim/1)

inputs
|> Stream.each(&IO.puts(SumThings.parse_and_sum(&1)))
|> Stream.run()
