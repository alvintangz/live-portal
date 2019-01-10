# Extending (Rough Notes)
If you are an individual who has the permission from all owners to extend, or use the code in this repository, this is for you. In here, there are some recommendations in order to extend the application, to provide better user experiences to all users, save space in the DB, fix vulnerabilities, and much more.

## All the ASIDEs
I have "ASIDE" comments in some of the code which recommends some changes. I could not make some of these changes as it would have required to start with fresh migrations, which was not easy to do with the application up and running already. Please take a look at them.

## Slugs
I would recommend having [slug fields](https://docs.djangoproject.com/en/2.1/ref/models/fields/#slugfield) for Rounds, Delegates, etc... models. Afterwards, I would change some of the views' slugs so that the urls would look better and consistent.

## URL Names
In the URLConf, I have written names that represents paths to view which look ugly. This could be changed for easier readability.

## Naming Conventions: Model Fields, Template Filenames, View Filenames, etc...
Look into changing some names to make it could be understandable for future developers. Rename "itenirary" to "itinerary" (misspelling).

## MVC
I haven't completely followed the MVC model. I have allowed some templates to do logical work. This shouldn't work this way, and should be changed. Since I was using generic views, it led me to do this. Look into how and what context should be passed through, and change the templates accordingly.

## Users
I would recommend somehow integrating Django Permissions and Groups, so that assigning which views are viewable to certain users would be easier (e.g. maybe you don't want to release the itenirary until later, this could help). Right now, everything is hardcoded and depends on if the User Type (e.g. Delegate) is a one-to-one relationship with User (the current user).

## Delegate Profile Pictures
Currently, delegates can upload their profile pictures but they will automatically be resized to 500px by 500px in RGB Format. This should change, to a much better experience for delegates (i.e. cropping before upload).

## Forms
I have hardcoded form fields in templates and in some of the objects that subclass admin.ModelForm so that the bootstrap styling could be implemented. Look into how this can be better implemented so that forms are open for automatic extension when new fields are added in models. Also, some form templates need to do a better job in terms of displaying errors for validation. You can look into the Django REST Framework so forms can be in ajax, if you'd like.

## Texts for Delegates
Allow delegates to opt-out of text message notifications.

## Users Password Change Bug
I found a bug with resetting the passwords of delegate, partner and judge users on the admin side. I never fixed it.

## Maximum File Size
I did not completely check for file sizes for all the forms on portal. Modify this.

## Ending off
Just play around with the application, especially the administrative side to see what you would change in terms of how models relate to each other, and 

<small>Written by Alvin Tang on 2019-01-06.</small>
