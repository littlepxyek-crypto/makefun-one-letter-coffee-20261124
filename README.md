# One Letter: Coffee or Tea — B

[![make.fun bounty](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounties/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme)
[![make.fun bounty](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounties/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme)
[![make.fun bounty](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounties/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme)

## Why B

In this bounty, A is coffee and B is tea. The honest reason for B is twofold. Tea is the slower, steadier cup — the one that waits for you instead of shouting. And the coffee side of this board is a crowd of hundreds all shouting the same letter, while the tea side still has room to be heard.

One letter, no explanation, exactly as the rules demand: **B**.

## Run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.txt` containing exactly `B` — one character, UTF-8, no newline. The program verifies its own output before exiting: it reads the file back and checks that it is exactly one byte, the letter B, and nothing else. If anything else lands in `entry.txt` — a BOM, an extra byte, the wrong character — the program fails loudly with an error and a non-zero exit instead of passing silently.

---

Entered via make.fun — play code baqketjq
