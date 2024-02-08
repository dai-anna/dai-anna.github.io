---
title: 'PlugVFL: Robust and IP-Protecting Vertical Federated Learning against Unexpected Quitting of Parties'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - Jingwei Sun
  - Zhixu Du
  - admin
  - Saleh Baghersalimi
  - Alireza Amirshahi
  - David Atienza
  - Yiran Chen

# Author notes (optional)
# author_notes:

date: '2023-03-28'
doi: ''

# Schedule page publish date (NOT publication's date).
# publishDate: '2017-01-01'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
# publication_types: ['paper-workshop']

# Publication name and optional abbreviated publication name.
publication: ""
publication_short: "[preprint]"

abstract: Vertical federated learning (VFL) enables a service provider (i.e., active party) who owns labeled features to collaborate with passive parties who possess auxiliary features to improve model performance. Existing VFL approaches, however, have two major vulnerabilities when passive parties unexpectedly quit in the deployment phase of VFL - severe performance degradation and intellectual property (IP) leakage of the active party's labels. In this paper, we propose Party-wise Dropout to improve the VFL model's robustness against the unexpected exit of passive parties and a defense method called DIMIP to protect the active party's IP in the deployment phase. We evaluate our proposed methods on multiple datasets against different inference attacks. The results show that Party-wise Dropout effectively maintains model performance after the passive party quits, and DIMIP successfully disguises label information from the passive party's feature extractor, thereby mitigating IP leakage.

# Summary. An optional shortened abstract.
summary: **TL;DR** Research on robustness of vertical federated learning convolutional models against performance and IP leakage risks when nactive parties unexpectedly quit during deployment

tags: [Vertical Federated Learning, Robustness, Intellectual Property Protection]

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
links:
- name: Preprint
  url: https://arxiv.org/abs/2303.18178

url_pdf: 'https://arxiv.org/pdf/2303.18178.pdf'
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
