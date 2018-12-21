%define _name xfconf

%def_with perl

Name: lib%_name
Version: 4.13.6
Release: alt1

Summary: Hierarchical configuration system for Xfce
Summary (ru_RU.UTF-8): Система конфигурации Xfce
License: %gpl2only
Group: Graphical desktop/XFce
Url: https://www.xfce.org/
Packager: Xfce Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/xfce/xfconf
Source: %_name-%version.tar
Patch: %_name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

%define _unpackaged_files_terminate_build 1

Requires: dbus-tools-gui
BuildPreReq: rpm-build-xfce4 libxfce4util-devel xfce4-dev-tools
BuildRequires: libgio-devel libdbus-devel
%if_with perl
BuildPreReq: rpm-build-perl perl-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Glib-devel
%endif
BuildRequires: gtk-doc intltool

%description
Xfconf is a hierarchical (tree-like) configuration system where the
immediate child nodes of the root are called "channels".  All settings
beneath the channel nodes are called "properties".

%package devel
Summary: Development files for %name
Group: Development/C
PreReq: %name = %version-%release

%description devel
Header files for the %name library.

%package -n %_name-utils
Summary: Utils for Xfce configuration system
Group: Graphical desktop/XFce
PreReq: %name = %version-%release

%description -n %_name-utils
Xfconfd is a small daemon that handles storage and retrieval of settings, as well
as notifying interested applications about changes to settings. It doesn't require
a GUI, so it could even be used for command-line applications.

Xfconf-query might be one of the tools many users have been waiting on for years,
especially those hanging around in our IRC channel. Instead of having to guide new
users through several dialogs and windows, it is now possible to have every control
over your Xfce desktop at your fingertips. You can view or change any setting stored
in xfconf with xfconf-query.

%if_with perl
%package -n perl-%_name
Summary:        Perl modules for xfconf
Group:          Development/Perl
Requires:       %name = %version-%release

%description -n perl-%_name
This package includes the perl modules and files you will need to
interact with xfconf using perl.
%endif

%prep
%setup -n %_name-%version
%patch -p1

%build
# Don't use git tag in version.
%xfce4_drop_gitvtag xfconf_version_tag configure.ac.in
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	--with-perl-options=INSTALLDIRS="vendor" \
	--enable-gsettings-backend \
	--enable-gtk-doc \
	--enable-debug=minimum
%make_build

%install
mkdir -p %buildroot/%_sysconfdir/xdg/xfce4/xfconf/xfce-perchannel-xml

%makeinstall_std
%find_lang %_name

%files -f %_name.lang
%doc AUTHORS NEWS
%_sysconfdir/xdg/xfce4/xfconf
%_libdir/*.so.*
%_libdir/gio/modules/*.so

%exclude %_libdir/gio/modules/*.la

%files devel
%doc %_datadir/gtk-doc/html/%_name
%_includedir/xfce4/xfconf-0
%_pkgconfigdir/*.pc
%_libdir/*.so

%files -n %_name-utils
%_bindir/*
%_libdir/xfce4/xfconf/
%_datadir/dbus-1/services/*.service

%if_with perl
%files -n perl-%_name
%perl_vendor_autolib/Xfce4*
%perl_vendor_archlib/Xfce4*
%endif

%changelog
* Mon Oct 22 2018 Mikhail Efremov <sem@altlinux.org> 4.13.6-alt1
- Updated to 4.13.6.

* Tue Aug 07 2018 Mikhail Efremov <sem@altlinux.org> 4.13.5-alt1
- xfconf-utils: Fix summary.
- Update url.
- Update BR.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated to 4.13.5.

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.12.0-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 4.12.0-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 4.12.0-alt1.1
- rebuild with new perl 5.22.0

* Thu Mar 05 2015 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt1
- Updated to 4.12.0.

* Thu Feb 19 2015 Mikhail Efremov <sem@altlinux.org> 4.11.0-alt1
- Fix Xfce name (XFCE -> Xfce).
- Updated to 4.11.0.

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 4.10.0-alt4.git20130919.1
- rebuild with new perl 5.20.1

* Tue Nov 05 2013 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt4.git20130919
- Upstream git snapshot.

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 4.10.0-alt3
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 4.10.0-alt2
- rebuilt for perl-5.16

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Updated to 4.10.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.9.1-alt1
- Updated to 4.9.1.

* Mon Apr 09 2012 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt1
- Fix License.
- Xfconf.pm.in: Fix comments.
- Updated to 4.9.0.

* Thu Dec 29 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt1
- Drop obsoleted patch.
- Updated to 4.8.1.

* Fri Oct 21 2011 Alexey Tourbin <at@altlinux.ru> 4.8.0-alt4.1
- Rebuilt for perl-5.14

* Fri Oct 21 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt4
- Fix build with rpm-build-perl >= 0.76.

* Mon Aug 29 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt3
- Updated Russian translation.

* Mon Aug 15 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt2
- Updated Russian translation (by Artem Zolochevskiy).

* Wed Jan 19 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt1
- Update summary and description (from FC spec).
- Remove rpath in perl module.
- Enable build of perl bindings.
- Fix Group.
- Fix license.
- Don't build static libraries.
- Spec cleanup.
- Updated to 4.8.0.

* Tue Jan 12 2010 Denis Koryavov <dkoryavov@altlinux.org> 4.7.0-alt1
- New version.

* Mon Jan 04 2010 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt3
- Fix build with gtkdocize.

* Sun May 24 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt2
- Added dbus-tools-gui as depency

* Sun Apr 19 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt1
Xfce 4.6.1

* Sun Apr 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.0-alt1
Xfce 4.6.0

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.93-alt1
- Xfce 4.6 beta 3

* Mon Oct 20 2008 Eugene Ostapets <eostapets@altlinux.org> 4.5.91-alt1
- Xfce 4.6 beta1
- First build for ALTLinux
