title: Mixxx to the first time contributor
authors: Aanyu Deborah Oduman
tags: personal, outreachy, internship
date: 2021-01-08 17:38:00
summary: In this blog post themed "Think about your audience", I explain the project that I'm working on for the Outreachy internship, the tasks involved, and I try to break down some of the technical concepts to the first time user and contributor.
I explain how my project fits into the larger Mixxx community and what makes me excited to work on it. I talk about some of the new concepts that I've learned and some the things that confused me when I was just getting started.

![Mixxx logo]({static}/images/news/mixxx_logo.png)

Mixxx is a free/open source DJ performance software for Windows/Mac/and Linux. It was first released in 2003 as a graduate student project, and was picked up by the community and greatly enhanced. All contributors, from programmers to skin designers to translators are unpaid volunteers, hence it is entirely community driven.

Mixxx is a feature-rich DJ mixing application that supports many MIDI and HID DJ controllers.
It supports effects, harmonic mixing, beat matching with thousands of users all over the world.
It integrates the tools DJs need to perform creative live mixes with digital music files.
Mixxx has an unusually broad community for an open-source project, encompassing performing musicians, C++ programmers and addicts, amateur DJs, Internet radio broadcasters and even casual users.

Besides being a fully-featured DJing application, the main problem that Mixxx is trying to solve is that a lot of DJing applications are either expensive or limited (for the free features).
Mixxx exists for people who want to try DJing or do not have the money to buy equipment or the latest fastest computers.
A large number of Mixxx users live in the global South, so Mixxx plays a vital role in allowing anyone anywhere to throw a party.

Before the Outreachy internship program, I had never contributed to open-source software.
I didn’t know what open source software was (or how different it was from other software) until a friend explained it to me. Since applying to Outreachy, I have learned a whole lot about different open source software and the different ways that you can contribute.
I thought it was rocket science (because of the term “open source”) but really, it’s not.
I feel fortunate to have earned the internship contributing to Mixxx DJ, and now I can’t wait to share everything that I know about contributing to open-source software – Mixxx in particular.

I am contributing to Mixxx by improving their documentation ([User manual](https://manual.mixxx.org/2.2/en/)).
Mixxx’s [user manual](https://manual.mixxx.org/2.2/en/) does a decent job of explaining the application, however, there is lots of room for improvement.
Many users come to Mixxx without any prior experience DJing and are left wondering how to practically use the application to mix music.
My job as an intern is to improve the manual by explaining not only how to set up Mixxx and how to use specific features, but also explain the bigger picture of how to play music with Mixxx.
There is some information in the manual that is obvious or already explained in the application with tooltips but some of this may be deleted from the manual.
Other text could be moved directly into the Mixxx GUI. One of my major tasks is to explain information that would take too many words to adequately explain in the Mixxx GUI.
This also involves adding more links to specific sections of the manual from the Mixxx GUI (and edit the manual text with this context in mind).

This project is important because it will better the experience of many first time users of Mixxx.
I had never used Mixxx before this internship and I think this turned out to be more of an advantage than a disadvantage.
I say this because if I was using a software for the first time, I would need to refer to the user manual a lot, and one of the things that I appreciate as a first time user is when documentation writers make the effort to explain technical application-specific concepts to non-developers and first time users in the simplest way possible.
Most long time users and developers of open source software might find difficulty doing this because they use these technical terms and apply these concepts every day in their work, therefore it comes easily to them.
It might slip a pro user’s mind once in a while that some terms might not be well known to the ordinary user.
So, as a newbie, I think that I am able to approach this project with fresh eyes and the perspective a first time user.
Are the concepts understandable? Are they easily relatable to the Mixxx graphical user interface? What sections of the manual need more emphasis? Are the directions easy to follow?
These are some of the questions that guide me as I work on this project.

Another Mixxx project that I am working on for this internship is the YouTube video tutorials project.
Mixxx does not have enough updated video content on YouTube, and these videos are absolutely necessary for Mixxx’s documentation.
In this project, I create illustrative videos to help Mixxx users understand how to use the software and thus, can be used by professional DJs, aspiring DJs, music lovers, and casual users.
The project involves creating a series of short, brief videos for various playlists and they are mostly OBS Studio desktop recordings with voice-overs, coupled with some illustrative animations to keep the content fun and interesting.

One of the things that I love about working on these projects is that the tools that I work with (git, OBS Studio, [Movavi video editor](https://www.movavi.com/videoeditor/), VSCode) are easy to use.
So I’m glad that I get to focus more on working on the actual tasks at hand, and not with the tools needed to get the tasks done (that happens sometimes 😊).
I make edits in [reStructuredText](https://docutils.sourceforge.io/rst.html) (.rst) for the manual and [markdown](https://www.markdownguide.org/basic-syntax/) (.md) for the website.
I found these two lightweight languages easy to learn and work with, so I was happy to get over that learning curve in no time (I’m still learning though).

Another thing that I love about working on Mixxx’s “Improve User manual” and “Create Video Tutorials” projects is that I get to contribute to an open-source project that many people rely on.
Some of the work that I do represents a solution to a problem that others may experience as well.

Through contributing to Mixxx, I have gained a much deeper understanding of the software.
It was not easy in the beginning as I had to determine which part of the project was worth contributing to.
Understanding the contribution guidelines also took me a day or two, and I made mistakes here and there, but that is all expected.
It also took me a while to understand some of the issues that were opened in the [manual repository](https://github.com/mixxxdj/manual) on GitHub – determining where the problem was and why it was a problem, researching on the issue and then finally making the requested changes.
Once you’ve gone through these steps, you will have gained a much deeper level of knowledge and understanding of the project at hand.
Contributing to an open-source project, in the end, lets you reach a higher level of expertise. Something that cannot be easily achieved by simply reading books or using the project at hand.

Before I learned about Mixxx, I was experimenting with [Virtual DJ](https://www.virtualdj.com/) but I didn’t use it often.
I only knew the basics of loading a song on a deck, cueing, crossfading into another song, and beatmatching. (Man, I felt like a real DJ!)
I knew enough to record a mix for my friends or get a high school party going, nothing too complicated 🙂

However, since I started working with Mixxx, I have learned a couple (understatement of the week) of new terms and concepts such as analyzing your tracks, the auto DJ feature (this is the coolest feature for me), microphone ducking (I always saw DJs do this, but I did not know that this was it was referred to), harmonic mixing, the difference between a crate and a playlist, kill switches among many other things.

When I first started contributing to Mixxx (during the contribution phase), I was fortunate enough to be in a [community](https://mixxx.zulipchat.com/) of really supportive people; developers, DJs, long time users of Mixxx, among others.
I learned how to get started on making a contribution by following the community chats in the different streams.
We (first-time contributors) all had the same questions.
“What next after cloning the manual repo?” “Which branches should we be creating ours off of?”
“Do you simply start working on an issue, or should you ask to have one assigned to you?”
I remember asking why the bugs reported in the [launchpad](https://bugs.launchpad.net/mixxx/+bugs) didn’t have `documentation` labels. 😌 Lol.

Starting out can be confusing, so, based on my experience so far,  here are a few key suggestions that I would make to a first-time contributor of the “Improve User Manual” project or any other project:

- If you ever get lost on how to start, try not to feel overwhelmed because you are not alone.
    You can always ask in the community Zulip chat, how to get started or even what tools you would need.
    But before you do so, I would suggest that you first read the [README.md](https://github.com/mixxxdj/manual#mixxx-user-manual) in the repository of Mixxx’s User Manual or the respective project that you’re working on.
    It has well-written guidelines on how to get started, prerequisites for the installation of some of the tools you will need, how to build your project and view it before you can commit it, how to troubleshoot in case you run into an issue, and so much more!
    In addition, there are high chances that what you want to ask in the community chat has already been asked in a previous conversation in the stream, so going through these messages can be helpful for you, especially if you’re shy. 🙂
- Try to understand the working of Mixxx. Experiment with it.
    Learn about the different features and how they work, and how you can manipulate them to make good mixes.
    You don’t need to be a DJ to do this – the purpose for this is so that you understand better the project that you’re working on.
    It only makes sense that if you’re documenting a feature, let’s say microphone ducking, that you have Mixxx installed on your computer and that you have used microphone ducking before.
    I believe that doing this will give your work more context, and things will go smoother.
![A DJing meme]({static}/images/news/bass_meme.png)
- Take note of the git tree structure.
    While working inside any branch in the repositories, make sure to understand the git tree for that repository so as to avoid running into git errors and then spending a lot of time correcting them.
    I forgot to do this once, and I all I can say is, I have never been frustrated about git in my life. I had to open a whole new pull request in the end. I wrote about this in my blog about [struggles]({filename}/news/2020-12-17-struggles.md). (you can check it out 🙂 )
- Research on the issue you want to work on before you start working on it.
    This will help you understand what exactly you need to do and how to go about it.
    Some times the issues may not have enough detail in the description or the description may be too technical for you.
    Google is your best friend. I mean it.
    Leave no stone unturned by the time you start working on that issue!
    By doing this, you will find that you will have less commits as well (this is a good thing). It means that you understood what exactly needed to be done and did it.
- Build the manual to see your changes, before you commit your work upstream.
    I think this is important to note because it helps keep your branch clean with fewer errors and less commits.
    I believe maintainers love working with clean code because it makes their work easier (remember that they maintain a lot of code already).
    So with an organised git commit history, I believe you’re more likely to get a review on your work faster because you’ve made the reviewers’ and mentors’ work easier.
    You might be tempted to depend on the Netlify deploy previews to preview your changes but that means you would have to commit every minor correction that you’re making and that could potentially make your pull requests messy.
- Last but not least, your mentors are here for you. Do not hesitate to ask when you feel stuck. If you need more clarification, ask.
    Its okay to ask the same question twice because what’s important is that you understand and learn. Even better, ask your questions in the community streams.
    Leave it open so that you can receive different suggestions from various community members.
    It might open your mind up to new approaches to solving your problem.
    On the other hand, I am also [very] happy to help in case you have a question about this project or my experience in the internship.
    You can reach me on email at deborahtrez12@gmail.com or even in the [community Zulip chat](https://mixxx.zulipchat.com/) at @Aanyu Deborah Oduman.
    I would be happy to hear from you!

That said, good luck with your first contribution, and happy documenting! 🙂
