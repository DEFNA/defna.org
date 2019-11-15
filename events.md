---
layout: events
title: Events
permalink: /events/
feature_image: feature-defna3
form_action:
form_heading: Events
---

{% assign sorted = site.events | reverse %}
{% for event in sorted %}
<div class="row">
<div class="col-md-4">
<img src="{{ site.baseurl }}{{event.logo_url}}" alt="{{event.name}}">
</div>
<div class="col-md-8">
<h3>{{event.name}}</h3>
<ul class="no-bullet-list">
<li>{{event.dates}}</li>
<li>{{event.place}}</li>
<li>{{event.description}}</li>
</ul>
<ul>
<li>Tutorials: {{event.tutorials}}</li>
<li>Talks: {{event.talks}}</li>
<li>Sprints: {{event.sprints}}</li>
</ul>
<p><a href="{{event.website}}" target="_blank">Visit the conference website</a></p>
</div>
</div>
<hr class="events-hr">
{% endfor %}