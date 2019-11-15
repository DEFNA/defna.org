---
layout: page
title: About
permalink: /about/
include_twocols: true
feature_image: feature-defna2
---

Django Events Foundation North America (DEFNA) is a non-profit based in California USA. It was formed in 2015 at the request of the Django Software Foundation (DSF) to run DjangoCon US. The DSF have licensed DEFNA to run DjangoCon US for 2015-2020. Beyond DjangoCon US we also plan to be involved with other events in North America that cover the education and outreach of Django.

<h2>Meet the DEFNA board</h2>
{% for boardmember in site.boardmembers %}
{% assign mod = forloop.index | modulo: 2 %}
<div class="row board-content">
{% if mod == 0 %}
    <div class="col-md-6 right">
{% else %}
	<div class="col-md-6">
{% endif %}
        <h3>{{ boardmember.name }}</h3>
        <p>{{ boardmember.description }}</p>
    </div>
	<div class="col-md-6">
        <img src="{{ boardmember.photo_url }}" alt="{{ boardmember.name }}">
    </div>
</div>
{% endfor %}

<hr>
<h2>Past board members</h2>

{% for pastmember in site.pastmembers %}
{% assign mod = forloop.index | modulo: 2 %}
<div class="row board-content">
{% if mod == 0 %}
    <div class="col-md-6">
{% else %}
	<div class="col-md-6 right">
{% endif %}
        <h3>{{ pastmember.name }}</h3>
        <p>{{ pastmember.description }}</p>
    </div>
	<div class="col-md-6">
        <img src="{{ pastmember.photo_url }}" alt="{{ pastmember.name }}">
    </div>
</div>
{% endfor %}