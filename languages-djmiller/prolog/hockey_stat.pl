% Facts
player_stat(john, goals, 10).
player_stat(john, assists, 15).
player_stat(john, points, 25).
player_stat(mike, goals, 5).
player_stat(mike, assists, 20).
player_stat(mike, points, 25).
player_stat(sarah, goals, 12).
player_stat(sarah, assists, 8).
player_stat(sarah, points, 20).
player_stat(james, goals, 8).
player_stat(james, assists, 12).
player_stat(james, points, 20).

% Rules
player_high_score(Player) :-
    player_stat(Player, goals, Goals),
    player_stat(Player, assists, Assists),
    Points is Goals + Assists,
    Points >= 20.

player_total_points(Player, Points) :-
    player_stat(Player, goals, Goals),
    player_stat(Player, assists, Assists),
    Points is Goals + Assists.

% Queries
?- player_stat(john, goals, Goals).
% Returns: Goals = 10

?- player_high_score(Player).
% Returns: Player = john ; Player = mike ; Player = sarah

?- player_total_points(john, Points).
% Returns: Points = 25