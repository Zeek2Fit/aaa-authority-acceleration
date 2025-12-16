# n8n MCP Server Setup Guide

This guide explains how to use the n8n MCP (Model Context Protocol) server with Claude Code to manage your AAA Content Publisher workflow.

## What is n8n MCP?

The n8n MCP server allows Claude Code to directly interact with your n8n instance:
- Create, read, update workflows
- Execute workflows via webhooks
- Monitor executions
- Validate workflow configurations

## Prerequisites

1. **n8n Instance** - Self-hosted or n8n Cloud
2. **API Access** - Admin access to generate API keys
3. **Claude Code** - With MCP support enabled

## Step 1: Enable MCP in n8n Settings

**IMPORTANT: This step is required for Claude Code to access your workflows!**

1. Open your n8n instance
2. Go to **Settings** → **API**
3. Find the **"Available in MCP"** toggle
4. **Enable the toggle** for workflows you want Claude to access
5. Generate an API key if you don't have one

```
Settings → API → Enable "Available in MCP" → Generate API Key
```

## Step 2: Configure Claude Code MCP

Add the n8n MCP server to your Claude Code configuration:

### Option A: Via Claude Code CLI

```bash
claude mcp add n8n-mcp --url https://your-n8n-instance.com --api-key YOUR_API_KEY
```

### Option B: Via Configuration File

Add to `~/.claude/mcp.json`:

```json
{
  "mcpServers": {
    "n8n-mcp": {
      "command": "npx",
      "args": ["-y", "@n8n/mcp-server"],
      "env": {
        "N8N_API_URL": "https://your-n8n-instance.com/api/v1",
        "N8N_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

## Step 3: Set Up Webhook Trigger

The AAA Content Publisher uses a **webhook trigger** to initiate publishing:

### Why Webhook?

- **External triggering**: Call from any system (Claude Code, cron, Zapier)
- **Instant execution**: No polling delays
- **Simple integration**: Just a curl command

### Webhook Configuration

1. In n8n, the workflow starts with a **Webhook** node
2. Set the path to something memorable: `aaa-publish`
3. Your webhook URL will be: `https://your-n8n.com/webhook/aaa-publish`

### Testing the Webhook

```bash
# Trigger the workflow
curl https://your-n8n-instance.com/webhook/aaa-publish

# With optional payload
curl -X POST https://your-n8n-instance.com/webhook/aaa-publish \
  -H "Content-Type: application/json" \
  -d '{"filter": "Email"}'
```

## Step 4: Import the Workflow

1. In n8n, go to **Workflows** → **Import from File**
2. Select `n8n/aaa-content-publisher.json`
3. **Replace placeholders** with your credentials:
   - `YOUR_AIRTABLE_BASE_ID`
   - `YOUR_CONTENT_TABLE_ID`
   - `YOUR_KIT_API_KEY`
   - `YOUR_AIRTABLE_PAT`

## Workflow Architecture

```
┌─────────────────┐
│  Webhook Trigger │ ← curl https://your-n8n.com/webhook/aaa-publish
└────────┬────────┘
         │
┌────────▼────────┐
│  Get Approved   │ ← Airtable: Status = "Approved"
│     Content     │
└────────┬────────┘
         │
    ┌────▼────┐
    │ Email?  │
    └────┬────┘
    Yes  │  No
    ▼    ▼
┌───────────┐  ┌──────────────┐
│ Kit Draft │  │ Route by     │
│ Creation  │  │ Platform     │
└─────┬─────┘  └──────┬───────┘
      │               │
      ▼               ▼
┌───────────┐  ┌──────────────┐
│ Mark      │  │ Twitter/     │
│ Published │  │ WordPress/   │
└───────────┘  │ LinkedIn     │
               └──────────────┘
```

## Using with Claude Code

Once configured, Claude Code can interact with your workflows:

```
"Show me my n8n workflows"
"Get the AAA Content Publisher workflow"
"Validate the workflow configuration"
"Check recent executions"
```

## Troubleshooting

### "Workflow not available in MCP"

1. Go to your workflow in n8n
2. Click the **three dots** menu → **Settings**
3. Enable **"Available in MCP"**
4. Save the workflow

### "Authentication failed"

1. Verify your API key is correct
2. Check the API key has proper permissions
3. Ensure the n8n URL doesn't have trailing slash

### "Webhook not triggering"

1. Ensure workflow is **active** (toggle in top-right)
2. Check the webhook path matches your curl command
3. Verify n8n is accessible from your network

## Security Notes

- **Never commit API keys** to version control
- Use environment variables for credentials
- The included workflow JSON has all secrets replaced with placeholders
- Rotate API keys periodically

## Resources

- [n8n MCP Documentation](https://docs.n8n.io/mcp/)
- [Claude Code MCP Guide](https://docs.anthropic.com/claude-code/mcp)
- [n8n Webhook Documentation](https://docs.n8n.io/nodes/n8n-nodes-base.webhook/)
