#!/usr/bin/env python3
"""
GitHub Activity CLI

A simple command-line interface to fetch and display recent GitHub activity for a user.

Usage: python github_activity.py <username>
"""

import urllib.request
import urllib.error
import json
import sys
from datetime import datetime

def get_github_activity(username):
    """
    Fetch recent GitHub events for a user.

    Args:
        username (str): GitHub username

    Returns:
        list: List of event dictionaries, or None if error
    """
    url = f"https://api.github.com/users/{username}/events"
    headers = {'User-Agent': 'GitHub-Activity-CLI/1.0'}

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
        return data
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: User '{username}' not found.")
        elif e.code == 403:
            print("Error: API rate limit exceeded. Try again later.")
        else:
            print(f"HTTP Error: {e.code} - {e.reason}")
        return None
    except urllib.error.URLError as e:
        print(f"Network Error: {e.reason}")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to parse API response.")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None

def display_activity(events):
    """
    Display the GitHub events in a readable format.

    Args:
        events (list): List of event dictionaries
    """
    if not events:
        print("No recent activity found.")
        return

    print(f"\nRecent GitHub Activity (last {len(events)} events):\n")
    for event in events:
        event_type = event.get('type', 'Unknown')
        repo_name = event.get('repo', {}).get('name', 'Unknown')
        created_at = event.get('created_at', '')
        
        # Parse and format date
        try:
            dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
            formatted_date = dt.strftime('%Y-%m-%d %H:%M:%S UTC')
        except:
            formatted_date = created_at

        # Customize display based on event type
        if event_type == 'PushEvent':
            commits = len(event.get('payload', {}).get('commits', []))
            print(f"📝 Pushed {commits} commit(s) to {repo_name} on {formatted_date}")
        elif event_type == 'IssuesEvent':
            action = event.get('payload', {}).get('action', '')
            print(f"🐛 {action.capitalize()} issue in {repo_name} on {formatted_date}")
        elif event_type == 'PullRequestEvent':
            action = event.get('payload', {}).get('action', '')
            print(f"🔄 {action.capitalize()} pull request in {repo_name} on {formatted_date}")
        elif event_type == 'CreateEvent':
            ref_type = event.get('payload', {}).get('ref_type', '')
            print(f"📁 Created {ref_type} in {repo_name} on {formatted_date}")
        elif event_type == 'WatchEvent':
            print(f"⭐ Starred {repo_name} on {formatted_date}")
        elif event_type == 'ForkEvent':
            print(f"🍴 Forked {repo_name} on {formatted_date}")
        else:
            print(f"📋 {event_type} on {repo_name} on {formatted_date}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python github_activity.py <username>")
        print("Example: python github_activity.py octocat")
        sys.exit(1)

    username = sys.argv[1].strip()
    if not username:
        print("Error: Username cannot be empty.")
        sys.exit(1)

    print(f"Fetching recent activity for GitHub user: {username}")
    activity = get_github_activity(username)
    
    if activity is not None:
        display_activity(activity)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()