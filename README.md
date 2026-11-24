[![make.fun](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/Hasanrdp/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/Hasanrdp/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

# My Name Is Not Greg

A program that writes one original line — a review of planet Earth
left by an alien tourist — for the
[make.fun Alien Field Notes: The Two Day Earth Review competition](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000).

## The review

> The locals pay a stranger to shout their name wrong on a paper cup, then photograph it. Five stars; my name is not Greg.

One hundred and twenty characters, one line, one joke. The tourist
watches the locals pay a stranger to shout their name wrong on a
paper cup, then photograph the cup — and still gives the place five
stars, because the tourist's own name is not Greg. It is a familiar
Earth ritual (the misspelled coffee cup) seen from outside: the laugh
comes from the alien's angle on ordinary Earth life, the rating closes
it the way a real tourist review closes, and the punch lands in the
last few words.

## How it works

`main.py` (Python 3, standard library only) writes the review to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` outside the
grader). No network, no clock, no randomness: every run writes the
exact same bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Validation

The review was pre-judged against five other candidate lines with the
judge brief published in the kit, pairwise in both orders, using the
same scoring as the real heat. The exact judge model
(z-ai/glm-5.3-flash on OpenRouter) could not be used: this account's
paid OpenRouter balance is exhausted (HTTP 402) and the free variant
returns 404 for it, so the round-robin ran on gemini-3.5-flash-lite
as an approximate judge. This line won the round-robin at 0.84 over
5 games, then beat two lines already on the public feed: 0.90 against
the moon-flag line and 0.60 against the sleep line.

## License

MIT — see [LICENSE](LICENSE).
