#
# spec file for package libcsplit
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name: libcsplit
Version: 20130904
Release: alt1

Summary: Library for cross-platform C split string functions
License: LGPLv3+
Group: Development/C

Url: http://code.google.com/p/libcsplit/
#DL-URL: https://googledrive.com/host/0B3fBvzttpiiSeE44MVpGWnpNeVU/libcsplit-alpha-20130904.tar.gz
#Git-Clone: http://code.google.com/p/libcsplit
Source: %name-alpha-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: pkg-config
BuildRequires: pkgconfig(libcerror) >= 20130904
# libcstring is not released as a package by upstream
#BuildRequires:  pkgconfig(libcstring) >= 20120425

%description
A library for cross-platform C split string functions.

This package is part of the libyal library collection
and is used by other libraries in the collection.

See also:
    libcdata; generic data functions
    libcdatetime; date and time functions
    libcerror; error functions
    libclocale; locale functions
    libcnotify; notification functions
    libcfile; file functions
    libcpath; path functions
    libcthreads; threads functions

%package devel
Summary: Development files for libcsplit, a cross-platform C split string library
Group: Development/C
Requires: %name = %version

%description devel
A library for cross-platform C split string functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcsplit.

%prep
%setup

%build
%configure \
	--disable-static \
	--enable-wide-character-type
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Fri May 09 2014 Michael Shigorin <mike@altlinux.org> 20130904-alt1
- initial build for ALT Linux Sisyphus

* Wed Oct  2 2013 Greg.Freemyer@gmail.com
- update to v20130904
  * code cleanup
* Sat Jul 27 2013 Greg.Freemyer@gmail.com
- update to v20130609
  * Fix in .pc.in file
  * small changes
  * removed unused LIBCSPLIT_SEPARATOR
  * textual changes
  * updated dependencies
  * fix for Libs in .pc file
  * 2013 update
- remove pkgconfig patch, now upstream
- changed to gz compression to eliminate conversion after download
* Mon Apr 22 2013 Greg.Freemyer@gmail.com
- run spec-cleaner
* Wed Apr  3 2013 jengelh@inai.de
- Initial package (version 20121224) for build.opensuse.org
