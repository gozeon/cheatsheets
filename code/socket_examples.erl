-module(socket_examples).

-export([nano_get_url/0, start_nano_server/0,  nano_client_eval/1, start_parallel_server/0, error_test/0, start_udp_server/0, udp_client/1]).

-define(TEST_HOST, "www.erlang.org").

% 从服务器获取数据
nano_get_url() ->
    nano_get_url(?TEST_HOST).

nano_get_url(Host) ->
    {ok, Socket} = gen_tcp:connect(Host, 80, [binary, {packet, 0}]),
    ok = gen_tcp:send(Socket, "GET / HTTP/1.0\r\n\r\n"),
    receive_data(Socket, []).
    % 格式化输出
    %  string:tokens(binary_to_list(receive_data(Socket, [])), "\r\n").

receive_data(Socket, SoFar) ->
    receive
        {tcp, Socket, Bin} ->
            receive_data(Socket, [Bin|SoFar]);
        {tcp_closed, Socket} ->
            list_to_binary(lists:reverse(SoFar))
    end.


% 一个简单的TCP服务器
start_nano_server() ->
    {ok, Listen} = gen_tcp:listen(2345, [binary, {packet,4}, {reuseaddr, true}, {active, true}]),
    % 收到消息，返回消息后会立刻退出
    % {ok, Socket} = gen_tcp:accept(Listen),
    % gen_tcp:close(Listen),
    % loop(Socket).

    % 顺序：一次接受一个
    seq_loop(Listen).

seq_loop(Listen) ->
    {ok, Socket} = gen_tcp:accept(Listen),
    loop(Socket),
    seq_loop(Listen).

loop(Socket) ->
    receive
        {tcp, Socket, Bin} ->
            io:format("Server receive binary = ~p~n", [Bin]),
            Str = binary_to_term(Bin),
            io:format("Server (unpackaed) ~p~n", [Str]),
            Reply = string:to_upper(Str),
            io:format("Server replying = ~p~n", [Reply]),
            gen_tcp:send(Socket, term_to_binary(Reply)),
            loop(Socket);
        {tcp_closed, Socket} ->
            io:format("Server socket closed~n")
    end.
nano_client_eval(Str) ->
    {ok, Socket} = gen_tcp:connect("localhost", 2345, [binary, {packet, 4}]),
    ok = gen_tcp:send(Socket, term_to_binary(Str)),
    receive
        {tcp, Socket, Bin} ->
            io:format("Client received binary = ~p~n", [Bin]),
            Val = binary_to_term(Bin),
            io:format("client recieved result = ~p~n", [Val]),
            gen_tcp:close(Socket)
    end.

% 并行: 同时 接受多个并行连接
start_parallel_server() ->
    {ok, Listen} = gen_tcp:listen(2345, [binary, {packet,4}, {reuseaddr, true}, {active, true}]),
    spawn(fun() -> par_connect(Listen) end).

par_connect(Listen) ->
    {ok, Socket} = gen_tcp:accept(Listen),
    spawn(fun() -> par_connect(Listen) end),
    loop(Socket).

% 异常处理
error_test() ->
    spawn(fun() -> error_test_server() end),
    timer:sleep(2000),
    {ok, Socket} = gen_tcp:connect("localhost", 4321, [binary, {packet, 4}]),
    io:format("connect: ~p~n", [Socket]),
    gen_tcp:send(Socket, <<"1234">>),
    receive
        Any ->
            io:format("Any=~p~n", [Any])
    end.

error_test_server() ->
    {ok, Listen} = gen_tcp:listen(4321, [binary, {packet,2}]),
    {ok, Socket} = gen_tcp:accept(Listen),
    error_test_server_loop(Socket).

error_test_server_loop(Socket) ->
    receive
        {tcp, Socket, Data} ->
            io:format("receive: ~p~n", [Data]),
            _ = atom_to_list(Data),
            error_test_server_loop(Socket)
    end.


% 一个简单的udp

start_udp_server() ->
    spawn(fun() -> udp_server(4000) end).
udp_server(Port) ->
    {ok, Socket}= gen_udp:open(Port, [binary]),
    io:format("Server open udp ~p ~n", [Socket]),
    udp_loop(Socket).

udp_loop(Socket) ->
    receive
        {udp, Socket, Host, Port, Bin} = Msg ->
            io:format("server receive ~p~n", [Msg]),
            N= binary_to_term(Bin),
            Fac = fac(N),
            gen_udp:send(Socket, Host, Port, term_to_binary(Fac)),
            udp_loop(Socket)
    end.

fac(0) -> 1;
fac(N) -> N * fac(N-1).

udp_client(N) ->
    {ok, Socket} = gen_udp:open(0, [binary]),
    io:format("clientopn ~p~n", [Socket]),
    ok = gen_udp:send(Socket, "localhost", 4000, term_to_binary(N)),
    Value = receive
                {udp, Socket, _, _, Bin} = Msg ->
                    io:format("clienr receive ~p~n", [Msg]),
                    binary_to_term(Bin)
            after 2000 ->
                    0
            end,
    gen_udp:close(Socket),
    Value.
