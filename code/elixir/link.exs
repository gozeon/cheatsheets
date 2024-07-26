defmodule Link do
  import :timer, only: [sleep: 1]

  def sad_function do
    sleep(500)
    exit(:boom)
  end

  def run do
    # Process.flag(:trap_exit, true)
    # spawn_link(Link, :sad_function, [])

    res = spawn_monitor(Link, :sad_function, [])
    IO.puts inspect(res)
    receive do
      msg ->
        IO.puts("Message receive: #{inspect(msg)}")
    after
      1000 ->
        IO.puts("timeout")
    end
  end
end

