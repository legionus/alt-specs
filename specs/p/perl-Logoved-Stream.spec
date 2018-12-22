%define module Logoved-Stream

Name: perl-%module
Version: 0.015
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: Stream parser library for rpmbuild -v, hasher, beehive logs.
Group: Development/Perl
License: GPL-1.0-only or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
#Url: http://search.cpan.org/dist/%module
Url: http://git.altlinux.org/people/viy/packages/Logoved-Stream.git

BuildRequires: perl-devel perl(Moo.pm) perl(MooX/Singleton.pm) perl(autodie.pm) perl(Source/Shared/CLI.pm)
Requires: perl(MooX/Singleton.pm)

%description
Perl stream parser library for rpmbuild -v, hasher, beehive logs.

%package Listener-Repocop
Summary: Repocop listener for Logoved-Stream beehive log parser.
Group: Development/Perl

%description Listener-Repocop
Repocop listener for Logoved-Stream beehive log parser.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build 

%install
%perl_vendor_install

%files
#doc Changes
#doc README
%perl_vendor_privlib/Logoved*
%exclude %perl_vendor_privlib/Logoved/Stream/Listener/Factory/Repocop*
%exclude %perl_vendor_privlib/Logoved/Role/Stream/Out/Listener/Repocop*
%exclude %perl_vendor_privlib/Logoved/Stream/Out/Listener/Repocop*

# demo
#%_bindir/*
%exclude %_bindir/*
#%exclude %_bindir/*-repocop

%files Listener-Repocop
%_bindir/*-repocop
%perl_vendor_privlib/Logoved/Stream/Listener/Factory/Repocop*
%perl_vendor_privlib/Logoved/Role/Stream/Out/Listener/Repocop*
%perl_vendor_privlib/Logoved/Stream/Out/Listener/Repocop*

%changelog
* Wed Oct 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- new version

* Fri Oct 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- new version

* Wed Sep 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- manually added Requires: perl(MooX/Singleton.pm)
- TODO: fix problem in perl.req

* Tue Sep 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- new version

* Mon Sep 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- added status of the main stream

* Sun Sep 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- rpmbuild::write conflict fixed

* Sun Sep 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- added versioning

* Fri Aug 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- added hasher::timeout section

* Thu Aug 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- added hasher::chroot::file_conflict section

* Wed Aug 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- corrections for error status

* Tue Aug 28 2018 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- added section status

* Tue Aug 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- added repocop listeners

* Sun Aug 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- new version

* Wed Aug 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- beehive support

* Mon Aug 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial rpm build

