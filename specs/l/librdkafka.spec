Name: librdkafka
Version: 0.11.6
Release: alt0.3

Summary: the Apache Kafka C/C++ client library

License: BSD-2-Clause
Group: Development/C++
Url: https://github.com/edenhill/librdkafka

Packager: Pavel Vainerman <pv@altlinux.ru>

# Source-url: https://github.com/edenhill/librdkafka/archive/v%{version}.tar.gz
Source: %name-%version.tar
Source1: rdkafka.pc

# Automatically added by buildreq on Fri Nov 09 2018
# optimized out: cmake-modules libcom_err-devel libkrb5-devel libstdc++-devel pkg-config python-base python-modules python3 python3-base zlib-devel
BuildRequires: cmake gcc-c++ libssl-devel

%description
librdkafka is a C library implementation of the Apache Kafka protocol, containing 
both Producer and Consumer support. It was designed with message delivery 
reliability and high performance in mind, current figures exceed 1 million 
msgs/second for the producer and 3 million msgs/second for the consumer.

%package devel
Group: Development/C++
Summary: the Apache Kafka C/C++ client library
Requires: %name = %version-%release

%description devel
librdkafka is a C library implementation of the Apache Kafka protocol, containing 
both Producer and Consumer support. It was designed with message delivery 
reliability and high performance in mind, current figures exceed 1 million 
msgs/second for the producer and 3 million msgs/second for the consumer.

%prep
%setup

%build
#%cmake_insource
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_libdir/pkgconfig
cp %SOURCE1 %buildroot%_libdir/pkgconfig/
%__subst 's|@VERSION@|%{version}|g' %buildroot%_libdir/pkgconfig/*.pc


rm -f %buildroot%_libdir/*.a
rm -f %buildroot%_datadir/licenses/librdkafka/LICENSES.txt

%if %_lib == lib64
    mv %buildroot/usr/lib/* %buildroot%_libdir/
%endif



%files
%doc LICENSE README.md
%_libdir/*.so

%files devel
%dir %_includedir/%name
%_includedir/%name/*.h
%dir %_libdir/cmake/RdKafka
%_libdir/cmake/RdKafka/*.cmake
%_libdir/pkgconfig/*.pc

%changelog
* Fri Nov 09 2018 Pavel Vainerman <pv@altlinux.ru> 0.11.6-alt0.3
- minor fixes in spec

* Fri Nov 09 2018 Pavel Vainerman <pv@altlinux.ru> 0.11.6-alt0.2
- added pc-file

* Fri Nov 09 2018 Pavel Vainerman <pv@altlinux.ru> 0.11.6-alt0.1
- new version (0.11.6) with rpmgs script

