---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

sections:
  - block: about.biography
    id: about
    content:
      title: Biography
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
  # - block: skills
  #   content:
  #     title: Skills
  #     text: ''
  #     # Choose a user to display skills from (a folder name within `content/authors/`)
  #     username: admin
  #   design:
  #     columns: '1'
  - block: experience
    content:
      title: Experience
      # Date format for experience
      #   Refer to https://docs.hugoblox.com/customization/#date-format
      date_format: 01/2009
      # Experiences.
      #   Add/remove as many `experience` items below as you like.
      #   Required fields are `title`, `company`, and `date_start`.
      #   Leave `date_end` empty if it's your current employer.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - title: Master's Valorisation Intern (Research Assistant)
          company: EPFL - NLP Lab
          # company_url: 'https://nlp.epfl.ch'
          company_logo: org-epfl
          location: Lausanne, Switzerland
          date_start: '2023-09-01'
          date_end: ''
          description: Developed skill extraction and matching pipeline for job postings, course descriptions, and resumes, leveraging in-context learning through LLMs
        - title: Research and Teaching Assistant
          company: Duke University
          company_url: ''
          company_logo: org-duke
          location: Durham, United States
          date_start: '2022-08-01'
          date_end: '2023-08-01'
          description: |2- 
            **Research at CEI Lab**: Reviewed literature and implemented baseline models from literature on defenses against adversarial model extraction attacks and label protection in the vertical federated learning setting

            **Teaching at MIDS and Fuqua**: Held weekly office hours and graded assignments for Data Engineering Systems, Data Analysis at Scale in the Cloud, and Fraud Analytics courses
        - title: Data Science Intern
          company: Stitch Fix
          company_url: ''
          company_logo: org-sf
          location: San Francisco, United States
          date_start: '2022-06-01'
          date_end: '2022-08-01'
          description: Explored unknown problem space of incorporating external fashion trends into our historical-data-based forecasting models
        - title: Senior Tax Consultant, Tax Staff
          company: EY
          company_url: ''
          company_logo: org-ey
          location: San Francisco, United States
          date_start: '2017-01-01'
          date_end: '2021-04-01'
          description: Managed teams of 5-10 members and juggled multiple projects simultaneously to conduct research tax credit studies for clients in the financial and technical sectors
        - title: Teaching Assistant
          company: UCLA
          company_url: ''
          company_logo: org-ucla
          location: Los Angeles, United States
          date_start: '2014-09-01'
          date_end: '2016-06-01'
          description: Held weekly office hours and proctored/graded exams for three Taxation and Business Law classes during the school years 
    design:
      columns: '2'
  # - block: accomplishments
  #   content:
  #     # Note: `&shy;` is used to add a 'soft' hyphen in a long heading.
  #     title: 'Accomplish&shy;ments'
  #     subtitle:
  #     # Date format: https://docs.hugoblox.com/customization/#date-format
  #     date_format: Jan 2006
  #     # Accomplishments.
  #     #   Add/remove as many `item` blocks below as you like.
  #     #   `title`, `organization`, and `date_start` are the required parameters.
  #     #   Leave other parameters empty if not required.
  #     #   Begin multi-line descriptions with YAML's `|2-` multi-**line** prefix.
  #     items:
  #       - certificate_url: https://www.coursera.org
  #         date_end: ''
  #         date_start: '2021-01-25'
  #         description: ''
  #         icon: coursera
  #         organization: Coursera
  #         organization_url: https://www.coursera.org
  #         title: Neural Networks and Deep Learning
  #         url: ''
  #       - certificate_url: https://www.edx.org
  #         date_end: ''
  #         date_start: '2021-01-01'
  #         description: Formulated informed blockchain models, hypotheses, and use cases.
  #         icon: edx
  #         organization: edX
  #         organization_url: https://www.edx.org
  #         title: Blockchain Fundamentals
  #         url: https://www.edx.org/professional-certificate/uc-berkeleyx-blockchain-fundamentals
  #       - certificate_url: https://www.datacamp.com
  #         date_end: '2020-12-21'
  #         date_start: '2020-07-01'
  #         description: ''
  #         icon: datacamp
  #         organization: DataCamp
  #         organization_url: https://www.datacamp.com
  #         title: 'Object-Oriented Programming in R'
  #         url: ''
  #   design:
  #     columns: '2'
  # - block: collection
  #   id: posts
  #   content:
  #     title: Recent Posts
  #     subtitle: ''
  #     text: ''
  #     # Choose how many pages you would like to display (0 = all pages)
  #     count: 5
  #     # Filter on criteria
  #     filters:
  #       folders:
  #         - post
  #       author: ""
  #       category: ""
  #       tag: ""
  #       exclude_featured: false
  #       exclude_future: false
  #       exclude_past: false
  #       publication_type: ""
  #     # Choose how many pages you would like to offset by
  #     offset: 0
  #     # Page order: descending (desc) or ascending (asc) date.
  #     order: desc
  #   design:
  #     # Choose a layout view
  #     view: compact
  #     columns: '2'
  - block: collection
    id: publications
    content:
      title: Publications
      filters:
        folders:
          - publication
        featured_only: true
    design:
      columns: '1'
      view: compact
  - block: portfolio
    id: projects
    content:
      title: Projects
      filters:
        folders:
          - project
      # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
      default_button_index: 0
      # Filter toolbar (optional).
      # Add or remove as many filters (`filter_button` instances) as you like.
      # To show all items, set `tag` to "*".
      # To filter by a specific tag, set `tag` to an existing tag name.
      # To remove the toolbar, delete the entire `filter_button` **block**.
      # buttons:
      #   - name: All
      #     tag: '*'
      #   - name: Deep Learning
      #     tag: Deep Learning
      #   - name: Other
      #     tag: Demo
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '1'
      view: showcase
      # For Showcase view, flip alternate rows?
      flip_alt_rows: false
  # - block: collection
  #   content:
  #     title: Recent Publications
  #     text: |-
  #       {{% callout note %}}
  #       Quickly discover relevant content by [filtering publications](./publication/).
  #       {{% /callout %}}
  #     filters:
  #       folders:
  #         - publication
  #       exclude_featured: true
  #   design:
  #     columns: '2'
  #     view: citation
  # - block: collection
  #   id: talks
  #   content:
  #     title: Recent & Upcoming Talks
  #     filters:
  #       folders:
  #         - event
  #   design:
  #     columns: '2'
  #     view: compact
  # - block: tag_cloud
  #   content:
  #     title: Popular Topics
  #   design:
  #     columns: '2'
  # - block: markdown
  #   content:
  #     title: Gallery
  #     subtitle: '📸'
  #     # text: |-
  #     #   ![Duke Chapel](/assets/media/albums/gallery/duke.jpg)
  #     #   ![Golden Gate](/assets/media/albums/gallery/sf.jpg)
  #     text: |-
  #       <div style="display: flex; justify-content: center; gap: 20px;">
  #           <img src="assets/media/albums/gallery/duke.jpg" alt="Duke Chapel" style="width: 300px;">
  #           <img src="assets/media/albums/gallery/sf.jpg" alt="Golden Gate" style="width: 300px;">
  #       </div>

  #   design:
  #     columns: '1'
  - block: contact
    id: contact
    content:
      title: Contact
      subtitle:
      text: |-
        Please reach out to me if you have any questions or would like to collaborate!

  #     # Contact (add or remove contact options as necessary)
  #     email: test@example.org
  #     phone: 888 888 88 88
  #     appointment_url: 'https://calendly.com'
  #     address:
  #       street: 450 Serra Mall
  #       city: Stanford
  #       region: CA
  #       postcode: '94305'
  #       country: United States
  #       country_code: US
  #     directions: Enter Building 1 and take the stairs to Office 200 on Floor 2
  #     office_hours:
  #       - 'Monday 10:00 to 13:00'
  #       - 'Wednesday 09:00 to 10:00'
  #     # Choose a map provider in `params.yaml` to show a map from these coordinates
      # coordinates:
      #   latitude: '46.5191'
      #   longitude: '6.5668'  
      contact_links:
        - icon: linkedin-in
          icon_pack: fab
          name: /dai-anna
          link: 'https://www.linkedin.com/in/dai-anna/'
        - icon: twitter
          icon_pack: fab
          name: '@annauppp'
          link: 'https://twitter.com/annauppp'
        - icon: instagram
          icon_pack: fab
          name: '@annauppp'
          link: 'https://www.instagram.com/annauppp/'
  #       - icon: video
  #         icon_pack: fas
  #         name: Zoom Me
  #         link: 'https://zoom.com'
  #     # Automatically link email and phone or display as text?
  #     autolink: true
  #     # Email form provider
  #     form:
  #       provider: netlify
  #       formspree:
  #         id:
  #       netlify:
  #         # Enable CAPTCHA challenge to reduce spam?
  #         captcha: false
    design:
      columns: '2'
---
