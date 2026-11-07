# josemanosalvas.ch

The homepage at [josemanosalvas.ch](https://josemanosalvas.ch). One static page, set in
Mitad, my personal design system.

## What's here

```
index.html        the page (site-only styles and the greeting script are inline)
favicon.svg       a horizon line
css/mitad.css     copy of design-system/dist/mitad.css
fonts/            Archivo, Literata, B612 Mono (woff2) + OFL.txt
```

No build step and no external requests: fonts are self-hosted, so the page loads nothing
from Google or any other third party.

## Updating Mitad

`css/mitad.css` and `fonts/` are copied from the design-system repo. After changing Mitad:

```sh
cp ../design-system/dist/mitad.css css/mitad.css
cp ../design-system/fonts/*.woff2 ../design-system/fonts/OFL.txt fonts/
```

`mitad.css` loads fonts from `../fonts/`, so keep `css/` and `fonts/` side by side.

## Previewing locally

Fonts don't load reliably over `file://`, so serve the folder:

```sh
python3 -m http.server 8000   # then open http://localhost:8000
```

## Deploying to Infomaniak

The site is hosted on Infomaniak's free Starter web hosting (10 MB). Upload these files to
the web root, keeping the folder structure:

- `index.html`, `favicon.svg`
- `css/`
- `fonts/`

Use Web FTP in the Infomaniak Manager or any FTP client. The repo's `README.md` doesn't need
to go up.

The Starter plan has no IPv6, so make sure the domain has no AAAA record, or SSL may not
activate.

## Fonts

Archivo, Literata and B612 Mono are licensed under the SIL Open Font License 1.1, see
`fonts/OFL.txt`.
