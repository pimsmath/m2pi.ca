---
widget: contact
headless: true
active: true
weight: 130
title: Contact Us
# subtitle: |
#   If you'd like to stay up to date with M2PI, please consider joining the <a
#   href="http://eepurl.com/hF9Wnf">m2pi mailing list</a>. The list is used for
#   announcements related to M2PI as well as opportunities relevant to participants.
#   {{< button-dark
#     url="http://eepurl.com/hF9Wnf"
#     text="Subscribe to m2pi emails"
#   >}}

autolink: true

content:
  autolink: true

  email: help@pims.math.ca
  phone: +1 604 822 3922
  address:
    street: 4176-2207 Main Mall
    city: Vancouver
    region: BC
    postcode: V6T 1Z4
    country: Canada
  contact_links:
    - icon: twitter
      icon_pack: fab
      name: Twitter
      link: https://twitter.com/pimsmath

---
<p>If you'd like to stay up to date with M2PI, please consider joining the <a
href="http://eepurl.com/hF9Wnf">m2pi mailing list</a>. The list is used for
announcements related to M2PI as well as opportunities relevant to participants.
{{< button-dark
  url="http://eepurl.com/hF9Wnf"
  text="Subscribe to m2pi emails"
>}}


<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
<p>
If instead you have a question or are interested in participating as an industry
mentor or student participant, please complete this form.  </p>

<form name="contact" method="POST" data-netlify="true">
  <div class="form-group">
    <input type="text" class="form-control" id="contactName" aria-describedby="contactHelp" placeholder="Your name">
  </div>
  <div class="form-group">
    <input type="text" class="form-control" id="contactEmail" aria-describedby="contactHelp" placeholder="Your email">
  </div>
  <div class="form-group">
    <label for="roleSelect">Reason you are getting in touch:</label>
    <select class="form-control" id="roleSelect">
      <option selected disabled>Choose...</option>
      <option>I have a question</option>
      <option>I'm interested in participating as an Industry Mentor</option>
      <option>I'm interested in participating as a Trainee</option>
    </select>
  </div>
  <div class="form-group">
    <label for="contactMessage">Message</label>
    <textarea class="form-control" id="contactMessage" rows="3"></textarea>
  </div>
  <button type="submit" class="btn btn-primary">Send</button>
</form>

