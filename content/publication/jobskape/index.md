---
title: 'JobSkape: A Framework for Generating Synthetic Job Postings to Enhance Skill Matching'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin
  - Antoine Magron
  - Mike Zhang
  - Syrielle Montariol
  - Antoine Bosselut

# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'

date: '2024-01-01'
doi: ''

# Schedule page publish date (NOT publication's date).
# publishDate: '2017-01-01'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
# publication_types: ['paper-workshop']

# Publication name and optional abbreviated publication name.
publication: The 1st Workshop on Natural Language Processing for Human Resources (NLP4HR), EACL 2024
publication_short: NLP4HR (EACL 2024)

abstract: Recent approaches in skill-to-surface-form matching, employing synthetic training data for classification or similarity model training, have shown promising results, eliminating the need for time-consuming and expensive annotation. However, previous datasets have limitations, such as featuring only one skill per sentence and generally comprising short sentences. This paper introduces JobSkape, a framework to generate synthetic data that resembles real-world job postings, specifically designed to enhance skill-to-taxonomy matching. Within this framework, we create SkillSkape, a comprehensive open-source synthetic dataset of job postings tailored for skill-matching tasks. We introduce several offline metrics that show our dataset is more diverse, realistic, and follows a higher quality based on similarities. Additionally, we present a multi-step pipeline utilizing large language models (LLMs), benchmarking against supervised methodologies. We outline that the performances are comparable and that each method can be used for different use cases.

# Summary. An optional shortened abstract.
summary: Developed a framework to generate synthetic job postings using LLMs to address the lack of annotated job posting data that support skill extraction and matching tasks.

tags: [NLP, Skill Matching, NLP4HR, LLMs, Synthetic Data]

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
links:
- name: Preprint
  url: https://arxiv.org/abs/2402.03242

url_pdf: 'https://arxiv.org/pdf/2402.03242.pdf'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# image:
#   caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
#   focal_point: ''
#   preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
# projects:
#   - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---
