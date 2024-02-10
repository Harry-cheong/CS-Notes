# Developer Skills

## ▷▷▷▷▷ Prettier ◁◁◁◁◁

- ctrl s to save and format the code

1. Opinionated Formatter
    - Extra lines are removed
    - spaces are consistent
    e.g. if () console.log(23);

2. Configuration
    - .prettierrc file

    e.g.

    ```prettierrc
    - singleQuote = true/false
    * arrowParens = true/false -> auto bracket the perimeter if only one is given for arrow functions
    ```

3. Ignore certain files
    - .prettierignore file

    e.g. [ignore all text files]

    ```prettierignore
    *.txt
    ```

## ▷▷▷▷▷ Vscode ◁◁◁◁◁

### Shorthands

e.g. [File > Preferrence > Configure User Snippets]

```json
{
  "Print to console": {
    "scope": "javascript, typescript",
    "prefix": "cl",
    "body": ["console.log();"],
    "description": "Log output to console"
  }
}
```

### Custom Colour Coding

- settings.json

e.g.

[File > Preferrence > Settings > Click on the icon on the top right corner]

```json
{
  "todohighlight.isCaseSensitive": true,
  "todohighlight.keywords": [
      {
      "text": "FIXME",
      "color": "#333",
      "backgroundColor": "#e67e22"
      },
      {
      "text": "BUG",
      "color": "#333",
      "backgroundColor": "#e74c3c"
      },
      {
      "text": "TODO",
      "color": "#333",
      "backgroundColor": "#2ecc71"
      }
  ]
}
```

## ▷▷▷▷▷ Debugging ◁◁◁◁◁

- Inspect > Sources

1. Setting breakpoints
    - Press the line (a red dot will appear)

2. Execution
    - Pause/Resume Execution
    - Sequential Execution

3. Summoning the debugger
    - run the debugger and observe for any unusual behaviour

## ▷▷▷▷▷ Node Package Manager ◁◁◁◁◁

### Commands

1. `npm i ~flag~ ~package~` or `npm i`
    - `flag`: `-g` (global) `-D` (development)

2. `npm ci`
3. `npm run ~script~`
4. `npm -v`
5. `npm list`

## ▷▷▷▷▷ Node Version Manager ◁◁◁◁◁

- always run nvm in terminal with elevated privileges

1. `nvm use ~var~`
2. `nvm i ~var~`
3. `nvm list`

## ▷▷▷▷▷ Deployment on Firebase ◁◁◁◁◁

1. `firebase init` and select hosting
2. organise all the code under `src` folder
3. cd into the `src` folder and prepare deployment files
4. cd to root and run `npm i -g firebase-tools`
5. edit the .firebaserc file accordingly to load deployment files
6. `firebase serve` : firebase local deployment
7. `firebase deploy` : firebase deploy to cloud server

## ▷▷▷▷▷ Deployment to GH Pages ◁◁◁◁◁

[Original GitHub Guide](https://github.com/lucpotage/nuxt-github-pages)

1. Install dev dependency `gh-pages`
2. Add the script `"deploy": "gh-pages -d dist"` in package.json file
3. Specifiy app `baseURL` in nuxt.config.ts
4. Specifiy `buildAssetsDir` in nuxt.config.ts that doesn't start with an underscore `_`. See the router config example below
5. Create an empty file `.nojekyll` at the root of the project
6. Generate with `npm run generate`
7. Deploy with `npm run deploy`

## ▷▷▷▷▷ Tech Stacks ◁◁◁◁◁

1. Nuxt - FastAPI - MongoDB Stack
    | Usage | Technology |
    | ----------- | ----------- |
    | Frontend | Nuxtjs/Vuejs |
    | CI/CD | GitHub Actions |
    | Backend | Flask/FastAPI |
    | Database | MongoDB |
    | Hosting/Cloud | Firebase/Google Cloud |

2. MERN
    | Usage | Technology |
    | ----------- | ----------- |
    | Frontend | Reactjs |
    | Backend | Expressjs |
    | Frontend/Backend | Nodejs |
    | Database | MongoDB |
