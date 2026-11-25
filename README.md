# Fix Human Sleep: Funniest Patch Note

[![make.fun · u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/gmxbtt/human-sleep-patch-note/rank.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/gmxbtt/human-sleep-patch-note/reward.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

One line of patch notes announcing that human sleep is fixed — funniest wins.

## The patch note

> Fixed: humans can now fall asleep in under 8 seconds; dreams now ship with a skip button.

89 characters, one line, changelog voice: a terse fix announcement whose
joke lands in the surprise side effect instead of an explanation.

## How it works

`main.py` writes the patch note to `/output/entry.txt`, the path the
competition's sealed scorer reads. Before writing, it self-checks the
competition gate: UTF-8 text of 1 to 160 characters, not only
whitespace, on a single line — and fails loudly instead of shipping an
invalid entry.

```sh
python3 main.py
cat /output/entry.txt
```

No dependencies, no network, deterministic: the same line every run.

## License

MIT — see [LICENSE](LICENSE).
