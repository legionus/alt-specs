%define rname	livejournal_addons
%define cid 	homo_nudus@livejournal.com
%define ciddir  %firefox_noarch_extensionsdir/%cid

Summary:	LiveJournal extensions for Firefox
Name:		%firefox_name-%rname
Version:	9.5
Release:	alt4
Source0:	http://vmb.ucoz.com/%rname-%version-fx.xpi
License:	MPL v1.1
Group:		Networking/WWW
URL:		https://addons.mozilla.org/ru/firefox/addon/4536/

BuildArch:      noarch
BuildRequires(pre):     rpm-build-firefox
BuildRequires:  unzip

%description
LJ addons

%prep
%setup -c
subst 's/maxVersion>8.0/maxVersion>24.*/g' install.rdf

%install
mkdir -p %buildroot/%ciddir
cp -r * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then
    [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Wed Oct 30 2013 Andrey Cherepanov <cas@altlinux.org> 9.5-alt4
- Adapt for Firefox 24.x

* Wed Dec 19 2012 Andrey Cherepanov <cas@altlinux.org> 9.5-alt3
- Adapt for Firefox 17.0

* Thu Jan 19 2012 Alexey Gladkov <legion@altlinux.ru> 9.5-alt2
- Rebuilt with firefox-9.0.1

* Thu Aug 04 2011 Alexey Gladkov <legion@altlinux.ru> 9.5-alt1
- New version (9.5).

* Tue Apr 05 2011 Mykola Grechukh <gns@altlinux.ru> 9.2-alt1
- new version

* Wed Jun 09 2010 Mykola Grechukh <gns@altlinux.ru> 9.0.1-alt1
- first build for ALT
