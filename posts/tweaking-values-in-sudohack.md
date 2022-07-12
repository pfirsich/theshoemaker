---
publish_date: '2015-02-22 19:00:44'
summary_length: 3
title: Tweaking Values in SudoHack
---
It is fairly known that just tweaking values in a game a few percent can make or break awesome gameplay and create the difference between an iconic franchise and the joy of gameplay you often get from games that are made by some 13-year olds and uploaded for testing on a game developement board. Not that I don't like games by 13 year olds, just that it took me a ridiculously long time to get the basic hang of making games remotely fun (I'm still very far from being good it). And let's face it: if you are a game developer and you're tweaking the friction that is applied to the player when the boss knocks him back using his extra-power-attack, you often stop after 20 minutes and call it a day. It's tedious and even if it that's not always the case, it is seldom any fun. Especially with a game like SudoHack I discover a new game almost every day by just trying out different parameter spaces for all the configuration values in it.

Until this morning, for every value I wanted to tweak, I had to make changes in the code and restart the game to view it's effects. There <em>was</em> a system in place, which let me press ctrl+r, generating a tweaks.lua-configuration file (it looked something like this: <a href="https://gist.github.com/pfirsich/854145171298f3175ecf">https://gist.github.com/pfirsich/854145171298f3175ecf</a>) and giving me the opportunity to change these values, hit ctrl+r again and have the changes show up in the game in real time. Even though this is almost neat, it is way too complicated to have actually been used (like once or twice maybe). I remember having something like this in one of the dozen C++ game engines I started developing, when I was a little younger, where I would define a `TWEAK(value)` macro, which would use `__FILE__` and `__COUNTER__` to uniquely identify every call of this macro. The actual implementation would look up the key-pair and upon triggering a reload (by pressing ctrl+r for example) parse all the source files for all occurences of `TWEAK` and update it's values, therefore giving me the opportunity to tweak everything in the source and only tell the game to reload the tweaks. And I thought it was awesome. So I set out to do something like this in Lua/löve. The first implementation worked fairly quickly using the already introduced tweak(defaultValue, name) functions all over the code, I update the values by parsing the source for these function calls. Because I fear that it might not fully be clear what I'm actually doing with this, here is an example work flow:

```lua
-- <implement new feature (for example: bit rendering)>
love.graphics.setColor(tweak(40, "bits: colR"),
                       tweak(150, "bits: colG"),
                       tweak(200, "bits: colB"),
                       255)
-- <change the values in the source code, while leaving the game running>
love.graphics.setColor(tweak(255, "bits: colR"),
                       tweak(100, "bits: colG"),
                       tweak(100, "bits: colB"),
                       255)
-- <hit ctrl+r>
-- => The changes are visible in the game
```

This is already pretty neat, but one might think: disregarding potential future uses, why do you even need names? Isn't the nth-occurence of a tweak()-function call and the source file enough to uniquely identify the values? And you're right, they are actually quite useless, but if you have a look at my implementation:

<script src="https://gist.github.com/pfirsich/51a5a51543da40a3c2fa.js"></script>

Then you might formulate this problem as: can we generate the tweak-value names ourselves? And the answer is: I don't know. I asked in #lua on freenode and people recommended me looking at the lua debug module, which has the capability of building a stacktrace at any point in the file, getting the source file name and the current executed line number, but this is not enough if you want to allow multiple tweak values in a single line.

I implemented a package loader, which will be invoked if another module is required in a source file that replaces every occurence of a specific `func()`-call with `func(x)`, where `x` is the filename and the number of occurences before it concatenated in a string. For the interested:

<script src="https://gist.github.com/pfirsich/549fc8cb38949feef665.js"></script>

Despite it working I don't really feel comfortable using it, since I don't like changing the actual entry point off my game to a different file, only to have it be included right after the tweak-loader. Especially if what I gain seems minimal. Also I really don't like messing with things like this, since love's filesystem sandbox might make this a little more complicated if it is run from a zip-archive (which is, in a shipped version, the default mode of operation), but I'm not entirely sure about this.

Finally I will just use the system that was in place today 5 hours ago and see how much entering names will annoy me pretending that they might have an actual use in the future. All the approaches discussed here are, of course, only actually usable in small teams or, more concretely, teams where everyone, who should have the possibility of tweaking game values, knows her/his way around the code. Otherwise a system where code and data are more separated is probably the way to go, since the amount of overhead can be justified with expanding the access to configuration values. Also in that case I would really like some Quake/Source engine like console, which makes easy changes in the game possible and gives the opportunity to spawn graphical elements like sliders/spindowns to edit them visually. For me though, the edit-quick and almost no-overhead solution is more desirable.
