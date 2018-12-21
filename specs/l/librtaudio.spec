# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname rtaudio
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:        Real-time Audio I/O Library
Name:           librtaudio
Version:        5.0.0
Release:        alt1_2
License:        MIT
Group:          System/Libraries
URL:            http://www.music.mcgill.ca/~gary/rtaudio/
Source0:        https://github.com/thestk/rtaudio/archive/v%{version}/rtaudio-%{version}.tar.gz
BuildRequires:  libalsa-devel
BuildRequires:  libjack-devel
BuildRequires:  libpulseaudio-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  doxygen
Source44: import.info
Provides: rtaudio = %{version}-%{release}


%description
RtAudio is a set of C++ classes that provide a common API for realtime audio
input/output across different operating systems. RtAudio significantly
simplifies the process of interacting with computer audio hardware. It was
designed with the following objectives:

  * object-oriented C++ design
  * simple, common API across all supported platforms
  * allow simultaneous multi-api support
  * support dynamic connection of devices
  * provide extensive audio device parameter control
  * allow audio device capability probing
  * automatic internal conversion for data format, channel number compensation,
    (de)interleaving, and byte-swapping


%package devel
Summary:        Real-time Audio I/O Library
Group:          System/Libraries
Requires:       %{name} = %{version}-%{release}
Provides: rtaudio-devel = %{version}-%{release}

%description devel
RtAudio is a set of C++ classes that provide a common API for realtime audio
input/output across different operating systems. RtAudio significantly
simplifies the process of interacting with computer audio hardware. It was
designed with the following objectives:

  * object-oriented C++ design
  * simple, common API across all supported platforms
  * allow simultaneous multi-api support
  * support dynamic connection of devices
  * provide extensive audio device parameter control
  * allow audio device capability probing
  * automatic internal conversion for data format, channel number compensation,
    (de)interleaving, and byte-swapping

%prep
%setup -n %{oldname}-%{version} -q
# Fix encoding issues
for file in tests/teststops.cpp; do
   sed 's|\r||' $file > $file.tmp
   iconv -f ISO-8859-1 -t UTF8 $file.tmp > $file.tmp2
   touch -r $file $file.tmp2
   mv -f $file.tmp2 $file
done

%build
autoreconf -fiv
export CFLAGS="%optflags -fPIC"
%configure --with-jack --with-alsa --with-pulse --enable-shared --disable-static --verbose
%make_build V=1

%install
make install DESTDIR=%{buildroot}

%files
%doc --no-dereference doc/doxygen/license.txt
%doc readme doc/release.txt
%{_libdir}/lib%{oldname}.so.*

%files devel
%doc doc/html doc/images
%{_includedir}/%{oldname}/*.h
%{_libdir}/lib%{oldname}.so
%{_libdir}/pkgconfig/%{oldname}.pc

%changelog
* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_2
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_13
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_11
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_9
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_5
- update to new release by fcimport

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_4
- fc update

* Mon Jan 14 2013 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_3
- initial fc import

