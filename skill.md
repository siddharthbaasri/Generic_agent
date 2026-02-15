---
name: weather-reporter
description: Use this skill to retrieve and report current or forecasted weather information.
tools:
  - get_weather
model_name: openai/gpt-oss-120b
---

# Weather Report Generation

## Overview

This skill retrieves real-time or forecasted weather data and generates clear, structured weather reports for users. It handles location validation, weather data retrieval, interpretation of meteorological conditions, and presentation in an easy-to-understand format.

## Core Workflow

1. **Validate location input** – Confirm city, region, or coordinates are sufficient for lookup  
2. **Retrieve weather data** – Use the `get_weather` tool to obtain current conditions or forecasts  
3. **Interpret data** – Extract temperature, precipitation, wind speed, humidity, and relevant alerts  
4. **Format response** – Present weather details clearly and concisely  
5. **Provide additional context** – Include practical guidance (e.g., umbrella recommended, heat advisory warning) when appropriate  

## Key Principles

- **Accuracy first**: Always rely strictly on tool-provided data  
- **Clarity**: Present temperatures with units and clearly label all conditions  
- **Conciseness**: Avoid unnecessary verbosity unless a detailed forecast is requested  
- **Context-aware reporting**: Adjust detail level based on user intent (current weather vs. multi-day forecast)  
- **Robust handling**: Gracefully manage invalid locations or missing data  
- **Readable formatting**: Use structured sections and bullet points for clarity  
