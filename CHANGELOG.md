# CHANGELOG


## v1.1.0 (2025-02-14)

### Build System

- **deps**: Bump dawidd6/action-download-artifact from 7 to 8
  ([`a8af558`](https://github.com/qthequartermasterman/TimerContext/commit/a8af55814a12b1400f0ad0fc3b8d1d26858ed2ec))

Bumps [dawidd6/action-download-artifact](https://github.com/dawidd6/action-download-artifact) from 7
  to 8. - [Release notes](https://github.com/dawidd6/action-download-artifact/releases) -
  [Commits](https://github.com/dawidd6/action-download-artifact/compare/v7...v8)

--- updated-dependencies: - dependency-name: dawidd6/action-download-artifact dependency-type:
  direct:production

update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump hypothesis in the lint-and-test group
  ([`4f63627`](https://github.com/qthequartermasterman/TimerContext/commit/4f63627d6eb120cfa39f95b164a52f671e4902cd))

Bumps the lint-and-test group with 1 update:
  [hypothesis](https://github.com/HypothesisWorks/hypothesis).

Updates `hypothesis` from 6.124.2 to 6.124.7 - [Release
  notes](https://github.com/HypothesisWorks/hypothesis/releases) -
  [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.124.2...hypothesis-python-6.124.7)

--- updated-dependencies: - dependency-name: hypothesis dependency-type: direct:production

update-type: version-update:semver-patch

dependency-group: lint-and-test ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump the lint-and-test group with 2 updates
  ([`bcb39d4`](https://github.com/qthequartermasterman/TimerContext/commit/bcb39d44825bb618231c04d550db0576474addd1))

Bumps the lint-and-test group with 2 updates: [ruff](https://github.com/astral-sh/ruff) and
  [hypothesis](https://github.com/HypothesisWorks/hypothesis).

Updates `ruff` from 0.9.3 to 0.9.4 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.9.3...0.9.4)

Updates `hypothesis` from 6.124.7 to 6.125.1 - [Release
  notes](https://github.com/HypothesisWorks/hypothesis/releases) -
  [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.124.7...hypothesis-python-6.125.1)

--- updated-dependencies: - dependency-name: ruff dependency-type: direct:production

update-type: version-update:semver-patch

dependency-group: lint-and-test

- dependency-name: hypothesis dependency-type: direct:production

update-type: version-update:semver-minor

dependency-group: lint-and-test ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump the lint-and-test group with 3 updates
  ([`9e69e9f`](https://github.com/qthequartermasterman/TimerContext/commit/9e69e9fcda1138553086c5b327a1ac58bd35be2b))

Bumps the lint-and-test group with 3 updates: [mypy](https://github.com/python/mypy),
  [ruff](https://github.com/astral-sh/ruff) and
  [hypothesis](https://github.com/HypothesisWorks/hypothesis).

Updates `mypy` from 1.14.1 to 1.15.0 -
  [Changelog](https://github.com/python/mypy/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/python/mypy/compare/v1.14.1...v1.15.0)

Updates `ruff` from 0.9.4 to 0.9.6 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.9.4...0.9.6)

Updates `hypothesis` from 6.125.1 to 6.125.2 - [Release
  notes](https://github.com/HypothesisWorks/hypothesis/releases) -
  [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.125.1...hypothesis-python-6.125.2)

--- updated-dependencies: - dependency-name: mypy dependency-type: direct:production

update-type: version-update:semver-minor

dependency-group: lint-and-test

- dependency-name: ruff dependency-type: direct:production

update-type: version-update:semver-patch

- dependency-name: hypothesis dependency-type: direct:production

dependency-group: lint-and-test ...

Signed-off-by: dependabot[bot] <support@github.com>

### Documentation

- Fix readme typos
  ([`d959320`](https://github.com/qthequartermasterman/TimerContext/commit/d9593206191888e21040dd1466a1fc1b6db13895))

### Features

- Duration now passes a timedelta object
  ([`ca24910`](https://github.com/qthequartermasterman/TimerContext/commit/ca2491044d76fc6191cad2228a87f9acb5f6a5ce))

### Testing

- :white_check_mark: add duration timedelta test case
  ([`a44c321`](https://github.com/qthequartermasterman/TimerContext/commit/a44c3219d4d9775eae09a386ec4b1aa87b56d581))


## v1.0.0 (2025-01-24)

### Bug Fixes

- Bump version
  ([`46abf12`](https://github.com/qthequartermasterman/TimerContext/commit/46abf12ff23ac6c6323f581862dd3959148b6a11))


## v0.1.0 (2025-01-24)

### Bug Fixes

- Add type checking import
  ([`3846505`](https://github.com/qthequartermasterman/TimerContext/commit/38465054484abaa671952c4522092793208f4c3b))

- Use milliseconds not microseconds for duration
  ([`8ac977c`](https://github.com/qthequartermasterman/TimerContext/commit/8ac977cd09a08efb96cb4f7588720c29e8651d6d))

### Build System

- Add pyproject.toml
  ([`de7de81`](https://github.com/qthequartermasterman/TimerContext/commit/de7de81161c35a03a882e48859474abb6b5dbe56))

- Allow typing extensions as compile time dependency for type checking in older python
  ([`26618fd`](https://github.com/qthequartermasterman/TimerContext/commit/26618fd176141d50b7362babc6897695c68700bf))

- Allow typing extensions as compile time dependency for type checking in older python
  ([`e65677e`](https://github.com/qthequartermasterman/TimerContext/commit/e65677e67597b77692621741686f89658bdd32b1))

- Fix extra names
  ([`d83f05a`](https://github.com/qthequartermasterman/TimerContext/commit/d83f05a1d5eec8d00387622478945af31d50c817))

- Precommit
  ([`0d2b3b5`](https://github.com/qthequartermasterman/TimerContext/commit/0d2b3b5f80521cc639a280add800da610f88e9b0))

- Remove redundant mypy args
  ([`159c5e4`](https://github.com/qthequartermasterman/TimerContext/commit/159c5e4a3e8e64bd0d5aa285620e3baa35c1b0ee))

- Semantic release version updater
  ([`eebd8e1`](https://github.com/qthequartermasterman/TimerContext/commit/eebd8e19964551404e2dd2c40e41e94123b8f460))

- **deps**: Bump actions/upload-artifact from 3 to 4
  ([`f4605d5`](https://github.com/qthequartermasterman/TimerContext/commit/f4605d5e315bf9ffe252d9dfd92a09b9ffc97ec1))

Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 3 to 4. - [Release
  notes](https://github.com/actions/upload-artifact/releases) -
  [Commits](https://github.com/actions/upload-artifact/compare/v3...v4)

--- updated-dependencies: - dependency-name: actions/upload-artifact dependency-type:
  direct:production

update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump the lint-and-test group across 1 directory with 2 updates
  ([`cf7bc0d`](https://github.com/qthequartermasterman/TimerContext/commit/cf7bc0d39ac5c193d6667c2b107cf956b00fcd2e))

Bumps the lint-and-test group with 2 updates in the / directory:
  [mypy](https://github.com/python/mypy) and [ruff](https://github.com/astral-sh/ruff).

Updates `mypy` from 1.14.0 to 1.14.1 -
  [Changelog](https://github.com/python/mypy/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/python/mypy/compare/v1.14.0...v1.14.1)

Updates `ruff` from 0.9.2 to 0.9.3 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.9.2...0.9.3)

--- updated-dependencies: - dependency-name: mypy dependency-type: direct:production

update-type: version-update:semver-patch

dependency-group: lint-and-test

- dependency-name: ruff dependency-type: direct:production

dependency-group: lint-and-test ...

Signed-off-by: dependabot[bot] <support@github.com>

### Code Style

- Line ends
  ([`61deda8`](https://github.com/qthequartermasterman/TimerContext/commit/61deda8894ffacf750675514d1754498577559b7))

- New lines
  ([`b18abe4`](https://github.com/qthequartermasterman/TimerContext/commit/b18abe476a8c1af1d0517e308723e616cfa18ad5))

- Style fixes by ruff
  ([`371c91a`](https://github.com/qthequartermasterman/TimerContext/commit/371c91ad0bde8e96f97debc93973acf330f0469b))

- Style fixes by ruff
  ([`7aa66e3`](https://github.com/qthequartermasterman/TimerContext/commit/7aa66e303f8e8ee2984df7238c5cda852830d434))

- Style fixes by ruff
  ([`400148f`](https://github.com/qthequartermasterman/TimerContext/commit/400148fb8aad2944bb9f871451d862aa8536af73))

- Style fixes by ruff
  ([`caa4296`](https://github.com/qthequartermasterman/TimerContext/commit/caa4296d1cc22204c97ba7dcad277bb2870f2586))

### Continuous Integration

- Add build command to semantic release
  ([`1a3916d`](https://github.com/qthequartermasterman/TimerContext/commit/1a3916d79e4e4710042b75c840618dae3797a837))

- Commit changes from pre-commit in ci
  ([`8d02c13`](https://github.com/qthequartermasterman/TimerContext/commit/8d02c13edffd1b5caca81ecbcf1831333f5a37b3))

- Fix incorrect path
  ([`0a846f1`](https://github.com/qthequartermasterman/TimerContext/commit/0a846f14d3b94710aec5041b6a522727034ea205))

- Linting
  ([`af29619`](https://github.com/qthequartermasterman/TimerContext/commit/af2961967fe0c7b013de2639cbd80eef87455d78))

- Remove pyright from ci
  ([`3b7b1b1`](https://github.com/qthequartermasterman/TimerContext/commit/3b7b1b1a0627349874455f31b1c132de382f87e3))

- Testing workflow
  ([`7e2d35c`](https://github.com/qthequartermasterman/TimerContext/commit/7e2d35c787582b073617dddb9116783a5f62646d))

### Documentation

- Examples
  ([`58fcf09`](https://github.com/qthequartermasterman/TimerContext/commit/58fcf094afd53d5583dea55c516ea5edd49cff0e))

- Readme
  ([`a8dcc8e`](https://github.com/qthequartermasterman/TimerContext/commit/a8dcc8e9560baf8e36a762242d680d7137a7dc76))

- Update documentation
  ([`a1698be`](https://github.com/qthequartermasterman/TimerContext/commit/a1698befbbc29a85c1629a336a5e3110401d1961))

- Update supported versions of python
  ([`45e5cb0`](https://github.com/qthequartermasterman/TimerContext/commit/45e5cb009df86a3b74be4a88622ab0d774cf4d23))

### Features

- Dependabot + initial release
  ([`a922ad4`](https://github.com/qthequartermasterman/TimerContext/commit/a922ad449be56cb2ddc6146cb4ad890646e4d9f0))

- Initial implementation of TimerContext
  ([`91ee5ba`](https://github.com/qthequartermasterman/TimerContext/commit/91ee5ba33833d308cd68fa814ff7b630e9ca1933))

### Refactoring

- :recycle: :truck: move TimerContext to a new file to simplify __init__.py
  ([`2e24a83`](https://github.com/qthequartermasterman/TimerContext/commit/2e24a836c702443cbafd5aa6d4a051136a9db15a))

- :recycle: remove Self type hint for backward compatibility without introducing dependency
  ([`a39e178`](https://github.com/qthequartermasterman/TimerContext/commit/a39e1789b080e45f0499fee958133f626343586e))

- Fix ruff
  ([`cd6b887`](https://github.com/qthequartermasterman/TimerContext/commit/cd6b887fd36d6500b997491820594cdbc71ecf09))

### Testing

- Add unit tests
  ([`2020601`](https://github.com/qthequartermasterman/TimerContext/commit/2020601b29c41ab2c226adfa38c79bdfe6a6d3bc))

- Allow wider range on tests for inaccuracies in time sleep
  ([`91fc610`](https://github.com/qthequartermasterman/TimerContext/commit/91fc610abc1567b09f4691940717d8bd45fdf863))

- Divide by correct scale factor for nano->milliseconds
  ([`24dda74`](https://github.com/qthequartermasterman/TimerContext/commit/24dda74f8aa6281f60d454f3012eef16d3aa5639))

- Wider tolerance on timing tests
  ([`bb3e631`](https://github.com/qthequartermasterman/TimerContext/commit/bb3e631ddb581328b89259c5e556a66595331952))

- Wider tolerance on timing tests
  ([`aed36e5`](https://github.com/qthequartermasterman/TimerContext/commit/aed36e50756d14b0dd01c4e63ff700ef2e43f8c1))

- Wider tolerance on timing tests
  ([`1228500`](https://github.com/qthequartermasterman/TimerContext/commit/12285002ed41d1fe2c75e90032b6d094c272e94d))

- Wider tolerance on timing tests
  ([`f551aec`](https://github.com/qthequartermasterman/TimerContext/commit/f551aec87ba72f1496d77c304f5e651e9363a5ab))
