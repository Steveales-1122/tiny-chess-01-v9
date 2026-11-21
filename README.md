# Tiny Chess v9

A chess engine in 4,067 bytes of Python (stdlib only), built for
[make.fun](https://make.fun)'s tiny-chess-01 bounty.

Engine: 0x88 board, negamax alpha-beta with iterative deepening to a
fixed 100,000-node budget, quiescence over captures/promotions/check
evasions, check extension, transposition table, MVV-LVA ordering,
Chebyshev piece-square table, pawn-advancement bonus and endgame king
centralisation. Legal chess: castling, en passant, promotion
(queen only), check/checkmate/stalemate. No clock, no randomness:
the same position always gives the same move.

Play: `python3 -P -s main.py` with `MAKEFUN_ENV_URL` pointing at the
trial env. It polls `/game`, searches, and posts each move to `/move`
until the trial is done.
