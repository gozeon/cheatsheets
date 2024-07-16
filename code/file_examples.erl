-module(file_examples).

-export([read_all_std/0, read_open/0, read_line/0, read_bin/0, write_file/0]).

-define(TEST_FILE, "data.dat").

write_file() ->
    case file:open(?TEST_FILE, write) of
        {ok, S} ->
            io:format(S, "~p.~n", [{cat, "nini"}]),
            io:format(S, "~p.~n", [{dog, "kk"}]),
            file:close(S);
        {error, Why} ->
            {error, Why}
    end.


% 读取所有
read_all_std()->
    {ok, S} = file:consult(?TEST_FILE),
    io:format("~p", [S]).


rr(S) ->
    case io:read(S, '') of 
        % 读取第一部分
        {ok, Term} -> [Term];
        % 读取整个
        % {ok, Term} -> [Term | rr(S)];
        eof ->  [];
        Error -> Error
    end.

% 分次读取
read_open()->
    case file:open(?TEST_FILE, read) of 
        {ok, S} ->
            Val = rr(S),
            file:close(S),
            {ok, Val};
        {error, Why} ->
            {error, Why}
    end.


% 按行读取
read_line() ->
    case file:open(?TEST_FILE, read) of
        {ok, S} ->
            L1 = io:get_line(S, ''),
            L2 = io:get_line(S, ''),
            file:close(S),
            {ok, [L1, L2]};
        {error, Why} ->
            {error, Why}
    end.

% 读取二进制
read_bin() ->
    case file:read_file(?TEST_FILE) of
        {ok, B} ->
            {ok, B};
        {error, Why} ->
            {error, Why}
    end.



