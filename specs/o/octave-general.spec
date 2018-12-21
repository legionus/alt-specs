# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave-config makeinfo pkgconfig(nettle)
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 2.1.0
%define octave_pkg_name general
%define octave_descr_name general
Epoch: 1
Name: octave-%octave_pkg_name
Version: 2.1.0
Release: alt1
Summary: General

Group: Sciences/Mathematics
License: GPLv3+, modified BSD, public domain
URL: http://octave.sf.net

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(general) = %version
# Depends: octave (>= 4.0.0)
Requires: octave >= 4.0.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
General tools for Octave.

%prep
%setup -q -n %{octave_pkg_name}-%{octave_pkg_version}

%build
octave -q -H --no-site-file --no-window-system --eval "pkg build -verbose -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
#octave -q -H --no-site-file --no-window-system --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg global_list %buildroot%_datadir/octave/packages; pkg local_list %buildroot%_datadir/octave/packages; pkg install -nodeps -verbose %{_builddir}/%{buildsubdir}/%octave_pkg_name-%octave_pkg_version-%{_arch}-alt-linux-gnu-api-v52.tar.gz"
octave -q -H --no-site-file --no-window-system --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -nodeps -verbose -local %{_builddir}/%{buildsubdir}/%octave_pkg_name-%octave_pkg_version-%{_arch}-alt-linux-gnu-api-v52.tar.gz"

%files
%_datadir/octave/packages/%octave_pkg_name-%octave_pkg_version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%octave_pkg_version
%endif

%changelog
* Wed May 23 2018 Igor Vlasenko <viy@altlinux.ru> 1:2.1.0-alt1
- regenerated from template by package builder

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 1:2.0.0-alt2
- regenerated from template by package builder

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.0.0-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1:1.3.4-alt2
- Rebuild with the next version of Octave: 4.0.0

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:1.3.4-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 1:1.3.4-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:1.3.2-alt2
- Rebuild with the next version of Octave: 3.8.0

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.3.2-alt1
- updated by octave-package-builder

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1
- initial import by octave-package-builder

