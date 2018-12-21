Name: perl-Mozilla-LDAP
Version: 1.5.2
Release: alt3.1.1.1.1

Summary: LDAP Perl module that wraps the Mozilla C SDK
License: MPL 1.1/GPL 2.0/LGPL 2.1
Group: Development/Perl

URL: http://www.mozilla.org/directory/perldap.html
Source: perl-mozldap-%version.tar.gz

# due to "version check failed at .../Mozilla/LDAP/Conn.pm"
Patch0: perl-mozldap-1.5-alt-perl-deps.patch

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: mozldap-devel perl-devel

%description
PerLDAP is a set of modules written in Perl and C that allow developers to
leverage their existing Perl knowledge to easily access and manage LDAP-
enabled directories.  PerLDAP makes it very easy to search, add, delete,
and modify directory entries.  For example, Perl developers can easily
build web applications to access information stored in a directory or
create directory sync tools between directories and other services.

%prep
%setup -q -n perl-mozldap-%version
%patch0 -p1
mv Makefile.PL{,.orig}
mv Makefile.PL{.rpm,}

%build
export LDAPPKGNAME=mozldap
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CREDITS README RELEASE
%perl_vendor_archlib/Mozilla*
%perl_vendor_autolib/Mozilla

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt3.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.5.2-alt3
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 1.5.2-alt2
- rebuilt for perl-5.16

* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 1.5.2-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.5.2-alt1.1
- rebuilt with perl 5.12

* Fri Oct 26 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.2-alt1
- 1.5.2
- License change to MPL/GPL/LGPL
- fix https://bugzilla.mozilla.org/show_bug.cgi?id=389731
- PerLDAP crashes when a bad URL is passed

* Mon Sep 24 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt4
- Change build to ALT-style, thanks to at@

* Mon Jul 09 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt3
- Spec cleanup

* Wed Jun 27 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt2
- Resolve bug #12170
- Spec cleanup

* Tue May 29 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt1
- Initial

* Wed Jan 10 2007 Rich Megginson <richm@stanfordalumni.org> - 1.5-8
- add perl_requires filter for the Entry module
- add the MPL-1.1.txt file to the DOCs

* Wed Jan 10 2007 Rich Megginson <richm@stanfordalumni.org> - 1.5-7
- Incorporate comments from Fedora Extras review - https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=219869
- Remove all Requires except perl - use autogenerated ones
- Remove ExclusiveArch
- Remove files that don't need to be packaged
- add full URL to sources
- set API.so to mode 755

* Tue Oct 17 2006 Rich Megginson <richm@stanfordalumni.org> - 1.5-6
- look for brp-compress first in /usr/lib then _libdir

* Tue Oct 17 2006 Rich Megginson <richm@stanfordalumni.org> - 1.5-5
- there is no TODO file; use custom Makefile.PL

* Mon Oct 16 2006 Rich Megginson <richm@stanfordalumni.org> - 1.5-4
- use pkg-config --variable=xxx instead of --cflags e.g.

* Mon Oct 16 2006 Rich Megginson <richm@stanfordalumni.org> - 1.5-3
- this is not a noarch package

* Mon Oct 16 2006 Rich Megginson <richm@stanfordalumni.org> - 1.5-2
- Use new mozldap6, dirsec versions of nspr, nss

* Tue Feb  7 2006 Rich Megginson <richm@stanfordalumni.org> - 1.5-1
- Based on the perl-LDAP.spec file
