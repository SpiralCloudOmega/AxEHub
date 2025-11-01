---
"""
OMEGA CrewAgent - Modular GitHub Agent inspired by crewAI

Features:
- Accepts a task description and input
- Executes task logic (can route to skills, APIs, etc.)
- Returns structured result
- Easily extensible, plug in more skills

Usage:
- Drop in .github/agents/ in your repo
- Trigger from workflow, webhook, or CLI

Example task:
  {
    "description": "Summarize recent issues",
    "input": {"repo": "SpiralCloudOmega/AxEHub"}
  }
"""

import requests
import json

class CrewAgent:
    def __init__(self, task: dict):
        self.task = task
        self.result = None
        self.skills = {
            "summarize_issues": self.summarize_issues,
            "echo": self.echo,
            # Add more skills here!
        }

    def run(self):
        description = self.task.get("description", "").lower()
        input_data = self.task.get("input", {})

        # Skill routing logic
        if "summarize" in description and "issues" in description:
            self.result = self.skills["summarize_issues"](input_data)
        elif "echo" in description:
            self.result = self.skills["echo"](input_data)
        else:
            self.result = {"error": "Unknown task or skill"}

        return self.result

    def summarize_issues(self, input_data):
        repo = input_data.get("repo")
        if not repo:
            return {"error": "Missing 'repo' in input"}
        # Simplified GitHub API call (public issues)
        url = f"https://api.github.com/repos/{repo}/issues"
        try:
            resp = requests.get(url)
            issues = resp.json()
            summary = [{"number": i["number"], "title": i["title"], "state": i["state"]} for i in issues if "pull_request" not in i]
            return {"summary": summary}
        except Exception as e:
            return {"error": str(e)}

    def echo(self, input_data):
        return {"echo": input_data}

if __name__ == "__main__":
    # Example usage
    example_task = {
        "description": "Summarize recent issues",
        "input": {"repo": "SpiralCloudOmega/AxEHub"}
    }
    agent = CrewAgent(example_task)
    print(json.dumps(agent.run(), indent=2))name:
description:
---

# My Agent

Describe what your agent does here...
