---
author_avatar: defna
author_name: Jeff Triplett
author_url: /about
categories: ""
date: 2020-04-15 14:00:00
feature_image: 2017-07-20
layout: post
permalink: /announcements/2020/04/15/vendor-update/
read_time: ""
show_avatar: true
show_related_posts: false
title: "Vendor Update"
---

Since 2015, DjangoCon US has used [Conference Badge](https://www.conferencebadge.com/) as a vendor to handle printing our conference badges. Conference Badge released [October 18th 2019 Incident Post-mortem](https://www.conferencebadge.com/security/20191018), which we believe impacts us.

While we believe that this was a hypothetical issue, we want you to be aware of it because we have no way of knowing for sure.

## What Happened

According to Conference Badge's report:

> On Friday October 18th 2019 at 3:20PM ET, a security vulnerability was identified in our system. It was brought to our attention by a 3rd party security researcher who has collaborated with companies such as Spotify, Tumblr and Twitter.

> The vulnerability was due to an Amazon S3 bucket (a file hosting service) that was misconfigured as public. This allowed listing and downloading files from the bucket.

Short version: Through a third-party security scan, it was determined that it was possible to access a list of printable PDF badges and to download them on Conference Badge's website, which included DjangoCon US's badges.

## What DEFNA has done

We contacted Conference Badge and requested copies of all our badges so that we could audit them. Next, we asked that all badge files and related information be destroyed, which we received confirmation of.

According to Conference Badge, *"NO logins, passwords, billing information or credit card information were included in the exposed data."*. No attendee information of this type has been shared with Conference Badge by DEFNA.

We verified that only basic attendee information, which included your full name and company name (if provided), was printed on the badges. Additionally, there was embedded QR code in our 2015 to 2018 badges, which included your full name, company name (if provided), and email address, which could be extracted. We stopped adding QR codes to our badges in 2019.

On behalf of DEFNA, we want to apologize to the community and make you aware that this vulnerability, albeit theoretical, existed and the steps that we went through to assess what information was available and to make sure that the badges were destroyed.

If you have any questions, please contact us at hello@djangocon.us.


