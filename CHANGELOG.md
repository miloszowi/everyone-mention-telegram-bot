# Change Log
All notable changes to this project will be documented in this file.

## [0.3.2] - 28.02.2023
### Changed
- fixed bug with missing '+' in replier
## [0.3.1] - 28.02.2023
### Changed
- fixed markdown replier to respect restricted characters provided in the [api docs](https://core.telegram.org/bots/api#markdownv2-style)
## [0.3.0] - 12.11.2021
### Added
- Dynamic mentioning by `@` character
### Changed
- `start` text
- Group name validation - those are forbidden now - `all`, `channel`, `chat`, `everyone`, `group`, `here`
### Deleted
- mentioning user that performed `/everyone` or dynamic mention in bot response
## [0.2.0] - 26.10.2021
### Added
- Inline Mode for `join`, `leave` & `everyone`
- Banned users environment variable
- Buttons for `start` message
### Changed
- Code quality improvements
- `start` text
- mongodb data structure
- group name max length to 40
### Deleted
- `/silent` command
## [0.1.0] - 06.10.2021
### Features
- `/join` command
- `/leave` command
- `/groups` command
- `/everyone` command
- `/start` command
- `/silent` command
- possibility to have multiple contexts for one chat
- docker setup & docker commands