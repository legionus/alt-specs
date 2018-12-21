# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           lpairs
Summary:        Classical memory game with cards
Version:        1.0.5
Release:        alt1_1
License:        GPLv2+ and CC-BY-SA and Freely redistributable without restriction
Group:          Games/Other
URL:            https://lgames.sourceforge.net/index.php?project=LPairs
Source0:        https://downloads.sourceforge.net/lgames/lpairs-%{version}.tar.gz
#there is a problem with data dir
#the author said it would be hard for him to fix it at autoconf level
Patch0:         lpairs-1.0.3-datadir.diff
Patch1:         lpairs-1.0.4-desktop.diff
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  libSDL-devel
BuildRequires:  gettext gettext-tools
Source44: import.info

%description
LPairs is a classical memory game. This means you have to find pairs of
identical cards which will then be removed. Your time and tries needed
will be counted but there is no highscore chart or limit to this.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
# FIXME: Package suffers from c11/inline issues
# Workaround by appending -std=gnu89 to CFLAGS
# Proper fix would be to fix the source-code
CFLAGS="${RPM_OPT_FLAGS} -std=gnu89"

%configure inst_dir="%{_datadir}/%{name}"
%make_build

%install
rm -fr %{buildroot}
make DESTDIR=%{buildroot} inst_dir="%{_datadir}/%{name}" install
%find_lang %{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp lpairs.png %{buildroot}%{_datadir}/pixmaps/

desktop-file-install --dir %{buildroot}%{_datadir}/applications \
        lpairs.desktop

%files -f %{name}.lang
%{_bindir}/lpairs
%{_datadir}/%{name}
%doc AUTHORS ChangeLog COPYING README
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_20
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_18
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_17
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_16
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_13
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_12
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_11
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_10
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_9
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_9
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_8
- converted from Fedora by srpmconvert script

* Tue Feb 15 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_8
- converted from Fedora by srpmconvert script

