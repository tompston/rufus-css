# Rufus CSS

Self-defined, utility-first, Tailwind-inspired CSS library.

### [Link to docs](https://rufus.pages.dev/)

## Why?

I like the concept of tailwind, but don't like using rem units. + I wanted something that you can tweak easier.

## Download

```bash
# with cmd
curl https://raw.githubusercontent.com/tompston/rufus-css/main/dist/rufus-content.css -O rufus.css
curl https://raw.githubusercontent.com/tompston/rufus-css/main/dist/rufus.css -O rufus-content.css

# with bash
wget https://raw.githubusercontent.com/tompston/rufus-css/main/dist/rufus-content.css
wget https://raw.githubusercontent.com/tompston/rufus-css/main/dist/rufus.css

# or just clone
git clone https://github.com/tompston/rufus-css.git
```

<!--

## https://css-irl.info/animating-underlines/

## Command to generate and combine css

    # from the root dir, using bash
    npm i
    npm run build

If this is added, every time you run `npm run build`, the postbuild script will
also be triggered and purge the css in the dist folder.

- note that you need to install purgecss as a dependency, if you're gonna do
  automatic builds for Netlify and stuff
- The `package.json` example is also written inside the output file, so u don't need to check the repo again.


## Purging CSS for Single Page Apps

You don't really need a seperate config file for postcss to purge unused
classes for small SPA projects. Just copy the following into your package.json file

```
  "scripts": {
    ...
    "postbuild": "purgecss --css dist/assets/*.css --content dist/assets/*.js -o dist/assets/  --safelist html body"
  },
``` -->

<!--

  "scripts": {
    "concat-css": "cat css/* > rufus.css",
    "postcss:build": "postcss rufus.css -o rufus.css",
    "build": "python3 generate_css_class.py && npm run concat-css && npm run postcss:build"
  },


--- this allows to add padding without affecting max width (useful for inputs)
    -moz-box-sizing: border-box;
    -webkit-box-sizing: border-box;
     box-sizing: border-box;


 -->
