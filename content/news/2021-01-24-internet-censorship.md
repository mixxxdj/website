title: "About my Outreachy internship with Mixxx DJ: Contributing to open source amid Uganda’s internet restrictions"
authors: Aanyu Deborah Oduman
tags: personal, outreachy, internship
date: 2021-01-24 14:00:00
summary: In the days leading up to the Ugandan election, access to major social media platforms and circumvention tools was blocked. This internet shutdown and the social media ban that followed affected many online jobs and businesses, my internship with Mixxx under the Outreachy program was no exception.

![Internet shutdown]({static}/images/news/internet_shutdown.jpg)

Last week, amid the 2021 general election, Uganda was disconnected from the internet entirely.
The country experienced a widespread internet blackout that lasted 4 days, starting on the eve of the election (13th January 2021) and ending in the morning of 18th January 2021.
In the days leading up to the election, access to major social media platforms and circumvention tools was blocked – even when the OTT (Over the Top) tax (commonly referred to as the “Social Media Tax”) was paid.
This internet shutdown and the social media ban that followed affected many online jobs and businesses, my internship with Mixxx under the Outreachy program was no exception.

Before I write this article, one thing to note is that Ugandans have been in this internet battle with the government for quite some time now.
The internet shut down came as a surprise when it did, but at the end of the day, I feel like we should have seen it coming.
By the time it dawned on us that the internet really had been disconnected, we were already in darkness, with only the people physically close to us to express our shock too.
The audacity of this government!

As the years go by, our President, H.E Yoweri Kaguta Museveni, has been feeling a lot of pressure about the presidential seat.
If elections were conducted freely and fairly, you would notice a declining trend in the number of votes his political party (NRM) has been getting over the years.
Ugandans are tired, and they want change. They have been more vocal about the injustices that have been happening in the country and it has cost them their lives, even their families’.
This resistance from the public has been causing anxiety in State House, and it’s starting to show.

In the 2016 presidential elections, Ugandan authorities blocked access to Facebook, Twitter and WhatsApp saying the platforms would be used by the opposition to mobilize protests.
([This article from the BBC](https://www.bbc.com/news/world-africa-35601220) has more context on the social media blockage)
President Yoweri Museveni was facing a tough challenge from veteran activist [Kizza Besigye](https://twitter.com/kizzabesigye1?s=20), and he believed shutting down social media would help to curb the “threat”.
Authorities also suspended mobile transfers of money.

In 2019, the government introduced a tax on the use of the social media, which activists have called an attempt at controlling free speech.
He said that the youth only use social media to gossip and spread wrong rumors (about him).
([This article from the BBC](https://www.bbc.com/news/world-africa-44315675) provides a better account of the imposition of the social media tax by President Museveni on Ugandans) .
He imposed OTT – Over the Top Tax and since then, it’s never been enough to simply have a good internet connection.
You have to pay a daily fee of UGX 200 to your Internet Service Provider, or if you’re being rebellious, a VPN application installed on your phone or computer.
He insisted that the revenue collected from the tax would help the country cope with the consequences of olugambo [gossiping].
I don’t know... but to me, these look like the actions of an increasingly anxious person in power.

On 12th January 2021, the Uganda Communications Commission (UCC) ordered internet service providers in the country to immediately suspend any access and use of all messaging apps and social media platforms until further notice.
This was done so suddenly and without prior notice that it took most of us a couple of failed OTT subscriptions to realize that social media platforms had indeed been blocked.
Before that, internet speeds had become excruciatingly slow, it was any wonder we were able to get anything done in those few days.
A few days after the social media block, the government decided to shut down the entire internet! (The social media ban was simply not cutting it)
So when Google stopped working and our parents were restarting their phones several times, is when we realized that truly, there was no end to the surprises.

During this (not so brief) period we were in total blackout. No internet services were available anywhere.
I was not doing any work as far as the [Outreachy](https://twitter.com/outreachy) internship with [Mixxx](https://mixxx.org/) goes.
I was not making any contributions, and sadly, that whole week went just like that.
We (devs) wondered if there was a backdoor to the whole situation, maybe some independent internet Service Provider that didn’t serve the government or something – lol.
I was not sure what to do without the internet so I read books, watched movies on CD, took nature walks, anything to pass the time. How did our forefathers survive without the internet ?

![Why Museveni banned social media]({static}/images/news/tweet_about_m7.png)

So after NRM won the Presidential election, the internet was restored on Monday evening (18th January).
There is speculation regarding this matter as to who exactly restored the internet.
Word has it that it was [the Anonymous](https://en.wikipedia.org/wiki/Anonymous_(group)) that had hacked the government systems and restored the internet.
On the other hand, neither the ISPs nor the Uganda Communications Commission openly came out to declare/ announce that internet had been restored.
The internet had been restored alright, but we still could not access social media.
Not with OTT, and definitely not with certain VPNs. But the election was over, was it not? Then why was social media still blocked?
This time, not only had social media been blocked, but all app stores, YouTube, and most VPN clients.
([This article by techjaja](https://techjaja.com/social-media-vpns-app-stores-and-youtube-indefinitely-banned-in-uganda/) provides more detail on the platorms that were banned in Uganda and when it happened.)

![email from Roke Telecom to customer]({static}/images/news/email.jpg) ![Email from UCC]({static}/images/news/email2.jpg)

At this point, I was ready for anything.
I had about two VPN applications installed – [Psiphon Pro](https://psiphon.ca/en/download.html), and [Thunder VPN](https://psiphon.ca/en/download.html).
Nothing was going to get in the way of work this time.]
The VPN connections were mostly flaky so I decided to add [Orbot](https://psiphon.ca/en/download.html) and [Tor Browser](https://www.torproject.org/download/) to that list.
Things were working for a while, but I should have known that the relief would be short-lived.

I was working one day when I encountered this error while trying to access GitHub.
![Github inaccessible]({static}/images/news/github_inaccessible.png)

I thought that was odd, considering I’ve always accessed GitHub with no difficulty.
I didn’t think much of it. I thought that as long I could run commands in the git command line, I would be okay.

While I was wrapping my head around the whole situation, [Gus](https://twitter.com/0xggus) from the [Tor Project](https://twitter.com/torproject) asked if I would volunteer to run a simple test
(See [the Emma repository on Github](https://github.com/NullHypothesis/emma)  for them to see if Tor Bridges were working. I said yeah! Sure!
Anything to bypass the next internet shut down.
So I had to access the repository for [Emma (a lightweight censorship analyzer)](https://gitlab.torproject.org/tpo/anti-censorship/emma) on GitLab, but to my dismay, I could not access GitLab.
I got returned the same error “this site can’t be reached”.
![Gitlab inaccessible]({static}/images/news/gitlab_inaccessible.png)

Well, that’s just ridiculous, I thought.
I entered this URL in my browser [https://www.torproject.org/](https://www.torproject.org/) to see if it was a “tor issue”.
The browser returned “This site can’t be reached”.
So then, I realized all Tor sites had been blocked too, probably because the government suspected that we would try to use Tor to bypass the internet restrictions.
Smart! I was pissed, but I thought it was smart.
I went ahead and opened the Tor Browser on my computer, pasted the same link there, copied the link to the repository and ran ‘git clone’ in my command line. Error!
![Error with cloning Emma from gitlab]({static}/images/news/git_error_tor.png)

I reported this error to Gus, who suspected that the [https://torproject.org](https://torproject.org/) domain had been blocked.
He then gave me a link to a different GitHub repository with the same code to clone but I kept getting returned the same error “Failed to connect to github.com port 443: Timed out”.
![Error with cloning Emma from a personal repo]({static}/images/news/emma_git_error.png)

My suspicions were right – the government had blocked GitHub too. GitHub!
I did not understand the reason for this considering GitHub is not even a social media application.
It’s not a VPN either, so what was going on?! I thought I had been blacklisted by the government and they had blocked my IP address from accessing these sites or something.

It was hard not to feel defeated. I wondered how I would get any work done if I couldn’t even use GitHub?
How would I get inspiration for the “Create video tutorials” project if [YouTube](https://www.youtube.com/) was blocked?
I had the Tor Browser installed on my computer which I could use to access [GitHub](https://github.com/) and [GitLab](https://about.gitlab.com/), but that virtual connection only worked inside the browser.
I needed to have my entire system tunneled so that I could push and clone from GitHub through the git command line.
I turned my mobile VPN on and took my frustrations to Twitter.
![For some reason, our government thinks github is a social media platform.]({static}/images/news/tweet_github_blocked.png)

A friend of mine then sent me a link, which I used to download the VPN for Windows.
I got the .exe setup downloaded on my phone, transferred it to my computer through Bluetooth, and run the installation.
It worked. [GitHub](https://github.com/) was working, everything was working fine.
I have tried asking other people if they are able to access GitHub.
Some are, but majority aren't. I thought it was an OS specific problem, but I was wrong.
A friend of mine who runs Linux on his computer does not need the VPN to push to GitHub, but I think it could just be coincidence.

So now, the new order of things is:

- boot computer
- connect to the mobile hotspot
- start VPN
- get to work

[This report by OONI](https://ooni.org/post/2021-uganda-general-election-blocks-and-outage/#circumvention-tools)
shows network measurement data on the blocking of social media and circumvention platforms leading up to Uganda’s elections,
as well as IODA data (and other public data sources) on the internet blackout that occurred amid and following the election.
It provides [a full account](https://explorer.ooni.org/country/UG) of all the sites that got blocked, when they did, and the various circumvention tools that could be employed to bypass the censorship.

I think it’s disappointing that our government sees the internet as a nuisance, and have very little regard for basic human rights.
Internet costs in Uganda are already very high, considering the social media tax (OTT) on top of that.
However, now that social media has been banned, OTT has been rendered ineffective. We do not know how long this social media ban is going to go on for, though word has it that it is indefinite.
It could be permanent, they say. I asked a close friend who works with [UCC](https://www.ucc.co.ug/) why [GitHub](https://github.com/) was being blocked, and he says that people would try to get updates and installations from GitHub (the same reason for blocking the app stores).

So the question that lingers in my mind is, if the government successfully blocks all VPNs, as well as [YouTube](https://www.youtube.com/) and [GitHub](https://github.com/) along with all the social media applications, what will happen to the jobs of all the Ugandan developers who work remotely, but most importantly, what will happen to my internship with Outreachy ??
