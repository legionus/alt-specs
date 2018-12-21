BuildRequires: perl-podlators
%define _unpackaged_files_terminate_build 1
%define dist Socket-GetAddrInfo
Name: perl-%dist
Version: 0.22
Release: alt2

Summary: RFC 2553's getaddrinfo and getnameinfo functions
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Perl core's Socket now contains getaddrinfo
Requires: perl-base >= 1:5.14
BuildRequires: perl-base >= 1:5.14

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Module-Build perl-Test-Pod

%description
The RFC 2553 functions "getaddrinfo" and "getnameinfo" provide an
abstracted way to convert between a pair of host name/service name and
socket addresses, or vice versa. "getaddrinfo" converts names into a set
of arguments to pass to the "socket()" and "connect()" syscalls, and
"getnameinfo" converts a socket address back into its host name/service
name pair.

%package scripts
Summary: %name scripts
Group: Development/Perl
Requires: %name = %EVR

%description scripts
scripts for %name


%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Socket

%files scripts
%_bindir/*
%_man1dir/*


%changelog
* Fri Jun 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.22-alt2
- fixed unpackaged files

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.22-alt1
- 0.21 -> 0.22
- built for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.21-alt1
- 0.10 -> 0.21
- now noarch

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 0.10-alt1.2
- rebuilt with perl 5.12

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1.1
- NMU for unknown reason

* Mon Aug 04 2008 Michael Bochkaryov <misha@altlinux.ru> 0.10-alt1
- first build for ALT Linux Sisyphus
