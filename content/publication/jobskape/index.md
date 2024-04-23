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

date: '2024-03-22'
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
# - name: Preprint
#   url: https://arxiv.org/abs/2402.03242

url_pdf: 'https://aclanthology.org/2024.nlp4hr-1.4/'
url_code: 'https://github.com/magantoine/JobSkape'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: 'https://s3.amazonaws.com/pf-user-files-01/u-59356/uploads/2024-02-20/8t03237/NLP4HR_2024_JobSkape_presentation.pdf'
# url_slides: 'https://assets.underline.io/lecture/95936/slideshow/6b2e4a43d924936d29604b32c4990ade.pdf?Expires=1714041591&Signature=ia-46BVUVPhW0CaOCEvMrK5D2uzc8Yd1glP35RBISI~sUx9PVDXmlHXNhwzPfZCd798AEq0~i~fGHusP-g9U6hdUfCUP-lmaQas47KNkZvGtStsB0PiEWFswx-hKJ-M86yAOSTvEx2GoyIIrwYaBTeLY1pxRWyiI4gLhO81N6zV8IDVvFUkkTr26oLtCaEyyax-XAKoQnbkCo3xRqJFb7W5Q9EKPz7oXFKjhEkw0OCPpmbk0HB-37wnZj3pqC9tUkFy2k9A5z9N6DxXs8TCFOnE3lHdoW2AeIwT7mAXodsZa82WNDlqCHuENyIXoi0eKWspgGhIr7nhkASdqW~puig__&Key-Pair-Id=K2CNXR0DE4O7J0'
url_source: ''
# url_video: 'https://underline.io/lecture/95936-jobskape-a-framework-for-generating-synthetic-job-postings-to-enhance-skill-matching'

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
