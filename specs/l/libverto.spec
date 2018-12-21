# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(tevent)
# END SourceDeps(oneline)
Group: Development/C
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global homepage https://github.com/latchset/libverto

Name:           libverto
Version:        0.3.0
Release:        alt1_5
Summary:        Main loop abstraction library

License:        MIT
URL:            %{homepage}
Source0:        %{homepage}/releases/download/%{version}/%{name}-%{version}.tar.gz

Patch0: Work-around-libev-not-being-c89-compliant.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  glib2-devel libgio libgio-devel
BuildRequires:  libevent-devel
# BuildRequires:  libtevent-devel
%if !0%{?rhel}
BuildRequires:  libev-devel
%endif

BuildRequires:  git

Obsoletes:      libverto-tevent < 0.3.0-2
Obsoletes:      libverto-tevent-devel < 0.3.0-2
Source44: import.info

%description
libverto provides a way for libraries to expose asynchronous interfaces
without having to choose a particular event loop, offloading this
decision to the end application which consumes the library.

If you are packaging an application, not library, based on libverto,
you should depend either on a specific implementation module or you
can depend on the virtual provides 'libverto-module-base'. This will
ensure that you have at least one module installed that provides io,
timeout and signal functionality. Currently glib is the only module
that does not provide these three because it lacks signal. However,
glib will support signal in the future.

%package        devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        glib
Group: Development/C
Summary:        glib module for %{name}
Requires:       %{name} = %{version}-%{release}

%description    glib
Module for %{name} which provides integration with glib.

This package does NOT yet provide %{name}-module-base.

%package        glib-devel
Group: Development/C
Summary:        Development files for %{name}-glib
Requires:       %{name}-glib = %{version}-%{release}

%description    glib-devel
The %{name}-glib-devel package contains libraries and header files for
developing applications that use %{name}-glib.

%package        libevent
Group: Development/C
Summary:        libevent module for %{name}
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-module-base = %{version}-%{release}

%description    libevent
Module for %{name} which provides integration with libevent.

%package        libevent-devel
Group: Development/C
Summary:        Development files for %{name}-libevent
Requires:       %{name}-libevent = %{version}-%{release}

%description    libevent-devel
The %{name}-libevent-devel package contains libraries and header files for
developing applications that use %{name}-libevent.

# %package        tevent
# Summary:        tevent module for %{name}
# Requires:       %{name}%{?_isa} = %{version}-%{release}
# Provides:       %{name}-module-base = %{version}-%{release}

# %description    tevent
# Module for %{name} which provides integration with tevent.

# This package provides %{name}-module-base since it supports io, timeout
# and signal.

# %package        tevent-devel
# Summary:        Development files for %{name}-tevent
# Requires:       %{name}-tevent%{?_isa} = %{version}-%{release}
# Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

# %description    tevent-devel
# The %{name}-tevent-devel package contains libraries and header files for
# developing applications that use %{name}-tevent.

%if !0%{?rhel}
%package        libev
Group: Development/C
Summary:        libev module for %{name}
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-module-base = %{version}-%{release}

%description    libev
Module for %{name} which provides integration with libev.

This package provides %{name}-module-base since it supports io, timeout
and signal.

%package        libev-devel
Group: Development/C
Summary:        Development files for %{name}-libev
Requires:       %{name}-libev = %{version}-%{release}

%description    libev-devel
The %{name}-libev-devel package contains libraries and header files for
developing applications that use %{name}-libev.

This package provides %{name}-module-base since it supports io, timeout
and signal.
%endif

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fiv
%configure --disable-static
%make_build

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'




#ldconfig_scriptlets tevent
%if !0%{?rhel}

%endif

%files
%{!?_licensedir:%global license %%doc}
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/verto.h
%{_includedir}/verto-module.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files glib
%{_libdir}/%{name}-glib.so.*

%files glib-devel
%{_includedir}/verto-glib.h
%{_libdir}/%{name}-glib.so
%{_libdir}/pkgconfig/%{name}-glib.pc

%files libevent
%{_libdir}/%{name}-libevent.so.*

%files libevent-devel
%{_includedir}/verto-libevent.h
%{_libdir}/%{name}-libevent.so
%{_libdir}/pkgconfig/%{name}-libevent.pc

# %files tevent
# %{_libdir}/%{name}-tevent.so.*

# %files tevent-devel
# %{_includedir}/verto-tevent.h
# %{_libdir}/%{name}-tevent.so
# %{_libdir}/pkgconfig/%{name}-tevent.pc

%if !0%{?rhel}
%files libev
%{_libdir}/%{name}-libev.so.*

%files libev-devel
%{_includedir}/verto-libev.h
%{_libdir}/%{name}-libev.so
%{_libdir}/pkgconfig/%{name}-libev.pc
%endif

%changelog
* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_5
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_1
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_7
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_5
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_2
- update to new release by fcimport

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.5-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.5-alt1_2
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.5-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1_3
- update to new release by fcimport

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1_2
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1_1
- initial import by fcimport

