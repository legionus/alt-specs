%define installdir %webserver_webappsdir/owncloud/3rdparty

%define major 8

Name: owncloud%major-3rdparty
Version: 8.0.9
Release: alt1

Summary: 3rdparty libs for owncloud
Group: Networking/WWW
License: Varioud free licenses
Url: http://www.owncloud.org/

BuildArch: noarch
BuildRequires(pre): rpm-macros-webserver-common
Requires: owncloud%major = %version

Source0: %name-%version.tar

%description
ownCloud gives you easy and universal access to all of your files.
This package provides a set of 3rdparty libs for owncloud.


%prep
%setup

%install
# install 
mkdir -p %buildroot%installdir

cp -rp * %buildroot%installdir/
rm -fr %buildroot%installdir/phpdocx/pdf/tcpdf/fonts/utils
find %buildroot%installdir -name '*.sh' | xargs rm

%files
%installdir/*

%changelog
* Mon Sep 05 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 8.0.9-alt1
- 8.0.9

* Wed Jun 29 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 7.0.9-alt1
- 7.0.9

* Wed Feb 04 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.4-alt1
- 7.0.4

* Wed Sep 03 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 7.0.2-alt1
- 7.0.2

* Wed May 21 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.3-alt1
- 6.0.3

* Wed Jan 29 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0.1-alt1
- 6.0.1

* Wed Jan 15 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.14a-alt1
- 5.0.14

* Wed Nov 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.13-alt1
- 5.0.13

* Thu Sep 19 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.11-alt1
- 5.0.11

* Mon May 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.6-alt1
- 5.0.6

* Thu Apr 11 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.4-alt1
- 5.0.4

* Wed Mar 20 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt1
- 5.0.0

