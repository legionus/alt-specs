%define _libexecdir %_prefix/libexec

%define api_ver 3.0
%def_enable python

Name: xed
Version: 2.0.1
Release: alt1

Summary: xed is a small and lightweight text editor.
License: GPLv2
Group: Editors
Url: https://github.com/linuxmint/xed

Source: %name-%version.tar

%define pkglibdir %_libdir/%name
%define pkgdatadir %_datadir/%name
%define pluginsdir %_libdir/%name/plugins

# From configure.ac
%define glib_ver 2.36.0
%define gtk_ver 3.10
%define gtksourceview_ver 3.10
%define enchant_ver 1.2.0

Requires: %name-data = %version-%release
Requires: dconf gnome-icon-theme gvfs zenity
%{?_enable_zeitgeist:Requires: zeitgeist}

Provides: typelib(Xed)

BuildPreReq: rpm-build-gnome >= 0.6

BuildPreReq: intltool >= 0.50.1
BuildRequires: yelp-tools xmllint itstool
BuildPreReq: gtk-doc >= 1.0
BuildPreReq: desktop-file-utils >= 0.22
BuildPreReq: libenchant-devel >= %enchant_ver
BuildPreReq: iso-codes-devel >= 0.35
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libgtksourceview3-devel >= %gtksourceview_ver
BuildRequires: meson
BuildRequires: libattr-devel gnome-common libxml2-devel libsoup-devel gsettings-desktop-schemas-devel
BuildRequires: libSM-devel
BuildRequires: libpeas-devel
BuildRequires: python3-dev
BuildRequires: libgtk+3-gir-devel
BuildRequires: libgtksourceview3-gir-devel
BuildRequires: libgspell-devel
BuildRequires: libxapps-devel

%description
xed is a small and lightweight text editor.

xed supports most standard editing features, plus several not found in your
average text editor (plugins being the most notable of these).

%package data
Summary: Arch independent files for xed
Group: Editors
BuildArch: noarch

%description data
This package provides noarch data needed for xed to work.

%package devel
Group: Development/C
Summary: Libraries needed to develop plugins for xed
Requires: %name = %version-%release
Requires: libgtksourceview-devel

%description devel
Libraries needed to develop plugins for xed.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

# additional mime types
desktop-file-install --dir %buildroot%_desktopdir \
	--add-mime-type=text/css \
	--add-mime-type=text/csv \
	--add-mime-type=text/english \
	--add-mime-type=text/plain \
	--add-mime-type=text/tab-separated-values \
	--add-mime-type=text/x-adasrc \
	--add-mime-type=text/x-bibtex \
	--add-mime-type=text/x-c++ \
	--add-mime-type=text/x-chdr \
	--add-mime-type=text/x-c++hdr \
	--add-mime-type=text/x-csharp \
	--add-mime-type=text/x-csrc \
	--add-mime-type=text/x-c++src \
	--add-mime-type=text/x-dsrc \
	--add-mime-type=text/x-fortran \
	--add-mime-type=text/x-gle \
	--add-mime-type=text/x-java \
	--add-mime-type=text/x-javascript \
	--add-mime-type=text/x-log \
	--add-mime-type=text/x-makefile \
	--add-mime-type=text/x-objcsrc \
	--add-mime-type=text/x-pascal \
	--add-mime-type=text/x-patch \
	--add-mime-type=text/x-perl \
	--add-mime-type=text/x-php \
	--add-mime-type=text/x-python \
	--add-mime-type=text/x-sql \
	--add-mime-type=text/x-sh \
	--add-mime-type=text/x-tcl \
	--add-mime-type=text/x-tex \
	%buildroot%_desktopdir/%name.desktop

rm -f %buildroot%_libdir/%name/*.la

%find_lang --with-gnome %name

%files
%_bindir/*
%dir %pkglibdir
%dir %pluginsdir
%pluginsdir/*
%_libdir/%name

%files data -f %name.lang
%pkgdatadir/
%_desktopdir/%name.desktop
%_mandir/man?/*
%config %_datadir/glib-2.0/schemas/*
%_datadir/metainfo/%name.appdata.xml
%_datadir/dbus-1/services/org.x.editor.*service
%doc README AUTHORS NEWS

%files devel
%_includedir/*
%_pkgconfigdir/*

%changelog
* Wed Dec 5 2018 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- New version

* Wed Nov 21 2018 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- New version

* Mon Jul 23 2018 Vladimir Didenko <cow@altlinux.org> 1.8.3-alt1
- New version

* Wed Jun 13 2018 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt1
- New version (1.8.1-2-g8c6125e)

* Mon May 7 2018 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt1
- New version

* Thu Nov 23 2017 Vladimir Didenko <cow@altlinux.org> 1.6.3-alt1
- New version

* Thu Aug 24 2017 Vladimir Didenko <cow@altlinux.org> 1.4.6-alt1
- New version

* Tue Jul 4 2017 Vladimir Didenko <cow@altlinux.org> 1.4.5-alt1
- New version

* Mon Jun 5 2017 Vladimir Didenko <cow@altlinux.org> 1.4.2-alt1
- 1.4.2-2-gc306c1b

* Thu May 18 2017 Vladimir Didenko <cow@altlinux.org> 1.4.1-alt1
- New version

* Wed Dec 14 2016 Vladimir Didenko <cow@altlinux.org> 1.2.2-alt1
- New version

* Sun Nov 13 2016 Vladimir Didenko <cow@altlinux.org> 1.2.1-alt1
- New version

* Tue May 26 2016 Vladimir Didenko <cow@altlinux.org> 1.0.5-alt1
- New version

* Thu Feb 25 2016 Vladimir Didenko <cow@altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus
