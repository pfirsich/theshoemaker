---
publish_date: '2013-01-28 23:04:00'
summary_length: 3
title: Global Game Jam - Cardiac Murmur
---
Last weekend I was attending the global game jam in cologne and I have to say that it was a really cool experience! Sadly my team mostly consisted of people from the design school this event took place in (they didn't study game design though) and they had to take part in this to receive certain credit points or something (in essence: My team was 60% people that have never made a game, don't play games and have no skills whatsoever to actively partake in making one) and we weren't lucky to incorporate an artist into our team, so we essentially ended up with two programmers. But otherwise it was still very cool! I was overwhelmed by all these productive talented people and all the awesome ideas. The theme of the game jam was the sound of a heartbeat (the actual sound. Not the description I just gave) and after a bit of brainstorming we decided to make a game where you had to listen to your heart. A kind of parallel-world-gameplay where you had to switch you view to see what your heart was telling you. We wanted to partake in the "Games for Change"-challenge and make a game that raises awareness of us often overlooking problems of the people surrounding us (not just by being ignorant, but because they try to hide). At first we wanted to focus on characters and their developement and stories. People you are friends with that secretly hide depression or family problems, but we ended up with not enough time and just made a cool platforming-level and one level that merely touched what we had planned. Still I am very content with what we did. I look at it as a prototype of a game that we might make some time.
Link: <a href="https://web.archive.org/web/20130522133503/http://globalgamejam.org/2013/cardiac-murmur">Global Game Jam - Project Site - Cardiac Murmur</a> <strong>(Update 7th of April 2015: this link seems to be broken. I added Screenshots and a Download-Link at the end of this page)</strong>

Technical stuff:
The paper-like look is achieved by a multiplied gradient from top-left to bottom-right and a "stencil-sketch" texture multiplied, which essentially is a noise-texture that is stretched in one direction to have little lines.
The normal world is encoded in the red-channel of the sprites and the heart-mode-version is encoded in the green channel. In a shader these channels are linearly interpolated with a game-defined value and converted to greyscale. We made the maps with <a href="http://www.mapeditor.org/">Tiled</a>, which is a great tool and I really recommend you using it (I certainly will use it again) and a little python script to convert them map files to a binary format and splice the tilemaps.

<span style="text-decoration: underline;"><strong>Update 7th of April 2015:</strong></span>

<a href="https://www.dropbox.com/s/4gsz7hi6dk1q4ro/CardiacMurmur.zip?dl=0">Download link</a>

<a href="https://youtu.be/M3AxFZOEyYc">Youtube link</a>

![Cardiac Murmur Light](/images/cardiac_murmur_screenshot_light.png)
![Cardiac Murmur Dark](/images/cardiac_murmur_screenshot_dark.png)
