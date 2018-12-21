# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install libX11-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           alltray
Version:        0.71b
Release:        alt2_14
Summary:        Dock any application in the tray

Group:          Accessibility
License:        GPLv2+
URL:            http://alltray.trausch.us/
Source0:        https://launchpad.net/alltray/old-maintenance/%{version}/+download/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel
BuildRequires:  GConf libGConf-devel libGConf-gir-devel
BuildRequires:  libgdk-pixbuf-devel
Source44: import.info
Patch33: alltray-0.65-message-fix.patch


%description
With AllTray you can dock any application without a native tray icon into the
system tray. It works well with GNOME, KDE, XFCE 4, Fluxbox, and WindowMaker.

%prep
%setup -q
%patch33 -p1

%build
export CFLAGS="-fPIC $RPM_OPT_FLAGS"
%configure
%make_build

%install
%makeinstall_std
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;
rm $RPM_BUILD_ROOT%{_libdir}/*.so
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --add-category Application \
  --add-category Utility \
  --add-category GTK \
  --delete-original \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_libdir}/liballtray.so*
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.71b-alt2_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.71b-alt2_12
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.71b-alt2_11
- update to new release by fcimport

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 0.71b-alt2_10
- new version

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.71b-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.71b-alt2_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.71b-alt2_6
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.71b-alt2_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.71b-alt2_4
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.71b-alt2_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.71b-alt1_3
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.71b-alt1_2
- update to new release by fcimport

* Wed Sep 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.71b-alt1_1
- initial release by fedoraimport

* Mon May 25 2009 Igor Vlasenko <viy@altlinux.ru> 0.69-alt1.qa2
- NMU (applied repocop patch).

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.69-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for alltray

* Thu Mar 01 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.69-alt1
- 0.69

* Thu Mar 09 2006 Eugene Suchkov <cityhawk@altlinux.ru> 0.65-alt4
- 8286 fixed 
- "as-needed" problem fix

* Wed Jan 11 2006 Eugene Suchkov <cityhawk@altlinux.ru> 0.65-alt2
- Menu bugfix.

* Mon Dec 12 2005 Eugene Suchkov <cityhawk@altlinux.ru> 0.65-alt1
- New version build for sisyphus. A lot of bugfixes

* Mon Sep 26 2005 Eugene Suchkov <cityhawk@altlinux.ru> 0.62-alt1
- New version build for sisyphus. A lot of improvements.

* Tue Sep 06 2005 Eugene Suchkov <cityhawk@altlinux.ru> 0.51-alt2
- Spec fix (Group field)

* Tue Aug 16 2005 Eugene Suchkov <cityhawk@altlinux.ru> 0.51-alt1
- Inital build for Sisyphus

