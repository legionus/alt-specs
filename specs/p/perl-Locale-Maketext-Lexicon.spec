%define _unpackaged_files_terminate_build 1
%define module Locale-Maketext-Lexicon
%define m_distro Locale-Maketext-Lexicon
%define m_name Locale::Maketext::Lexicon
%define m_author_id DRTECH
# until perl-I18N-LangTags updated
%define _disable_test 1

Name: perl-Locale-Maketext-Lexicon
Version: 1.00
Release: alt2

Summary: Locale::Maketext::Lexicon - Use other catalog formats in Maketext

License: Artistic
Group: Development/Perl
Url: %CPAN %m_distro

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/D/DR/DRTECH/Locale-Maketext-Lexicon-%{version}.tar.gz

# Automatically added by buildreq on Sun Jan 02 2011 (-bi)
BuildRequires: perl-Locale-Maketext perl-Module-Install perl-PPI perl-Template perl-YAML perl(Text/Haml.pm)

%description
This module provides lexicon-handling modules to read from
other localization formats, such as Gettext, Msgcat, and so on.
If you are unfamiliar with the concept of lexicon modules, please
consult Locale::Maketext and http://www.autrijus.org/webl10n/ first.
A command-line utility xgettext.pl is also installed with this module,
for extracting translatable strings from source files.

%prep
%setup -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/xgettext.pl
%_man1dir/xgettext.pl*
%perl_vendor_privlib/Locale/

%changelog
* Fri Jun 29 2018 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2
- fixed unpackaged files

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1
- automated CPAN update

* Thu Jan 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1
- automated CPAN update

* Tue Jan 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.97-alt1
- automated CPAN update

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1
- automated CPAN update

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1
- automated CPAN update

* Sun Jan 02 2011 Vitaly Lipatov <lav@altlinux.ru> 0.84-alt1
- new version 0.84, update requires, fix build

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.62-alt2
- fix directory ownership violation

* Sun Jun 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.62-alt1
- new version 0.62 (with rpmrb script) - fix bug #11940

* Mon Jun 06 2005 Vitaly Lipatov <lav@altlinux.ru> 0.49-alt1
- first build for ALT Linux Sisyphus
