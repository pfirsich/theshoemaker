---
publish_date: '2013-12-20 16:58:00'
summary_length: 3
title: Metroidlike & 2D-Water & Bone-Animations - Catching Up Part 1
---
I have a huge list of stuff that I should have put on my blog (just to document what I'm programming and maybe have a look at the progression afterwards) and today is the day I try to catch up. I'm thinking about making big posts with multiple things I worked on, so I don't have to create a myriad of posts today and also because some of them are related. Especially the three in this post, since they were intended to be part of the same game.

<h2>Metroidlike</h2>
I love the Metroid franchise. Almost every metroid game is one of my favourite games ever (except the Wii-Titles since I haven't played them). And for anyone wondering which I think are the best: My number one is Super Metroid without a doubt. I adore this game indefinitely. Prime and Fusion in no particular order are also among the better ones. So all along my time of programming games I started many Metroid 2D or Metroid Prime clones (though I never finished one) and I felt that it is again time to make one, since I know a whole lot more and had nothing to to do and a huge urge to start a project.

Although I'm doing mostly 2D-stuff lately I'm a really graphics-affine guy and I really like to spend time making effects and I'm really interested in graphics techniques, so naturally I spent most of my efforts on making the game look nice. First a video:
<center><iframe width="560" height="315" src="https://www.youtube.com/embed/dJSdzbMAj7Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>

As you will see again I tried to make the content-creation-pipeline for this game really programmer-friendly, so part of the look has to do with that. I know that tiles are a really easy way to make level geometry, but I think that they often just look a little jaggy and not as next-gen as they could, so I decided to make "high resolution tiles", which are tilesets with very many different tiles. I wrote a program that generates such tile maps for me, passing the resolution of the resulting tile map and the number of points per side. Here is an example of the map used for this level and with 5 points per side:

![](/images/metroidvania_tilemap.png)

This makes it possible to make level geometry which can have very irregular shapes as you can see in the video (but only at the beginning of the level since I got a little lazy after that). These mono-coloured tile maps are then masked in a shader with a texture. In this case I used a rock texture. In the main program the tile map is rendered black on a white backdrop which as a whole is then blurred. This image is then used as a light-map. Also there are raytraces done from the top side of the map to genereate shadows and a sense of "inside and outside" (regarding inside the cave and outside the cave). Also the gradient in the background is generated that way. I also used a form of deferred rendering, but in multiple passes since löve doesn't support multiple render targets and multi-texturing. The normal maps and an image consisting of the lights (in the video: player and bullets) are rendered seperately and the resulting lighting is calculated in a final composition-pass. Especially the specular reflections make it look very plastic. I must say, that I really like the look of the game.
<h2>2D-Water</h2>
I intended the game to start deep down in a cave, probably with the main character being unconscious lying in a little puddle or a little mini-lake. So I got started with programming water! First the video:

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/6onBYjnob7w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>

Excuse the waves, which seem to be splashing way to high. This has to do with the fact that I didn't implement fixed timesteps in this test program and Fraps having a huge impact on framerate, making the forces way more impactful than at a high framerate.
Just a little while ago a new löve-version was released which allows user defined geometry with user defined texture coordinates (but I don't know how much control is given over the way the geometry is stored. Since we want to update it every frame, one needs the possibility to make the VBO of type `GL_STREAM_DRAW`, but at the time I did this I had to find another way, which then consisted of an array of values, which represent the height of the water surface. In the water-shader these values are interpolated for every x and the water surface is drawn accordingly. The actual geometry drawn is a box that encloses the water and it's waves. This also makes it rather easy to not only make a sharp border, but also give the color a gradient (which I did) and highlight the surface, which improves the realism <b>a lot</b>. Water getting darker when it's deeper is one of the things that a lot of water-implementation that don't seem right lack. Also there is obviously a distortion-texture and the previously rendered scene passed to the shader (so this has do be done in a separate pass) to achieve the distortion effect, which also has a huge impact it looking plausible and is also not hard to implement. The values passed to the shader are determined in the main program using collision-checks of points on the water surface with the game world's geometry. The forces acting on the points are consisting of a force that always puts the point to the zero-level of the water surface (a harmonic force), damping (linear) and a relative harmonic force between the points to couple the oscillators so waves can pass through them. To make the simulation more stable I'm using a form of verlet integration and multiple iterations per frame. Also there is a force which is responsible for the box to be able to "push" water, that is calculated by checking the velocity of every object that collided with the surface and pushing the water up in front of the moving object and pushing it down behind it (in front and behind are obviously determined by the velocity) This water effect alone makes mit a little sad that I decided to stop working on this project.. But there is even more cool stuff, like:

<h2>Bone-Animations</h2>
As I said before, I wanted to make the pipeline very programmer-friendly. And since drawing is probably my worst skill I just <span style="text-decoration: underline;">had</span> to have bone animations. It is also something that I wanted on multiple occasions for a very long time. And after searching the net for a freeware 2D bone animations editor with an easy to read format and not finding anything, I decided to roll my own.

This is also just semi-finished and not very sophisticated feature-wise. The only thing missing is a proper way to specify interpolation curves for the frames. There is not an easy way to approach this by using only one type of interpolation (linear, smoothed) because different things need very different types of interpolation. So there is an editor missing for that kind of stuff and this is actually the point where I started to stop the project for other stuff I'm busy with. Writing this though made me really want to keep on working on it. I have a feeling that a well-working animation editor might not just be something nice I can find use of a few times, but something other people might find useful too. There are some things that make it not very useful for other people though, which is mainly löves policy of not making it possible to write to the file system outside of `C:\Users\user\AppData\Roaming\LOVE` or `%appdata%\LOVE`.

Maybe I should start a rewrite in C++ or Python or similar and this is certainly too much work to be still interested in continuing.

### Pictures / Video:
RiggEd, which is for rigging (making bone skeletons and attaching images):

![](/images/rigged_guy_1.png)

![](/images/rigged_guy_2.png)

![](/images/rigged_plant_1.png)

![](/images/rigged_plant_2.png)

AnimEd (has two files to deal with. A `.skel`-file which is the output of RiggEd and contains a skeleton with images and an `.anim` files which contains keyframes for the skeleton. The `.anim` files can be used on multiple skeletons, so the animations can be reused for different characters and different image sets:

![](/images/animed_1.png)

![](/images/animed_2.png)

![](/images/animed_3.png)

![](/images/animed_4.png)

![](/images/animed_5.png)
