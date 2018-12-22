# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 0.25.0
%global api 1.2
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           libvtemm
Version:        0.25.0
Release:        alt4_14

Summary:        C++ interface for VTE (a GTK2 terminal emulator widget)

Group:          System/Libraries
# library is LGPLv3+, examples are GPLv3+.
License:        LGPLv3+ and GPL-3.0-or-later
URL:            http://gtkmm.org
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{release_version}/%{name}-%{version}.tar.bz2

BuildRequires:  libglibmm-devel >= 2.22.0
BuildRequires:  libpangomm-devel >= 2.24.0
BuildRequires:  libgtkmm2-devel >= 2.19.2
BuildRequires:  libvte-devel python-module-vte-devel vte
Source44: import.info

%description
libvtemm provides a C++ interface to the VTE library.

%package        devel
Summary:        Headers for developing programs that will use %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       vte
Requires:       pkg-config

%description devel
This package contains the static libraries and header files needed for
developing libvtemm applications.

%package        docs
Summary:        Documentation for %{name}, includes full API docs
Group:          Documentation
Requires:       libgtkmm2-doc
BuildArch: noarch

%description    docs
This package contains the full API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
%add_optflags -std=c++11
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build V=1

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc AUTHORS ChangeLog COPYING COPYING.lesser NEWS README
%doc old_news_and_changelogs/ChangeLog* old_news_and_changelogs/NEWS*
%{_libdir}/*.so.*

%files devel
# examples
%doc %{_datadir}/%{name}-%{api}
%{_includedir}/%{name}-%{api}
%{_libdir}/*.so
%{_libdir}/%{name}-%{api}
%{_libdir}/pkgconfig/*.pc

%files docs
%doc %{_docdir}/%{name}-%{api}
%doc %{_datadir}/devhelp/

%changelog
* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.25.0-alt4_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.25.0-alt4_12
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.25.0-alt4_11
- update to new release by fcimport

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 0.25.0-alt4_10
- new release

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0.25.0-alt4_5.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * arch-dep-package-consists-of-usr-share for libvtemm-docs

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.25.0-alt4_5
- update to new release by fcimport

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.25.0-alt4_4
- applied repocop patches

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.25.0-alt3_4
- update to new release by fcimport

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.25.0-alt3_3
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.25.0-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.25.0-alt2_2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.25.0-alt1_2
- initial import by fcimport

