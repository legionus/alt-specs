Name: perl-Hash-MultiValue
Version: 0.16
Release: alt1

Summary: Hash::MultiValue - Store multiple values per key
Group: Development/Perl
License: Perl

Url: %CPAN Hash-MultiValue
# cloned from git://github.com/miyagawa/Hash-MultiValue.git
Source: http://www.cpan.org/authors/id/A/AR/ARISTOTLE/Hash-MultiValue-%{version}.tar.gz

BuildArch: noarch
BuildRequires: perl-devel perl-threads

%description
Hash::MultiValue is an object (and a plain hash reference) that may
contain multiple values per key, inspired by MultiDict of WebOb.

%prep
%setup -q -n Hash-MultiValue-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Hash/MultiValue*
%doc Changes README*

%changelog
* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update
- this module changed CPAN maintainers, current CPAN
  maintainer (Aristotle Pagaltzis) did not use git.
  So I upload it as srpm.

* Tue Oct 15 2013 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt1
- 0.15

* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- 0.12

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- initial build
