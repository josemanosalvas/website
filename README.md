# josemanosalvas.ch

The homepage at [josemanosalvas.ch](https://josemanosalvas.ch). Set in Mitad, my personal
design system: its faces and colours, with a composition of its own.

## What's here

```
index.html               the whole site: markup, CSS, script, fonts and favicon inline
OFL.txt                  licence for the embedded fonts
tools/inline-fonts.py    subsets the fonts to the page's text and embeds them
```

A visit is one request. The CSS is only what the page uses, and the three fonts are subset to
the characters they draw (about 17 KB in total) and embedded as base64.

## Changing the text

The fonts only contain the characters on the page. After editing the greetings, the name,
the email or the GitHub label, update the `text` entries in `tools/inline-fonts.py` to match, then
regenerate the fonts from the Mitad repo checked out next to this one:

```sh
pip install fonttools brotli
python3 tools/inline-fonts.py              # or pass the path to design-system/fonts
```

A character that isn't in the subset falls back to Helvetica, Georgia or Courier.

## Previewing locally

Open `index.html` in a browser. Nothing else needs to load.

## Deploying to Infomaniak

The site is hosted on Infomaniak's free Starter web hosting. Upload `index.html` and
`OFL.txt` to the web root using Web FTP in the Infomaniak Manager or any FTP client.

The Starter plan has no IPv6, so make sure the domain has no AAAA record, or SSL may not
activate.

## Fonts

Archivo, Literata and B612 Mono are licensed under the SIL Open Font License 1.1, see
`OFL.txt`.
