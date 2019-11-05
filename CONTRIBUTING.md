# Pre-Commit

This project uses pre-commit hooks to ensure consistent code style throughout the repo. We use
[black](https://github.com/ambv/black) for Python files and Python code within documentation. We use
[prettier](https://github.com/prettier/prettier) for all other filetypes.

Make sure you've installed all the packages listed in `requirements.txt` and `requirements-dev.txt`.
This will install pre-commit for you. Then run `pre-commit install` to set up the local pre-commit environment.

Pre-commit will run each time you attempt to commit staged changes. You can run the pre-commit checks at any time
using `pre-commit run`.

If you are using macOS Mojave or greater, you may run into an issue with setting up your pre-commit environment the first time it runs. If you see `ssl.SSLCertVerificationError` in your stack trace, you need to install Python certificates. To do this, go to `/Applications/Python 3.x/` and open the following files

- `Install Certificates.command`
- `Update Shell Profile.command`

You should now be able to proceed.

# Community Standards

In general, PRs will be acknowledged within one week of receipt. I wish I could say that they would all be
reviewed and merge in in this time frame, but sometimes life gets the better of us. I'll do my best.

All contributions and discussions in this repo should abide by the [Code of Conduct](CODE_OF_CONDUCT.md).
