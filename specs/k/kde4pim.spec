
%add_findpackage_path %_kde4_bindir
%ifdef _kde_alternate_placement
%add_findreq_skiplist %_kde4_bindir/kmail_*.sh
%else
%add_findreq_skiplist %_K4bindir/kmail_*.sh
%endif

%def_disable kitchensync
%def_disable kpilot
%def_disable kmobiletools
%def_disable korn
%def_enable kjots
%def_enable ktnef

%define rname kdepim
%define major 4
%define minor 14
%define bugfix 10
Name: kde4pim
Version: %major.%minor.%bugfix
Release: alt7%ubt

Group: Graphical desktop/KDE
Summary: K Desktop Environment
License: GPL
Url: http://www.kde.org

Requires: kde4pim-environment
Requires: %name-common = %version-%release
Requires: %name-akonadi = %version-%release
Requires: %name-akregator = %version-%release
Requires: %name-blogilo = %version-%release
Requires: %name-kalarm = %version-%release
%if_enabled kitchensync
Requires: %name-kitchensync = %version-%release
%endif
%if_enabled kjots
Requires: %name-kjots = %version-%release
%endif
Requires: %name-kleopatra = %version-%release
Requires: %name-ksendemail = %version-%release
%if_enabled kmobiletools
Requires: %name-kmobiletools = %version-%release
%endif
Requires: %name-knode = %version-%release
Requires: %name-kontact = %version-%release
%if_enabled korn
Requires: %name-korn = %version-%release
%endif
%if_enabled kpilot
Requires: %name-kpilot = %version-%release
%endif
Requires: %name-kresources = %version-%release
Requires: %name-ktimetracker = %version-%release
%if_enabled ktnef
Requires: %name-ktnef = %version-%release
%endif



Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%rname-%version.tar
# FC
Patch1: kdepim-4.11.90-install_kleopatra_headers.patch
# ALT
Patch101: kdepim-4.0.80-alt-kmail-acctlocal-lock.patch
Patch102: kdepim-4.12.2-alt-nepomuk-warning.patch
Patch103: kdepim-4.7.1-alt-force-7bit-cte.patch
Patch104: kdepim-4.7.2-alt-migration.patch

# Automatically added by buildreq on Tue Feb 09 2010
#BuildRequires: akonadi-devel gcc-c++ glib2-devel kde4pimlibs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libassuan-devel libgpgme-devel libindicate-qt-devel libxkbfile-devel soprano soprano-backend-redland xorg-xf86vidmodeproto-devel xsltproc
BuildRequires(pre): kde4libs-devel libassuan-devel rpm-build-ubt
BuildRequires: akonadi-devel gcc-c++ glib2-devel kde4pimlibs-devel libgpgme-devel prison-devel qjson-devel
#BuildRequires: soprano soprano-backend-redland
BuildRequires: xsltproc grantlee-devel libsasl2-devel
#BuildRequires: dblatex
BuildRequires: kde4-pim-runtime-devel libkgapi-devel >= 2.2
BuildRequires: kde4-baloo-devel kde4-baloo-widgets-devel
#BuildRequires: libindicate-qt-devel
BuildRequires: liblink-grammar-devel

%if_enabled kitchensync
BuildRequires: libopensync-devel >= 0.30
%endif

BuildRequires: kde4libs-devel >= %version
BuildRequires: kde4pimlibs-devel >= %version
BuildRequires: kde4base-workspace-devel

%description
Information Management applications for the K Desktop Environment.
	- blogilo: Blogging client.
	- kaddressbook: The KDE addressbook application.
	- korganizer: a calendar-of-events and todo-list manager
	- kpilot: to sync with your PalmPilot
	- kalarm: gui for setting up personal alarm/reminder messages
	- kalarmd: personal alarm/reminder messages daemon, shared by
           korganizer and kalarm.
	- kaplan: A shell for the PIM apps, still experimental.
	- karm: Time tracker.
%if_enabled kitchensync
	- kitchensync: Synchronisation framework, still under heavy development.
%endif
	- kfile-plugins: vCard KFIleItem plugin.
%if_enabled kjots
	- kjots: manages several "books" with a subject and notes
%endif
	- knotes: yellow notes application
	- konsolecalendar: Command line tool for accessing calendar files.
	- kmail: universal mail client
	- kmailcvt: converst addressbooks to kmail format


%package common
Summary: Core files for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common >= %major.%minor
Conflicts: kdepim-common <= 1:3.5.12-alt1
%description common
Common package for  %name

%package core
Summary: Core files for %name
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
%description core
Core files for %name

%package environment-workstation
Summary: KDE PIM desktop applications
Group: Graphical desktop/KDE
BuildArch: noarch
Provides: kde4pim-environment = %version-%release
Requires: %name-kaddressbook
Requires: %name-kmail
Requires: %name-korganizer
Requires: %name-knotes
%description environment-workstation
KDE PIM desktop applications

%package environment-mobile
Summary: KDE PIM mobile applications
Group: Graphical desktop/KDE
BuildArch: noarch
Provides: kde4pim-environment = %version-%release
Requires: %name-kaddressbook-mobile
Requires: %name-kmail-mobile
Requires: %name-korganizer-mobile
Requires: %name-notes-mobile
Requires: %name-tasks-mobile
%description environment-mobile
KDE PIM mobile applications

%package blogilo
Summary: Blogging client for kde
Group: Graphical desktop/KDE
Requires: %name-core = %version-%release
%description blogilo
Blogilo is a blogging client for KDE, which supports famous blogging
APIs.

Its current features:
* A full featured WYSIWYG editor.
* An HTML editor with syntax highlighting.
* Previewing your post with your blog style! like when you are
visiting it at your blog.
* Support for Blogger1.0, MetaWeblog, MovableType (Wordpress supports
All of these!) and Google GData (used on Blogspot.com blogs) APIs!
* Support for Creating/Modifying/Deleting posts.
* Support for creating drafts and scheduled posts!
* Support for uploading media files to your blog (Just on supported
APIs e.g. MetaWeblog and MovableType)
* Support for uploading to FTP server.
* Support for Fetching your recent blog entries.
* Support for adding Images to post from your system. It will upload
them on Submitting post to blog (Just on supported APIs e.g.
MetaWeblog and MovableType)
* Support for saving local entries before publishing.
* Saving your writing copy to prevent data loss, at configurable
intervals.
* and ...

%package -n libkdepim4-copy
Summary: %name library
Group: System/Libraries
%description -n libkdepim4-copy
%name library

%package -n libcalendarsupportcollectionpage4
Summary: %name library
Group: System/Libraries
%description -n libcalendarsupportcollectionpage4
%name library

%package -n libkorganizer4_core
Summary: %name library
Group: System/Libraries
%description -n libkorganizer4_core
%name library

%package -n libgwsoap4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libgwsoap4
%name library

%package -n libkabcgroupwise4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkabcgroupwise4
%name library

%package -n libkcalgroupwise4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkcalgroupwise4
%name library

%package -n libkleopatraclientcore4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkleopatraclientcore4
%name library

%package -n libkleopatraclientgui4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkleopatraclientgui4
%name library

%package -n libkontactinterfaces4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkontactinterfaces4
%name library

%package -n libkschema4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkschema4
%name library

%package -n libkschemawidgets4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkschemawidgets4
%name library

%package -n libkxmlcommon4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkxmlcommon4
%name library

%package -n libschema4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libschema4
%name library

%package -n libwscl4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libwscl4
%name library

%package -n libwsdl4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libwsdl4
%name library

%package kjots
Summary: KDE notes books manager
Group: Graphical desktop/KDE
Requires: %name-common = %version-%release
Provides: kde4utils-kjots = %version-%release
Obsoletes: kde4utils-kjots < %version-%release
%description kjots
Manages several "books" with a subject and notes

%package -n libimap4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libimap4
%name library

%package -n libakonadi4-xml
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakonadi4-xml
%name library

%package -n libakonadi4_next
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakonadi4_next
%name library

%package -n libakonadi4_kabc
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakonadi4_kabc
%name library

%package -n libakonadi4_kcal
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakonadi4_kcal
%name library

%package -n libakonadi4_kabccommon
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakonadi4_kabccommon
%name library.

%package -n libkaddressbookprivate4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkaddressbookprivate4
%name library

%package -n libkontactprivate4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkontactprivate4
%name library

%package akonadi
Summary: KDE PIM storage framework
Group: Graphical desktop/KDE
Requires: %name-core = %version-%release
Requires: kde4-pim-runtime
%description akonadi
KDE PIM storage framework

%package -n libkdepim4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkdepim4
%name library

%package -n libkholidays4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkholidays4
%name library

%package -n libkpgp4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkpgp4
%name library

%package kleopatra
Summary: Certificate Manager for KDE
Group: Graphical desktop/KDE
Requires: %name-core = %version-%release
Requires: gnupg2 dirmngr pinentry-x11
%description kleopatra
Certificate Manager for KDE

%package -n libksieve4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libksieve4
%name library

%package -n libmimelib4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libmimelib4
%name library

%package -n libakregatorinterfaces4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakregatorinterfaces4
%name library

%package -n libakregatorprivate4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakregatorprivate4
%name library

%package akregator
Summary: RSS/Atom feed reader for KDE
Group: Networking/News
Requires: %name-core = %version-%release
%description akregator
RSS/Atom feed reader for KDE

%package -n libkitchensyncprivate4
Summary: %name library
Group: System/Libraries
Requires: %name-core = %version-%release
%description -n libkitchensyncprivate4
%name library

%package -n libqopensync4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libqopensync4
%name library

%package kitchensync
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version-%release
%description kitchensync
Dialog KDE base widgets

%package -n libknodecommon4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libknodecommon4
%name library

%package knode
Summary: A newsgroup (NNTP) reader for KDE
Group: Networking/News
Requires: %name-core = %version-%release
Requires: kde4pimlibs
%description knode
A newsgroup (NNTP) reader for KDE

%package -n libkabinterfaces4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkabinterfaces4
%name library

%package kaddressbook
Summary: Addressbook for KDE
Group: Graphical desktop/KDE
Provides: kde4-kaddressbook = %version-%release
Requires: %name-core = %version-%release
Requires: akonadi kde4-pim-runtime %name-akonadi
%description kaddressbook
Addressbook for KDE

%package kaddressbook-mobile
Summary: Mobile addressbook for KDE
Group: Graphical desktop/KDE
Provides: kde4-kaddressbook = %version-%release
Requires: %name-core = %version-%release
Requires: akonadi kde4-pim-runtime %name-akonadi
%description kaddressbook-mobile
Mobile addressbook for KDE

%package -n libkalarm4_resources
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkalarm4_resources
%name library

%package -n libkmtaddressbook4_service
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkmtaddressbook4_service
%name library

%package kalarm
Summary: Personal Alarm Scheduler
Group: Graphical desktop/KDE
Requires: %name-core = %version-%release
%description kalarm
Personal Alarm Scheduler

%package ktimetracker
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %version-%release
%description ktimetracker
KTimeTracker is an application that allows you to track how much time
you spent on various tasks. When you start a new task, you start a timer for it.
At the end of the day, you can see how much time you spent on various task.

%package -n libkmailprivate4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkmailprivate4
%name library

%package ksendemail
Summary: %{name} ksendemail
Group: Networking/Mail
Requires: %name-core = %version-%release
%description ksendemail
%{name} ksendemail

%package kmail
Summary: A mail client for KDE
Group: Networking/Mail
URL: http://userbase.kde.org/KMail
Requires: %name-core = %version-%release
Requires: %name-kmail-common = %version-%release
Requires: kde4pimlibs akonadi kde4-pim-runtime %name-akonadi
Provides: %name-plugins = %version-%release
Obsoletes: %name-plugins = %version-%release
%description kmail
A mail client for KDE

%package kmail-mobile
Summary: A mobile mail client for KDE
Group: Networking/Mail
URL: http://userbase.kde.org/KMail
Requires: %name-core = %version-%release
Requires: %name-kmail-common = %version-%release
Requires: kde4pimlibs akonadi kde4-pim-runtime %name-akonadi
%description kmail-mobile
A mobile mail client for KDE

%package kmail-common
Summary: Common support for KMail
Group: Graphical desktop/KDE
URL: http://userbase.kde.org/KMail
%description kmail-common
Common files needed by kmail and kmail-mobile used to view messages.

%package kmailcvt
Summary: The KDE Mail Import tool
Group: Graphical desktop/KDE
Requires: %name-core = %version-%release
%description kmailcvt
KMailCVT communicates with KMail via its DCOP interface to add messages

%package knotes
Summary: Post-It notes on the KDE desktop
Group: Graphical desktop/KDE
Requires: %name-core = %version-%release
Requires: %name-kresources
Requires: akonadi kde4-pim-runtime %name-akonadi
%description knotes
Post-It notes on the desktop

%package notes-mobile
Summary: Post-It notes on the mobile KDE desktop
Group: Graphical desktop/KDE
Requires: %name-core = %version-%release
Requires: %name-kresources
Requires: akonadi kde4-pim-runtime %name-akonadi
%description notes-mobile
Post-It notes on the mobile desktop

%package -n libkpinterfaces4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkpinterfaces4
%name library

%package kontact
Summary: Integrated solution to your KDE PIM
Group: Graphical desktop/KDE
Requires: %name-core = %version-%release
Requires: akonadi kde4-pim-runtime %name-akonadi
%description kontact
Integrated solution to your KDE PIM

%package -n libkocorehelper4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkocorehelper4
%name library

%package -n libkorg4_stdprinting
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkorg4_stdprinting
%name library

%package -n libkorganizer4_calendar
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkorganizer4_calendar
%name library

%package -n libkorganizer4_eventviewer
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkorganizer4_eventviewer
%name library

%package -n libkorganizer4_interfaces
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkorganizer4_interfaces
%name library

%package korganizer
Summary: Electronic organizer for KDE
Group: Graphical desktop/KDE
Requires: %name-core = %version-%release
Requires: %name-kresources
Requires: akonadi kde4-pim-runtime %name-akonadi
%description korganizer
Electronic organizer for KDE

%package korganizer-mobile
Summary: Electronic mobile organizer for KDE
Group: Graphical desktop/KDE
Requires: %name-core = %version-%release
Requires: %name-kresources
Requires: akonadi kde4-pim-runtime %name-akonadi
%description korganizer-mobile
Electronic mobile organizer for KDE

%package tasks-mobile
Summary: Mobile Kontact Touch Tasks
Group: Graphical desktop/KDE
Requires: %name-core = %version-%release
Requires: %name-kresources
%description tasks-mobile
Mobile Kontact Touch Tasks

%package -n libkorganizerprivate4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkorganizerprivate4
%name library

%package -n libkmobiletoolsengineui4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkmobiletoolsengineui4
%name library

%package kmobiletools
Summary: Control mobile phones from KDE
Group: Communications
Requires: %name-core = %version-%release
Conflicts: kmobiletools < 0.4.3.3-alt2
%description kmobiletools
Control mobile phones from KDE

%package korn
Summary: Multi-folder new mail monitor for KDE
Group: Networking/Mail
Requires: %name-core = %version-%release
%description korn
Multi-folder new mail monitor for KDE

%package -n libkpilot4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkpilot4
%name library

%package kpilot
Summary: Synchronizing data with a Palm(tm) or compatible PDA
Group: Communications
Requires: %name-core = %version-%release
%description kpilot
Synchronizing data with a Palm(tm) or compatible PDA

%package -n libkabc4_groupdav
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkabc4_groupdav
%name library

%package -n libkabc4_slox
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkabc4_slox
%name library

%package -n libkabc4_xmlrpc
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkabc4_xmlrpc
%name library

%package -n libkabckolab4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkabckolab4
%name library

%package -n libkcal4_groupdav
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkcal4_groupdav
%name library

%package -n libkcal4_resourceblog
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkcal4_resourceblog
%name library

%package -n libkcal4_resourceremote
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkcal4_resourceremote
%name library

%package -n libkcal4_slox
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkcal4_slox
%name library

%package -n libkcal4_xmlrpc
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkcal4_xmlrpc
%name library

%package -n libkcalkolab4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkcalkolab4
%name library

%package -n libkgroupwarebase4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkgroupwarebase4
%name library

%package -n libkgroupwaredav4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkgroupwaredav4
%name library

%package -n libknotes4_xmlrpc
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libknotes4_xmlrpc
%name library

%package -n libknoteskolab4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libknoteskolab4
%name library

%package -n libkslox4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkslox4
%name library

%package -n libkabcommon4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkabcommon4
%name library

%package -n libkcal4_resourcefeatureplan
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkcal4_resourcefeatureplan
%name library

%package -n libkfeed4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkfeed4
%name library

%package -n libkleo4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkleo4
%name library

%package -n libkmobiletoolslib4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkmobiletoolslib4
%name library

%package kresources
Summary: KDE kresources
Group: Graphical desktop/KDE
Requires: %name-core = %version-%release
%description kresources
KDE kresources

%package ktnef
Summary: TNEF File Viewer
Group: Networking/Mail
Requires: %name-core = %version-%release
%description ktnef
TNEF File Viewer

%package wizards
Summary: KDE PIM wizards
Group: Graphical desktop/KDE
Requires: %name-core = %version-%release
%description wizards
KDE PIM wizards

%package -n libmaildir4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libmaildir4
%name library

%package -n libkabcscalix4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkabcscalix4
%name library

%package -n libkcalscalix4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkcalscalix4
%name library

%package -n libknotesscalix4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libknotesscalix4
%name library

%package -n libakonadi4-kcal_next
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakonadi4-kcal_next
%name library

%package -n libkalarm4_calendar
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkalarm4_calendar
%name library

%package -n libmbox4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libmbox4
%name library

%package -n libmessagecore4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libmessagecore4
%name library

%package -n libmessagelist4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libmessagelist4
%name library

%package -n libmessageviewer4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libmessageviewer4
%name library

%package -n libmessagecomposer4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libmessagecomposer4
%name library

%package -n libakonadi4-filestore
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libakonadi4-filestore
%name library

%package -n libcalendarsupport4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libcalendarsupport4
%name library

%package -n libeventviews4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libeventviews4
%name library

%package -n libincidenceeditorsng4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libincidenceeditorsng4
%name library

%package -n libincidenceeditorsngmobile4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libincidenceeditorsngmobile4
%name library

%package -n libkdepimdbusinterfaces4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkdepimdbusinterfaces4
%name library

%package -n libkdepimmobileui4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkdepimmobileui4
%name library

%package -n libkdgantt24
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkdgantt24
%name library

%package -n libkmanagesieve4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkmanagesieve4
%name library

%package -n libkmindexreader4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkmindexreader4
%name library

%package -n libksieveui4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libksieveui4
%name library

%package -n libmailimporter4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libmailimporter4
%name library

%package -n libmailcommon4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libmailcommon4
%name library

%package -n libtemplateparser4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libtemplateparser4
%name library

%package -n libpimcommon4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libpimcommon4
%name library

%package  -n libcomposereditorng4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libcomposereditorng4
%name library

%package  -n libgrammar4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libgrammar4
%name library

%package  -n libpimactivity4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libpimactivity4
%name library

%package  -n libsendlater4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libsendlater4
%name library

%package  -n libfolderarchive4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libfolderarchive4
%name library

%package  -n libgrantleetheme4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libgrantleetheme4
%name library

%package  -n libgrantleethemeeditor4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libgrantleethemeeditor4
%name library

%package  -n libkaddressbookgrantlee4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkaddressbookgrantlee4
%name library

%package  -n libknotesprivate4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libknotesprivate4
%name library

%package  -n libnoteshared4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libnoteshared4
%name library

%package  -n libfollowupreminder4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libfollowupreminder4
%name library

%package  -n libpimsettingexporterprivate4
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libpimsettingexporterprivate4
%name library

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: %name-common = %version-%release
Requires: kde4libs-devel kde4-pim-runtime-devel
%description devel
This package contains header files needed if you wish to build applications
based on kdepim.


%prep
%setup -q -n %rname-%version
%patch1 -p1
###%patch101 -p1
#%patch102 -p1
#%patch103 -p1
#%patch104 -p1


%build
%K4build \
    -DKDE4_BUILD_TESTS=OFF \
    -DKDE4_ENABLE_FPIE:BOOL=ON \
    -DKDEPIM_BUILD_DESKTOP:BOOL=ON \
    -DKDEPIM_BUILD_MOBILE:BOOL=ON \
    -DAKONADI_INSTALL_PREFIX:STRING=%_prefix
#    -DKDE4_ENABLE_FINAL:BOOL=ON \

%install
%K4install

# move icons
if [ -d %buildroot/%_K4iconsdir/oxygen -a ! -d %buildroot/%_kde4_iconsdir/oxygen ] ; then
    mkdir -p %buildroot/%_kde4_iconsdir
    mv %buildroot/%_K4iconsdir/oxygen %buildroot/%_kde4_iconsdir/
fi

%files
%files environment-workstation
%files environment-mobile
%files common
%dir %_K4apps/libkleopatra/
#%_datadir/ontology/kde/*
%_K4conf/ksieve_script.knsrc

%files core
%_K4bindir/mboximporter
%_K4xdg_apps/mboximporter.desktop
#
%_K4bindir/contactthemeeditor
%_K4apps/contactthemeeditor/
%_K4xdg_apps/contactthemeeditor.desktop
%_K4doc/en/contactthemeeditor/
#
%_K4bindir/calendarjanitor
%_K4bindir/kabc2mutt
%_K4bindir/kabcclient
%_K4bindir/konsolekalendar
%_K4bindir/pimsettingexporter
%_K4bindir/storageservicemanager
#%_K4lib/kcm_pimactivity.so
#%_K4lib/grammar_link.so
%_K4lib//plugins/grantlee/
#%_K4libdir/strigi/*
%_K4apps/composereditor/
%_K4apps/pimsettingexporter/
%_K4apps/storageservicemanager/
%_K4conf/messageviewer_header_themes.knsrc
%_K4conf_update/grantleetheme.upd
%_K4xdg_apps/konsolekalendar.desktop
%_K4xdg_apps/pimsettingexporter.desktop
%_K4xdg_apps/storageservicemanager.desktop
%_K4iconsdir/locolor/*/*/*
%_K4iconsdir/hicolor/*/*/*
%_kde4_iconsdir/oxygen/*/*/*
%_K4srv/kontact/
#%_K4srv/kcmpimactivity.desktop
#%_K4srv/grammar_link.desktop
%_K4doc/en/konsolekalendar
%_K4doc/en/kabcclient
%_K4doc/en/pimsettingexporter/
#  runtime
%_K4dbus_system/org.kde.kalarmrtcwake.conf
%_K4exec/kalarm_helper
%_K4dbus_sys_services/org.kde.kalarmrtcwake.service
%_datadir/polkit-1/actions/org.kde.kalarmrtcwake.policy
#
%_K4bindir/headerthemeeditor
%_K4xdg_apps/headerthemeeditor.desktop
%_K4apps/headerthemeeditor/
%_K4doc/en/headerthemeeditor/
#  mobile
%dir %_K4lib/imports/
%dir %_K4lib/imports/org
%_K4lib/imports/org/kde
%_K4apps/mobileui/

%files kaddressbook-mobile
%_K4bindir/kaddressbook-mobile
%_K4xdg_apps/kaddressbook-mobile.desktop
%_K4apps/kaddressbook-mobile/

%files kmail-mobile
%_K4bindir/kmail-mobile
%_K4xdg_apps/kmail-mobile.desktop
%_K4apps/kmail-mobile/

%files korganizer-mobile
%_K4bindir/korganizer-mobile
%_K4xdg_apps/korganizer-mobile.desktop
%_K4apps/korganizer-mobile/

%files notes-mobile
%_K4bindir/notes-mobile
%_K4xdg_apps/notes-mobile.desktop
%_K4apps/notes-mobile/

%files tasks-mobile
%_K4bindir/tasks-mobile
%_K4xdg_apps/tasks-mobile.desktop
%_K4apps/tasks-mobile/

%files -n libmbox4
%_K4libdir/libmessagecore.so.*
%files -n libmessagelist4
%_K4libdir/libmessagelist.so.*
%files -n libmessageviewer4
%_K4plug/accessible/messagevieweraccessiblewidgetfactory.so
%_K4libdir/libmessageviewer.so.*
%files -n libmessagecomposer4
%_K4libdir/libmessagecomposer.so.*

%files blogilo
%_K4bindir/blogilo
%_K4xdg_apps/blogilo.desktop
%_K4apps/blogilo
%_K4cfg/blogilo.kcfg
%_K4doc/*/blogilo

%files -n libkorganizer4_core
%_K4libdir/libkorganizer_core.so.*

%files -n libkleopatraclientcore4
%_K4libdir/libkleopatraclientcore.so.*

%files -n libkleopatraclientgui4
%_K4libdir/libkleopatraclientgui.so.*

%if_enabled kjots
%files kjots
%_K4bindir/kjots
#%_K4bindir/kjotsmigrator
%_K4lib/kjotspart.so
%_K4lib/kontact_kjotsplugin.so
%_K4lib/kcm_kjots.so
%_K4lib/plasma_applet_akonotes_*.so
%_K4apps/kjots/
%_K4apps/kontact/ksettingsdialog/kjots.setdlg
%_K4apps/desktoptheme/default/widgets/stickynote.svgz
%_K4xdg_apps/Kjots.desktop
%_K4srv/akonotes_*.desktop
%_K4srv/kjotspart.desktop
%_K4srv/kjots_config_*.desktop
%_K4cfg/kjots.kcfg
%_K4doc/*/kjots
%endif

%files -n libakonadi4_next
%_K4libdir/libakonadi_next.so.*

%files -n libkaddressbookprivate4
%_K4libdir/libkaddressbookprivate.so.*

%files -n libkontactprivate4
%_K4libdir/libkontactprivate.so.*

%files akonadi
%_K4bindir/akonadi_*_agent
%_K4bindir/akonadiconsole
%_datadir/akonadi/
%_K4apps/akonadiconsole/
%_K4apps/akonadi_*_agent/
%_K4xdg_apps/akonadiconsole.desktop
%_K4conf_update/mailfilteragent.upd
%_K4conf_update/migrate-kmail-filters.pl
%_K4doc/en/akonadi_*_agent/

%files -n libkdepim4
%_K4libdir/libkdepim.so.*

%files -n libkpgp4
%_K4libdir/libkpgp.so.*
%_K4conf_update/kpgp-3.1-upgrade-address-data.pl
%_K4conf_update/kpgp.upd

%files kleopatra
%_K4bindir/kleopatra
%_K4bindir/kgpgconf
%_K4bindir/kwatchgnupg
%_K4conf/libkleopatrarc
%_K4xdg_apps/kleopatra_import.desktop
%_K4xdg_apps/kleopatra.desktop
%_K4apps/kleopatra
%_K4apps/kwatchgnupg
%_K4srv/kleopatra_config_*
%_K4srv/kleopatra_decrypt*.desktop
%_K4srv/kleopatra_sign*.desktop
%_K4lib/kcm_kleopatra.so
%doc %_K4doc/*/kleopatra
%doc %_K4doc/*/kwatchgnupg

%files -n libksieve4
%_K4libdir/libksieve.so.*

#%files -n libmimelib4
#%_K4libdir/libmimelib.so.*

%files -n libakregatorinterfaces4
%_K4libdir/libakregatorinterfaces.so.*

%files -n libakregatorprivate4
%_K4libdir/libakregatorprivate.so.*

%files akregator
%_K4bindir/akregator
%_K4bindir/akregatorstorageexporter
%_K4xdg_apps/akregator.desktop
%_K4lib/akregator*
%_K4lib/kontact_akregatorplugin.so
%_K4apps/akregator/
%_K4apps/akregator_sharemicroblog_plugin/
%_K4apps/kontact/ksettingsdialog/akregator.setdlg
%_K4cfg/akregator.kcfg
%_K4srv/akregator_*
%_K4srv/feed.protocol
%_K4srvtyp/akregator_plugin.desktop
%doc %_K4doc/en/akregator


%if_enabled kitchensync
%files -n libqopensync4
%_K4libdir/libqopensync.so.*
%files -n libkitchensyncprivate4
%_K4libdir/libkitchensyncprivate.so.*
%files kitchensync
%_K4bindir/kitchensync
%_K4xdg_apps/kitchensync.desktop
%_K4apps/kitchensync
%_K4lib/kitchensyncpart.so
%endif

%files -n libknodecommon4
%_K4libdir/libknodecommon.so.*

%files knode
%_K4bindir/knode
%_K4lib/kcm_knode.so
%_K4lib/knodepart.so
%_K4lib/kontact_knodeplugin.so
%_K4apps/knode
%_K4apps/kontact/ksettingsdialog/knode.setdlg
%_K4apps/kconf_update/knode.upd
#%_K4srv/knewsservice.protocol
%_K4srv/knode_config_accounts.desktop
%_K4srv/knode_config_appearance.desktop
%_K4srv/knode_config_cleanup.desktop
%_K4srv/knode_config_identity.desktop
%_K4srv/knode_config_post_news.desktop
%_K4srv/knode_config_privacy.desktop
%_K4srv/knode_config_read_news.desktop
%_K4xdg_apps/KNode.desktop
%_K4doc/en/knode
#%_K4doc/en/kioslave/news

%files kaddressbook
%_K4bindir/kaddressbook
%_K4xdg_apps/kaddressbook.desktop
%_K4xdg_apps/kaddressbook-importer.desktop
%_K4lib/kaddressbookpart.so
%_K4lib/kontact_kaddressbookplugin.so
%_K4lib/kcm_ldap.so
%_libdir/akonadi/contact/editorpageplugins/cryptopageplugin.so
%_K4conf/kaddressbook_themes.knsrc
%_K4apps/kaddressbook
%_K4apps/kontact/ksettingsdialog/kaddressbook.setdlg
%_K4srv/kaddressbookpart.desktop
%_K4srv/kcmldap.desktop

%files kalarm
%_K4bindir/kalarm
%_K4bindir/kalarmautostart
%_K4xdg_apps/kalarm.desktop
%_K4start/kalarm.autostart.desktop
%_K4apps/kalarm
%_K4conf_update/kalarm-*.pl
%_K4conf_update/kalarm.upd
%_K4cfg/kalarmconfig.kcfg
%_K4doc/en/kalarm

%files ktimetracker
%_K4bindir/karm
%_K4bindir/ktimetracker
%_K4lib/ktimetrackerpart.so
%_K4lib/kcm_ktimetracker.so
#%_K4lib/kontact_ktimetrackerplugin.so
%_K4xdg_apps/ktimetracker.desktop
%_K4apps/ktimetracker
#%_K4apps/kontact/ksettingsdialog/ktimetracker.setdlg
#%_K4apps/kontact/ktimetrackerui.rc
%_K4srv/ktimetracker_config_*.desktop
%_K4srv/ktimetrackerpart.desktop
%_K4doc/en/ktimetracker/

%files -n libkmailprivate4
%_K4libdir/libkmailprivate.so.*
%files -n libmailimporter4
%_K4libdir/libmailimporter.so.*

%files ksendemail
%_K4bindir/ksendemail

%files kmail
%_K4bindir/kmail
%_K4bindir/kmail_antivir.sh
%_K4bindir/kmail_clamav.sh
%_K4bindir/kmail_fprot.sh
%_K4bindir/kmail_sav.sh
%_K4bindir/sieveeditor
%_K4lib/kcm_kmail.so
%_K4lib/kmailpart.so
%_K4lib/kontact_kmailplugin.so
%_K4lib/ktexteditorkabcbridge.so
%_K4xdg_apps/KMail2.desktop
%_K4xdg_apps/kmail_view.desktop
%_K4xdg_apps/sieveeditor.desktop
%_K4conf_update/kmail*
%_K4conf_update/upgrade-signature.pl
%_K4conf_update/upgrade-transport.pl
#%_K4apps/kmail/
%_K4apps/kmail2/
%_K4apps/kontact/ksettingsdialog/kmail.setdlg
%_K4apps/sieve/
%_K4apps/sieveeditor/
%_K4cfg/customtemplates_kfg.kcfg
%_K4cfg/kmail.kcfg
#%_K4cfg/replyphrases.kcfg
%_K4cfg/templatesconfiguration_kfg.kcfg
%_K4conf/kmail.antispamrc
%_K4conf/kmail.antivirusrc
%_K4srv/kmail_config_accounts.desktop
%_K4srv/kmail_config_appearance.desktop
%_K4srv/kmail_config_composer.desktop
%_K4srv/kmail_config_identity.desktop
%_K4srv/kmail_config_misc.desktop
%_K4srv/kmail_config_security.desktop
%_K4srv/ServiceMenus/kmail_addattachmentservicemenu.desktop
%_K4srvtyp/dbusmail.desktop
%_K4doc/en/kmail
%_K4doc/en/sieveeditor/
#
%_K4bindir/kmailcvt
%_K4apps/kmailcvt/
%_K4doc/en/kmailcvt/
#
%_K4bindir/importwizard
%_K4xdg_apps/importwizard.desktop
%_K4doc/en/importwizard/

%files kmail-common
%_K4lib/messageviewer_bodypartformatter_application_mstnef.so
%_K4lib/messageviewer_bodypartformatter_text_calendar.so
%_K4lib/messageviewer_bodypartformatter_text_vcard.so
%_K4lib/messageviewer_bodypartformatter_text_xdiff.so
%_K4lib/kcm_kpimidentities.so
%_K4srv/kcm_kpimidentities.desktop
%_K4apps/libmessageviewer
%_K4apps/messageviewer
%_K4apps/messagelist

%files knotes
%_K4bindir/knotes
%_K4lib/kontact_knotesplugin.so
#%_K4lib/knotes_local.so
%_K4lib/kcm_knotessummary.so
%_K4lib/kcm_knote.so
#%_K4lib/knotes_scalix.so
%_K4xdg_apps/knotes.desktop
%_K4conf/knotes_printing_theme.knsrc
#%_K4cfg/knoteconfig.kcfg
%_K4cfg/knotesglobalconfig.kcfg
%_K4apps/kconf_update/noteglobalsettings.upd
%_K4apps/knotes/
%_K4apps/kontact/ksettingsdialog/knotes.setdlg
#%_K4srv/kresources/knotes/local.desktop
#%_K4srv/kresources/knotes_manager.desktop
%_K4srv/knote_config_*.desktop
%_K4srv/kcmknotessummary.desktop
%_K4doc/en/knotes

#%files -n libkpinterfaces4
#%_K4libdir/libkpinterfaces.so.*

%files kontact
%_K4bindir/kontact
%_K4xdg_apps/Kontact.desktop
%_K4xdg_apps/kontact-admin.desktop
#%_K4apps/knotes/knotes_part.rc
%dir %_K4apps/kontact
%dir %_K4apps/kontact/ksettingsdialog/
%_K4apps/kontact/about/
#%_K4apps/kontact/kontact.setdlg
%_K4apps/kontact/kontactui.rc
%_K4apps/kontactsummary/kontactsummary_part.rc
%_K4cfg/kontact.kcfg
%_K4srv/kontactconfig.desktop
%_K4srv/kcmapptsummary.desktop
%_K4srv/kcmkmailsummary.desktop
%_K4srv/kcmkontactsummary.desktop
%_K4srv/kcmsdsummary.desktop
%_K4srv/kcmtodosummary.desktop
#%_K4srvtyp/kontactplugin.desktop
%_K4lib/kcm_apptsummary.so
%_K4lib/kcm_kmailsummary.so
%_K4lib/kcm_kontact.so
%_K4lib/kcm_kontactsummary.so
%_K4lib/kcm_sdsummary.so
%_K4lib/kcm_todosummary.so
%_K4lib/kontact_specialdatesplugin.so
%_K4apps/kontact/ksettingsdialog/summary.setdlg
%_K4apps/kontact/ksettingsdialog/specialdates.setdlg
%_K4lib/kontact_summaryplugin.so
%_K4lib/kontact_journalplugin.so
%_K4doc/*/kontact
%_K4doc/*/kontact-admin
# mobile
%_K4apps/kontact-touch/

#%files -n libkocorehelper4
#%_K4libdir/libkocorehelper.so.*

#%files -n libkorg4_stdprinting
#%_K4libdir/libkorg_stdprinting.so.*

#%files -n libkorganizer4_calendar
#%_K4libdir/libkorganizer_calendar.so.*

#%files -n libkorganizer4_eventviewer
#%_K4libdir/libkorganizer_eventviewer.so.*

%files -n libkorganizer4_interfaces
%_K4libdir/libkorganizer_interfaces.so.*

%files korganizer
%_K4bindir/ical2vcal
%_K4bindir/korgac
#%_K4bindir/thememain
%_K4bindir/korganizer
%_K4bindir/kincidenceeditor
%_K4lib/kcm_korganizer.so
%_K4lib/korg_*
%_K4lib/korganizerpart.so
%_K4lib/kontact_korganizerplugin.so
%_K4lib/kontact_todoplugin.so
#%_K4lib/kontact_specialdatesplugin.so
%_K4conf_update/korganizer.upd
%_K4apps/korgac
%_K4apps/korganizer
%_K4apps/kontact/ksettingsdialog/korganizer.setdlg
#%_K4apps/kontact/ksettingsdialog/specialdates.setdlg
%_K4start/korgac.desktop
%_K4cfg/korganizer.kcfg
#%_K4cfg/todosettings.kcfg
#%_K4cfg/calendarsettings.kcfg
%_K4conf/korganizer.knsrc
%_K4srv/korganizer*
%_K4srv/webcal.protocol
%_K4srvtyp/calendardecoration.desktop
%_K4srvtyp/calendarplugin.desktop
%_K4srvtyp/dbuscalendar.desktop
#%_K4srvtyp/korganizerpart.desktop
#%_K4srvtyp/korgprintplugin.desktop
%_K4xdg_apps/korganizer-import.desktop
%_K4xdg_apps/korganizer.desktop
%doc %_K4doc/*/korganizer

%files -n libkorganizerprivate4
%_K4libdir/libkorganizerprivate.so.*

%if_enabled kmobiletools
%files -n libkmtaddressbook4_service
%_K4libdir/libkmtaddressbook_service.so.*
%files -n libkmobiletoolsengineui4
%_K4libdir/libkmobiletoolsengineui.so.*
%files -n libkmobiletoolslib4
%_K4libdir/libkmobiletoolslib.so.*
%files kmobiletools
%_K4bindir/kmobiletools
%_K4xdg_apps/kmobiletools.desktop
%_K4apps/akonadi/plugins/serializer/akonadi_serializer_sms.desktop
%_K4apps/kmobiletools
%_K4cfg/kmobiletools_devices.kcfg
%_K4srv/kmobiletools_mainpart.desktop
%_K4srv/fake_engine.desktop
%_K4srvtyp/kmobile*
%_K4lib/kmobiletools*
%_K4doc/en/kmobiletools
%endif

%if_enabled korn
%files korn
%_K4bindir/korn
%_K4xdg_apps/KOrn.desktop
%_K4conf_update/korn*
%_K4doc/en/korn
%endif

%if_enabled kpilot
%files -n libkpilot4
%_K4libdir/libkpilot.so.*
%files kpilot
%_K4bindir/kpilot
%_K4bindir/kpilotDaemon
%_K4libdir/libkpilot_conduit_base.so
%_K4libdir/libkpilot_akonadibase.so
%_K4lib/kcm_kpilot.so
%_K4lib/kpilot_*
%_K4xdg_apps/kpilot.desktop
%_K4xdg_apps/kpilotdaemon.desktop
%_K4conf_update/kpilot.upd
%_K4apps/kpilot/kpilotui.rc
%_K4cfg/kpilot.kcfg
%_K4cfg/kpilotlib.kcfg
%_K4cfg/memofileconduit.kcfg
#%_K4cfg/popmail.kcfg
%_K4cfg/timeconduit.kcfg
#%_K4cfg/vcalconduitbase.kcfg
#%_K4cfg/keyringconduit.kcfg
%_K4srv/kpilot_config.desktop
%_K4srv/*-conduit*
%_K4srv/time_conduit.desktop
%_K4srvtyp/kpilotconduit.desktop
%_K4doc/en/kpilot
%endif

%files -n libkcal4_resourceblog
%_K4libdir/libkcal_resourceblog.so.*
%files -n libkcal4_resourceremote
%_K4libdir/libkcal_resourceremote.so.*

%files -n libkleo4
%_K4libdir/libkleo.so.*
%_K4apps/libkleopatra/*

%files kresources
%_K4srv/kresources/kcal/remote.desktop
%_K4srv/kresources/kcal/blog.desktop
%_K4lib/kcal_*.so

%if_enabled ktnef
%files ktnef
%_K4bindir/ktnef
%_K4xdg_apps/ktnef.desktop
%_K4apps/ktnef
%_K4doc/en/ktnef
%endif

%files -n libcalendarsupport4
%_K4libdir/libcalendarsupport.so.*
%files -n libeventviews4
%_K4libdir/libeventviews.so.*
%files -n libincidenceeditorsng4
%_K4libdir/libincidenceeditorsng.so.*
%files -n libincidenceeditorsngmobile4
%_K4libdir/libincidenceeditorsngmobile.so.*
%files -n libkdepimdbusinterfaces4
%_K4libdir/libkdepimdbusinterfaces.so.*
%files -n libkdepimmobileui4
%_K4libdir/libkdepimmobileui.so.*
%files -n libkdgantt24
%_K4libdir/libkdgantt2.so.*
%files -n libkmanagesieve4
%_K4libdir/libkmanagesieve.so.*
%files -n libksieveui4
%_K4libdir/libksieveui.so.*
%files -n libmailcommon4
%_K4libdir/libmailcommon.so.*
%files -n libtemplateparser4
%_K4libdir/libtemplateparser.so.*
%files -n libpimcommon4
%_K4libdir/libpimcommon.so.*
%files -n libcomposereditorng4
%_K4libdir/libcomposereditorng.so.*
%files -n libsendlater4
%_K4libdir/libsendlater.so.*
%files -n libgrantleetheme4
%_K4libdir/libgrantleetheme.so.*
%files -n libgrantleethemeeditor4
%_K4libdir/libgrantleethemeeditor.so.*
%files -n libkaddressbookgrantlee4
%_K4libdir/libkaddressbookgrantlee.so.*
%files -n libknotesprivate4
%_K4libdir/libknotesprivate.so.*
%files -n libnoteshared4
%_K4libdir/libnoteshared.so.*
%files -n libfollowupreminder4
%_K4libdir/libfollowupreminder.so.*
%files -n libcalendarsupportcollectionpage4
%_K4libdir/libcalendarsupportcollectionpage.so.*
%files -n libpimsettingexporterprivate4
%_K4libdir/libpimsettingexporterprivate.so.*

%files devel
%_K4link/*.so
%_K4includedir/*
#%_K4apps/cmake/modules/*
%_K4apps/kdepimwidgets
%_K4lib/plugins/designer/*.so
%_K4dbus_interfaces/*

%changelog
* Fri Apr 20 2018 Sergey V Turchin <zerg@altlinux.org> 4.14.10-alt7%ubt
- rebuild with new gpgme

* Fri Mar 11 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.10-alt6
- update from 4.14 branch

* Fri Jan 29 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.10-alt5
- move oxygen icons to kde-specific place

* Mon Nov 16 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.10-alt4
- update from 4.14 branch

* Thu Oct 22 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.10-alt3
- update from upstream/KDE/4.14

* Fri Aug 28 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.10-alt2
- update from upstream/KDE/4.14

* Thu Jul 16 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.10-alt1
- new version

* Fri Jun 12 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.9-alt1
- new version

* Thu May 14 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.8-alt1
- new version

* Wed Apr 22 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.7-alt1
- new version

* Thu Mar 12 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.6-alt1
- new version

* Fri Feb 06 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.5-alt1
- new version

* Mon Jan 26 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.4-alt1
- new version

* Fri Nov 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt1
- new version

* Tue Oct 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.2-alt1
- new version

* Thu Sep 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.1-alt1
- new version

* Wed Aug 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Mon Jul 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.3-alt1
- new version

* Wed Jun 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.2-alt1
- new version

* Tue May 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.1-alt1
- new version

* Mon Apr 21 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Mon Mar 31 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.4-alt0.M70P.1
- built for M70P

* Fri Mar 28 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.4-alt1
- new version

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt0.M70P.1
- built for M70P

* Fri Mar 07 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.3-alt1
- new version

* Mon Feb 03 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt2
- install kleopatra headers

* Fri Jan 31 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- new version

* Wed Dec 18 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt1.M70P.2
- built for M70P

* Wed Dec 18 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt2
- update from 4.11 branch

* Thu Dec 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt0.M70P.1
- built for M70P

* Thu Dec 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.4-alt1
- new version

* Thu Nov 07 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt0.M70P.1
- built for M70P

* Thu Nov 07 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.3-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt0.M70P.1
- built for M70P

* Thu Oct 03 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.2-alt1
- new version

* Thu Sep 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Thu Jul 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt1
- new version

* Wed Jun 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.4-alt1
- new version

* Mon May 13 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.3-alt1
- new version

* Mon Apr 22 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt2
- remove nepomuk warning

* Mon Apr 08 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.2-alt1
- new version

* Thu Mar 21 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt2
- update from 4.10 branch

* Tue Mar 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.1-alt1
- new version

* Mon Feb 25 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt2
- update from 4.10 branch

* Fri Feb 01 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt1
- update from 4.10 branch

* Wed Jan 30 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.3
- update from 4.10 branch

* Fri Jan 11 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- update from 4.10 branch

* Tue Dec 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Thu Dec 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.4-alt1
- new version

* Mon Nov 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt1
- new version

* Mon Oct 15 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.2-alt1
- new version

* Mon Oct 01 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Tue Aug 28 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt1.M60P.1
- built for M60P

* Tue Aug 28 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt2
- update from 4.8 branch (kde bug 295484)

* Fri Aug 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt0.M60P.1
- built for M60P

* Thu Aug 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt1
- new version

* Wed Jun 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt2.M60P.1
- built for M60P

* Tue Jun 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt3
- update from 4.8 branch

* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1.M60P.1
- built for M60P

* Thu Jun 14 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt2
- update from 4.8 branch

* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Wed May 30 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt2.M60P.1
- build for M60P

* Tue May 22 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt3
- update from 4.8 branch

* Thu May 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1.M60P.1
- build for M60P

* Sat May 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt2
- update from 4.8 branch

* Wed May 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1.M60P.1
- built for M60P

* Mon Mar 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt2
- update from 4.8 branch

* Mon Mar 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Wed Feb 08 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt3
- update from 4.8 branch

* Tue Jan 31 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- update from 4.8 branch

* Fri Jan 20 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Tue Jan 17 2012 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt5.M60P.1
- built for M60P

* Tue Jan 17 2012 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt6
- update from 4.7 branch

* Thu Jan 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt4.M60P.1
- built for M60P

* Thu Jan 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt5
- fix creation of mixedmaildir(KMail folders) akonadi resource from UI
- update from 4.7 branch

* Wed Jan 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt3.M60P.1
- built for M60P

* Wed Jan 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt4
- set defaults for maildir and mixedmaildir akonadi resources

* Fri Dec 30 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt2.M60P.1
- built for M60P

* Wed Dec 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt3
- update from 4.7 branch

* Mon Dec 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1.M60P.1
- built for M60P

* Fri Dec 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt2
- update from 4.7 branch

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Fri Dec 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Thu Dec 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt5
- don't fail migration on empty mail accounts (ALT#26656)

* Wed Nov 30 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt4
- fix migrate pop3 passwords (ALT#26640)

* Sun Nov 27 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt2.M60P.1
- built for M60P

* Fri Nov 25 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt3
- update from 4.7 branch

* Thu Nov 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1.M60P.1
- built for M60P

* Wed Nov 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt2
- add upstream fixes against some crashes

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Sun Oct 30 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Fri Oct 21 2011 Sergey V Turchin <zerg at altlinux dot org> 4.7.2-alt5.M60T.1
- built for M60T

* Thu Oct 20 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt6
- fix akonadi mixedcollection waiting (ALT#26479)
- update from 4.7 branch

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt4.M60T.1
- built for M60T

* Mon Oct 17 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt5
- update from 4.7 branch

* Thu Oct 13 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt4
- fix kmail migration
- update from 4.7 branch

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt3
- update from 4.7 branch

* Fri Oct 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt2
- update from 4.7 branch
- show akonadi setup in systemsettings
- allow select akonadi sqlite driver

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Wed Sep 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt2
- remove "nepomuk disabled" notification
- update from 4.7 branch
- fix requires
- force 7bit content transfer encoding

* Tue Sep 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Wed Sep 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1.M60P.1
- built for M60P

* Wed Sep 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt2
- fix kleoparta startup crash

* Wed Jul 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Tue Jun 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Wed May 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- update from 4.4 branch

* Tue Apr 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- update from 4.4 branch

* Thu Mar 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt3
- update kdepim-runtime sources

* Sat Mar 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt2
- move to standart place

* Tue Mar 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- update from 4.4 branch

* Fri Jan 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- update from 4.4 branch

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- update from 4.4 branch

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- update from 4.4 branch

* Tue Nov 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- update from 4.4 branch

* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- update from 4.4 branch

* Mon Aug 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- update from 4.4 branch

* Wed Aug 04 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Tue Jun 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Sun May 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Fri Apr 23 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1.M51.1
- build for M51

* Fri Apr 23 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt2
- fix requires

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Mon Mar 29 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Mon Mar 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Thu Feb 18 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt2
- allow to hide "Nepomuk not running" error dialog

* Wed Feb 10 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Sun Feb 07 2010 Dmitry V. Levin <ldv@altlinux.org> 4.3.95-alt3
- Rebuilt with libassuan2.so.0.
- Updated build dependencies.

* Wed Feb 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt2
- built with new libassuan

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Wed Jan 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Mon Jan 11 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt2
- rebuilt with new gnokii

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Tue Dec 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Mon Nov 02 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Fri Oct 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Mon Aug 31 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Wed Aug 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Wed Jul 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Fri Jul 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Mon Jul 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt2
- update from branches/4.2

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Fri Jun 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Mon May 04 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Fri Apr 03 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Tue Mar 03 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Thu Jan 15 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version
- remove deprecated macroses from specfile

* Fri Nov 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Wed Oct 15 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt2
- rebuilt with new gnokii

* Tue Oct 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- new version

* Tue Sep 02 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.1-alt1
- new version

* Thu Jul 31 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.0-alt1
- new version

* Tue May 27 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.80-alt1
- 4.1 beta1

* Wed May 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.72-alt2
- built for Sisyphus

* Mon May 05 2008 Sergey V Turchin <zerg at altlinux dot org> 4.0.72-alt1
- initial build

