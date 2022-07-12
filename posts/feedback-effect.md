---
publish_date: '2013-01-29 12:00:00'
summary_length: 3
title: Feedback Effect
---
I played around with an old demoscene effect often called "feedback". It probably happend to you, that you forgot the glClear (or equivalent clear screen commands) at the beginning of your renderloop which lead you to very funny results. This effect is essentially this but kicked up a notch.

A video first:
<center><iframe width="560" height="315" src="https://www.youtube.com/embed/AiWi9A39LxU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>

The code is a mess, so I just present some pseudo-code:
<ul>
	<li>Set render target to texture "fboTex"</li>
	<li>Add a translation to the transforms (I used my own "continousRandom", which returns an interpolated value from a buffer of random values and polar coordinates (an angle and a magnitude), so the translation changes, but randomly and continuous)</li>
	<li>Add a scaling to the transforms with a little more than screen size (in my example 1.011 times)</li>
	<li>Set color (you have to keep in mind, that having 0.5 as the red channel for example results in having half of the red in the next frame, and fourth in the next, and eighth in the next and so fort, so the values are very close to one and very hard to tweak) (I used: 0.999, 0.995, 0.1, 1.0)</li>
	<li>Render a quad with fboTex (the last frame)</li>
	<li>Just render the image you want to effectify (In my case an image which said "screensaver" using a cool font)</li>
	<li>Render fboTex to screen</li>
</ul>
