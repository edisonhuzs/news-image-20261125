# The World Today — 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/edisonhuzs/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/edisonhuzs/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A newspaper front page that sums up the world's news of Wednesday, 25 November 2026, in a single image. The masthead reads "The World Today", the date line names the day, and the front page carries the day's four biggest stories plus an "Also today" strip of five more. The lead illustration — a warship at dusk, an explosion on the horizon — is drawn for this page, not a photograph, and every story is labelled in plain words so the page reads on its own.

## What is in the picture

- **Lead story — Ukraine strikes Russian ships in the Baltic and off Libya.** Kyiv said its forces hit Russian vessels in the Baltic Sea and off the Libyan coast. President Volodymyr Zelenskyy confirmed the attacks, and Moscow called them "terrorism". The front page illustrates it with a warship at dusk under an orange sky, an explosion lighting the horizon.
- **COP31 collapses in Antalya — no deal on fossil fuels.** Climate talks in Antalya ended without agreement on phasing out fossil fuels, as the divide between major emitters and vulnerable states held.
- **Houthis hit Riyadh's tallest tower, 11 wounded.** A Houthi attack struck the tallest tower in Riyadh, wounding 11 people, in a sharp escalation of the conflict spilling across the region.
- **700,000 Russian troops killed in Ukraine war, new analysis finds.** A new analysis puts Russian military deaths in the Ukraine war at 700,000.
- **Also today:** NATO to deploy early-warning aircraft in Poland; Iran tankers hit by mines in Hormuz; Gaza toll 74,746; Trump pardons turkeys Freedom and Feathers; Sarkozy corruption case to trial.

## Run it

```sh
python3 main.py
```

`main.py` copies the front page in this repository (`entry.png`) to `/output/entry.png`, then prints the byte count and SHA-256 of what it wrote. It needs no network and no extra packages — Python 3 standard library only.

## Verification

```sh
python3 main.py --out /tmp/check/entry.png
python3 main.py --out /tmp/check2/entry.png
sha256sum /tmp/check/entry.png /tmp/check2/entry.png
```

The two runs must print the same byte count and the same SHA-256, and the output file must be a 1024 by 1024 PNG under 1 MiB — the gate's limits. The checked-in image is 113873 bytes with SHA-256 `a0e2c47f4340ce122a9965464ed91ff0dd93a3be3c189fb515d1a7c2dbc20d36`. `main.py` also re-reads the file it just wrote and refuses to report success if the copy does not match.

---

<sub>Entered on [make.fun](https://make.fun/?ref=ch95n9v3&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
