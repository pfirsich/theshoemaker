---
publish_date: '2015-01-13 16:07:00'
summary_length: 4
title: SudoHack - Bits, AI, Weapons, Movement and a Lot More Prettiness
---
*SudoHack is a multiplayer roguelike  where you and your friends, playing as computer programs, try to infiltrate a computer system. You gain "Bits" by destroying the guardian programs that are put in your way, but also lose them for every hit you take and every second that passes by. Your goal is to reach the end of the room before you run out of Bits and get destroyed yourself,  therefore gaining access to deeper levels of the system, until you reach the core.*

So this week really has been rather productive (sadly just regarding SudoHack.

Video (now on Youtube!):
<iframe width="560" height="315" src="https://www.youtube.com/embed/C2Jum5neMJU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


I added Bits (the little blue things you can see in the video), which serve as a HP/time countdown hybrid. They decrease over time and you lose them by taking damage, representing your integrity as a little computer program guy, because, you know, that's exactly how that works (#1337hackz0r). I plan on making the games a little more swingy, by picking up Bits being a lot stronger, but also losing a lot more over time. Awesomely though they dont't just have an effect on a dandy little bar you can fill and empty, but also trigger a (placeholder) death screen, giving you the opportunity to start again.

Which leads me to the <a href="http://en.wikipedia.org/wiki/JMP_%28x86_instruction%29">jmp</a>-tiles, which don't just enable you to restart the game, but advance you to other maps once you cleared the room of all enemies, being a key part of the game and also finally implemented!

Also the random weapons have been changed, so I don't have to restart the game ten times before I can make a video ;) Now they are a lot more even in power level (by equalizing metrics like damage per second), but I don't have the impression that they feel that diverse at the moment, which may change after I implemented a lot more special powers or I might just drop the random weapon idea alltogether and stick with weapon upgrades or something. Testing will tell! Also I integrated ShotSynth, which I mentioned (and showcased) in <a href="http://theshoemaker.de/2015/01/sudohack/">a previous blog post</a>.

Some of you might have noticed (definitely those of you who had the gift of being asked to test the game) that the enemies are not as clever as they could be and often get randomly stuck or behave a little strange. I tweaked this a little and removed two huge bugs I'm still ashamed to even think about, let alone mention to any living person. For days they collided with dead enemies, and significant parts of their behaviour were never executed (still did it).

Formerly the movement was just a regular euler integration with friction and keypresses corresponded to forces that were being exerted on the player mass. But I think that it was really hard to dodge bullets and all in all the movement looked and felt very floaty, albeit smooth. I changed it to partly setting the velocity and partly interpolating into a target velocity, which should (and did) give the game a little more of a Gradius/R-Type feel regarding movement. I really like the change, though some have expressed dislike (In my opinion, mostly because of the significantly different feel).&nbsp; Also I invested a little time to make the game compatible with the 360 controller and added the traditional twinstick shooting controls, so you don't have to also press a button to shoot.

Finally the part that was definitely the most fun and the stuff that interests me the most in game programming: the graphics part. At first I added the grid effects, which can be explained if there is any need for it (just tell me), but certainly help to give the game it's cyber feel I was aiming for and also make the level a lot more dynamic and lively. To enhance these effects and because no cyber space game can live without copious amounts of it I added bloom/a glow effect, which still might be a little too much at the moment and will probably be toned done, but not until I got completely sick of it, which might take longer than anyone likes (but please tell me if you think that I should tackle my severe case of bloom addiction and kick it down a notch). Also I added a scanline and a rgb-shift shader, which should give the game the look of an old monitor, because again: cyber space and stuff. I plan on adjusting their parameters using the current amount of Bits, compromising the image more and more with less Bits being left. The bullets look a little prettier too, players have awesome, yet still unexplicable cyber-tails and on top of it all I managed to squeeze in approximately 60 hours of research and implementation for a neat little aim line.

I also tried a few level generators, that I really, really didn't like and at the moment I plan on not having random maps, but rather prebuilt and randomly chosen rooms. I will definitely put more time into a generator first, after I built a few to get a feel of what works and what doesn't.

The immediates milestones are a semi-working prototype for the <a href="http://globalgamejam.org/">Global Game Jam</a>, which I will attend from the 23rd to the 25th this month. For this the next things on my ToDo-list are a lot of minor changes, new enemies, a few maps and a new (wordpress) blog!
