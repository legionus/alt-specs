%define rname	exit_button_firefox
%define cid 	\{94B08592-E5B4-45ff-A0BE-C1D975458688\}
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		firefox-exit_button
Version:	0.4.3
Release:	alt2

Summary:	Toolbar button to exit Firefox.

License:	GPL
Group:		Networking/WWW
URL:		http://www.linnhe.net/firefox/extensions.html

Packager:	Sergey Shilov <hsv@altlinux.ru>
Source0:	exitbutton_ff.xpi


BuildArch:	noarch

BuildRequires(pre):	rpm-build-firefox
BuildRequires: 		unzip
Requires:		%firefox_name >= 2.0

%description 	
Exit Button Firefox plugin - adds a correspond button to Firefox toolbar.

%prep
%setup -c
subst 's/17\./24./' install.rdf

%install
mkdir -p %buildroot/%ciddir
cp -r * %buildroot/%ciddir

%files
%ciddir

%changelog
* Wed Oct 30 2013 Andrey Cherepanov <cas@altlinux.org> 0.4.3-alt2
- Adapt for Firefox 24.x

* Tue Dec 18 2012 Andrey Cherepanov <cas@altlinux.org> 0.4.3-alt1
- New version 0.4.3 compatible with Firefox 17.0

* Tue Oct 18 2011 Sergey Shilov <hsv@altlinux.org> 0.4.1-alt6
- Rebuild for Firefox 7.0

* Wed Aug 24 2011 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt5
- Rebuild for Firefox 6.0 

* Sun Jul 31 2011 Sergey Shilov <hsv@altlinux.org> 0.4.1-alt4
- Firefox 5.* comptibility fix.

* Sun May 1 2011 Sergey Shilov <hsv@altlinux.org> 0.4.1-alt3
- Initial build for Sisyphus.
