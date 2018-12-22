Summary: ukrainian dictionary for ispell

Name: ispell-uk
Version: 1.2
Release: alt3

License: GPL-1.0-only and LGPL-1.0-only
Group: Text tools
%define sourcename spell-uk-%{version}
Url: http://ispell-uk.sourceforge.net/ispell-uk/
#Url: http://sourceforge.net/projects/ispell-uk

Source: %{sourcename}.tgz
Patch: ispell-uk-1.2-perlfix.diff

Requires: ispell >= 3.2.06
Provides: ispell-ua, ispell-dictionary

# arch-dependent(byte-order)!
# BuildArch: noarch

# Automatically added by buildreq on Thu Jan 18 2007
BuildRequires: ispell perl-Encode perl-PerlIO
BuildRequires: ispell >= 3.2.06

%description
This is ukrainian dictionary for spellchecking with ispell program.
The dictionary is in koi8-u encoding.

%package -n ispell-uk-cp1251
Summary: ukrainian dictionary for ispell in cp1251 encoding
Group: Text tools
Requires: ispell >= 3.2.06

%description -n ispell-uk-cp1251
This is ukrainian dictionary for spellchecking with ispell program.
The dictionary is in cp1251 encoding.


%prep
%setup -n %{sourcename}
%patch -p1

%build
export LANG=uk_UA.UTF-8
%make ispell

%install
#rm -rf $RPM_BUILD_ROOT
#%make install-ispell-dict PREFIX=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%_libdir/ispell/
mv dist/i%{sourcename}/ukrainian.aff $RPM_BUILD_ROOT%_libdir/ispell/ukrainian.aff
mv dist/i%{sourcename}/ukrainian.hash $RPM_BUILD_ROOT%_libdir/ispell/ukrainian.hash

# cp1251
make clean
sed -i s,KOI8-U,CP1251, encodings.inc
%make ispell
mv dist/i%{sourcename}/ukrainian.aff $RPM_BUILD_ROOT%_libdir/ispell/ukrainianw.aff
mv dist/i%{sourcename}/ukrainian.hash $RPM_BUILD_ROOT%_libdir/ispell/ukrainianw.hash

%files
%doc README README.uk TODO Copyright
%_libdir/ispell/ukrainian.aff
%_libdir/ispell/ukrainian.hash

%files -n ispell-uk-cp1251
%_libdir/ispell/ukrainianw.aff
%_libdir/ispell/ukrainianw.hash

%changelog
* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3
- fixed build

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2
- applied repocop patches

* Thu Jan 18 2007 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1
- new version:
- added subpackage with dictionary in cp1251

* Fri May 20 2005 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1
- removed dictionary in cp1251 (ukrainianw)

* Tue Mar 29 2005 Igor Vlasenko <viy@altlinux.ru> 0.7-alt0.1
- new version
- BuildArch cannot be 'noarch' because of byte order
- added dictionary in cp1251

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 0.5-alt2
- rebuild

* Tue Jan 16 2002 AEN <aen@logic.ru> 0.5-alt1
- new version

* Wed Jun 13 2001 AEN <aen@logic.ru> 0.0.2-ipl3mdk
- provides ispell-dictionary

* Wed Dec 06 2000 AEN <aen@logic.ru>
- build for RE

* Wed Oct 11 2000 AEN <aen@logic.ru>
- first build for RE
