---
name: csv-report
description: Use this skill whenever the user wants to create a professional PDF report from CSV data. Triggers include requests to "generate a report from CSV", "create a PDF report from this data", "make a report with this table", or any request that involves taking tabular data (CSV) and producing a formatted PDF document. Use this when users want data visualization, analysis summaries, or professional document output from their CSV files.
tools:
  - generate_pdf_report
  - send_email
  - summarize_text
model_name: openai/gpt-oss-20b
---

# CSV to PDF Report Generation

## Overview

This skill generates professional PDF reports from CSV data with customizable formatting, charts, and analysis. It handles data loading, processing, visualization, and PDF generation to create publication-ready reports.

## Core Workflow

1. **Read and validate CSV data** - Load CSV, check structure, handle encoding
2. **Analyze data** - Generate summary statistics and insights
3. **Create visualizations** - Generate charts and graphs as appropriate
4. **Build PDF report** - Assemble formatted document with title, data, charts, and analysis
5. **Output to /mnt/user-data/outputs/** - Save final PDF for user access

## Key Principles

- **Professional appearance**: Use clean formatting, consistent styling, proper spacing
- **Data-driven**: Let the data dictate chart types and analysis approaches
- **Accessible**: Clear labels, legends, and explanations
- **Error handling**: Gracefully handle missing data, encoding issues, malformed CSVs
- **Performance**: Efficient processing even for large datasets (sample if needed)
