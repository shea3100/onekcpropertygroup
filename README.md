# onekcpropertygroup.com

Website for **One KC Property Group, LLC** — plain HTML and CSS, hosted free on
GitHub Pages, served over HTTPS at <https://onekcpropertygroup.com>.

No framework, no build tools required to make edits. `build.py` is optional
(see below).

---

## Live URLs

| Page | URL |
|---|---|
| Home | `https://onekcpropertygroup.com/` |
| Application Requirements | `https://onekcpropertygroup.com/requirements/` |
| FAQ | `https://onekcpropertygroup.com/faq/` |
| About Us | `https://onekcpropertygroup.com/about/` |
| Contact | `https://onekcpropertygroup.com/contact/` |

The "Resident Portal" nav item is an external link to TenantCloud, not a page
in this repo.

---

## File layout

```
index.html              Home page
requirements/index.html Application Requirements
faq/index.html          FAQ
about/index.html        About Us
contact/index.html      Contact

styles.css              All styling for every page
build.py                Optional generator (see "Making changes")

requirements.html       ┐
faq.html                │ Redirect stubs. These are the OLD addresses.
about.html              │ They bounce visitors to the new /folder/ URLs.
contact.html            ┘ Do not edit or delete.

sitemap.xml             List of pages for Google
robots.txt              Tells search engines everything is crawlable
CNAME                   Custom domain. Deleting this breaks the site.
.nojekyll               Skips GitHub's Jekyll step. Do not delete.
README.md               This file
```

**Why the folders:** GitHub Pages serves `requirements/index.html` at the URL
`/requirements/`. That is the only way to get URLs without `.html` on the end.

---

## Making changes

### Small text edits (no setup needed)

1. Open the file on GitHub — e.g. click into the `requirements` folder, then
   `index.html`.
2. Click the pencil icon.
3. Make the edit, then **Commit changes** at the top right.
4. Wait ~30 seconds. GitHub rebuilds and deploys automatically.

If the change does not appear, hard-refresh your browser
(**Cmd+Shift+R** on Mac, **Ctrl+F5** on Windows) before assuming something broke.

### Changes that affect every page

The header, nav, footer and page shell are defined once in `build.py`. Editing
that file and running it regenerates all five pages, which keeps them in sync.

```bash
python3 build.py
```

Then commit the regenerated `.html` files. You only need this for site-wide
changes (adding a nav item, changing the footer, editing contact details).

`build.py` also regenerates `sitemap.xml`, `robots.txt`, `CNAME`, `.nojekyll`
and the redirect stubs, so those stay correct automatically.

**Careful:** editing an `index.html` directly and *also* running `build.py`
later will overwrite your direct edit. Pick one approach per change.

### Stylesheet cache

`CSS_VERSION` near the top of `build.py` is appended to the stylesheet link
(`/styles.css?v=8`). If you change `styles.css`, bump that number and rebuild —
otherwise returning visitors keep seeing the old design from their browser cache.

---

## Photos

Images are free-to-use photos from [Unsplash](https://unsplash.com), linked
from Unsplash's servers rather than stored here. The photo IDs are listed at the
top of `build.py`.

**To use your own photos instead:** create an `images/` folder in this repo,
upload your files, and change the image constants in `build.py` to point at
them, e.g. `IMG_HOME_EXTERIOR = "/images/front-exterior.jpg"`. Real photos of
your properties will do more for the site than any styling change.

---

## Hosting and deployment

- **Host:** GitHub Pages, published from the `main` branch, root folder.
- **Deploy:** automatic. Any commit to `main` triggers the "pages build and
  deployment" workflow (see the **Actions** tab). Takes about 25 seconds.
  There is no manual publish step.
- **HTTPS:** enabled, with "Enforce HTTPS" on. `http://` redirects to `https://`.

### DNS (managed at Spaceship)

| Type | Host | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | shea3100.github.io |

The domain's other DNS records (MX, SPF, DKIM, and a Google verification TXT)
belong to Zoho email and Google Search Console. **Do not delete them** — removing
the mail records breaks email, and removing the Google TXT record un-verifies
the site in Search Console.

---

## Search

The site is verified in [Google Search Console](https://search.google.com/search-console)
as a Domain property, with `sitemap.xml` submitted. New or changed pages are
picked up automatically; to speed one up, use **URL inspection → Request indexing**.
