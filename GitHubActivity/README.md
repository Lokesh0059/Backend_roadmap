# GitHub Activity CLI

A simple command-line interface (CLI) tool to fetch and display recent GitHub activity for any user.

## Features

- Fetch recent GitHub events for a specified user
- Display activity in a readable, emoji-enhanced format
- Handle various event types (pushes, issues, pull requests, etc.)
- Graceful error handling for invalid usernames, API failures, and network issues
- No external dependencies - uses only Python standard library

## Requirements

- Python 3.6 or higher

## Usage

```bash
python github_activity.py <username>
```

### Examples

```bash
# Fetch activity for the GitHub mascot
python github_activity.py octocat

# Fetch activity for a real user
python github_activity.py torvalds
```

## Output

The tool displays recent events with:
- Event type with emoji
- Repository name
- Timestamp in UTC
- Relevant details (e.g., number of commits for push events)

Example output:
```
Fetching recent activity for GitHub user: octocat

Recent GitHub Activity (last 30 events):

📝 Pushed 3 commit(s) to octocat/Hello-World on 2023-10-15 14:30:22 UTC
🐛 Opened issue in octocat/Spoon-Knife on 2023-10-14 09:15:10 UTC
🔄 Merged pull request in octocat/Hello-World on 2023-10-13 16:45:33 UTC
```

## Error Handling

The tool handles common errors gracefully:
- **Invalid username**: Displays "User not found" message
- **API rate limits**: Informs about rate limit exceeded
- **Network issues**: Shows network error messages
- **API failures**: Displays appropriate HTTP error codes

## API Information

This tool uses the GitHub Events API:
- Endpoint: `https://api.github.com/users/{username}/events`
- Returns the last 30 public events for the user
- Requires a User-Agent header (included automatically)

## Limitations

- Only shows public activity
- Limited to the most recent 30 events
- Subject to GitHub API rate limits (60 requests per hour for unauthenticated requests)

## Contributing

Feel free to improve the tool by:
- Adding support for more event types
- Improving the display format
- Adding command-line options (e.g., limit number of events)
- Implementing authentication for higher rate limits