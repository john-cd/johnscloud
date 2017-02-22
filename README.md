# John's Cloud

John's CloudFormation templates and devops scripts.


## Documentation Generation

Files in /documentation are generated by Mkdocs.

To install MkDocs / create a new documentation site:
```bash
$ pip install mkdocs
$ mkdocs new documentation
```

To build the documentation site:
```bash
$ cd documentation
$ mkdocs build
```

To start the live-reloading docs server - [http://localhost:8000/](http://localhost:8000/)
```bash
$ mkdocs serve
```

MkDocs can use the ghp-import tool to commit to the gh-pages branch and push the gh-pages branch to GitHub Pages:
```bash
$ mkdocs gh-deploy
```

For full documentation visit [mkdocs.org](http://mkdocs.org).

### Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
