%define dist Perl4-CoreLibs
Name: perl-%dist
Version: 0.004
Release: alt1

Summary: Libraries historically supplied with Perl 4
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
# http://search.cpan.org/CPAN/authors/id/Z/ZE/ZEFRAM/Perl4-CoreLibs-%version.tar.gz
Source: %dist-%version.tar.gz

%add_findreq_skiplist %perl_vendor_privlib/chat2.pl

BuildArch: noarch

Requires: perl-base >= 1:5.14
Provides: perl4-compat = 1:5.14
Obsoletes: perl4-compat < 1:5.14

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Module-Build perl-Test-Pod

%description
This is a collection of ".pl" files that have historically been bundled
with the Perl core but are planned not to be so distributed with
core version 5.15 or later.  Relying on their presence in the core
distribution is deprecated; they should be acquired from this CPAN
distribution instead.  From core version 5.13, until their removal,
it is planned that the core versions of these libraries will emit a
warning when loaded.  The CPAN version will not emit such a warning.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Perl4
%perl_vendor_privlib/*.pl

%changelog
* Thu Aug 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.004-alt1
- Updated to upstream version 0.004.

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.003-alt1
- initial revision
