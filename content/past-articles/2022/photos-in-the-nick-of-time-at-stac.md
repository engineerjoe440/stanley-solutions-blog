Title: Photos in the Nick of Time at STAC
Date: 2022-07-02 11:25
Modified: 2022-07-02 11:25
Tags: Python, React.Js, 4H, Fastapi, Materialui, Linode
Category: Youth
Slug: photos-in-the-nick-of-time-at-stac
Authors: Joe Stanley
Summary: Well. It was here, and now it's gone. The Idaho State Teen Association Convention, or STAC - as we fondly call it, has come and gone. It was a great week of little sleep, much excitement, and lots of smiles; but what's more, is that we had some technology wins and losses to talk about. Thank you, Python!
Gallery: {photo}stac-2022

I don't like making "a big deal of myself" or patting myself on the back, but I have to say, I'm very proud of my little team's accomplishments
with this project for our Idaho State 4-H youth conference. Sure; not everything worked perfectly. Not everything was exactly what we wanted.
But that's just how some of these things go, and overall, it was a phenominal success.

If you're not sure what I'm talking about, let me point you at some of the other blogposts I've written on the subject...

* [React.js, Python, Pictures, and 4-H!](./react.js-python-pictures-and-4-h)
* [Using Python to Provide Simple Photo Connections for Youth](./using-python-to-provide-simple-photo-connections-for-youth)
* [Automagic Test Websites](./automagic-test-websites)
* [Error Pages for Education](./error-pages-for-education)

# Our Wins
<img src="{attach}/images/stac-2022/FBAC19F1-F146-4038-BCFF-0D7CF2C3CCD5.jpeg" style="width: 30%; margin: 10px;" align="right" alt="Go Team!">

Yeah! We did have some big wins this year. First and foremost was that we had a great conference. The youth all really seemed to enjoy themselves,
and minor challenges and hiccups aside, all things were good.

You know, we even had more delegates than usual! Idaho invited Washington State to bring a small delegation of youth who are going to be involved
in planning their own STAC-equivalent in Washington, next year. Pretty cool, huh?

Whats more, we had a successful first run of our Photo Uploader Site. Hmm... I think we still need a better name, don't we? Thoughts, anyone?
Leave them in the comments. The site didn't crash, it didn't buckle, it didn't lose anything (that I didn't accidentally delete). And it didn't
go haywire in some other way.

In total, we had more than 1200 photos uploaded to [`albums.idaho4h.com`](https://albums.idaho4h.com/). Yeah, that's right. More than 1200 in
less than 4 days. Whoop, whoop! Now, in reality, there's nothing terribly impressive about this. That's not really *that many* pictures in today's
world, but for an app built on weekends by two people who were both learning all the way through, it's a big win!

> Ok. Let me toot my own horn, one more time.

Our biggest win, is that *we* built this thing. I worked with a youth member who's involved (and super-clever, might I add) in some of these state
events, and together we created this tool to help all of the adults, and all of his peers to engage in a pleasant and simpler way. If you ask me,
*THAT* is the biggest win. We've definatively proven that the youth are more than capable of building their own infrastructure with guidance; and,
after all, that's what 4-H is all about. The whole ethos really is *"learn by doing."*

# Where's the Proof?
<img src="{attach}/images/stac-2022/20220619_172613.jpg" style="width: 50%; margin: 10px;" align="left" alt="Where is it all?">

Oh! You want to see the uploader? The album-site? The photos? OK!

| **Description** &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  | **Link**                                                                                 |
|------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Photo Uploader                                             | [`photos.idaho4h.com`](https://photos.idaho4h.com/)                                      |
| Albums and Pics                                            | [`albums.idaho4h.com`](https://albums.idaho4h.com/)                                      |
| Source Code                                                | [StanleySolutions Gitlab](https://gitlab.stanleysolutionsnw.com/idaho4h/4HPhotoUploader) |

You can go browse all of the source code that our team (one of the Steering Committee youth members and myself) created, or you can go look at the
finished product (the uploader), and even take a look at the album site. The album site has a single public album where all of the photos have
been moved after they've been filtered and cleaned.

Ah! But before you ask; yes, that filtering and cleaning *is* a manual process. Someone has to go through all of them and look for anything that
shouldn't be made public before the photos become viewable. And that sorta takes us into the next topic...

# Our Losses
<img src="{attach}/images/stac-2022/DSC_0630.JPG" style="width: 40%; margin: 10px;" align="right" alt="This clown...">

As much as I would *LOVE* to say that we had zero issues this year with our new tool, that just isn't the truth. We had some great failures, too.
I mean, after all, just look at that guy on the right. Would you trust him to make something that didn't have at least one or two hiccups? Me neither.

So here are all the little things that went wrong...

#### 1) Not all Districts Were Accounted For
Ok. Admittedly, this isn't exactly a failure, but I wanted to call it out, anyway, since there was some work to be done here, and it emphasized a
point of contention in our system. You see, we've got a hard-coded mechanism for managing district validation for the district selection. That selection
is this little section here...

<img src="{attach}/images/district-selection.png" style="width: 55%; margin: 10px;" align="left" alt="District Selection">

<br><br>

In the code snippet below, you can see that there's a hard-coded number of options that are validated against. This isn't the only place though, the
React.js frontend also has these values hard-coded. SO... We'll need to determine a way to make those selections more discrete, and customizable. Hmm...

<br><br><br>

<details>
  <summary>Click to examine the district validator function...</summary>
```python
def validate_district(district_name: str) -> ValidatedDistrict:
    """
    District Validation Function
    
    This function validates a string providing the name of the district which
    photos should be uploaded in association with. If the name is valid, it will
    return `True` and the sanitized name, should the name NOT be valid, `False`
    will be returned with an empty string.
    """
    count = 0
    district = ""
    if district_name.lower().find("eastern") != -1:
        district = "Eastern District"
        count += 1
    if district_name.lower().find("northern") != -1:
        district = "Northern District"
        count += 1
    if district_name.lower().find("central") != -1:
        district = "Central District"
        count += 1
    if district_name.lower().find("southern") != -1:
        district = "Southern District"
        count += 1
    if district_name.lower().find("washington") != -1:
        district = "Washington State"
        count += 1
    if count == 0:
        return(False, "This isn't a district!")
    elif count > 1:
        return(False, "This is a weirdly named district!")
    else:
        return True, district
```
</details>

Ultimately, this came up last minute (Sunday night before the delegation arrived) when we were discussing the Washington-State delegation's participation
in the district competitions. Since they would be participating, we'd need them added to the list. Thankfully, due to our automated build system (thank
goodness I spent the time to get that thing working), I was able to make the code changes, verify that my changes had some bugs, fix the bugs, and deploy
- all within the time of about a half-an-hour.

So yeah, I'll call it a loss, but there was a hidden win, too!

#### 2) Limited Number of Photos in an Upload Group

We've all heard that joke about assumptions, right?

You know, the one that says something about making an a$$ out of you and me? That one... Well, is it not the case that in engineering, we have to make a
LOT of assumptions? Oh yeah. We do.

Well, we made an assumption about how many pictures people would want to upload at any given time. Guess we got those numbers a little wrong. We quickly
learned that people wanted to upload a lot more than 10 pictures at any given time. Dang. Good thing GitLab has bug-tracking! So I went ahead and logged
it already: https://gitlab.stanleysolutionsnw.com/idaho4h/4HPhotoUploader/-/issues/48  -- Love GitLab.

#### 3) Limited Download Access
<img src="{attach}/images/stac-2022/20220619_172534.jpg" style="width: 40%; margin: 10px;" align="left" alt="Not Enough Access.">

Unfortunately, another thing that we learned the hard way this year was that downloading an entire album as a zipped file isn't as easy when you're not
the web-admin (*coughs* that's me). The teen officers (who are in charge of putting together a slide-show with all of these pictures), had one heck of a
time trying to interact with the Lychee albums app to get the pictures that they need. Now, admittedly, this is partly a combination of lack of teaching
from me, and partly general technical challenges, but in total, this application is supposed to make things easier for these youth, lowering the barrier
to entry and making the process simpler, so they have more time to enjoy the conference.

There are learning points to take away from it, as a whole. There's the sentiment of:

> There's no better time to learn something than the present.

Still, if it's easier, overall, it could give the teen officers a greater opportunity to enjoy their conference. So we'll need to figure out a better
way to make those images available for download in a zip.

#### 4) Manually Screening Pictures

You know me... I hate doing something that I think the computer can. That's why I consider myself an "automation engineer," I automate things; that's
what I do.

So when we still have to manually screen pictures and make sure that they're appropriate, that makes a small part of me cry inside. There HAS to be a
better way. I still think there is, but I don't know what it is yet.

I think I'd like to explore what those ever-present buzz-word technoligies might be able to provide. You know the ones; AI and ML. What can a little
computer-learning bring to the table? Can it identify photos that would be considered explicit, or inappropriate? We're 4-H, so we *shouldn't* be seeing
those, anyway. But, we're working with youth. So there's always the possibility. Right? So we should have some screening mechanism in place. Even if it's
for nothing else than to remove photos that just aren't flattering.

# Closing Thoughts and Special Thanks

> Administrative note: We're diverging from the technical stuff, here, so if that's what you came for, you're free to take off at this point!
> However, if you like the 4-H memories, stick around and read on!

I truly love participating in this event. It excites me each year to watch these young people grow and find themselves, and become true leaders. They're
going places, and I love seeing that. I'm so happy to work alongside some really cool people who make the event possible.

<img src="{attach}/images/stac-2022/528FB398-BCDA-435E-A3E8-EC5AF00A1F4F.jpeg" style="width: 50%" align="left" alt="These Folks Rock!">
<img src="{attach}/images/stac-2022/028EFD6B-950A-4995-B1E5-A98BF31BD10A.jpeg" style="width: 50%" align="right" alt="What goofs...">

This isn't everyone, but it's a solid group! From left-to-right, Tara, Teresa, (yours truly), SheilAnne, and Kandee. Not pictured are Carrie and Mike
who help to "round out" the remaining adults on the STAC Steering Committe. They're all a great group of folks to work with, and spend time with. I
couldn't be happier to collaborate with them. Of course, I'd be remiss to ignore the fact that there's plenty of youth wha also make up the team. They
all make it so much fun to work on.

### Dr. Lindstrom

I'm a bit of a sap, so I want to end on this sappy note. Think of that what you will.

It's hard to believe that nine years ago was *my* first time attending this conference as a youth, myself. That year was a wild and wonderful ride; I
learned so much. That was also Dr. Jim Lindstrom's first year as the Idaho State 4-H Director.

<img src="{attach}/images/stac-2022/DSC_0925.JPG" style="width: 100%; margin: 10px;" align="right" alt="Dr. Lindstrom">

I don't want to spend too much time pounding on this point, but I want to leave a lasting "Thank You," right here. There's a lot that has gone on
behind the scenes in the state. I'm glad to have been able to have seen some of these trials and tribulations, so that I might understand a small part
of the process. It takes an army, not just a villiage, to keep a state 4-H program strong, and ours is. We have wonderful volunteers, leaders, parents
youth, educators, and 4-H professionals. Many times, there are folks who wear several of those hats all at the same time.

Dr. Lindstrom has been behind this development for that entire time. He's worked diligently to keep the pipelines flowing and keep all of those folks
engaged. I still remember sitting with Dr. Lindstrom at our formal banquet the first year at STAC and talking to him about what projects I was taking
that year, and what I enjoyed about 4-H in the state. This is Dr. Lindstrom's last year, and it's been wonderful to reflect on all of the great things
that the state has accomplished over these years, and I'm so thankful for Jim's leadership, care, and persistence. He's been a solid guide, and a true
leader. The sort of person we all hope to "grow up to be."

Thank you, Dr. Lindstrom! May Idaho 4-H continue to reap the benefits of all the greatness you've sewn, and may you be able to look back on it with
fond memories of all the youth who've seen tremendous growth.

---

Last thing...

Keep Making the Best Better.

~Joe
