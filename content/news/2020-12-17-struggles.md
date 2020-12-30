title: About my Outreachy internship with Mixxx DJ: Struggles
authors: Aanyu Deborah Oduman
tags: personal, outreachy, internship
date: 2020-12-06 18:10:00
summary: Everybody struggles. This blog post is about a struggle that i went through in the past two weeks. I ran into this blocker while using git (as i normally do) and making some improvements on the Mixxx manual. I write about how i got stuck and the measures that i took to get unstuck.

####  I thought i knew git until this day - struggles

I hate feeling stuck.
Staring at your screen blankly, at the verge of ripping your hair out because you have exhausted all the possible solutions and none of them has worked.

![stressed out]({static}/images/news/frustrated_dev.jpg)

It makes me second guess myself, what I know, how I got here, the education that I got and all of the things that have led me to this career path.
I have been in this position many times before and yet each time, the feelings of self-doubt are as fresh as the first time that I encountered a bug in my code (it was HTML by the way).
I was in this position last week, and I have to admit, its not a good feeling.

It’s not that I did not know how to approach the task at hand.
I did, but perhaps, git had other plans that day. So what happened is that I hadn’t pulled the latest changes from the upstream branch in a very long time and by then, a lot had changed; the branches had been renamed (from `manual-2.3.x` to just `2.3`, and `manual-2.2.x` to `2.2`, and so on), new sections and content had been added by some of the Outreachy applicants during the contribution phase.

I needed my work to be updated I did the usual git pull and I thought everything was fine.
I usually never break a sweat when working with version control because I have been using git for the longest time – I think it’s coming to four years now.
I created another branch from the `manual-2.3.x` branch (remember it had been renamed) and I started working.
I finished making edits, committed, pushed and sat back as my code got tested on GitHub. My problems began when my code failed all of the checks on GitHub.
In my head, I was like, “Wait, what?”.
![failed checks]({static}/images/news/failed_checks.png)
I was shocked because my code wasn’t even passing the basic RST syntax check. I began to panic.
I got the feeling that I had not pulled the latest work from the upstream even though I had run “git pull”.
Maybe I did, but perhaps I didn’t do it the right way. So many thoughts were running through my mind at this moment.

Panicked, I began to run a myriad of Git commands.

![i run too many git commands]({static}/images/news/myriad_git.png)

In doing so, I was required to fix merge conflicts. Now we all know how badly this can go.
You could easily push outdated work and set everybody ten steps back. Or you could easily commit completely wrong work – work that has been deleted or moved.
I tried to avoid fixing merge conflicts as much as I could, but in trying to do so, I made things worse, and I was not making any progress.
When I finally got the guts to fix the merge conflicts, my commits were actively trying to disorganise progress in the upstream.
Git revert wasn’t even enough to reverse the mess that I had pushed.

![git revert doing the most]({static}/images/news/git_revert.png)

[Aimen Batool](https://www.freecodecamp.org/news/how-im-working-to-overcome-my-struggles-as-a-junior-developer-a6ab18ac29b2/) was right. It hurts when you don’t know how to resolve merge conflicts.
You spend hours finding the solution to a problem and then you end up losing your code in an attempt to fix the merge conflict.

I looked for solutions from [Stack Overflow](https://stackoverflow.com/), [freeCodeCamp](https://www.freecodecamp.org/) blogs, [Medium](https://medium.com/) blogs, closed GitHub issues, and run them in my command line but none of them was working for me.
I got to a point where Google kept returning me the same search results, the same [Stack Overflow](https://stackoverflow.com/) solutions and that’s when I realised I was going in circles.
I was not achieving anything. I thought that I had missed something the first time, so the second time (and many after that) I would squint at my screen looking through the same solutions with a more critical eye but nothing!
I checked the code of the branch into which I was trying to merge on GitHub, and compared it with mine.
I realised that the work in my repo was quite outdated and for some reason, my local repo was refusing to sync with the upstream.

By this time, I had run too many git commands in my git bash, therefore, in this process of trial and error, I couldn’t tell what had or hadn’t changed in my repo.
I had spent over nine hours on the internet searching for solutions and suggestions by people who had come across a similar issue.
I was tired, discouraged and all out of options. I heavily pondered on whether I should just come out and ask some of the contributors from the [Mixxx community](https://mixxx.zulipchat.com/) for help.
For lack of a better option, this is exactly what I did. I explained the errors that I was getting and how I got there.
They understood what the problem was and guided me on what to do. One of the things they told me to do was rebase on my branch, so I thought “okay….”.
I had never rebased on a branch before so I looked up what it meant.
I read a blog about it and after I had understood the concept, I told myself, I got it. I got it.
I ran a couple of other git commands and things looked like they would work out after all. I was happy. And then….

I got to building. `sphinx-build` generates documentation from the files in `sourcedir` and places it in the `outputdir`.
It will create documentation in different formats whereby a format is selected by specifying the builder name on the command line – the default is HTML.
So when I ran this command, I got extension errors. `Could not import extension xxx (exception: No module named 'xxx')`

I reached out again about this error and one of the contributors suggested that I install some build dependencies and build inside a python virtual environment.
Again, huge relief! I do everything as told and then build. At this point, I’m pretty confident that things will work out this time.

![extension errors]({static}/images/news/extension_error.png)

The darned extension errors came back again. At this point, I just wanted to crawl under a blanket and scream. I am thinking “What is everyone going to think if I go back and ask about yet ANOTHER error?”
“What if they think that I’m not good enough?” “What if they finally see me for the fraud that I am?” (not that I am a fraud) “What if they start to wonder how I even landed this internship?” “What if my mentors get tired of my endless questions?” “What if the questions never end?”

As hard as it was, I forced myself to ignore all these fears and just asked. Again.
By then, this conversation with my mentors was happening under a GitHub issue and the thread had gotten too long.
One of them then suggests that I should open a new topic in the community development help stream on Zulip so that the discussion on GitHub didn’t go too off-topic.
So I move the discussion there and the community starts helping me debug.
In my heart, I knew that nobody in the community would think less of me for asking about an error because, well, this is part of the reason for why the community exists in the first place – to help fellow Mixxx users find solutions to the various problems they are facing while using Mixxx.
Even with this knowledge in mind, I was scared and felt small.

So the discussion in the community forum is going on very well, and I’m getting replies in not more than 10 seconds. I was pleasantly surprised by the community’s willingness to help with this (little) error.
And then just as I was getting comfortable, one of the community members suggested that I run `pip install sphinxcontrib-svg2pdfconverter`.
I was thinking “It can’t be that easy” when I got returned `Successfully installed sphinxcontrib-svg2pdfconverter-1.1.0` . So I ran `sphinx build` one more time and it was successful! I couldn’t believe it took them all of two seconds (okay not two seconds, but it was really short time) to know exactly what was wrong with my code and provide me with the correct solution. It worked! I laughed.

![lol]({static}/images/news/giphy2.gif)

I laughed at how simple the solution was even though I never would have guessed that that was it all along.
I laughed at how long it took me to get here (it was a little over 9 hours) – to finally get the guts to ask somebody for help.
I laughed because if I had just asked for help the minute I got stuck, who knows how many GitHub pull requests I would have created by now (not that many, but still…). I just laughed and shook my head.
All my inhibitions seemed silly now, like, what did I think would happen, spontaneous combustion from embarrassment?!

So, moving on, I was able to build and preview my work before committing and everything looked good. I went ahead and created a pull request for this issue, feeling relief to my toes. I watch as the tests on Github run my code and then my heart dropped.

![failed checks]({static}/images/news/failed_checks.png)

Again?! These errors just keep on giving, huh? This time I wasn’t going to panic.
I told myself that I had been given all the resources that I needed to solve this, and if all failed, I would not waste time. I would reach out to somebody for help.

I decided to start afresh, on a completely new page. I created a new branch,  made another pull request for the same issue, this time paying extra attention to the branch tree. Everything went smoothly and the checks passed (except for one) but I had been told before that that particular test was nothing to worry about. The joy!

### Lessons learned

So through this experience, I was able to learn new concepts in git merging, committing, rebasing, and resolving merge conflicts. But besides that, here are a few key things that this experience has taught me.

Firstly, we have to learn to ask for help when we need it, even when it seems like the hardest thing to do.
Despite what you think people will think about you when you ask for help, the fact is, asking for help will get you to where you want in way less time than repeatedly trying the same solutions that aren’t working or remaining seated and feeling dejected.
We have to be humble enough to acknowledge that indeed things aren’t working and then make the effort to try to reach out to somebody for help.

Secondly, it’s always good to ask for help but before you do, please, do your research.

![the question]({static}/images/news/research.jpg)

Try to ensure that you have exhausted all the resources at your disposal so that by the time you ask, you are better informed about all the alternative methods you could have used, but didn’t for justifiable reasons.
You will not feel completely clueless when asked if you’ve tried a certain solution because you know that you tried it, and it didn’t work or that if you had tried it, it wouldn’t work for reasons A, B, C and D.
I believe mentors feel more enthusiastic about providing help if they see that the intern has put in the effort to look for a solution to the problem and they did it exhaustively. But then again, don't research for 9 hours😉.

Thirdly. In  [Syeda Aimen Batool’s words](https://www.freecodecamp.org/news/how-im-working-to-overcome-my-struggles-as-a-junior-developer-a6ab18ac29b2/) (who also got the suggestion from Sarah), “Do not take things personally and focus on learning”. I read this in his article just the other day and I feel like this piece of advice resonated with me.
He said that it can be hard to not take things personally and feel insulted when a senior dev or mentor makes a correction or suggestion.
It’s even harder when you’re working in open source and it’s in a public platform. The most important thing is to focus on the main points and have a learning attitude.
We won’t be able to learn new concepts and good coding practices unless we put all our ego aside and focus on learning from the experience and knowledge of others.

And finally, it’s important to remember that everybody struggles.
Every pro dev started somewhere. They all faced some pretty difficult bugs and blockers but this is exactly how they became the senior developers that they are today. It’s all part of the journey.
Once we understand that it is completely normal to get stuck, then we can normalize asking for help when we need it.
