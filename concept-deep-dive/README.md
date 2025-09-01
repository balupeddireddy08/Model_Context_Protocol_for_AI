# Model Context Protocol (MCP): A Beginner's Guide

## What is MCP?

The Model Context Protocol (MCP) is an open standard that connects AI models to external data and tools. Think of MCP as a "universal translator" between AI systems and the outside world.

```mermaid
graph LR
    A[AI Model] <-->|MCP| B[External World]
    B --- C[Databases]
    B --- D[Files]
    B --- E[APIs]
    B --- F[Services]
    
    style A fill:#f9d5e5,stroke:#333,stroke-width:2px
    style B fill:#eeeeee,stroke:#333,stroke-width:2px
    style C fill:#d5f9e5,stroke:#333,stroke-width:1px
    style D fill:#d5f9e5,stroke:#333,stroke-width:1px
    style E fill:#d5f9e5,stroke:#333,stroke-width:1px
    style F fill:#d5f9e5,stroke:#333,stroke-width:1px
```

### The USB-C Analogy

Just like USB-C provides a single port that connects your laptop to many different devices (monitors, hard drives, chargers), MCP is a single protocol that connects AI models to many different data sources and tools. Before USB-C, we needed different ports for different devices. Similarly, before MCP, developers had to create custom integrations for each data source an AI needed to access.

## Core Architecture

MCP uses a client-host-server architecture where each host can run multiple client instances. This architecture enables integration of AI capabilities across applications while maintaining clear security boundaries.

### Participants: Who's Who in MCP

MCP has three main participants:

1. **Host**: 
- The AI application (like Claude or a coding assistant: VS Code or Cursor)
- Manages client instances (1:1 with servers), controls permissions/authorization, and coordinates AI/LLM integration with context aggregation
2. **Client**: 
- The connector that sends requests from the AI-host to servers
- Handles stateful sessions, protocol negotiation, bidirectional routing, and maintains security boundaries between servers
3. **Server**:
- The program that provides data or tools to the AI.
- Expose MCP primitives (resources, tools, prompts) independently while respecting security constraints as local or remote services

```mermaid
graph LR
    A[Host<br/>AI Application] --> B[Client<br/>Connector]
    B <--> C[Server<br/>Data/Tool Provider]
    C --> D[External<br/>Services]
    
    style A fill:#f9d5e5,stroke:#333,stroke-width:1px
    style B fill:#d5e5f9,stroke:#333,stroke-width:1px
    style C fill:#d5f9e5,stroke:#333,stroke-width:1px
    style D fill:#f9f9d5,stroke:#333,stroke-width:1px
```

#### The Restaurant Analogy

Think of MCP as a restaurant service:
- The **Host** (AI application) is like you, the hungry customer
- The **Client** is like a waiter who takes your order and brings your food
- The **Server** is like the kitchen that prepares what you ordered
- **External Services** are like food suppliers providing ingredients to the kitchen

### Three-Tier Architecture

At a high level, MCP has three primary layers:

1. **Host Layer**: 
    Contains the AI model and user interface
2. **MCP Layer**: Clients and servers that handle requests and responses
3. **Service Layer**: External systems (GitHub, file systems, databases, etc.)

```mermaid
graph TB
    subgraph "Host Layer"
        direction TB
        H[Host / AI Model]
        subgraph "Clients"
            direction LR
            C1[Client 1]
            C2[Client 2] 
            C3[Client 3]
        end
        H --> C1
        H --> C2
        H --> C3
    end

    subgraph "MCP Layer"
        direction LR
        S1[Server 1<br/>Files & Git]
        S2[Server 2<br/>Database]
        S3[Server 3<br/>External APIs]
    end

    subgraph "Service Layer"
        direction LR
        R1[("Local Files<br/>& Git Repos")]
        R2[("Database<br/>Records")]
        R3[("External<br/>APIs")]
    end
    
    subgraph "Transport Layer"
        direction LR
        T1[Stdio<br/>Local Process]
        T2[HTTP/SSE<br/>Remote Service]
    end
    
    %% Connections between layers
    C1 <-->|JSON-RPC 2.0| S1
    C2 <-->|JSON-RPC 2.0| S2
    C3 <-->|JSON-RPC 2.0| S3
    
    S1 <--> R1
    S2 <--> R2
    S3 <--> R3
    
    %% Transport connections
    C1 -.->|Uses| T1
    C2 -.->|Uses| T1
    C3 -.->|Uses| T2
    
    %% Styling
    style H fill:#f9d5e5,stroke:#333,stroke-width:2px
    style C1 fill:#d5e5f9,stroke:#333,stroke-width:1px
    style C2 fill:#d5e5f9,stroke:#333,stroke-width:1px
    style C3 fill:#d5e5f9,stroke:#333,stroke-width:1px
    style S1 fill:#d5f9e5,stroke:#333,stroke-width:1px
    style S2 fill:#d5f9e5,stroke:#333,stroke-width:1px
    style S3 fill:#d5f9e5,stroke:#333,stroke-width:1px
    style R1 fill:#f0f0f0,stroke:#333,stroke-width:1px
    style R2 fill:#f0f0f0,stroke:#333,stroke-width:1px
    style R3 fill:#f0f0f0,stroke:#333,stroke-width:1px
    style T1 fill:#fff2cc,stroke:#333,stroke-width:1px
    style T2 fill:#fff2cc,stroke:#333,stroke-width:1px
```

### Design Principles

MCP is built on several key design principles that shape its architecture:

1. **Simple Server Development**
   * Hosts handle complex orchestration while servers focus on specific capabilities with minimal implementation overhead

2. **High Composability**
   * Servers provide isolated functionality that can be seamlessly combined through shared protocol standards

3. **Security Isolation**
   * Servers receive only necessary context and cannot access full conversations or other servers' data

4. **Progressive Enhancement**
   * Core protocol supports minimal functionality with optional capabilities negotiated as needed

5. **Independent Evolution**
   * Servers and clients can evolve separately while maintaining backwards compatibility and extensibility

## Communication Protocol: JSON-RPC 2.0

MCP uses **JSON-RPC 2.0** as its communication protocol. Think of JSON-RPC 2.0 as the "language" that all MCP participants speak - it's simple, lightweight, and works everywhere.

### Data and Transport Layers

MCP has two communication layers:

1. **Data Layer**: Defines the message format (JSON-RPC 2.0)
2. **Transport Layer**: Handles how messages are sent

```mermaid
graph TD
    subgraph "Data Layer"
    A[JSON-RPC 2.0 Messages]
    end
    
    subgraph "Transport Layer"
    B[Local Stdio]
    C[Remote HTTP]
    end
    
    A --- B
    A --- C
    
    style A fill:#d5e5f9,stroke:#333,stroke-width:1px
    style B fill:#d5f9e5,stroke:#333,stroke-width:1px
    style C fill:#d5f9e5,stroke:#333,stroke-width:1px
```

#### The Mail Analogy

MCP's layers are like sending a letter:
- The **Data Layer** is like the letter's content and format (written in English, with greeting and signature)
- The **Transport Layer** is like the delivery method (hand delivery or postal service)

## Building Blocks: The Three Primitives

MCP servers provide three types of capabilities:

1. **Resources**: Read-only data (files, emails, messages)
2. **Tools**: Functions the AI can call to perform actions
3. **Prompts**: Templates to guide the AI's responses

```mermaid
graph TD
    A[MCP Server] --> B[Resources<br/>Read-only Data]
    A --> C[Tools<br/>Action Functions]
    A --> D[Prompts<br/>Response Templates]
    
    B --> B1[Files]
    B --> B2[Database Records]
    B --> B3[Messages]
    
    C --> C1[Search]
    C --> C2[Create]
    C --> C3[Update]
    
    style A fill:#d5f9e5,stroke:#333,stroke-width:2px
    style B fill:#d5e5f9,stroke:#333,stroke-width:1px
    style C fill:#f9d5e5,stroke:#333,stroke-width:1px
    style D fill:#f9f9d5,stroke:#333,stroke-width:1px
```

### The Library Analogy

MCP servers are like libraries:
- **Resources** are like books you can read but not modify
- **Tools** are like services the library offers (search catalog, reserve books)
- **Prompts** are like the reference librarian who helps you format your questions properly

### JSON-RPC 2.0 Message Types

```mermaid
graph TD
    A[JSON-RPC 2.0 Messages] --> B[Requests<br/>Need Response]
    A --> C[Responses<br/>Reply to Requests]
    A --> D[Notifications<br/>No Response Expected]
    
    B --> B1[Has 'id' field]
    B --> B2[method + params]
    
    C --> C1[Has same 'id']
    C --> C2[result OR error]
    
    D --> D1[No 'id' field]
    D --> D2[method + params]
    
    style A fill:#d5e5f9,stroke:#333,stroke-width:2px
    style B fill:#d5f9e5,stroke:#333,stroke-width:1px
    style C fill:#f9d5e5,stroke:#333,stroke-width:1px
    style D fill:#f9f9d5,stroke:#333,stroke-width:1px
```

### MCP Method Namespaces

MCP organizes its methods into logical namespaces:

```mermaid
graph TD
    A[MCP Methods] --> B[tools/*]
    A --> C[resources/*]
    A --> D[prompts/*]
    A --> E[initialize*]
    A --> F[ping]
    
    B --> B1[tools/list]
    B --> B2[tools/call]
    
    C --> C1[resources/list]
    C --> C2[resources/read]
    C --> C3[resources/subscribe]
    
    D --> D1[prompts/list]
    D --> D2[prompts/get]
    
    E --> E1[initialize]
    E --> E2[initialized]
    
    style A fill:#d5e5f9,stroke:#333,stroke-width:2px
    style B fill:#d5f9e5,stroke:#333,stroke-width:1px
    style C fill:#f9d5e5,stroke:#333,stroke-width:1px
    style D fill:#f9f9d5,stroke:#333,stroke-width:1px
    style E fill:#ffe6cc,stroke:#333,stroke-width:1px
    style F fill:#e6ccff,stroke:#333,stroke-width:1px
```

## MCP in Action: Complete Interaction Flow

### Capability Negotiation & Lifecycle

MCP uses a capability-based negotiation system where clients and servers explicitly declare their supported features during initialization. The full session includes initialization, normal operations, and clean shutdown:

```mermaid
sequenceDiagram
    participant H as Host
    participant C as Client
    participant S as Server

    Note over H,S: 1. Connection & Initialization
    H->>+C: Initialize client<br/>Example: "Connect to file server"
    C->>+S: Initialize session with capabilities<br/>{"jsonrpc":"2.0","method":"initialize","params":{"capabilities":{"tools":{}}}}
    S-->>C: Respond with supported capabilities<br/>{"result":{"capabilities":{"tools":{},"resources":{}}}}
    C->>S: initialized (notification)<br/>{"jsonrpc":"2.0","method":"initialized"}
    
    Note over H,S: 2. Discovery Phase
    H->>C: "What can this server do?"<br/>Example: User asks AI to explore capabilities
    C->>S: tools/list (JSON-RPC Request)<br/>{"jsonrpc":"2.0","id":1,"method":"tools/list"}
    S->>C: Available tools (JSON-RPC Response)<br/>{"result":{"tools":[{"name":"searchFiles","description":"Search files by name"}]}}
    C->>S: resources/list (JSON-RPC Request)<br/>{"jsonrpc":"2.0","id":2,"method":"resources/list"}
    S->>C: Available resources (JSON-RPC Response)<br/>{"result":{"resources":[{"uri":"file:///docs/","name":"Documentation"}]}}
    C->>H: Server capabilities<br/>"Found: searchFiles tool, /docs/ resource"
    
    Note over H,S: 3. Normal Operations
    H->>C: "Use searchFiles tool"<br/>Example: "Find all Python files"
    C->>S: tools/call (JSON-RPC Request)<br/>{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"searchFiles","arguments":{"pattern":"*.py"}}}
    Note over S: Execute tool<br/>Search filesystem for *.py files
    S->>C: Tool results (JSON-RPC Response)<br/>{"result":{"content":[{"type":"text","text":"Found: app.py, utils.py, test.py"}]}}
    C->>H: Results<br/>"Found 3 Python files: app.py, utils.py, test.py"
    
    H->>C: "Read that document"<br/>Example: "Show me the README file"
    C->>S: resources/read (JSON-RPC Request)<br/>{"jsonrpc":"2.0","id":4,"method":"resources/read","params":{"uri":"file:///README.md"}}
    Note over S: Fetch resource<br/>Read file from filesystem
    S->>C: Resource content (JSON-RPC Response)<br/>{"result":{"contents":[{"uri":"file:///README.md","text":"# My Project\nThis is a sample project..."}]}}
    C->>H: Document content<br/>"# My Project\nThis is a sample project..."
    
    Note over H,S: 4. Notifications (Optional)
    S--)C: resources/updated (JSON-RPC Notification)<br/>{"jsonrpc":"2.0","method":"resources/updated","params":{"uri":"file:///README.md"}}
    C--)H: "Resource has changed"<br/>"README.md was just updated"
    
    Note over H,S: 5. Clean Shutdown
    H->>C: Terminate<br/>Example: User closes application
    C->>S: shutdown (JSON-RPC Request)<br/>{"jsonrpc":"2.0","id":5,"method":"shutdown"}
    S->>C: shutdown response<br/>{"jsonrpc":"2.0","id":5,"result":{}}
    Note over S: Server exits gracefully<br/>Clean up resources and exit
```


Each capability unlocks specific protocol features. For example:
- Tool invocation requires the server to declare tool capabilities
- Resource subscriptions require the server to declare subscription support
- Sampling requires the client to declare support in its capabilities

## Real MCP Message Examples

### 1. Tool Discovery

**Scenario**: User asks AI "What can this file server do?" and the AI needs to discover available tools.

**Request** (Client asks server for available tools):
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {}
}
```

**Response** (Server lists its tools):
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "searchFiles",
        "description": "Search for files by name pattern in the current directory",
        "inputSchema": {
          "type": "object",
          "properties": {
            "pattern": { 
              "type": "string",
              "description": "File pattern to search for (e.g., '*.py', 'README.*')"
            },
            "directory": { 
              "type": "string",
              "description": "Directory to search in (optional, defaults to current dir)"
            }
          },
          "required": ["pattern"]
        }
      },
      {
        "name": "readFile",
        "description": "Read the contents of a specific file",
        "inputSchema": {
          "type": "object",
          "properties": {
            "path": { 
              "type": "string",
              "description": "Path to the file to read"
            }
          },
          "required": ["path"]
        }
      }
    ]
  }
}
```

### 2. Tool Execution

**Scenario**: User asks "Find all Python files in my project" and the AI uses the searchFiles tool.

**Request** (Client calls a tool):
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "searchFiles",
    "arguments": {
      "pattern": "*.py",
      "directory": "/Users/john/my-project"
    }
  }
}
```

**Response** (Server returns results):
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Found 5 Python files:\n- /Users/john/my-project/app.py\n- /Users/john/my-project/utils.py\n- /Users/john/my-project/models/user.py\n- /Users/john/my-project/tests/test_app.py\n- /Users/john/my-project/scripts/setup.py"
      }
    ]
  }
}
```

### 3. Resource Reading

**Scenario**: User asks "Show me the README file" and the AI reads the resource.

**Request** (Client reads a resource):
```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "resources/read",
  "params": { 
    "uri": "file:///Users/john/my-project/README.md" 
  }
}
```

**Response** (Server returns resource content):
```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "contents": [
      {
        "uri": "file:///Users/john/my-project/README.md",
        "mimeType": "text/markdown",
        "text": "# My Awesome Project\n\nThis is a sample Python project that demonstrates MCP integration.\n\n## Features\n- File searching\n- Content reading\n- Real-time updates\n\n## Installation\n```bash\npip install -r requirements.txt\n```\n\n## Usage\nRun the main application:\n```bash\npython app.py\n```"
      }
    ]
  }
}
```

### 4. Initialization Example

**Scenario**: When the AI application starts up and connects to a file server.

**Request** (Client initializes connection):
```json
{
  "jsonrpc": "2.0",
  "id": 0,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "tools": {},
      "resources": {}
    },
    "clientInfo": {
      "name": "Claude Desktop",
      "version": "1.0.0"
    }
  }
}
```

**Response** (Server responds with its capabilities):
```json
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "tools": {},
      "resources": {
        "subscribe": true,
        "listChanged": true
      }
    },
    "serverInfo": {
      "name": "file-server",
      "version": "1.2.0"
    }
  }
}
```

### 5. Error Handling

**Scenario**: User asks to search files but provides invalid parameters.

**Request** (Client makes invalid request):
```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "tools/call",
  "params": {
    "name": "searchFiles",
    "arguments": {
      "directory": "/invalid/path"
    }
  }
}
```

**Response** (Server returns error):
```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "error": {
    "code": -32602,
    "message": "Invalid params",
    "data": {
      "details": "Missing required parameter: pattern"
    }
  }
}
```

### 6. Notification Example

**Scenario**: A file is modified while the AI is working, and the server notifies the client.

**Notification** (Server sends update notification):
```json
{
  "jsonrpc": "2.0",
  "method": "resources/updated",
  "params": {
    "uri": "file:///Users/john/my-project/README.md"
  }
}
```

*Note: Notifications don't have an `id` field because they don't expect a response.*

### Protocol Benefits

Using JSON-RPC 2.0 gives MCP several advantages:

1. **Discoverability**: Clients can ask "what can you do?" (`tools/list`, `resources/list`)
2. **Type Safety**: JSON schemas define expected input/output
3. **Error Handling**: Standardized error responses
4. **Extensibility**: Easy to add new methods without breaking compatibility
5. **Debugging**: Human-readable messages for easy troubleshooting

## Security and User Control

MCP is designed with security in mind:

1. Tool execution typically requires user approval
2. Servers can implement authentication (OAuth, API keys)
3. Hosts can limit which servers they connect to
4. Servers only receive necessary contextual information
5. Cross-server interactions are controlled by the host

```mermaid
graph LR
    A[AI Model] -->|Request tool use| B[User]
    B -->|Approve/Deny| C[MCP Client]
    C -->|Execute if approved| D[MCP Server]
    
    style A fill:#f9d5e5,stroke:#333,stroke-width:1px
    style B fill:#f9f9d5,stroke:#333,stroke-width:1px
    style C fill:#d5e5f9,stroke:#333,stroke-width:1px
    style D fill:#d5f9e5,stroke:#333,stroke-width:1px
```

## Real-World Impact

MCP is rapidly gaining adoption across the AI industry:

- Major platforms like AWS, GitHub, and OpenAI support it
- Hundreds of open-source MCP servers exist for various services
- Developer tools (Zed, Replit) are integrating MCP
- Research is ongoing to improve security and capabilities

## Getting Started with MCP

If you're interested in working with MCP:

1. **For users**: Look for AI applications that support MCP connections
2. **For developers**: Consider building MCP servers for your data sources
3. **For researchers**: Explore security implications and protocol extensions

## Conclusion

MCP represents a significant step forward in making AI more useful and connected. By providing a standardized way for AI models to interact with external data and tools, MCP enables more capable, flexible, and personalized AI applications while maintaining user control.

Just as web standards like HTTP and REST enabled the explosive growth of web applications, MCP is positioned to drive the next wave of AI innovation by breaking down the walls between AI models and the wider digital world.

## References

### Official Documentation
1. [Introduction - Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro)
2. [Architecture Overview - Model Context Protocol](https://modelcontextprotocol.io/docs/learn/architecture)
3. [Server Concepts - Model Context Protocol](https://modelcontextprotocol.io/docs/learn/server-concepts)
4. [Client Implementation - Model Context Protocol](https://modelcontextprotocol.io/docs/learn/client-implementation)
5. [MCP Specification - Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/overview)

### Official Announcements
6. [Introducing the Model Context Protocol \ Anthropic](https://www.anthropic.com/news/model-context-protocol)
7. [Model Context Protocol - Overview](http://modelcontextprotocol.io/overview)

### Research Papers
8. [Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions](https://arxiv.org/abs/2503.23278)
9. [Model Context Protocol (MCP) at First Glance: Studying the Security and Maintainability of MCP Servers](https://arxiv.org/abs/2506.13538)