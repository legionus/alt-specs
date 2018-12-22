%define _unpackaged_files_terminate_build 1
%define dist Event-RPC
Name: perl-%dist
Version: 1.10
Release: alt1

Summary: Event based transparent Client/Server RPC framework
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/J/JR/JRED/%{dist}-%{version}.tar.gz
Patch: perl-Event-RPC-ipv6.patch

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011
BuildRequires: perl-Event perl-AnyEvent perl-Glib perl-IO-Socket-SSL perl-devel perl(JSON/XS.pm) perl(Sereal.pm)

%description
Event::RPC supports you in developing Event based networking
client/server applications with transparent object/method access from
the client to the server. Network communication is optionally encrypted
using IO::Socket::SSL. Several event loop managers are supported due to
an extensible API. Currently Event and Glib are implemented.

%prep
%setup -q -n %{dist}-%{version}
#patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_privlib/Event

%changelog
* Thu Jun 28 2018 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Tue Mar 11 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Tue Oct 08 2013 Ilya Mashkin <oddity@altlinux.ru> 1.03-alt1
- 1.03

* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 1.01-alt3
- fixed unpackaged directory

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Sep 01 2009 Ilya Mashkin <oddity@altlinux.ru> 1.01-alt2
- fix build, thanks to Alexey Tourbin

* Mon Oct 27 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.01-alt1
- 1.01 release.
- Fix FTBFS with new perl.

* Tue Oct 24 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.90-alt1
- 0.90 version.
- New packager.

* Tue Jan 03 2006 Vitaly Lipatov <lav@altlinux.ru> 0.88-alt1
- first build for ALT Linux Sisyphus

