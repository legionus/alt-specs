Group: System/Libraries
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          archivemount
Version:       0.8.12
Release:       alt1_3
Summary:       FUSE based filesystem for mounting compressed archives

License:       LGPLv2+
URL:           http://www.cybernoia.de/software/archivemount/
Source0:       http://www.cybernoia.de/software/archivemount/%{name}-%{version}.tar.gz
Patch0:        fix-debuginfo.patch

Requires:      fuse
BuildRequires:  gcc
BuildRequires: libfuse-devel
BuildRequires: libarchive-devel
Source44: import.info

%description
Archivemount is a piece of glue code between libarchive and FUSE. It can be
used to mount a (possibly compressed) archive (as in .tar.gz or .tar.bz2)
and use it like an ordinary filesystem.

%prep
%setup -q
%patch0 -p1

%build
%configure
%make_build

%install
rm -f archivemount.1
%makeinstall_std

%files
%doc CHANGELOG README
%doc --no-dereference COPYING
%{_mandir}/*/*
%{_bindir}/archivemount

%changelog
* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.8.12-alt1_3
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.8.12-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.7-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.7-alt1_3
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.7-alt1_2
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.8.7-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_2
- update to new release by fcimport

* Fri Nov 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_1
- update to new release by fcimport

* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_2
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_1
- update to new release by fcimport

* Tue Aug 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt2_12
- update to new release by fcimport

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.1-alt2_11.qa1
- NMU: rebuilt with libarchive.so.13.

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt2_11
- update to new release by fcimport

* Wed Jan 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt2_9
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt2_8
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_8
- update to new release by fcimport

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_7
- update to new release by fcimport

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_6
- update to new release by fcimport

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_5
- initial release by fcimport

