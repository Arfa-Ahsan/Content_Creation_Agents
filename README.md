# Content Creation Agents

## Project Overview

This project automates the process of generating high-quality, platform-specific content for any given topic. It uses a team of specialized AI agents to handle research, writing, and SEO optimization, making it easy for businesses or individuals to quickly create engaging content for blogs, social media, and more.

---

## What Problem Is It Solving?

Manual content creation is slow, inconsistent, and often misses current trends.

- Researching what’s trending takes time and expertise.
- Writing content that fits each platform’s style and audience is challenging.
- Optimizing for SEO without losing readability is a specialized skill.

**This project solves these problems by:**

- Automatically researching trending topics in any area you specify.
- Generating tailored content for your chosen platform (blog, Instagram, LinkedIn, etc.).
- Optimizing the content for search engines and platform engagement.

---

## How Does It Work?

### Media Analyst Agent

- Researches the latest trends in your chosen topic using sources like Twitter, Reddit, LinkedIn, and news.
- Filters out noise and finds actionable, specific trends.
- Summarizes what’s popular right now and suggests content angles.

### Content Writer Agent

- Takes the analyst’s findings and crafts engaging content in the requested format (blog, LinkedIn post, Instagram caption, etc.).
- Adapts the tone and style for each platform.
- Ensures the content is clear, concise, and encourages interaction.

### SEO Optimizer Agent

- Refines the draft for search engine visibility and platform best practices.
- Adds keywords, meta descriptions, and improves structure.
- Makes sure the content ranks well and remains engaging.

---

## LLM Provider Options

This project supports multiple LLM backends. By default, it uses **Hugging Face Inference (Llama 3 70B Instruct)**, but you can switch to:

- **ChatGroq Moonshot AI (kimi k2 instruct 0905)**
- **Azure AI Foundry (gpt-oss-120b)**

You can select your preferred LLM by editing the `Posttrend` class in `src/posttrend/crew.py` and uncommenting the relevant section.

---
