Name: notmuch-addrlookup
Version: 8
Release: alt2

Summary: Notmuch Address Lookup tool

Group: Office
License: MIT
Url: https://github.com/aperezdc/notmuch-addrlookup-c

Packager: Evgenii Terechkov <evg@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: glib2-devel libnotmuch-devel

%description
This is an address lookup tool similar to the addrlookup one found in
the (apparently unmaintained) Vala Notmuch binding, using the Notmuch
database as source.

The one and only feature is accepting a string as first argument, and
it will use the Notmuch database to output the names and e-mail
addresses of the people you have exchanged e-mails with, most used
ones first. This works neatly as address completer for the Notmuch
Emacs interface.

%prep
%setup
%patch -p1

%build
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
%make_build

%install
install -p -D -m 755 %name %buildroot%_bindir/%name

%files
%_bindir/%name
%doc README.md CHANGELOG.md

%changelog
* Wed Oct 25 2017 Terechkov Evgenii <evg@altlinux.org> 8-alt2
- v8-5-g99b4315

* Tue Aug 22 2017 Terechkov Evgenii <evg@altlinux.org> 8-alt1
- v8-4-g88f156d

* Tue Jul 19 2016 Terechkov Evgenii <evg@altlinux.org> 7-alt1
- 7

* Sun Jul 26 2015 Terechkov Evgenii <evg@altlinux.org> 5-alt1
- Initial build for ALT Linux Sisyphus
