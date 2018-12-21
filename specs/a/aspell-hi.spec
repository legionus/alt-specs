Group: Text tools
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global debug_package %{nil}
%global lang hi
%global langrelease 0

Name:           aspell-hi
Version:        0.02
Release:        alt2_17
Summary:        GNU Aspell Hindi Dictionary Package

License:        GPLv2
URL:            http://aspell.net/
Source0:        ftp://ftp.gnu.org/gnu/aspell/dict/%{lang}/aspell6-%{lang}-%{version}-%{langrelease}.tar.bz2

BuildRequires:  aspell >= 0.60
Requires:       aspell >= 0.60
Source44: import.info

%description
GNU Aspell Hindi Dictionary Package

# Note that this package, like other aspell's language packs, does not come up
# cleanly through rpmlint, but with the following errors:
# E: aspell-hi no-binary
# E: aspell-hi only-non-binary-in-usr-lib
# This is because the package contains only data files which sit under /usr/lib.
# They have to stay there, as they are architecture-dependent (due to
# byte-ordering issues).
# E: aspell-hi configure-without-libdir-spec
#  The configure script isn't actually one generated by autoconf and doesn't accept
#  --libdir, so this error is bogus.

%prep
%setup -q -n aspell6-%{lang}-%{version}-%{langrelease}
iconv -f ISO-8859-1 -t UTF-8 Copyright > Copyright.utf8
mv Copyright.utf8 Copyright

%build
./configure
%make_build

%install
make install DESTDIR=%{buildroot}

%files
%doc Copyright README info
%doc COPYING
%{_libdir}/aspell/*
%{_datadir}/aspell/*

%changelog
* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_17
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_15
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_14
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_12
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_7
- update to new release by fcimport

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_6
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_5
- Group: should be Text tools

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_5
- update and rebuild with proper aspell datadir

* Tue Jul 29 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_2
- build for Sisyphus

