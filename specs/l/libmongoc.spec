%def_disable tests

Name: libmongoc
Version: 1.12.0
Release: alt1%ubt
Summary: Client library written in C for MongoDB
Group: System/Libraries
License: Apache-2.0 and ISC and MIT and Zlib
Url: https://github.com/mongodb/mongo-c-driver
#vsc-git https://github.com/mongodb/mongo-c-driver.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++
BuildRequires: cmake >= 3.1
BuildRequires: python-module-sphinx
BuildRequires: libssl-devel libsasl2-devel libicu-devel
BuildRequires: zlib-devel libsnappy-devel

%{?_enable_tests:BuildRequires: mongodb-server openssl}

%description
mongo-c-driver is a client library written in C for MongoDB.

%package devel
Group: Development/C
Summary: C Driver for MongoDB
Requires: %name = %EVR

%description devel
This package contains the header files and development libraries
for mongo-c-driver

%package -n libbson
Group: System/Libraries
License: Apache-2.0
Summary: A BSON utility library

%description -n libbson
libbson is a library providing useful routines related to building,
parsing, and iterating BSON documents. It is a useful base for those
wanting to write high-performance C extensions to higher level languages
such as python, ruby, or perl.

%package -n libbson-devel
Summary: Development files of libbson
Group: Development/C
Requires: libbson = %EVR

%description -n libbson-devel
libbson is a library providing useful routines related to building,
parsing, and iterating BSON documents. It is a useful base for those
wanting to write high-performance C extensions to higher level languages
such as python, ruby, or perl.

This package contains development files of libbson.

%prep
%setup

%build
%cmake \
    -DENABLE_STATIC:STRING=OFF \
    -DENABLE_BSON:STRING=ON \
    -DENABLE_MONGOC:BOOL=ON \
    -DENABLE_SHM_COUNTERS:BOOL=ON \
    -DENABLE_SSL:STRING=OPENSSL \
    -DENABLE_SASL:STRING=CYRUS \
    -DENABLE_ICU:STRING=ON \
    -DENABLE_AUTOMATIC_INIT_AND_CLEANUP:BOOL=OFF \
    -DENABLE_CRYPTO_SYSTEM_PROFILE:BOOL=ON \
    -DENABLE_MAN_PAGES:BOOL=ON \
    %{?_disable_tests:-DENABLE_TESTS:BOOL=OFF} \
    -DENABLE_EXAMPLES:BOOL=OFF


%cmake_build

%install
%cmakeinstall_std

%check
%if_enabled tests
# Run a server
mkdir dbtest
mongod \
  --journal \
  --unixSocketPrefix /tmp \
  --logpath     $PWD/server.log \
  --pidfilepath $PWD/server.pid \
  --dbpath      $PWD/dbtest \
  --fork
# Run the test suite
ret=0
export MONGOC_TEST_OFFLINE=on
#export MONGOC_TEST_SKIP_SLOW=on
make check || ret=1
# Cleanup
[ -s server.pid ] && kill $(cat server.pid)
exit $ret
%endif

%files
%doc COPYING NEWS *.md *.rst
%_bindir/*
%_libdir/libmongoc*.so.*

%files devel
%_includedir/libmongoc*
%_libdir/libmongoc*.so
%_pkgconfigdir/libmongoc*.pc
%_man3dir/mongoc*
%_libdir/cmake/libmongoc*

%files -n libbson
%doc NEWS README.rst
%_libdir/libbson*.so.*

%files -n libbson-devel
%_includedir/libbson*
%_libdir/libbson*.so
%_pkgconfigdir/libbson*.pc
%_man3dir/bson*
%_libdir/cmake/libbson*


%changelog
* Tue Sep 04 2018 Alexey Shabalin <shaba@altlinux.org> 1.12.0-alt1%ubt
- 1.12.0

* Fri Mar 09 2018 Alexey Shabalin <shaba@altlinux.ru> 1.9.3-alt1%ubt
- 1.9.3

* Tue Feb 13 2018 Alexey Shabalin <shaba@altlinux.ru> 1.9.2-alt1%ubt
- 1.9.2

* Fri Dec 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1.8.2-alt1%ubt
- 1.8.2

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20150310
- Version 1.1.2

* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20140826
- Version 1.0.0

* Fri Mar 08 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.1-alt1
- Biuld fot ALT
