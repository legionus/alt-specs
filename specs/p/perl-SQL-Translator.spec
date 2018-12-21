%define _unpackaged_files_terminate_build 1
Name: perl-SQL-Translator
Version: 0.11024
Release: alt1

Summary: Manipulate structured data definitions (SQL and more)
License: GPLv2
Group: Development/Perl

URL: http://search.cpan.org/dist/SQL-Translator/
Source0: http://www.cpan.org/authors/id/I/IL/ILMARI/SQL-Translator-%{version}.tar.gz

BuildArch: noarch

# avoid dependency on perl-devel
%add_findreq_skiplist */Test/SQL/Translator*

# Automatically added by buildreq on Sat Nov 19 2011 (-bi)
BuildRequires: perl-Carp-Clan perl-Class-Base perl-Class-Data-Inheritable perl-Class-MakeMethods perl-Class-XSAccessor perl-DBI perl-Digest-SHA1 perl-File-ShareDir perl-GD perl-Graph perl-Moo perl-Spreadsheet-ParseExcel perl-Template perl-Test-Differences perl-Test-Exception perl-Test-Pod perl-Text-RecordParser perl-XML-LibXML perl-XML-Parser perl-XML-Writer perl-YAML perl(Digest/SHA.pm) perl(Package/Variant.pm) perl(Pod/Man.pm) perl(Try/Tiny.pm) perl(JSON.pm)

%description
SQL::Translator is a group of Perl modules that converts vendor-specific
SQL table definitions into other formats, such as other vendor-specific
SQL, ER diagrams, documentation (POD and HTML), XML, and Class::DBI classes.
The main focus of SQL::Translator is SQL, but parsers exist for other
structured data formats, including Excel spreadsheets and arbitrarily
delimited text files.

%prep
%setup -q -n SQL-Translator-%{version}

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README AUTHORS
%_bindir/sqlt*
%_man1dir/sqlt*.1*
%perl_vendor_privlib/SQL
%perl_vendor_privlib/Test
%perl_vendor_privlib/auto/share/dist/SQL-Translator

%changelog
* Tue Jan 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.11024-alt1
- automated CPAN update

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.11023-alt1
- automated CPAN update

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.11021-alt1
- automated CPAN update

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.11020-alt1
- automated CPAN update

* Fri Nov 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.11018-alt1
- automated CPAN update

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.11016-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.11013-alt1
- automated CPAN update

* Sat Nov 19 2011 Alexey Tourbin <at@altlinux.ru> 0.11010-alt2
- disabled build dependency on perl-Module-Install
- packaged %perl_vendor_privlib/auto/share/dist/SQL-Translator

* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 0.11010-alt1
- 0.11006 -> 0.11010

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.11006-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.11006-alt1
- automated CPAN update

* Mon Apr 12 2010 Alexey Tourbin <at@altlinux.ru> 0.11005-alt1
- 0.09001 -> 0.11005

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 0.09001-alt1
- 0.09001 version
- fix directory ownership violation

* Wed Apr 23 2008 Michael Bochkaryov <misha@altlinux.ru> 0.09000-alt1
- updated to 0.09000 version

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.08-alt1
- first build for ALT Linux Sisyphus
