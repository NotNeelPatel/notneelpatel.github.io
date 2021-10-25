---
layout: page
title: Tags
permalink: /tags/
---
{% assign sortedTags = site.tags | sort %}
{% for tag in sortedTags %}
<div id=title>
<h2> {{tag[0]}}</h2>
</div>
{% for post in tag[1] %}

<div id="centerText">
 <p><a href="{{ post.url }}">{{ post.title }}</a> | {{ post.date | date: '%m/%d/%Y' }}</p>

{% endfor %}

</div>

{% endfor %}




