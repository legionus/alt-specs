%define _unpackaged_files_terminate_build 1
#
#   - Text::Quoted -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --spec-only -U Text::Quoted --version 1.8
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Text-Quoted
%define m_distro Text-Quoted
%define m_name Text::Quoted
%define m_author_id RUZ
%define _enable_test 1

Name: perl-Text-Quoted
Version: 2.10
Release: alt1

Summary: Text-Quoted - Extract the structure of a quoted mail message

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/~ruz/%m_distro-%version/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/B/BP/BPS/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Mon Jun 06 2005
BuildRequires: perl-Text-Autoformat perl-Text-Reform perl-devel

%description
"Text::Quoted" examines the structure of some text which may contain
multiple different levels of quoting, and turns the text into a nested
data structure.

The structure is an array reference containing hash references for each
paragraph belonging to the same author. Each level of quoting recursively
adds another list reference.

This also tells you about what's in the hash references: "raw" is the
paragraph of text as it appeared in the original input; "text" is what
it looked like when we stripped off the quotation characters, and "quoter"
is the quotation string.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%doc Changes README
%perl_vendor_privlib/Text/*

%changelog
* Fri Jul 27 2018 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.08-alt1
- automated CPAN update

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.05-alt2
- fix directory ownership violation
- disable man packaging

* Fri Jun 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.05-alt1
- new version 2.05 (with rpmrb script)

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 2.03-alt1
- new version 2.03 (with rpmrb script)

* Fri Jul 06 2007 Vitaly Lipatov <lav@altlinux.ru> 2.02-alt1
- new version 2.02 (with rpmrb script) (fix bug#12226)
- add some doc files

* Mon Jun 06 2005 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- first build for ALT Linux Sisyphus
