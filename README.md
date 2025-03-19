# Monday Night Bytes website

# Contributing 

Website is based on [mkdocs](https://www.mkdocs.org/) which is an engine that will render markdown file to a nice html website.
Theme is mkdocs material : https://squidfunk.github.io/mkdocs-material/

To keep it simple : Just edit the page on `docs/` and update `mkdocs.yml` if necessary.

Any change done to the `main` branch will retrigger a build of the website.
The static web site is then generated inside the `gh-pages` branch

## Local dev 

You can edit and preview locally

```shell
git clone https://github.com/totetmatt/mondaynightbytes.git
cd mondaynightbytes
python -m venv .venv
. venv/bin/activate #Windows: .venv\Script\activate
pip install -r req.txt
mkdocs serve
```

Then update what you want. The `mkdocs serve` should keep updating when you change file.

When happy with the result, just push back to `main`

## Github update
You can also edit directly from the Github file editor online. As long as the change is reflected on the `main` branch. it will retrigger the build of the website.


