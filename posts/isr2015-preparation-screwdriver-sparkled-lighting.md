---
publish_date: '2015-11-06 01:35:12'
summary_length: 3
title: Preparation for Indie Speed Run 2015 - Screwdriver, SparklEd, Lighting
---
In preparation for Indie Speed Run 2015 (which went well and for which I will post our game when the voting period starts) me and a long time programming buddy, <a href="http://shellfishgames.com/">Markus</a>, decided to prepare by building a handful of tools that are going to make some things a little easier. We find ourself discarding the same ideas time and time again, because we don't deem them feasible in the often severly limited amount of time or not discarding them but spending too much time on them, so we decided to prepare them beforehand.
We had a lot of stuff in mind including a post-process library, realtime and precomputed 2D lighting, pre-built character controllers and smooth collision detection and response solutions for different scenarios that we might need, finally a proper particle system and a corresponding editor, an editor and a library for skeletal animations, and a level editor that supplements the awesome <a href="http://www.mapeditor.org/">Tiled</a> for games that are not tile based (but either polygon or simply sprite based). But as it becomes glaringly obvious this is quite a lot of work and of course we did not manage to finish everything we had on the list, although still a considerable part of it.
Markus worked on the animation editor/library and manged to finish it in time. Sadly we didn't have any use for it in the jam, just as we didn't for everything I worked on. We wanted to implement the best idea we had and coincidentally (and unexpectedly) there was no need for the tech we developed beforehand (exluding a small exception elaborated on later). The projects I took on and managed to finish mostly before the jam were the lighting system, the particle effect editor and the level editor.
<h2>The Level Editor (Screwdriver) - <a href="https://github.com/pfirsich/Screwdriver">GitHub</a></h2>
This level editor uses my GUI, kraidGUI. It's a GUI made for being modified in a sense. It only serves as a slim core for handling/passing events and handling properties. Look and feel are implemented in a "theme", which makes use of a very simple backend, which, as of yet, is only implemented for löve. Every part of it can be exchanged and extended easily. For Screwdriver I had to implement and color picker and was surprised how well kraidGUI did it's work by making this very easy.
Both the GUI and the Editor were meant as an exercise in writing actual software. I feel like, lacking a formal education and professional experience, I tend to "make things work" first and foremost often leaving proper software design behind. This certainly also has a lot to do with me participating in game jams a lot. But GUIs and Editors (in this case especially) are meant to be used a lot more than once. kraidGUI has some things I'm still not completely content with and Screwdriver is also not free from a few sketchy ways to do things, that I would consider hacks, but all in all I think that it's still mostly quite readable, maintainable and hack free. Both of them lack documentation, but I think it's very common for programmers to not be particularly fond of creating these. Anyways I will try to still spend some time on documenting kraidGUI soon, since I think it's a nice piece of software and other people might deem it useful too.

Regarding the editor itself, I made it for usage with many different games in mind. Every type of entity in the game world has an entity description, which contains Metadata (modifiable or not), so a seemingly fairly custom fitted editor can be prepared for any game without much effort. The system corresponding to the components that make up the entities are implemented in the components itself, which kind of defeats the purpose of ECSs, since special cases still have to be handled inside the components, but the editor was supposed to be modular and capable of being extended with rather complicated edit modes without treating the main components special. Therefore I'm borrowing terminology more than anything from entity component systems. Thankfully I didn't regret the way of doing this yet, since there was no special case except shared behaviour that could be resolved by properly breaking up functionality and using inheritance. The editor remains very modular and can be extended fairly easily with rather comprehensive editing capabilities.

An example of such a entity description file can be seen here (and should be self-explanatory):
<script src="https://gist.github.com/pfirsich/4e9e7fb9bf626e3085d4.js"></script>

The editor itself can be seen used in this video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/x0ldw3uBklg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<h2>The Particle Effect Edtior (SparklEd) - <a href="https://github.com/pfirsich/SparklEd">GitHub</a></h2>
After collecting some notes about the particle system I wanted to implement for this editor, I remembered briefly that I might have heard of löve having a particle system already. I didn't check, but a properly tested system that is potentially a lot more efficient (instancing, geometry shaders) should be preferred to anything I could implement in löve itself. So I could reduce the amount of work I had to do to making an editor for löve's partice system.
I made the editor in a day plus a few days fixing bugs while using it. I borrowed the idea of using the mousewheel for numeric value editing to reduce the amount of GUI related work (didn't want to bloat a project that small with kraidGUI). Using the mousewheel while hovering a property reduces/increases it, while holding shift decreases the amount of change. Loading is done by using the mousewheel above a property (serving as a radio button) and saving via shortcut. It supports multiple emitters to make many-layered effects (explosions for example need smoke, debris, fire, etc.). It supports continuous effects (e.g. fire) and bursted effects (you can press space to emit "Emit amount" of particles). And has a brief built-in documentation in the form of tooltips. It can be seen used in this video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/FxFmrirFCmA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<h2>Lighting</h2>
When I started on this I was very short on time, so I had to make some suboptimal decisions. I would probably do a lot of things differently if I had to do it again, so I will not go into much detail. Every light in the world has an own lightmap (normally a lot smaller than the in-game pixels it affects, because of the soft shadows that alleviate a lof of these visual impact of lower resolution lightmaps), which is only update if the light or if the occluders the light affects change (if it throws shadows). I also implemented soft shadows by appending fins to the shadow geometry on both sides and scaling them appropriately.

Hard Shadows, 1 Light:
[![Hard Shadows, 1 Light](/images/lighting_hard_shadows_1_light.png)](/images/lighting_hard_shadows_1_light.png)

Soft Shadows, 1 Light:
[![Soft Shadows, 1 Light](/images/lighting_soft_shadows_1_light.png)](/images/lighting_soft_shadows_1_light.png)

Hard Shadows, 11 Lights:
[![Hard Shadows, 11 Lights](/images/lighting_hard_shadows_11_lights.png)](/images/lighting_hard_shadows_11_lights.png)

Soft Shadows, 11 Lights:
[![Soft Shadows, 11 Lights](/images/lighting_soft_shadows_11_lights.png)](/images/lighting_soft_shadows_11_lights.png)
