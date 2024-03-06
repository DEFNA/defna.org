---
layout: page
title: About
permalink: /about/
include_twocols: true
feature_image: defna2023
logo_image: DEFNA-Logotype.png
---

Django Events Foundation North America (DEFNA) is a non-profit based in California USA. It was formed in 2015 at the request of the [Django Software Foundation (DSF)](https://www.djangoproject.com/foundation/) to run [DjangoCon US](https://djangocon.us). The DSF have licensed DEFNA to run DjangoCon US for 2015-2022. Beyond DjangoCon US we also plan to be involved with other events in North America that cover the education and outreach of Django.

<h2>Meet the DEFNA Board</h2>
{% assign boardmembers = site.boardmembers | sort:"index" %}
{% for boardmember in boardmembers %}
{% assign mod = forloop.index | modulo: 2 %}
<div class="row board-content">
{% if mod == 0 %}
    <div class="col-md-6 right">
{% else %}
	<div class="col-md-6">
{% endif %}
        <h3>{{ boardmember.name }}</h3>
        <h4>{{ boardmember.role }}</h4>
        {{ boardmember.content }}
    </div>
	<div class="col-md-6">
        <img src="{{ site.baseurl }}{{ boardmember.photo_url }}" alt="{{ boardmember.name }}">
    </div>
</div>
{% endfor %}

<hr>
<h2>Past Board Members</h2>

{% assign pastmembers = site.pastmembers | sort:"index" %}
{% for pastmember in pastmembers %}
{% assign mod = forloop.index | modulo: 2 %}
<div class="row board-content">
{% if mod == 0 %}
    <div class="col-md-6">
{% else %}
	<div class="col-md-6 right">
{% endif %}
        <h3>{{ pastmember.name }}</h3>
        <h4>{{ pastmember.role }}</h4>
        {{ pastmember.content }}
    </div>
	<div class="col-md-6">
        <img src="{{ pastmember.photo_url }}" alt="{{ pastmember.name }}">
    </div>
</div>
{% endfor %}
