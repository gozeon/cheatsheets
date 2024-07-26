## 命令行

```
# 帮助
iex> h
iex> h Enum
iex> h IEx

# 查看类型
iex> i
iex> i 10
iex> i %{a: 1}

# 编译和执行文件

iex> c "hello.exs"
```

## 模式匹配(pattern matching)

```
# 正常匹配
iex(8)> list  = [1, 2, 3]
[1, 2, 3]
iex(9)> [a, b, c] = list
[1, 2, 3]
iex(10)> a
1
iex(11)> b
2
iex(12)> c
3

# 错误匹配
iex> list = [1, 2, 3]
[1, 2, 3]
iex> [a, 1, b ] = list
** (MatchError) no match of right hand side value: [1, 2, 3]

# 忽略

iex> [1, _, _] = [1, 2, 3]

# 不可变(bind once/per macth)
iex(25)> [a, a] = [1, 1]
[1, 1]
iex(26)> a
1
iex(27)> [b, b] = [1, 2]
** (MatchError) no match of right hand side value: [1, 2]
    (stdlib 5.2.1) erl_eval.erl:498: :erl_eval.expr/6
    iex:27: (file)

# 不可变锁定
iex(38)> a = 2
2
iex(39)> [^a, 2, 3] = [1, 2, 3]
** (MatchError) no match of right hand side value: [1, 2, 3]
    (stdlib 5.2.1) erl_eval.erl:498: :erl_eval.expr/6
    iex:39: (file)
iex(39)> a
2
```

## 不可变性(immutability)

> 没用erlang里面那么变态，但函数式编程思想一致

```
iex(48)> list = [3, 2, 1]
[3, 2, 1]
iex(49)> list2 = [4 | list]
[4, 3, 2, 1]
iex(50)> name = "elixir"
"elixir"
iex(51)> name1 = String.capitalize name
"Elixir" 
iex(52)> name
"elixir"
```

## 基本类型 basics

```
# integers and float

iex(56)> 1234
1234
iex(57)> 10_000
10000
iex(58)> 1_0000
10000
iex(59)> 1.0
1.0
iex(60)> 3.1415923
3.1415923
iex(61)> 0.314159e1
3.14159

# atom

iex> :abc

# regex

iex(68)> Regex.run ~r{[aeiou]}, "cateprillar"
["a"]
iex(69)> Regex.scan ~r{[aeiou]}, "cateprillar"
[["a"], ["e"], ["i"], ["a"]]
iex(70)> Regex.split ~r{[aeiou]}, "cateprillar"
["c", "t", "pr", "ll", "r"]
iex(71)> Regex.replace ~r{[aeiou]}, "cateprillar", "*"
"c*t*pr*ll*r"

# tuples
iex(72)> {1, 2}
{1, 2}
iex(73)> {:ok, 42, "next"}
{:ok, 42, "next"}

# list
iex(2)> [1, 2, 3] ++ [4, 5, 6]
[1, 2, 3, 4, 5, 6]
iex(3)> [1, 2, 3] -- [2, 4]
[1, 3]
iex(4)> 1 in [1, 2]
true
iex(5)> "wombat" in [1]
false
iex(6)>

# keyword list
iex(7)> [name: "a", city: "d"]
[name: "a", city: "d"]
iex(8)> [{:name, "a"}, {:city, "d"}]
[name: "a", city: "d"]

# map
iex(10)> states = %{"key" => 1}
iex(15)> states = %{"k" => "s"}
%{"k" => "s"}
iex(16)> resp = %{{:error, :enoent} => :fatal, {:error, :busy} => :retry}
%{{:error, :busy} => :retry, {:error, :enoent} => :fatal}
iex(17)> colors = %{:red => 0xff0000, :green => 0x00ff00, :blue => 0x0000ff}
%{green: 65280, red: 16711680, blue: 255}
iex(19)> colora = %{red: 0xff0000, green: 0x00ff00,  blue: 0x0000ff}
%{green: 65280, red: 16711680, blue: 255}

# map取值
iex(2)> state = %{"a" => 1, :a => 2}
%{:a => 2, "a" => 1}
iex(3)> state["a"]
1
iex(4)> state[:a]
2
```

## 匿名函数

```
iex(11)> sum = fn(a,b) -> a+b end
#Function<41.105768164/2 in :erl_eval.expr/6>
iex(12)> sum.(1,2)
3

iex(15)> h = fn -> IO.puts "H" end
#Function<43.105768164/0 in :erl_eval.expr/6>
iex(16)> h.()
H
:ok
iex(17)> swap = fn {a, b} -> {b, a} end
#Function<42.105768164/1 in :erl_eval.expr/6>
iex(18)> swap.({1, 2})
{2, 1}

# 闭包
iex(19)> fun1 = fn -> (fn -> "h" end) end
#Function<43.105768164/0 in :erl_eval.expr/6>
iex(20)> fun2 = fun1.()
#Function<43.105768164/0 in :erl_eval.expr/6>
iex(21)> fun2.()
"h"
iex(22)> fun1.().()
"h"
```

## 数据扩展

```
defmodule Cat do
  defstruct name: "", age: 0
  def log(cat = %Cat{}) do
    IO.inspect(cat)
  end
end

cat = %Cat{name: "ca", age: 1}
Cat.log(cat)
```

## Binaries

> elixir 有字符串类型, 区分单双引号

```
iex(43)> b = <<1,2,3>>
<<1, 2, 3>>
iex(44)> byte_size b
3
iex(45)> bit_size b
24

iex> b = << 1::size(2), 1::size(3) >> # 01 001
<<9::size(5)>>                        # = 9 (base 10)
iex> byte_size b
1
iex> bit_size b
5
```

## spawn

```elixir title="spawn.exs"
--8<-- "code/elixir/spawn.exs"
```

## link

```elixir title="link.exs"
--8<-- "code/elixir/link.exs"
```
