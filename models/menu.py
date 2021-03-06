# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('JBTUS'))
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

DEVELOPMENT_MENU = True


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------

def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------
    response.menu += [
        (T('Get Paid'), False, URL('worthit', 'default', 'index')),
        (T('Blog'), False, URL('blog', 'default', 'index')),
        (T('User Groups'), False, '#', [
            (T('Straight'), False, URL('default', 'straight_users' )),
            (T('Gay'), False, URL('default', 'gay_users')),
            (T('Bisexual'), False, URL('default', 'bi_users')),
        ]),
        (T('User Feed'), False, URL('feed', 'index')),
        (T('Inbox'), False, URL('default', 'my_messages')),
        (T('Chat Rooms'), False, URL('default', 'group_chat')),
        (T('Forum'), False, URL('default', 'forum')),
        (T('Upgrade'), False, URL('default', 'upgrade')),
        (T('This App'), False, '#', [
            (T('Contact Me'), False, URL('default', 'contact' )),
            (T('About'), False,
             URL('default', 'about' )),
            (T('Disclaimer'), False,
             URL( 'default', 'disclaimer' )),
            LI(_class="divider"),
            (T('Help'), False, URL('default', 'tips')),
        ]),
    ]


if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()
