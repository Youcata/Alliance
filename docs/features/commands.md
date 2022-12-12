---
description: A list of all the commands
---

# Commands

{% hint style="info" %}

1. The default prefix is used below for simplicity. Replace this with your prefix for the server.
2. `<>` means a required parameter and `{}` means a optional parameter.
{% endhint %}

{% hint style="warning" %}
Do **not** include the `<>` or `{}` while doing commands. This is just a indicator to show you need to fill it in.
{% endhint %}

## General commands

| Command | Description | Permission Level |
| :--- | :--- | :--- |
| `~help` | Displays help | `@everyone` |
| `~info` | Displays information about the bot | `@everyone` |
| `~ping` | Returns the bots current command latency | `@everyone` |

## Message commands

| Command | Description | Permission Level |
| :--- | :--- | :--- |
| `~`[`send <channel> <content>`](messages.md#sending-messages) | Sends a message to a specified channel | Management Role |
| [`~edit <channel> <message id> <new content>`](messages.md#editing-messages) | Edits a message that was previously sent by the bot | Management Role |
| [`~fetch <channel> <message id>`](messages.md#fetching-messages) | Returns the raw content of that message | Management Role |
| [`~delete <channel> <message id>`](messages.md#deleting-messages) | Deletes a message that the bot sent | Management Role |
| `~`[`send-embed <channel>`](messages.md#sending-basic-embeds) | Sends an embed to a specified channel | Management Role |
| `~`[`send-embed-json <channel>`](messages.md#sending-basic-embeds) | Sends a fully customized embed to a specified channel | Management Role |
| [`~edit-embed <channel> <message id> <new content>`](messages.md#editing-messages) | Edits an embed that was previously sent by the bot | Management Role |
| [`~edit-embed-json <channel> <message id> <new content>`](messages.md#editing-messages) | Edits a fully customized embed that was previously sent by the bot | Management Role |

## Setup commands

{% hint style="info" %}
All commands below will return the current setting if the optional parameter is not included.
{% endhint %}

| Command | Description | Permission Level |
| :--- | :--- | :--- |
| [`~setup`](../startup/setup/config.md) | Gives information about the setup commands | `ADMINISTRATOR` |
| [`~setup prefix {new prefix}`](../startup/setup/config.md#prefix) | Changes the guild's prefix to the new prefix. | `ADMINISTRATOR` |
| [`~setup admin {admin role}`](../startup/setup/config.md#management-role) | Sets the administrative role, or as is more commonly called, the management role | `ADMINISTRATOR` |
| `~prefix` | Returns the current prefix for the guild. This is useful if you forget the prefix because it can be invoked with the bot mention prefix | `@everyone` |
