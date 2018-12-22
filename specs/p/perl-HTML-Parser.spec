%define _unpackaged_files_terminate_build 1
%define dist HTML-Parser
Name: perl-%dist
Version: 3.72
Release: alt1.1.1

Summary: Parsing and extracting information from HTML documents
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/G/GA/GAAS/HTML-Parser-%{version}.tar.gz

# avoid circular dependency on perl-libwww
%add_findreq_skiplist */HTML/HeadParser.pm

# Automatically added by buildreq on Tue Oct 25 2011
BuildRequires: perl-HTML-Tagset perl-Test-Pod perl-URI perl-threads

%description
This is a collection of perl modules that parse and extract
information from HTML documents.

%prep
%setup -q -n %dist-%version

%ifdef __buildreqs
# avoid build dependency on perl-libwww
mv t/headparser-http.t t/headparser-http.t.orig
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README eg
%perl_vendor_archlib/HTML
%perl_vendor_autolib/HTML

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.72-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 3.72-alt1.1
- rebuild with new perl 5.24.1

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 3.72-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 3.71-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.71-alt2.1
- rebuild with new perl 5.20.1

* Thu Aug 22 2013 Vladimir Lettiev <crux@altlinux.ru> 3.71-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 3.71-alt1
- automated CPAN update

* Mon Aug 27 2012 Vladimir Lettiev <crux@altlinux.ru> 3.69-alt2
- rebuilt for perl-5.16

* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 3.69-alt1
- 3.68 -> 3.69

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 3.68-alt2
- rebuilt for perl-5.14
- rebuilt as plain src.rpm

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 3.68-alt1
- 3.66 -> 3.68
- built for perl-5.12

* Thu Aug 05 2010 Alexey Tourbin <at@altlinux.ru> 3.66-alt1
- 3.65 -> 3.66

* Thu Apr 08 2010 Alexey Tourbin <at@altlinux.ru> 3.65-alt1
- 3.64 -> 3.65

* Fri Oct 30 2009 Alexey Tourbin <at@altlinux.ru> 3.64-alt1
- 3.62 -> 3.64

* Fri Oct 23 2009 Alexey Tourbin <at@altlinux.ru> 3.62-alt2
- avoid circular dependency on perl-libwww

* Fri Aug 28 2009 Alexey Tourbin <at@altlinux.ru> 3.62-alt1
- 3.61 -> 3.62

* Thu Jul 09 2009 Alexey Tourbin <at@altlinux.ru> 3.61-alt1
- 3.60 -> 3.61

* Fri Feb 27 2009 Alexey Tourbin <at@altlinux.ru> 3.60-alt1
- 3.58 -> 3.60

* Sun Nov 23 2008 Alexey Tourbin <at@altlinux.ru> 3.58-alt1
- 3.56 -> 3.58

* Sun Mar 02 2008 Alexey Tourbin <at@altlinux.ru> 3.56-alt2
- packaged examples

* Sat Jan 13 2007 Alexey Tourbin <at@altlinux.ru> 3.56-alt1
- 3.55 -> 3.56
- imported into git and adapted for gear

* Thu Jul 13 2006 Alexey Tourbin <at@altlinux.ru> 3.55-alt1
- 3.54 -> 3.55

* Mon May 22 2006 Alexey Tourbin <at@altlinux.ru> 3.54-alt1
- 3.51 -> 3.54

* Mon Apr 17 2006 Alexey Tourbin <at@altlinux.ru> 3.51-alt1
- 3.45 -> 3.51

* Sat Jun 25 2005 Alexey Tourbin <at@altlinux.ru> 3.45-alt2
- added support for XSLoader (cpan #13409)

* Fri Jan 07 2005 Alexey Tourbin <at@altlinux.ru> 3.45-alt1
- 3.43 -> 3.45

* Sun Dec 19 2004 Alexey Tourbin <at@altlinux.ru> 3.43-alt1
- 3.36 -> 3.43
- HTML-TokeParser-Simple decoupled because of extra build dependencies
- manual pages not packaged (use perldoc)

* Mon Apr 19 2004 Alexey Tourbin <at@altlinux.ru> 3.36-alt1
- 3.35 -> 3.36
- packaged HTML-TokeParser-Simple-2.2 here (laziness is a virtue)

* Mon Dec 15 2003 Alexey Tourbin <at@altlinux.ru> 3.35-alt1
- 3.35

* Tue Oct 28 2003 Alexey Tourbin <at@altlinux.ru> 3.34-alt1
- 3.34; segfault fixed: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=217616
- alt-unicode.patch: enable support for unicode entities

* Fri Oct 17 2003 Alexey Tourbin <at@altlinux.ru> 3.33-alt1
- 3.33

* Thu Aug 28 2003 Alexey Tourbin <at@altlinux.ru> 3.31-alt1
- 3.31

* Mon Apr 28 2003 Alexey Tourbin <at@altlinux.ru> 3.28-alt1
- 3.28

* Fri Mar 14 2003 Alexey Tourbin <at@altlinux.ru> 3.27-alt1
- 3.27
- spec file cleanup; sample programs added to docs

* Tue Oct 22 2002 Alexey Tourbin <at@altlinux.ru> 3.26-alt2
- rebuilt for perl-5.8 with new rpm macros

* Wed Apr 03 2002 Stanislav Ievlev <inger@altlinux.ru> 3.26-alt1
- 3.26

* Tue Aug 21 2001 Stanislav Ievlev <inger@altlinux.ru> 3.25-alt1
- 3.25

* Mon Jul 23 2001 Stanislav Ievlev <inger@altlinux.ru> 3.18-alt2
- Rebuilt with new perl

* Mon Jun 25 2001 Konstantin Volckov <goldhead@altlinux.ru> 3.18-alt1
- Rebuilt with perl-5.6.1
- Some spec cleanup

* Sun Jan 28 2001 Mikhail Zabaluev <zabaluev@parascript.com> 3.15-ipl1mdk
- Updated:
  + version 3.15
- Changed:
  + Sisyphus adaptations

* Wed Jun 28 2000 Mikhail Zabaluev <mookid@sigent.ru> 3.09-1mdk_mhz
- new version
- redid filelist

* Wed May 17 2000 David BAUDENS <baudens@mandrakesoft.com> 3.05-4mdk
- Fix build for i486
- Use %%_tmppath for BuildRoot

* Fri Mar 31 2000 Pixel <pixel@mandrakesoft.com> 3.05-3mdk
- rebuild, new group, cleanup

* Tue Feb 29 2000 Jean-Michel Dault <jmdault@netrevolution.com> 3.0.5-1mdk
- upgrade to 3.05

* Mon Jan  3 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- final cleanup for Mandrake 7

* Thu Dec 30 1999 Jean-Michel Dault <jmdault@netrevolution.com>
-updated to 3.02

* Sun Aug 29 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- bzip2'd sources
- updated to 2.23

* Tue May 11 1999 root <root@alien.devel.redhat.com>
- Spec file was autogenerated.
