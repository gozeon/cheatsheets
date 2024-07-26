defmodule Spawn do
  def greet do
    receive do
      {sender, msg} ->
        send(sender, {:ok, "hello #{msg}"})

        # 如果不循环，只接受一次
        greet()
    end
  end
end

pid = spawn(Spawn, :greet, [])
send(pid, {self(), "word"})

receive do
  {:ok, message} ->
    IO.puts(message)
end

send(pid, {self(), "Goze"})

receive do
  {:ok, message} ->
    IO.puts(message)
after
  500 ->
    IO.puts("timeout")
end

