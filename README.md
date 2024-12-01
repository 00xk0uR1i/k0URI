# WP ExploitScanner
![360_F_228230865_YowfNN5a7r6WDQu97swpRPeTdJd1VRkt](https://github.com/user-attachments/assets/3710f08f-bcfc-4cc0-bbb5-891b0efd0509)
WP Exploit Scanner is a multi-functional tool for scanning, detecting, and exploiting vulnerabilities in WordPress websites. It integrates multiple features such as Shodan and ZoomEye queries, Nuclei scanning, and auto-exploitation. Additionally, it allows users to import custom Python exploit scripts for dynamic execution.
## Features
1. WordPress Vulnerability Scanning: Detect vulnerabilities in WordPress sites using APIs and known methods.
2. Shodan Integration: Search for WordPress-related systems using the Shodan API.
3. ZoomEye Integration: Query ZoomEye for WordPress-related systems.
4. Nuclei Scanning: Use Nuclei templates to scan for CVEs, misconfigurations, and WordPress-specific issues.
5. Auto-Exploitation: Exploit known vulnerabilities automatically.
6. Custom Exploit Import: Import and execute Python-based exploit scripts dynamically.

## Install

1. Go to [VS Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.github-vscode-theme).
2. Click on the "Install" button.
3. Then [select a theme](https://code.visualstudio.com/docs/getstarted/themes#_selecting-the-color-theme). The GitHub themes try to match the themes available in [github.com's settings](https://github.com/settings/appearance):
    - `GitHub Light Default`
    - `GitHub Light High Contrast` ✨ new ✨
    - `GitHub Light Colorblind` ✨ new ✨
    - `GitHub Dark Default`
    - `GitHub Dark High Contrast`
    - `GitHub Dark Colorblind` ✨ new ✨
    - `GitHub Dark Dimmed`

Additionally, there are also two older themes. **Note**: They might not get updated frequently and are kept for legacy reasons:

- `GitHub Light` (legacy)
- `GitHub Dark` (legacy)

## Override this theme

To override this (or any other) theme in your personal config file, please follow the guide in the [color theme](https://code.visualstudio.com/api/extension-guides/color-theme) documentation. This is handy for small tweaks to the theme without having to fork and maintain your own theme. 

## Contribute

1. Clone and open this [repo](https://github.com/primer/github-vscode-theme) in VS Code
2. Run `yarn` to install the dependencies.
3. Press `F5` to open a new window with your extension loaded
4. Open `Code > Preferences > Color Theme` [`⌘k ⌘t`] and pick the "GitHub ..." theme you want to test. Note: It seems this has to be done 2x because the first time it switches back to the default light theme. This might be a bug?
5. Make changes to the [`/src/theme.js`](https://github.com/primer/github-vscode-theme/blob/master/src/theme.js) file.
    - **UI**: For all changes to the "outer UI", like (status bar, file navigation etc.), take a look at the [Theme Color](https://code.visualstudio.com/api/references/theme-color) reference.
    - **Syntax**: For changes to the "code highlighting", examine the syntax scopes by invoking the [`Developer: Inspect Editor Tokens and Scopes`](https://code.visualstudio.com/api/language-extensions/syntax-highlight-guide#scope-inspector) command from the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac) in the Extension Development Host window.
6. Run `yarn build` to update the theme. You can also run `yarn start` instead to automatically rebuild the theme while making changes and no reloading should be necessary.
7. Once you're happy, commit your changes and open a PR.

Note:

- If possible use colors from [Primer's color system](https://primer.style/primitives/colors).

## Publish (internal)

> Note: Publishing a new version of this theme is only meant for maintainers.

This repo uses [changesets](https://github.com/atlassian/changesets) to automatically make updates to [CHANGELOG.md](https://github.com/primer/github-vscode-theme/blob/main/CHANGELOG.md) and publish a new version to the [VS Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.github-vscode-theme).
