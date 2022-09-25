title: GSoC 2022 Work Product - Track Suggestion Feature
authors: Fatih Emre YILDIZ
status: draft
tags: gsoc, gsoc-2022
comments: yes

Disclaimer: *The blog post primarily serves as the documentation for the [Google Summer of Code](https://summerofcode.withgoogle.com/) 2022 project: "Track Suggestion Feature". Thus, it contains a lot more detailed description, than the other Mixxx blog posts.*

#### Introduction
After long hours of playing, when the floor is crowded the question shows up. "What to play next?". That is a big problem for almost every DJ. This project aims to give suggestions according to tracks playing on the decks. With this feature, Mixxx will have a helper for all the DJs. 

Hey everyone! It's Emre and you've just read my project description. I would like to introduce myself before I dive into the detailed explanation of the blog. I love to listen and play music. I have been always into DJing. That's why I wanted to take a part in Mixxx. I am a person who plays music while chilling-partying with my friends. They always find my music choices are the right fit. But they don't know how difficult to pick the right song, especially after a while of playing. So I thought that would be the best project to work on this summer.

#### Motivation
The track suggestion feature was on the wishlist a long time ago. This feature was mentioned firstly on the [Bug Tracker](https://github.com/mixxxdj/mixxx/issues/6106) and on the [Forum](https://mixxx.discourse.group/t/individual-possible-followers-for-each-track-track-mind/11893). These discussions inspired me to do this project. 

Before we started to work on this project, I and my mentor decided to do it with the side projects. We choose the side projects so with that, implementation of the big features is split into pieces and with that we have a chance to test and review them in smaller environment. These side projects also helped me to get to know the code base, we can think of them just like preparation ground. Also, in one of those side projects we have encountered a bug that took long time to review and test, there was a risk to exceed the time of the project, but luckily we made it and could focus on the main part.

We have come up with a few different side project ideas.

The first idea was to have a feature called *Find On Web*. This feature aims to help users if they are looking for additional info about a track on online music databases. After this is implemented roughly, we decided to polish it with the *Factory Design Pattern* which simplifies adding other online music databases later on. After these two side projects we decided to get cover art of the tracks which is *Cover Art Fetcher*. When I collect tracks for my library, I always wanted to have the correct metadata of the track and also the correct cover art. As a person who cares about appearance a lot, I thought that I am not alone in this situation and people would love it too. That's why I found this side project very helpful and important! At last, the main project comes along, the *Track Suggestion Feature* which is getting Track Suggestions from various services.

#### Implementation
##### *Find On Web Feature*
The first side project *Find On Web* is supposed to help user finding additional info about a track, album, or artist.

Think about a scenario, you have only just a track from an album and you would like to get more information about other tracks in that album. Until now, you would first open your favourite web browser, then you type the Artist and Album in your search engine, you hit the button to search and you find the web page and finally you can get more information. This is very time-consuming. This is where the Find On Web comes in handy.

Let's think about another scenario. You love to find out remixes of each track in your library and with those remixes you expend your library. You probably use [SoundCloud](https://soundcloud.com/) or a similar service very often. Luckily we have this service in our *Find On Web* feature. If you are looking for remixes in your library very often, *Find On Web* feature will help you along with that.

This feature is placed in the Track Menu. When you right-click on a track, you will see different Menus and Actions that you can take over a track. This is called *Track Menu*. On the track menu, in the Metadata section, you can see the *Find On Web*. There are three main Online Music Databases that exist as menus. They will be called services after this part. These services are:

* [SoundCloud](https://soundcloud.com/)
* [Discogs](https://www.discogs.com/)
* [Last.fm](https://www.last.fm/)

When you hover your mouse over those services menus, you can see the related track properties as actions. Each action populates the suggested service with the suggested track information for your default browser. This looks like:

*Find On Web Feature*
![Find On Web Feature]({static}/images/news/findonwebfeature.png)

This Implementation was designed roughly for the next step. The next step was:

##### *Find On Web With Factory Design Pattern*
This implementation aims to have a Factory Design Pattern for the Find On Web feature. 

As its name states, you can think about you have a factory and you can produce products. Our factory is the *Find On Web* itself and our products are the services. The most important point here is that all products coming out of a factory must be derived from the same interface or class. Thanks to this pattern, you can abstract our Services for future use. You can produce products - add new services - straight forward.

Since there are many other online music databases, that is nice to have *Find On Web* feature with the Factory Design Pattern. Just in case if needed any other service can be added easily without making any changes in the code base.

Related Files:

* [findonwebfactory.cpp](https://github.com/mixxxdj/mixxx/blob/main/src/widget/findonwebmenufactory.cpp)
* [findonwebfactory.h](https://github.com/mixxxdj/mixxx/blob/main/src/widget/findonwebmenufactory.h)
* [Find On Web Menu Services Folder](https://github.com/mixxxdj/mixxx/tree/main/src/widget/findonwebmenuservices)

##### *Editable Track Menu*
While discussing about *Find On Web* feature and where we could placed it on Mixxx. We have decided to place it on Track Menu. There was an idea on Zulip, that the Track Menu was gettin crowded, and we can consider to make it configurable.

At first I thought the same and this feature would be nice to have and that can help me to get to know the code base for the preferences option. 

I introduced this idea on the Zulip channel. The idea of making the track menu configurable rejected in the discussion with the community in favor of Mixxx. Sometimes the configuration option proves the developers' inability to make decisions for them. As a result, we have chosen not to implement this.

##### *Cover Art Fetcher*
This is the third side project for the Track Suggestion Feature. Fetching cover art from online resources. According to the search we have done, we decided to fetch the cover art from Cover Art Archive (CAA) hosted by [Archive.org](https://archive.org) . The Cover Art Archive is a joint project between the Internet Archive and [MusicBrainz](https://musicbrainz.org/).

The CAA uses the track's Release MBID (MusicBrainz Identifier) to retrieve cover art. For that, the *Import Metadata From Musicbrainz* feature could be used.

To get cover arts, we needed two different processes that should work in order. These processes are called *tasks*. First, we should get the cover art links. Second, by using that links and according to the user choice we should get the cover art itself.

Cover Art Archive works a little bit different than the other services. I discovered that after I sent my first-ever request. I received the response but it was redirected. Thanks to Qt's class *QNetworkAccessManager* has [Redirect Policy](https://doc.qt.io/qt-6/qnetworkrequest.html#RedirectPolicy-enum) which is designed for these situations.

The response consists of links to the cover art in different sizes. The possible sizes were 250px and 500px all the time and if it is available 1200px and also the HQ. This response also had the back cover art of the albums. After discussing that with the community, we have decided to only allow the front cover art but with every possible size, which includes the HQ!

On the preferences the user will see these options:

* Lowest:  250x250
* Medium:  500x500
* High:    1200x1200 if available on CAA.
* Highest: More than 1200px if available on CAA.

Then we needed the second task to get the *Actual Image* of the cover art. According to the preferences chosen by the user, the actual image is retrieved. 

After this task was successfully done, there was only one thing left and it was the use case.

The best use case was to change the *Import Metadata From Musicbrainz* window to be suitable for cover art fetching and updating metadata at the same time. That was solving all the possible issues mentioned.  

Right now, users can select between the lowest quality to highest quality, when they press apply on the tag fetcher cover art is downloaded and updated for that track.

Related files:

[coverartarchivelinkstask.cpp](https://github.com/mixxxdj/mixxx/blob/18ed28d9061feb19b58aa4db1730f347622686a5/src/musicbrainz/web/coverartarchivelinkstask.cpp)

[coverartarchiveimagetask.cpp](https://github.com/mixxxdj/mixxx/blob/18ed28d9061feb19b58aa4db1730f347622686a5/src/musicbrainz/web/coverartarchiveimagetask.cpp)


*Cover Art Fetcher*
![Cover Art Fetcher]({static}/images/news/coverartfetcher.png)

##### *Track Suggestion Feature*

This is the main part of the project. In my opinion, Track Suggestion is a cool feature for a DJ app. Getting a hint for the next track at right time would be so precious for a DJ. But the possibility of the finding correct track has also the same amount of difficulty. 

To find similar tracks, we have used Last.fm Thanks to their [API](https://www.last.fm/api) we can get track suggestions by just providing the Artist and Title. What is changed is basically on the library sidebar, there is a new feature called "Track Suggestion" which can be turned on or turned off on the preferences page. There are five different sub-menus located under this feature. Four of them belong to the decks and one of them belongs to the user's choice. When a track is placed on a deck, the correlated sub-menu changes to the *Artist | Track Title*. If the user clicks on that menu a new library is populated. If the suggestions are fetched before the user will be retrieved from the database, if it is not, the user will see a button that says *Load Track Suggestions For Artist | Track Title*. After this button is pressed, we send the request and get the response cached in the database.

The new library is an External Library. The located tracks are not available for to play, because they are only text retrieved from Last.fm. But the tracks listed in that library can give an idea to the DJ about what to play next. DJ can see a title or an artist and this can help about picking the next song.

There is a problem with the Last.fm service, when the track or artist name is misspelled the suggestions can not be fetched. Also for some tracks, there is no suggestion available on the Last.fm servers. To fix this issue, we have discussed few different solutions, such as finding another service as a back up.

*Track Suggestion Feature*
![Track Suggestion Feature]({static}/images/news/tracksuggestionfeature.png)

Related files:

* [lastfmgettracksimilartask.cpp](https://github.com/mixxxdj/mixxx/blob/03b1b6831e15428745398c20e36ef704db336c29/src/library/tracksuggestion/lastfm/lastfmgettracksimilartask.cpp)
* [tracksuggestionfeature.cpp](https://github.com/mixxxdj/mixxx/blob/03b1b6831e15428745398c20e36ef704db336c29/src/library/tracksuggestion/tracksuggestionfeature.cpp)

#### Pull Requests and Issues
##### Pull Requests

[mixxx#4697](https://github.com/mixxxdj/mixxx/pull/4697)
- *BasePlaylistFeature*: add popup asking deletion playlist

*Status: Merged*

This PR is the beginning of my story. That was my initial PR in my open-source experience. As mentioned on the Mixxx [GSoC advice page](https://github.com/mixxxdj/mixxx/wiki/gsocadvice) before, I fixed a bug from the easy tag. 

In order to do that, I needed to fork the project, clone it, compile it, make changes, install the pre-commit, push the changes, and open a PR.

As a total beginner, that took my whole day to figure things out. But If I look at it now, I can say that I am more experienced, and that is easy peasy - lemon squeezy now.

---

[mixxx#4700](https://github.com/mixxxdj/mixxx/pull/4700)
- *CrateFeature*: add popup to avoid accidental remove of Crate

*Status: Merged*

This PR is similar to my first PR. After the first PR is merged, That was also mentioned on the bug that it is needed for crates as well.

---

[mixxx#4752](https://github.com/mixxxdj/mixxx/pull/4752)
- Parserm3u export

*Status: Merged*

This PR aims to have a better playlist/crate exporting experience. While I was surfing on the
discourse, in one of the topics a user asked a question related to the exporting playlist. Just to help the user, I tried to export my playlist, but suddenly I realized that when I import my playlist back there was some tracks were missing. I have mentioned that on Zulip and with the help of other developers, I realized that there were missing characters and I wanted to solve this issue and I did. 

Meanwhile, I've learned that m3u files can have different encodings while m3u8 files are UTF-8.

---

[mixxx#4772](https://github.com/mixxxdj/mixxx/pull/4772)
- *WFindOnWebMenu*: Menu for to find track properties in online music databases

*Status: Merged*

This PR was my first PR in the coding period. *FindOnWebMenu* helps users to find related
track properties on various online music databases.

In this PR, I had the chance to get to know the code base and got familiar with the QT. I also used the git command rebase for the first time, that was difficult at those days, but right now I am more experienced with the git commands.

---

[mixxx#4836](https://github.com/mixxxdj/mixxx/pull/4836)
- *WFindOnWebMenu*: Implementing the factory pattern

*Status: Merged*

This PR is the second step of the previous one. This changes all the code into the factory pattern.

In this PR, I have learned design patterns. Not only the factory design pattern, I also learned the other design patterns, such as Abstract Factory, Singleton, and more. I am pretty sure that I will encounter these general problems in software and I will use the design patterns.

---

[mixxx#4851](https://github.com/mixxxdj/mixxx/pull/4851)
- Cover Art Fetcher

*Status: Open (WIP) | last GSoC commit: [8856e4b](https://github.com/mixxxdj/mixxx/pull/4851/commits/8856e4b994e48a80eac5f03f85459eb5649e1260)*

This is the main PR about the cover art fetcher.

---

[mixxx#4864](https://github.com/mixxxdj/mixxx/pull/4864)
- Cover Art Label & Cover Art Full Size composition with menu

*Status: Merged*

There was a problem with the cover art label displayed on the cover art fetcher. We decided to implement the cover art fetcher into "Import Metadata From Musicbrainz", and I wanted to add the existing cover art and the fetching cover art on the "MusicBrainz" dialog. The problem was, the cover art menu which consists of actions "update-clear-reload" was populating from the fetched cover art label too. To solve that, we first decided to have a base class for the cover art label which doesn't have any menu at all, and Inherit another label which has the menu. But this was not good looking in the code base with the duplication of the code and also locating/naming of the new base class. So with the help of my mentor, we have decided to have a composition approach. This has taught me a terminology in Object Oriented Programming. Which is very simple but effective in design. *Is-a & Has-a * relationship. When we inherit from a base class, we can simply say "Cover Art Label *is a* Cover Art Label With The Menu". But that doesn't just sound right. So instead, we added Cover Art Menu as a parameter in the constructor. Now we can say "Cover art label *has a* cover art menu". Thanks to this PR, this is not going to be used just not in the cover art fetcher also in the cover art worker.

---

[mixxx#4871](https://github.com/mixxxdj/mixxx/pull/4871)
- DlgTagFetcher new feedback system

*Status: Open (WIP) | last GSoC commit: [47bbc15](https://github.com/mixxxdj/mixxx/pull/4871/commits/47bbc157885b4f343479d7f4291970fc67744f3e)*

This PR was to aim for a better interface for "Import Metadata From MusicBrainz". Because when the user wants to get cover art from the cover art archive, the process was too long and confusing about the initial status of cover art fetching. To have a better feedback system, we have decided to add a *QProgressBar* to show the initial progress not just for the cover art archive, but also for fetching Metadata from Musicbrainz. While Implementing this new feedback system, I discovered a few related bugs that were affecting the existing release of Mixxx version 2.3. That PR and also the bugs were going to lead me to learn more.

---

[mixxx#4887](https://github.com/mixxxdj/mixxx/pull/4887)
- Ask user after changing the cover art.

*Status: Draft | last GSoC commit: [693ab90](https://github.com/mixxxdj/mixxx/pull/4887/commits/693ab90bff30f88bf4bbaaae64a574a251dd4c72)*

This PR was about a "TODO:" comment in the code base. But after I work on it for a while, I discovered that this is a must, for the cover art fetcher. This PR asks users if they want to copy the cover art which they have updated. It started simply with a *QMessageBox* and then became big with the needed implementations. Such as making it atomic writing, moving to a separate thread, and adding a comparison between the old and new cover art. This PR was becoming more big and difficult to review-implement. So we had to break this into smaller PRs but this one is still open for the future implementation.


---

[mixxx#4909](https://github.com/mixxxdj/mixxx/pull/4909)
- CoverArtUtils: Fix Reload From File/Folder, Updates Wrong Cover Art 

*Status: Merged*

This PR aims to fix the related bug mentioned below.

---

[mixxx#10822](https://github.com/mixxxdj/mixxx/pull/10822)
- Fix: Rate limit exceeds for Musicbrainztask.

*Status: Closed*

This was a bug that I noticed while working on the new Musicbrainz design. I've tried to fix this by adding a state called "Looping" in the first place. But later on, this PR was superseded by [mixxx#10875](https://github.com/mixxxdj/mixxx/pull/10875). But even though, thanks to my mentor for providing additional information about how to overcome this issue. I have learned about the activity diagram 'Swimlane' and UML State charts.


---

[mixxx#10860](https://github.com/mixxxdj/mixxx/pull/10860)
- Track Suggestion Feature: Get tracks suggestions according to the track playing on the decks

*Status: Open (WIP) | last GSoC commit: [0c02074](https://github.com/mixxxdj/mixxx/pull/10860/commits/0c020741edc5a4f9c3dcb7916bad959744c72602)*

This is an initial PR about the Track Suggestion Feature. This is used Last.fm's API to get similar tracks that are placed on the deck and also tracks selected by the user.

---

[mixxx#10861](https://github.com/mixxxdj/mixxx/pull/10861)
- BaseSqlTableModel: remove duplicated line. 

*Status: Merged*

While I was working on the Track Suggestion feature, I encountered a duplicated line in one of the classes. This PR deletes this duplicated line.

---

[mixxx#10878](https://github.com/mixxxdj/mixxx/pull/10878)
- FIX: Tag Fetcher close button doesn't abort task

*Status: Merged*

This PR aims to fix the related bug mentioned below.

---

[mixxx#10897](https://github.com/mixxxdj/mixxx/pull/10897)
- Moving SafelyWritableFile class to the utility folder. 

*Status: Merged*

This is a part of the cover art copy worker PR. This PR aims to move the SafelyWritableClass from inside a file to the utility folder. 

---

[manual#517](https://github.com/mixxxdj/manual/pull/517)
- Update Getting Involved

*Status: Merged*

There was a new user who introduced himself on the Zulip channel. I wanted to give additional info for to guide him. To do that I was looking at to documentation and realized that the links for bug reporting were directed to the launchpad which was the old bug tracker of Mixxx. This PR aims to delete the old links and replace them with the GitHub issues link.

---

[mixxx#10902](https://github.com/mixxxdj/mixxx/pull/10902)
- Cover Art Copy Worker

*Status: Open (WIP) | last GSoC commit: [2e13c64](https://github.com/mixxxdj/mixxx/pull/10902/commits/2e13c64705390e3dd58526ec66a28c126347792c)*

This PR was opened due to the size of the PR about "Ask user after changing the cover art". This is the smaller version of it. There is no comparison, wizard, or dialog but the other must-needed parts for the cover art fetcher are included in this PR.


---

[mixxx#10908](https://github.com/mixxxdj/mixxx/pull/10908)
- ImageFileData class added to write images without loss

*Status: Merged*

While the worker was writing new cover art where the track was located, there was a decrease in the cover art file size. This PR was needed to save the cover art without loss. While working on this I have learned that the formats for images. Between these formats, "jpg"-"jpeg" format(s) is a lossy format that compresses the images. That is useful for websites to downgrade the size of the web page but not in our situation which quality is really important.

---

##### Issues

[mixxx#10877](https://github.com/mixxxdj/mixxx/issues/10877)
- Closing Tag Fetcher via the "x" close button doesn't stop the WebTask

*Status: Closed*

I was testing the latest status of the *Tag Fetcher*. If the Musicbrainz window is closed via the ESC button or 'x' button the *Tag Fetcher* was not aborting and working in the background.


---

[mixxx#10816](https://github.com/mixxxdj/mixxx/issues/10816)
- Updating Cover Art on Track Properties Doesn't Take Effect 

*Status: Open*

This bug is related to the *Track Properties* and it is different than mentioned in the title. Normally all the cover art actions update the cover art right away, but when we update it on the track properties the cover art was not updated. That was a mistake by me and this was the correct behavior of the track properties.

The bug is actually when the new cover art is updated on Track Properties and the user wanted to see it in full size, the old cover art populates.


---

[mixxx#10807](https://github.com/mixxxdj/mixxx/issues/10807)
- Reload From File/Folder, Updates Wrong Cover Art 

*Status: Closed*

This was a bug that I encountered while working on the cover art fetcher. I have updated the cover art of all the tracks in my library. But the problem was all of my tracks were updated with only single cover art.

---

[mixxx#10796](https://github.com/mixxxdj/mixxx/issues/10796)
- If MusicBrainz Returns an empty XML (404) whole task fails and no results displayed 

*Status: Open*

This bug was affecting some of the tracks in my library. While I was working on the Tag Fetcher, I realized some songs in my library were having an interesting error which is displayed as "Not Found" on the Musicbrainz windows. But the logs were not saying the same thing, they were some tasks were successful and related results exist for these tracks. But they were failing for some reason. When I dig that down, I realized that the responses from Musicbrainz are successful but empty, and in the codebase that was meant to be no results. This is still in progress, but after that is resolved we will increase the rate of the successful results of our Tag Fetcher.

---

[mixxx#10795](https://github.com/mixxxdj/mixxx/issues/10795)
- Rate Limit exceeds for some songs while Importing Metadata From MusicBrainz 

*Status: Closed*

This bug is discovered the same as above. The error message displayed to the user was confusing too. The difference is, it was quite easier to find out why there was error. The tracks that can not have the results were the ones that have a lot of Recording IDs compared with the other tracks. When that is digged down, we found out that MusicBrainz Rate Limit was a request per second. But that was designed without any delay. That's why if a track has many Recording ID's retrieved from AcoustID, we were hitting the rate limits.

---

[mixxx#10782](https://github.com/mixxxdj/mixxx/issues/10782)
- Mixxx crashes when click on a track updated with Musicbrainz Metadata 

*Status: Closed*

This bug was happening due to debug assertion when I select the tracks updated from "Import Metadata From MusicBrainz".

---

*Discourse*

In my free time, I was surfing through the Mixxx Forum to help the users as much as I could with my knowledge. In some of the topics, I was able to help the users, these topics and my answers were: 

[Discourse - Exporting a playlist to m3u invalid characters](https://mixxx.discourse.group/t/exporting-a-playlist-to-m3u-invalid-characters/25181)

[Discourse - Easy Uncheck Assume Constant Tempo In Track Properties When Default](https://mixxx.discourse.group/t/easy-uncheck-assume-constant-tempo-in-track-properties-when-default/24479/4?u=fatihemreyildiz)



#### Future work
There are only a few to-do's left for the side projects we have discussed before. They can be improved just like in any other feature that exists in the Mixxx. For the track suggestion feature, there are still additional future works that still needs to be done. These are:

* Merge the cover art worker for *Cover Art Fetcher*, with the caching class of the fetched cover art *Cover Art Fetcher* can be easily integrated.
* Specialized External Playlist model for *Track Suggestion Feature* for better database interaction
* Determination if the suggestions are in the user's library, with that *Track Suggestion Feature* can be much more usefull.

There are few ideas that have been discussed before on Zulip. These are not mandatory works but that would have been nice to have. These can be a future reference. 

* Get cover art of the suggestions so the *Track Suggestion Feature* would look better.
* User Clustering Playlists! There was a brilliant idea while we were brainstorming about Track Suggestion Feature. User's can make their own suggestions by using their own library.
* There could be a field in preferences for *Find On Web* feature, which is a field can be filled by the user. With that users can add their own services.
* *Find On Web* could have a preference option to enable - disable the services.

#### Things I learned from GSoC
First of all, I can easily say that GSoC was one of the best experiences in my life. It deserves Its title "Summer of Code". I had a great summer full of coding and I learned a lot and had so much fun meanwhile. During this period, being an open-source contributor to a community felt amazing. Before the GSoC, I did some projects for my university projects and used git very basically. But first time in my life, I did coding for a real project and used git professionally, and learned a lot about it. I have learned that every aspect is really important while coding and even small glitches can cause a big bug. I have developed features which people can use. Fixed existing bugs that people encountered. This was such a unique experience. If I wouldn't meet with GSoC this year, I wouldn't be an open source contributor or I would have been very late in another time in my life. I can easily say that I've learned a lot about C++, Qt, design patterns, web services, testing, debugging, git and gained important experience on all of them. What I have learned was I am enjoying hours of coding, testing, hunting bug, and solving problems. If I should have compare myself before the GSoC and after the GSoC, the difference is awesome.

#### Conclusion
At the end of the coding period, the decided side projects and their little steps were implemented into Mixxx. Such as *Find On Web*, *Find on Web with Factory Design*, and *Cover Art Label* without a menu.  Besides the side projects, there were many bugs (which were affecting both the stable 2.3.3 version and the upstream branch) reported and fixed. Such as the empty XML, the rate limit of MusicBrainz, aborting the tag fetcher, etc. With those fixes, Mixxx users will have the better fetching metadata experience. At the end of the period, unfortunately, the Track suggestion feature couldn't be implemented into the Mixxx code base but we have a working POC as an open PR. Also, an existing request from a long time ago was discussed seriously with the developers and users on the Zulip GSoC channel. We have over-searched the available services and discussed the main problems with fetching suggestions from different services, how to make this feature useful and what needs to be done to have the best use-case. This will be a reference to the future for sure.

#### Acknowledgements
I want to start with how great Mixxx is! Since the first day I joined the community and introduce myself on Zulip today, I am enjoying it a lot and I am so happy to be part of Mixxx. Everybody in the community was really helpful and they are doing their bests to make Mixxx the best DJ Software. I would like to thank all the developers and contributors who contributed to Mixxx in any way.

I can not express how thankful I am, to my mentor [@Daniel Schürmann]({author}daniel-schurmann). He has been such a great adviser, teacher, and guide from the very beginning to the end of the project. It won't be my fault if I say that he has been the best mentor! Besides being a really good mentor, he was so friendly. The ideas that he shared with me broadened my aspect through the project. At the beginning of the project, I was nervous about the whole big thing that needs to be done, and he gave me perspective in those sorts of circumstances. That was "broom stroke after broom stroke". This perspective helped me from the beginning till the end. There is one last thing left that I need to add, which is... "It's Friday Again!".

I would like to thank [@ronso0](https://github.com/ronso0) for his brilliant ideas about the GUI of the Tag Fetcher Dialog, Cover Art Fetcher also for the Track Suggestion Feature. His ideas about UI/UX were really helpful for me to move forward in my PRs. I would like to thank [@Swiftb0y](https://github.com/Swiftb0y) for his reviews in "Factory Pattern Design", that was nice to work with him, also I would like to thank him for his ideas about the cover art fetcher. I would like to thank my friend [@David Chocholatý](https://github.com/davidchocholaty) who is also a 2022 GSoC Mixxx participant for his coworking and help with the final blog. I would like to also congratulate him on his successful project!

I would like to thank everyone interested and who shared their precious ideas related to the "Track Suggestion Feature" and Its little side projects.

At last, I would like to thank Google for this amazing program and giving us this opportunity .
