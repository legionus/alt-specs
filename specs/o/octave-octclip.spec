# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 1.0.8
%define octave_pkg_name octclip
%define octave_descr_name OctCLIP
Name: octave-%octave_pkg_name
Version: 1.0.8
Release: alt3
Summary: GNU Octave clipping polygons tool

Group: Sciences/Mathematics
License: GPLv3+, modified BSD
URL: http://davis.wpi.edu/~matt/courses/clipping/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
BuildRequires: libGL-devel libGLU-devel libGraphicsMagick-c++-devel libGraphicsMagick-devel fontconfig-devel libfreetype-devel libX11-devel libgl2ps-devel libcurl-devel libsuitesparse-devel libarpack-ng-devel libqrupdate-devel libpcre-devel
%else
BuildArch: noarch
%endif
Provides: octave(octclip) = %version
# Depends: Octave (>= 2.9.7)
Requires: octave >= 2.9.7

%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
This package allows to do boolean operations with polygons using

%prep
%setup -q -n %{octave_pkg_name}-%{octave_pkg_version}

%build
%define build_flags CXXFLAGS=$CXXFLAGS
%build_flags octave -H --no-site-file --eval "pkg build -verbose -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
octave -H --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -verbose -local -nodeps %octave_pkg_name-%octave_pkg_version-$(octave -H --no-site-file --eval "printf([__octave_config_info__(\"canonical_host_type\"), \"-\",  __octave_config_info__(\"api_version\")])").tar.gz"

%files
%_datadir/octave/packages/%octave_pkg_name-%octave_pkg_version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%octave_pkg_version
%endif

%changelog
* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt3
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 1.0.8-alt2
- regenerated from template by package builder

* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1.0.3-alt3
- Rebuild with the next version of Octave: 4.0.0

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.3-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1.0.3-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Oct 10 2013 Paul Wolneykien <manowar@altlinux.ru> 1.0.3-alt1
- updated by octave-package-builder

* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1
- initial import by octave-package-builder

