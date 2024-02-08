---
title: 'MODELGUARD: Information-Theoretic Defense Against Model Extraction Attacks'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - Minxue Tang
  - admin
  - Louis DiValentin
  - Aolin Ding
  - Amin Hass
  - Neil Zhenqiang Gong
  - Yiran Chen
  - Hai "Helen" Li

# Author notes (optional)
# author_notes:


date: '2024-08-14'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2024-01-01'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
# publication_types: ['paper-workshop']

# Publication name and optional abbreviated publication name.
publication: 33rd USENIX Security Symposium
publication_short: USENIX Security 2024

abstract: Malicious utilization of a query interface can compromise the confidentiality of ML-as-a-Service (MLaaS) systems via model extraction attacks. Previous studies have proposed to perturb the predictions of the MLaaS system as a defense against model extraction attacks. However, existing prediction perturbation methods suffer from a poor privacy-utility balance and cannot effectively defend against the latest adaptive model extraction attacks. In this paper, we propose a novel prediction perturbation defense named MODELGUARD, which aims at defending against adaptive model extraction attacks while maintaining a high utility of the protected system. We develop a general optimization problem that considers different kinds of model extraction attacks, and MODELGUARD provides an information-theoretic defense to efficiently solve the optimization problem and achieve resistance against adaptive attacks. Experiments show that MODELGUARD attains significantly better defensive performance against adaptive attacks with less loss of utility compared to previous defenses.

# Summary. An optional shortened abstract.
summary: **TL;DR** Proposed novel defense against adaptive model extraction attacks through prediction perturbation by leveraging information theory.

tags: [Adversarial Machine Learning, Model Extraction Attacks, Information Theory]

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://www.usenix.org/system/files/sec24summer-prepub-409-tang.pdf'
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
