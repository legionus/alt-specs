%define _unpackaged_files_terminate_build 1
%define dist Parse-Method-Signatures
Name: perl-%dist
Version: 1.003019
Release: alt1

Summary: Perl6 like method signature parser
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/K/KE/KENTNL/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-MooseX-Traits perl-MooseX-Types-Structured perl-PPI perl-Pod-Escapes perl-Test-Differences perl-Test-Exception perl-aliased

%description
Inspired by Perl6::Signature but streamlined to just support the subset
deemed useful for TryCatch and MooseX::Method::Signatures.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Parse

%changelog
* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.003019-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.003017-alt1
- automated CPAN update

* Tue Jan 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.003016-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.003015-alt1
- automated CPAN update

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 1.003014-alt1
- initial revision
