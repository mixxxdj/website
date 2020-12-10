title: The Mixxx Class Diagram
author: Albert
date: 2010-08-16 04:59:00
comments: no

{% extends "post.html" %}

{% block post %}

<div class="separator" style="clear: both; text-align: center;"><a href="{% static '/static/images/news/lolclassdiagram.png' %}" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="233" src="{% static '/static/images/news/lolclassdiagram.png' %}" width="400" />
</a>
</div>
<br />
<div style="text-align: center;"><b>Sorry, I just had to post this.</b>
</div>
<div style="text-align: center;"><br />
</div>
I'm scraping together a press kit for the new 1.8.0 website and I came across this awesome class diagram in the "<a href="http://haste.dk/tue/articles/nime03-mixxx.pdf">The Mixxx Paper</a>
". Tue Haste Andersen presented Mixxx and that paper at a conference back in 2003, and this diagram represents Mixxx's internals at the time. You're looking at a snapshot inside one of the earliest versions of Mixxx, which has since grown to be the world's most popular free DJ software.<br />
<br />
The diagram you're looking at is a standard tool software engineers use called a <i>UML class diagram</i>
, and it lets developers effectively communicate their ideas about code layout. If we had to make a new UML class diagram for Mixxx in 2010, it'd probably cover one of the walls of my apartment. Although the MixxxApp, ControlObject, EngineObject, and SoundSource classes still exist (!) and might even be recognizable from their original incarnations, pretty much everything else has changed drastically.<br />
<br />
The Mixxx architecture has expanded to&nbsp;accommodate an arbitrary number of sound devices, MIDI controllers, and soon, and arbitrary number of decks.&nbsp;Good things are in store.

{% endblock %}
