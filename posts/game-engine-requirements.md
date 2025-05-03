---
publish_date: "2025-01-15 20:27:00" # date -Is
summary_length: 5
title: Game Engine Requirements
---

## Introduction

A few days ago I found [Tramway SDK](https://racenis.github.io/tram-sdk/why.html) on HackerNews and I thought its design decisions and motiviations really resonated with me.

I have been keeping similar notes on why I want to make my own engine scattered across my hard drive for years and thought maybe I should write it down and extend it over time as a living document.

Of course I know this is not how every engine should be and I certainly don't think there is a huge market for an engine as I am describing it here, but it is what **I** want.

## Table of Contents

- [No Editor / Code First](#no-editor-code-first)
- [No Intentionally Opaque Shit](#no-intentionally-opaque-shit)
- [VCS aware](#vcs-aware)
- [Usability over Architecture](#usability-over-architecture)
- [Target Audience: Experienced Programmers](#target-audience-experienced-programmers)
- [Fast Iteration Time](#fast-iteration-time)
- [Small Scope](#small-scope)
- [Cross-Platform](#cross-platform)
- [Single Executable](#single-executable)

## Details

### No Editor / Code First

I hate editors so fucking much. Of course you need to place your objects in the level with an editor, but I don't want to do literally everything in the damn editor.
Whatever engine you are today, your UI is way too fucking full of stuff, it's dog shit slow and most of the time just plain weird.
Digging through layers of options dialogs and settings makes me want to cry, turn off the computer and never turn it on again.
Editor UIs just evolve **horribly**. Every new thing increases the complexity of everything else.
And almost always they are so fucking buggy it makes you lose respect and faith in the software altogether.
Instead everything should be handled in code, human-readable text(-ish) files and via CLI tools that can be automated and used in scripts at every step of the way.

### No Intentionally Opaque Shit

I don't want your silly files that are not documented properly anywhere. Even if your stuff is open source, I do not care. I want _official_ specifications or open file formats (even better)!
If I need to do some modification to a file, I don't want to modify the engine, but write my own tool. This is how an engine is actually easily extensible!
If the engine needs proprietary file formats (which it very likely does, that is normal), they should have proper specifications or ideally be so simple that a brief glance tells you all you need to know.
Also I don't want any files I'm not supposed to understand, because they should _just work_ (or something). They don't - constantly. Every file should be for the developers to consume and produce, no other garbage please.

### VCS aware

When I say VCS aware of course I mean git. If your engine works great with version control and that means "just Perforce" or god forbid some proprietary thing, that doesn't count. I DO NOT CARE.
Every file the engine tools write to or reads from the disk should be VCS friendly (i.e. doesn't diff randomly and auto-merges well). This sort of implies that all interesting files are either assets (like textures, sounds, meshes) or human-readable text files.
I am human, let me read my files!
This also ties into the previous section - I don't want to think about whether a file should or should not be added to VCS. It should be obvious.

### Usability over Architecture

I have wasted quite a few years building engines with grand concepts and beautiful architectures that ended up not being very useful or putting road blocks in my way while doing simple things, so that I could make complex things easier.
There are plenty of architecture astronauts that build abstract temples made of archetypal ECSs with relationships, queries and schedulers and I think most of you are going too far.
If you built the most amazing architecture and no one has made a real game with it in 5 years (there are multiple popular examples of this), then you should consider if you went too far as well.
Abstractions make sense and are necessary, but they should solve a problem and too often they solve problems, that (approximately) no one really has yet.
So the engine should have just as much abstraction as necessary. Imho if there is any grand, clever architectural idea in your engine you might brag about on your website, that is a _big negative_, not a positive!

### Target Audience: Experienced Programmers

So many engines are built for people that just get started and don't know what they are doing yet.
It's great those engines exist, but if you have some general experience with game development, you tend to fight a lot against the "noob-layer" put on top of everything.
My engine should be made for experienced _programmers_ (not artists or designers), that have made (multiple) games before.
You should know how to use a computer and you know how it works and you are not afraid of code or the terminal.

### Fast Iteration Time

It should never take more than one second (non-negotiable) to try out a change you have made to game code (engine code is not included).
I have worked on some C++ games, where the iteration times went up to 30s and it killed curiosity to try out things, the joy in development and ultimately the fun.
I have also worked on software that takes 15min to (incremental!) build and you just end up adopting weird habits to avoid rebuilding.
As soon as you develop a hint of laziness about experimenting with your game, there is no way you will make it as good as you can.
In practice this means you either do something crazy (shared libs with game code in C) or you use scripting (Lua is my strong preference).

### Small Scope

It's purposely made for game jam games and small/medium indie games. Making AAA stuff possible should never be a design goal or constraint.

The engine is not does-it-all.
If you make a bigger game or want to do something special, it's guaranteed you need your own build of the engine (with significant modifications).
It should include a basic version of _everything_ and a fancy version of _absolutely nothing_. Only the simplest usable thing is built-in.
Everything gets sucky over time, because it grows and bloats and tries to solve every problem for everyone.
So you have to commit to not add every feature that might be useful to someone and maybe not even fix every bug. You should try to keep it small _aggressively_, but of course add everything that almost everyone needs.
Half the reason I hate most engines is because they are "do everything" tools.

Even if you use something big like Unity or whatever, if you make a serious game, you eventually have to make your own specialized tools anyways and write your own libs and everything else.
They include the feature-complete option already, but they are so "feature complete" (read: bloated), that it gets simpler to just remake the damn thing with 10% of the features, because you gain stability and speed.

Making a single tool that works for ten different people is often less work than making a tool that works for a single person once.
And if you have those ten tools, they are faster and easier to use and more tailored the users needs.
Users of the engine should be expected to replace certain parts according to their needs.
Reinventing the wheel exists, but people try to avoid it too much and they should "reinvent" it more often.

### Cross-Platform

The engine can be built on Windows and Linux and both are equally important. And you can build your game for Windows, Linux, Mac and Web _out of the box_.
`engine build --release mygame/` should give you distributables for all platforms without much fuss.
Increasingly many game jams require all submissions to be playable in the browser, therefore a web export is very important.

### Single Executable

Yes, everything you want to do is in that executable. This makes for an easy download and easy experiments.
You can run your debug builds with it, you can create your release builds with it, you can convert your assets. Everything the engine needs to do, is in that single executable.
This is not in contrast to what I said in [Small Scope](#small-scope), because I am talking about a means of software distribution only. This is about the stuff that is part of the engine anyways.

## Final Note

I didn't expect this to bring out such anger, but I think it stems from bad experiences I have made with existing engines and it is likely this anger that drives me towards making my own.

I should also mention that [löve](https://love2d.org/) comes very close to almost all of these requirements. I've used and enjoyed it for a very long time, but it's mostly geared towards 2D games and most of the games I want to make today are 3D games.
Also there are a few smaller things I wish it did differently (only user directory is writable, there should be official build tools, etc.).
