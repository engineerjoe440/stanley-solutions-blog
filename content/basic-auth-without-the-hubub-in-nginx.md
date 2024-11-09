Title: Basic Auth without the Hubub in NGINX
Date: 2024-11-08 20:49
Modified: 2024-11-08 20:49
Tags: auth, html, http, nginx, proxy
Category: development
Slug: basic-auth-without-the-hubub-in-nginx
Authors: Joe Stanley
Summary: Today I learned that it IS possible to make a relatively simple static site that has some automatic authentication built in to NGINX that will use a custom HTML file for the login page as opposed to the basic-auth prompt that gets so annoying.

Okay... As I write this, I'm falling asleep. Hah! So I'll make this quick.

I wanted a website that:

* was a static site (no ORM, database, etc.)
* had some basic authentication (yeah, BasicAuth is fine)
* had a custom login page with my own styled HTML/CSS

Now, I've known that NGINX allows users to configure basic auth for some time.
I've done that, before. But I didn't know how to get it to do the custom HTML in
conjunction with that. Here's what I did.

I set up a route that would allow any login, or static file to be served without
authentication.

```nginx
    location ~* ^/(login|css|fonts|img|js|404.html) {
        root /home/.../public/;         
    }
```

And I had the main part of the website set up to use basic auth. Even had the
`401` redirect in there to manage spitting users out in the right spot. But that
used the annoying "basic auth popup" that I was trying to avoid.

```nginx
    location / {
        root /home/.../public/;
        auth_basic "Restricted";
        auth_basic_user_file /home/.../.htpasswd;
        proxy_intercept_errors on;
        error_page 401  /login/;
    }
```

> What to do, what to do...

After I don't even know how much searching, it dawned on me that I could use an
`if` statement to do a redirect, and after a little more tweaking, and learning
how to "hack" together a logical "AND" between three `if` statements, I was able
to come up with this:

```nginx
    if ($http_authorization = "") {
        set $temp_cache 1;
    }
    if ($request_uri !~* ^/(login|css|fonts|img|js|404.html)) {
        set $temp_cache 1$temp_cache;
    }
    if ($temp_cache = 11) {
        return 302 https://$host/login/;
    }
```

If there's no authorization header and the request URI isn't the login or static
file, then set a redirect to the `/login` page. TADA!

```nginx
server {
    listen 443 ssl; # managed by Certbot
    server_name k3b4h.idaho4h.org;

    client_max_body_size 512M;
    client_body_timeout 300s;

    if ($http_authorization = "") {
        set $temp_cache 1;
    }
    if ($request_uri !~* ^/(login|css|fonts|img|js|404.html)) {
        set $temp_cache 1$temp_cache;
    }
    if ($temp_cache = 11) {
        return 302 https://$host/login/;
    }

    location / {
        root /home/.../public/;
        auth_basic "Restricted";
        auth_basic_user_file /home/.../.htpasswd;
        proxy_intercept_errors on;
        error_page 401  /login/;
    }

    location ~* ^/(login|css|fonts|img|js|404.html) {
        root /home/.../public/;         
    }


    ssl_certificate /etc/...fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/...privkey.pem; # managed by Certbot
}
```

Now... I've yet to get some javascript cobbled together to actually set the
authorization header. That's next, but I *think* that should be manageable.

> God, I hope so.

Good night!

## Update:

Dangit. That won't work at all. Seems that while it does everything that I want
in terms of the visual component, it won't let me actually set the authorization
header for the browser to retain it for subsequent navigation.

Maybe there's a workaround for it, but I haven't found one yet. I'll have to
keep thinking/looking.
