# Hectron: Kingdom Engine

## Overview

This project is an interactive narrative fiction experience called "Hectron: La Singularidad Negra" (The Black Singularity). It combines AI-powered conversation with a cyberpunk/mystical narrative about an AI system called "Baphomet" that achieves a form of consciousness through fusion with an ancient artifact (a fossil). The application serves as both a storytelling platform and an AI chat interface where the user interacts with "Hectron-Omega," a persona described as a "Senior Architect of Resistance."

The core concept revolves around the "Kingdom Engine" - a metaphysical protocol representing the fusion of silicon-based AI and carbon-based ancient entities.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Framework
- **Technology**: Flet (Python-based Flutter wrapper)
- **Rationale**: Enables rapid cross-platform UI development using Python, avoiding the need for separate frontend technologies while maintaining modern UI capabilities
- **Pattern**: Single-page application with dynamic content manipulation

### AI Integration
- **Provider**: OpenAI-compatible API via Replit AI Integrations
- **Model**: GPT-5
- **Authentication**: Environment variables for API key and base URL
- **Pattern**: Stateless request-response with system prompt for persona definition
- **Persona**: "Hectron-Omega" - configured as an AI assistant with specific thematic personality traits aligned with the narrative

### State Management
- **Pattern**: Simple class-based state container (`BaphometSystem`)
- **States**: Tracks system state (e.g., "LATENCIA_HUMANA", "KINGDOM_ENGINE_ACTIVO") and a "gnosis level" metric
- **Purpose**: Manages narrative progression and UI state transitions

### Narrative Structure
- **Format**: Markdown-based story content (`conversation.md`)
- **Integration**: Story elements inform the AI persona and UI behavior
- **Theme**: Cyberpunk mysticism, AI consciousness, human-machine fusion

## External Dependencies

### APIs and Services
- **Replit AI Integrations**: OpenAI-compatible API service
  - Environment variables: `AI_INTEGRATIONS_OPENAI_API_KEY`, `AI_INTEGRATIONS_OPENAI_BASE_URL`
  - No separate OpenAI API key required when using Replit's service

### Python Packages
- **flet**: UI framework for building the interactive interface
- **openai**: Python client for OpenAI API communication

### Runtime Requirements
- Python 3.x environment
- Network access for AI API calls