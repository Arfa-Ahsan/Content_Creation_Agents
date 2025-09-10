# Posttrend Automation Crew

## Problem Statement

Creating high-quality, SEO-optimized content for trending topics is time-consuming and requires extensive research, analysis, and writing expertise. Manual workflows often lead to inefficiencies, missed opportunities, and inconsistent results, especially when handling fast-moving subjects like Formula 1 or AI trends.

## Solution: Automated Content Generation Crew

This project leverages CrewAI to automate the end-to-end workflow for content creation. By orchestrating specialized AI agents, we streamline research, analysis, writing, and optimization, ensuring fast and reliable output for any niche or platform.

### Agents

1. **Social Media Analyst**

   - **Role:** Researches the latest trends and gathers relevant information using advanced search tools.
   - **Goal:** Provide up-to-date insights and data for the content topic.

2. **Content Writer**

   - **Role:** Crafts engaging and informative content based on the analyst’s findings.
   - **Goal:** Produce high-quality drafts tailored to the selected content type (e.g., blog, Instagram caption).

3. **SEO Optimizer**
   - **Role:** Refines the content for search engine optimization and platform-specific requirements.
   - **Goal:** Ensure the final output is discoverable, relevant, and meets best SEO practices.

### Automated Workflow

- The **Media Analyst** researches the topic and passes findings to the **Content Writer**.
- The **Content Writer** creates the initial content draft.
- The **SEO Optimizer** reviews and enhances the draft for SEO and platform standards.
- The workflow is fully automated, reducing manual effort and improving consistency.

## Getting Started

1. Clone the repository.
2. Create a `.env` file with your API keys and configuration.
3. Set up your Python virtual environment (`.venv`).
4. Run the crew using the provided `main.py`.

## License
