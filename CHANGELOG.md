# Changelog - Bot

## v3.1.0 - Minor updates

- Restart the image automatically
- Update invite link

## v3.0.0 - Use docker

Use docker containers to run the bot, this is breaking and requires configuration changes and database migration (backup from current database, and restore to database in docker container)

## v2.2.1 - Small Fixes

- Handle JSON embed errors correctly

## v2.2 - Logging and timeout

- Added 60s timeout to the confirm stage
- Added sentry logging

## v2.1 - Interactions

- Add custom interaction handlers
  - Remove `discord-py-slash-command`
- Add component handlers
- Add components
- Add checks to message commands
- Fix aerich
- Upgrade dependencies

## v2.0.1 - Changes

- Fix `id` named `channel_id` when fetching channel from database.

## v2 - Changes

- Use `tortoise-orm` for database management

## v1.7 - Changes

- Add action that deploys changes on non major tag release
- Fix bug when user doesn't have required permissions and uses a `/settings` command

## v1.6 - Changes

- Bump dependencies
- Improve logger format (code logger)
- Improve db migration
- Typing fixes
- Refactoring internals
- Add slash commands for logging setting (`/settings get/set logging`)
- Add security and contact info to readme
- Update contributing templates
- Implement caching for guild settings
  - Updated privacy policy
- Make `/info` slash commands ephemeral

## v1.5.1 - Changes

- Slash commands:
  - Made commands global
  - Added descriptions
  - Removed "slash beta"
  - Restructure slash commands
  - Add settings slash commands

## v1.5.0 - Changes

- Rename `cogs.src` to `cogs.utils`
- Added logging
  - Added docs for logging
  - Update invite link with new permissions
  - Update privacy policy

## v1.4.0

### Add slash commands

- Add column to database
- Add database functions
- Add management / syncing feature
- Add info slash commands
- Add opt int request system

## v1.3.1

### Clean up after removal of stats function

Remove `bot_channel` and `member_channel` columns from the database.

## v1.3.0

### Add embeds to message function

8th of December 2020

- Add commands `send-embed`, `send-embed-json`, `edit-embed` and `edit-embed-json`.
- Change `delete` to add the JSON version of any embeds in the message that's being deleted to the log file when
- Change `fetch` to add the JSON version of any embeds in the message that's being fetched to the log file
- Add aliases to existing commands:
  - To `fetch` add `fetch-embed`
  - To `delete` add `delete-embed`
- Add new commands and aliases to the docs
- Add link to embed section of docs in help command

## v1.2.0

### Add support command and fix various internal workings

28th of November 2020

- Add command `support` that responds with an invite to the discord support server
- Remove dev command `listservers`
- Send a plain non-embed message when asking for more input on messages commands
- Check if the bot has view permissions before trying to send, edit, delete, or fetch anything
- Check if the person sending has view permissions in that channel, this is to allow owners to have greater control over what can be edited by members with the admin role
- Stop deleting the command invocation
- Raise a clearer error when trying to edit a message that was sent by a different user than the bot

## v1.1.1

### Fix version not consistent across bot

The version of the bot was not from the value of `__version__` in the info command.

#### Changes

- Edit the value of version on the info command
- Add a check to see if the version of the database and the bot are the same at startup
- Bump version to v1.1.1
- Remove un used database functions

## v1.1.0

### Stats Function Removed

#### Summary

The stats function, which updated the names of two voice channels every thirty minutes with the amount of bot users and non bot users in a guild has been removed.  
From now on any command relating to the stats function, eg `~stats update`, `~setup botstats`, will display a warning message saying that the function was removed and a link to this changelog. After a month this will be removed.

#### Reasons

Discord has recently added restrictions on what information bots can receive from the api. These are called Privileged Intents and required approval from discord to have them after a bot reaches one hundred guilds.
One of the intents is the member intent which allows the bot to receive member_join and member_leave events among other things. Without this intent the guild count can't be updated without making a request to discord for every guild. Previously, with the member intent the guild count was updated every time the bot received the join and leave events, meaning the count was accurate.
Making a request to discord for every single guild every 30 minutes would have got out of hand after 100 guilds or so. On top of this even if the bot could keep an up to date guild count without the members intent it would not be able to get the amount of bot vs non bot accounts. This bot was unlikely to have received approval from discord for the member intent because this is the only feature that needs it and it's a very small feature. Also this feature is not following the main theme of the bot which focuses on messages in a guild.

#### Code Changes

- Replace all stats related commands with warning messages to be removed in one month.
- Remove the loop that automatically updated the stats channels.
- Remove db functions that fetched / set stats channels.
- Remove command `~stats update` from help command.
- Add warning message to setup help to be removed in one month.
- Replace setup commands relating to stats with warning messages to be removed in one month.
- Remove stats references in docs.
- Update invite link to no longer ask for manage channel permissions.
- Remove manage channel permissions from the permissions page in the docs.

> Note: I have not removed entries from the database for the stats channels, i will do this and update the database that the bot creates in one month.
