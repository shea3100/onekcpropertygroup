# onekcpropertygroup.com

Static website for One KC Property Group, LLC — hosted on GitHub Pages.

## Files

| File | Purpose |
|---|---|
| `index.html` | Home page |
| `requirements.html` | Application Requirements |
| `faq.html` | FAQ |
| `about.html` | About Us |
| `contact.html` | Contact |
| `styles.css` | All styling for every page |
| `CNAME` | Tells GitHub Pages the custom domain (`onekcpropertygroup.com`) — do not delete |
| `.nojekyll` | Serves files as-is, no Jekyll processing |
| `build.py` | Optional generator: rebuilds all 5 HTML pages from one shared template |

## Making changes

**Small text edits:** open the `.html` file on GitHub, click the pencil icon, edit, commit.
The site updates in about a minute.

**Changing the header, footer or nav on every page at once:** edit `build.py` and run
`python3 build.py` locally, then commit the regenerated HTML files.

## DNS (Spaceship)

`onekcpropertygroup.com` → four A records pointing at GitHub Pages:
185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153

`www` → CNAME to `<github-username>.github.io`
