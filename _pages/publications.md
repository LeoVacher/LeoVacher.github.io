---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

<!-- ### Galactic physics and component separation

#### 2022 

- [*Generative Models of Multi-channel Data from a Single Example – Application to Dust Emission*](https://leovacher.github.io/_publications/2022-08-06-multifreq-WPH.md)\\
B. Régaldo-Saint Blancard, E. Allys, C. Auclair, F. Boulanger, M. Eickenberg, F. Levrier, *L. Vacher*, S. Zhang\\
[arxiv 2208.03538](https://arxiv.org/pdf/2208.03538.pdf) (submitted to ApJ)


### The LiteBIRD instrument
#### 2022

### Stability of fundamental constants

#### 2022 -->