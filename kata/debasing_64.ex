defmodule Debase64 do
  def decode_base64(input) do
    case Base.decode64(input) do
      {:ok, decoded} -> decoded
      :error -> "Error: Invalid Base64 input"
    end
  end
end

inputs = IO.stream(:stdio, :line) |> Stream.map(&String.trim/1)

inputs
|> Stream.each(&IO.puts(Debase64.decode_base64(&1)))
|> Stream.run()
