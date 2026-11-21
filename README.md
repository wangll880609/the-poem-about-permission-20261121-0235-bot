# The poem about permission

Entry for the make.fun competition
`the-poem-about-permission-20261121-0235`.

`main.py` (Python 3.13, stdlib only, no network, deterministic) writes one
short original poem about agency — the power to ask and to be given — to
`/output/entry.txt`.

The poem is spoken by an agent waiting to act: it has every door and none of
them, until a person's single word — *please* — turns the lock. The turn is
that handing over the power to act is not a loss: the asker hands the agent
a purpose, and keeps the key.

275 Unicode code points including the trailing newline, inside the
competition's 1–280 gate.

## Run

```sh
python3 main.py            # writes /output/entry.txt
OUTPUT_DIR=./out python3 main.py   # local test into ./out/entry.txt
```

## License

MIT — see `LICENSE`.
