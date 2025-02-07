---
publish_date: "2025-02-07 20:03:00" # date -Is
summary_length: 3
title: Stop Overcomplicating Parsing
---

## Introduction

I have been working on a little programming language for the last couple of days and the software and theory around parsing is just eternally frustrating. People have built mind-boggling theory temples around this and I think nothing attracts architecture astronauts like parsing. I am not convinced that most of it is not necessary and it is not actually this difficult.

You read about `LL(k)` parsers, `LL(*)` parsers, `LL(1)` parsers, `LR(k)` parsers, `LALR` parsers, `SLR` parsers, `GLR` parsers, Earley parsers (all of these are real) and more. It makes your head spin and barf all the `LOL(k)` parsers right back onto the screen. I keep thinking "no one cares dude, just parse the thing".

We haven't just lost bright minds to parsing theory, but (the real tragedy) countless of people have been discouraged to parse something by the overwhelming overcomplication of the subject.

It's so silly to me that people that know nothing about parsing just parse stuff with recursive descent and when you go to the really complicated languages and the really large parsers (JavaScript V8, TypeScript, Rust, CPython, GCC), you end up having to use recursive descent again. It's kind of weird there is a whole science inbetween. Maybe the stuff in the middle is not really that useful?

## Recursive Descent

For everyone who doesn't really know much about parsing: A recursive descent parser is just the thing you would write down if you didn't know anything about parsing.

Consider this simple grammar ([EBNF](https://de.wikipedia.org/wiki/Erweiterte_Backus-Naur-Form)-like):

```none
action: ("run" | "stop") (flag | arg)*
flag: "--verbose" | "--force"
arg: WORD
```

which defines a language that has `action`s, which start either with `"run"` or `"stop"` and are followed by any number of `flag`s or `arg`s. `flag` can either be `--verbose` or `--force` and `arg` must be a `WORD` (whatever that is, it doesn't matter). You would just write it with each rule being a function, sequences just being code after other code and choices (`|`) being an `if/else`:

```python
def parse_action(parser):
  action = Action()
  parser.skip_whitespace()
  if parser.input.startswith("run"):
    action.verb = "run"
  elif parser.input.startswith("stop"):
    action.verb = "stop"
  else:
    return None

  while parser.has_input():
    parser.skip_whitespace()
    flag = parse_flag(parser)
    if flag:
      action.flags.append(flag)
      continue
      arg = parse_arg(parser)
    if arg:
      action.args.append(arg)
  return action
```

Ignore some `parser.skip_whitespace()` I might have missed and pretend `parse_flag` and `parse_arg` look mostly like that. You don't even have to think much when you write a parser like that.

There is no science here. You are just writing it out. And I didn't even need a `ROFL(69)` parser or whatever. If you don't know anything and are humble enough, you might think "but maybe this is slow" (because it's dumb/straightforward), but no, recursive descent parsers is often some of the fastest ways to parse things.

Maybe there are languages / grammars you can't parse with it? No, not even that. Recursive descent is one of the only popular algorithms that can parse context sensitive languages.

Other parsers have problems with error recovery (mostly a meme as well btw. - [see below](#error-recovery)) or with reporting good error messages. Even that is trivial with recursive descent parsers.

And they are also comparatively easy to debug.

It can do more, it can do it faster, it can do it better, it can do it easier. What the hell is everyone doing?

### Expressions

The actual real downside of recursive descent parsers is parsing expressions. You can do it, but encoding operator precedence is tricky and non-intuitive (you need a separate parsing function for each precedence level). And if you do it that way, it tends to do a lot of backtracking, which ends up being slow (worst case exponential time - blegh).

People have come up with [packrat parsing](https://en.wikipedia.org/wiki/Packrat_parser), which caches some of the intermediate results during parsing, which reduces it to linear time, but this honestly also makes my "overcomplication" senses tingle.

The cool thing about recursive descent is that it is so ad-hoc that you can easily combine it with other algorithms, for example algorithms that are made specifically to parse expressions with different operators that have different precedence levels. One of the best (and coolest) algorithms to do this is "[Pratt parsing](https://en.wikipedia.org/wiki/Operator-precedence_parser#Pratt_parsing)" (I recommend this blog post: [link](https://eli.thegreenplace.net/2010/01/02/top-down-operator-precedence-parsing)). So if recursive descent is the best for almost anything and Pratt parsing is the best at parsing expressions and you can combine them well, why not just use those two? I wrote a parser for a small language recently in a couple days that does exactly this and it's great. I cannot find a single parser generator that does this and it confuses me to no end.

### Actual Downsides

The actual problem I am willing to acknowledge is that recursive descent parsers can remove ambiguity from an ambiguous grammar. Ambiguous grammars are grammars which allow that an input is parsed in different ways. This is mostly bad. And if you don't notice that your grammar is ambiguous and write a recursive descent parser for that grammar (which cannot be ambiguous), then you have kept the ambiguity in your grammar hidden and your grammar does not fit to the parser anymore!

All the other fancy parsers that get CS students and academics excited have the cool property that you can derive a parser from an unambiguous grammar and if you have an `LL/LR` parser or whatever you can derive a grammar from it. Of course recursive descent does not have any nice theoretical properties like that.

First of all I think it's silly to choose a parser based on whether it helps you find problems with your grammar. If you want, you can use an existing `LR` parser to verify that your grammar is unambiguous and then write the recursive descent parser (many people do this).

People are rightfully obsessed with removing ambiguities in their grammar, but why not simply come up with a grammar that can't even have them? Like PEG! [Parsing Expression Grammars](https://en.wikipedia.org/wiki/Parsing_expression_grammar) replace the choice operator (`|` before) with an ordered choice which implies a priority of the first (left hand side) option and thereby removes ambiguity.

This is actually sick, because if you notice above I started with checking for `run` and then checked for `stop`. The grammar didn't actually imply a priority there, but my code did of course. There might be an expression that can get parsed by both `if`s. And if you use a PEG then those different branches in your code DO have a well-defined, correct order. In that way PEGs map to recursive descent parsers more directly.

Parsing experts don't like them much and I don't really understand why. I read that it's somehow undesirable that PEGs are unambiguous because you can write stuff that looks correct, but actually isn't and no one complains. I think this is mostly (again) related to operator precedence. Also they use more memory, which I respect as a limitation in certain scenarios, but I have 32G of RAM and that's not even a lot, but more than plenty to parse a couple MBs of code.

### Theory

Generally I am all for theory. It's important that someone understand these things (and anything else) on a truly deep level. Someone needs to know what is possible and provable and correct, but what confuses me is the ratio of people doing pragmatic parsing and people swooning over parsing algorithms. I feel like the whole world is tricking me into thinking I actually need a lecture to parse text. I don't - you can literally just parse it.

I acknowledge that there was a time where all this theory was actually necessary to compile C on an analogue toothbrush in some ancient sumerian assembly. And they did develop some great ideas that are useful to this day (like precedence climbing / Pratt parsing), but honestly I think most of this stuff is just not really interesting to most people that just want to turn text into trees.

## Lexing

I think everyone is overdoing it on lexing / tokenization. I get what lexing is for, but it also feels like it is mainly to make the parser more elegant, because it can just work on tokens and doesn't have to skip whitespace and comments itself. I am not convinced its actually solving a real problem. The fact alone that plenty of parsers do not lex as a separate step proves this.

When I see "struct" in the right place, I _know_ there has to be an identifier next and if there is not, I should error out right then and there. I don't need to figure out _generally_ what could be at any point in the text. It feels like I now have to solve two problems (parsing and figuring out what kind of token a string might be without knowing where it is), when I can solve it in one go and effectively have FEWER problems this way.

I heard that lexing separately can actually be faster, because it's cheap to do and it makes parsing simpler, but I heard more often that a "scannerless parser" (no separate lexing step) is usually faster. And even if having a separate lexing step is slightly faster, I am not convinced it's worth the trouble.

## Parse Generators / Existing Libraries

When I see YACC/Bison or Lemon all these other things I cannot believe how people started putting C in their grammar. And it's not just regular C, which is bad enough, but stuff like `$$ = system__create_ast_node_ternary(auxil, AST_NODE_TYPE_STATEMENT_IF_ELSE, range__new($0s, $0e), e, s, t);`. This is not code, this is garbage. You went the wrong way!

Why do _none_ of the popular parser generators just output a damn AST by default? If you write a parser generator, just give me the AST! Don't overdo it, just give me a bunch of these:

```c++
struct Node {
    NodeType type;
    size_t start, end;
    Node* children;
    size_t num_children;
};
```

Where is the "common man" tool/library that accomodates practical parsing needs and is not just for parsing nerds? I don't need your help, if I already know how to do it! Do I have to make one myself? I already don't have enough time.

**Honestly more than half the tools I come across I don't even understand! I have been programming for 20 years and done a bunch of different things. I have Bachelor's degree in Physics. I'm stupid, but not completely stupid. Parsing text is really not difficult if you do it the right way, but somehow everything out there is super complicated anyways.**

I tried getting a grip on all this stuff multiple times through the years, eventually just gave up (until now) after a few hours and ended up writing a recursive descent parser again, in the beginning not even knowing they were called that.

### Expressions

_EVERY LANGUAGE_ needs expressions. Why do we have to solve this a million times? Why can't I just define a set of sub-languages with their operators and precedences and then the parser will work it out.
If you build a parser generator there should be a built-in feature for operator expressions. What do you think people use your generators for? Everyone needs this.

## What I Want

Like I said I gave up many times on parsing. The first tool that changed my mind was [lark](https://github.com/lark-parser/lark). It is so cool in large part because it eats almost any grammar you give it and because it spits out an AST right away, which you can just post-process (or you can customize the AST generation).

The problem with lark is of course that it's a Python library and I don't want to call into Python to parse (lol). Also it's pretty slow. I wrote a grammar for a language I am working on and it takes about 10 seconds to parse less than 200 lines, which is of course absurd.

The thing I want should generate a C parser, because you can integrate those into anything. It should have roughly these features:

- PEG grammars with sub-grammars for a Pratt parser for expressions
- Generates recursive descent parser (with Pratt sub-parser for expressions)
- Easy way to skip whitespace and comments (you need that almost always - It has to be built-in!)
- Generates AST right away by default

Something like this (don't hold me to that - I already don't like a bunch of things about this):

```
start: assignment*
assignment: IDENTIFIER "=" expr ";"
expr: {
  primary: IDENTIFIER | NUMBER | "(" expr ")"
  prefix "-" (10): expr
  infix "-" (1): expr
  infix "+" (1): expr
  infix "*" (2): expr
  infix "/" (2): expr
  infix "^" right (5): expr
}

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*
NUMBER: [0-9]+
WS: [ \t\n\r]
COMMENT: "#" (!"\n".)* "\n"

!ignore COMMENT WS
```

I just want to say which operators I have, what operands they take, their binding powers (in parentheses in the example above) and whether they are prefix/infix/postfix and the parser will do the rest.

I feel like a tool like that would be _stupidly_ useful and allow people to prototype programming languages in _hours_. I really do not understand why there are not 10 of those already. Can someone please make this?

I think by the time most people are capable of doing something like this, they already got nerd-sniped into parsing theory and lose sight of the forest for the trees.

## Links

These links say some of the things I said here, but not as clearly distressed and much more measured and intelligent:

- [Modern Parser Generator](https://matklad.github.io/2018/06/06/modern-parser-generator.html)
- [Just write the #!%/\* parser](https://tiarkrompf.github.io/notes/?/just-write-the-parser/aside1)
- [Why I write recursive descent parsers (despite their issues)](https://utcc.utoronto.ca/~cks/space/blog/programming/WhyRDParsersForMe)

## Foot Notes

### Error Recovery

Most people do not need it. You need it for parsers in IDEs for language servers and stuff like that, but most of the time you just want to error out on the first error. Whenever I get an error in any programming language, I just skip to the first one and doing anything else is (almost) always a waste of time. Imho error recovery is overrated.
