title: Migrated to GitHub Issues
authors: Nikolaus Einhauser
tags: infrastructure, development, contribute
comments: yes
date: 2022-08-24 15:19:17


Yes everybody, we officially moved our bug tracking away from Launchpad to
GitHub. If you've never tried to report a bug in Mixxx or wanted to contribute
in other ways, it's very likely you have no idea what this post is about, but if
you do it's even better. No matter if you do or don't, keep reading.

The Mixxx team has traditionally been using Canonical's (the makers of Ubuntu)
Launchpad platform for hosting their code, managing bug reports and releases.
Over the years, Launchpad has become increasingly dated, lack of modern
features, old UI, and bad user experience is the primary reason why many people
(myself included), stay away from Launchpad. Especially for new contributors the
mandatory Ubuntu One account was another reason for not to immediately report a
bug when they encountered it.

We've started transitioning away from Launchpad quite a while ago:  
Back in 2013 we have transitioned from the Bazaar version control system to Git
and moved our `main` branch to GitHub. At that point in time, GitHub issues
where not yet suitable for managing our bugfix and release workflow, thus bug
reports continued to be handled on Launchpad. This has progressively changed
over the past couple of years, now GitHub has a "duplicate issue" detection
feature, can organize bugs in projects and the labeling feature is flexible
enough to fulfill most of our needs.

Going forward, Launchpad will only be used for publishing to our Ubuntu PPA.
Hence no contributor outside of the core team will have to bother with Launchpad
again.

Shortly before starting the migration, we made our Launchpad bug tracker
read-only (some of you might have noticed that and/or have seen our heads-up
post). The migration took about 50 Hours. All of the existing messages were
copied to GitHub including links to any attachments and patches uploaded as part
of message. We also carry over the state of a bug by mapping them to Github
issue Labels:

| Launchpad  | GitHub |
| ------------- | ------------- |
| Confirmed | `confirmed` |
| Fix Committed | *close issue*  |
| Fix Released | *close issue*  |
| Incomplete | `incomplete` |
| In Progress | *no label* |
| Invalid | `invalid` |
| New | *no label* |
| Triaged | `confirmed` |
| Won't Fix | `wontfix` |
| Critical | `party stopper`,  `bug` |
| High | `bug` |
| Low | `bug` |
| Medium | `bug` |
| Undecided | *no label* |
| Wishlist | `feature` |

Since Mixxx is a project exclusively maintained by volunteers where each
volunteer is free to work on whatever they choose anyways, we decided to drop
the different priority levels assigned to issues.  

I want to express a special thanks to our core team member
[@Holzaus]({author}jan-holthuis) for writing a [custom import
script](https://gist.github.com/Holzhaus/ed384b93465dcc516ae205090e4f179b) which
made this migration feasible in the first place.

Due to the big number of bugs and the flood of related notifications, I have
noticed quickly that the script will likely hit various rate limits and spam
protection facilities.  
After [getting in contact with GitHub via
Twitter](https://twitter.com/mixxxdj/status/1546544041038422019) they assembled
a team of engineers and FOSS experts to help us evaluate possible solutions.
Thanks to them, we were able to avoid email spam and reduce the time the import
took by two orders of magnitude.

# What does this mean for existing contributors?

From today on, no more bug reports should be filed on Launchpad. Currently
ongoing discussions should be continued on GitHub instead. Note that any
comments made after 2022-08-22 12:00 UTC have not been migrated to GitHub.
Existing bug reporters need to create a GitHub account if they haven't already.

Thank you everyone for your patience.
