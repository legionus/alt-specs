%define debug_package %nil

Name: rpm-macros-mingw32
Version: 62
Release: alt2

Summary: MinGW RPM helper macros

Group: Development/Other
License: GPLv2+
Url: http://altlinux.org
BuildArch: noarch

Packager: Boris Savelev <boris@altlinux.org>

Source: COPYING
Source1: macros.mingw32

%description
These helper macros provide possibility to rebuild
by some Alt Linux Team Policy compatible way.
Macroses from Fedora.
http://fedoraproject.org/wiki/Packaging/MinGW

%prep
%setup -q -c -T
cp %SOURCE0 COPYING

%build
# nothing

%install
mkdir -p %buildroot%_rpmmacrosdir
install -m 644 %SOURCE1 %buildroot%_rpmmacrosdir/mingw32

%files
%doc COPYING
%_rpmmacrosdir/mingw32

%changelog
* Wed Feb 08 2017 Vitaly Lipatov <lav@altlinux.ru> 62-alt2
- drop _mingw32_c++ macro (RedHat bug #974773)

* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 62-alt1
- added %%_mingw32_pkg_name

* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 61-alt1
- synchronized with mingw32-filesystem-69-7
- fixed bug with undefined %%__cmake

* Mon Jul 27 2009 Boris Savelev <boris@altlinux.org> 52-alt2
- fix optflags

* Fri Jul 17 2009 Boris Savelev <boris@altlinux.org> 52-alt1
- build for Sisyphus from Fedora

* Wed Jun 24 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 52-2
- Updated ChangeLog comment from previous version as the RPM variable
  __debug_install_post needs to be overridden instead of __os_install_post
  for -debuginfo subpackage generation

* Mon Jun 22 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 52-1
- Add script to create -debuginfo subpackages
  This script was created by Fridrich Strba
- All mingw32 packages now need to add these lines to their .spec files:
%%define __debug_install_post %%{_mingw32_debug_install_post}
%%{_mingw32_debug_package}

* Thu Jun  4 2009 Adam Goode <adam@spicenitz.org> - 51-1
- Add CMake rules

* Tue Apr 21 2009 Richard W.M. Jones <rjones@redhat.com> - 50-4
- Fix dependency problem with + in DLL name (Thomas Sailer).

* Fri Mar 27 2009 Richard W.M. Jones <rjones@redhat.com> - 50-3
- Fix up and test mingw32-pkg-config changes.

* Thu Mar 26 2009 Levente Farkas <lfarkas@lfarkas.org> - 50-1
- Add mingw32-pkg-config.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 49-2
- Rebuild for mingw32-gcc 4.4

* Thu Feb 19 2009 Richard W.M. Jones <rjones@redhat.com> - 49-1
- Added virtual provides for mingw32(cfgmgr32.dll) and mingw32(setupapi.dll).

* Wed Feb 18 2009 Richard W.M. Jones <rjones@redhat.com> - 48-1
- Fix _mingw32_configure.

* Tue Feb 17 2009 Richard W.M. Jones <rjones@redhat.com> - 47-1
- Rename mingw32-COPYING to COPYING.
- Rename mingw32-macros.mingw32 to macros.mingw32.
- _mingw32_configure looks for configure in "." and ".." dirs.
- Added _mingw32_description.
- Added mingw32(version.dll) virtual provides (rhbz#485842).

* Sun Feb  1 2009 Richard W.M. Jones <rjones@redhat.com> - 46-1
- Unset PKG_CONFIG_PATH because %_libdir/rpm/macros sets it (Erik van
  Pienbroek).

* Wed Jan 28 2009 Richard W.M. Jones <rjones@redhat.com> - 45-1
- Use PKG_CONFIG_LIBDIR instead of PKG_CONFIG_PATH so that native pkgconfig
  is never searched.

* Mon Jan 26 2009 Richard W.M. Jones <rjones@redhat.com> - 44-1
- Install rpmlint overrides file to suppress some rpmlint warnings.

* Sat Jan 24 2009 Richard W.M. Jones <rjones@redhat.com> - 43-6
- Don't claim C++ compiler exists if it's not installed, as this
  breaks autoconf and (in particular) libtool.

* Wed Jan 14 2009 Richard W.M. Jones <rjones@redhat.com> - 42-1
- Add pseudo-provides secur32.dll

* Wed Dec 17 2008 Levente Farkas <lfarkas@lfarkas.org> - 41-1
- Re-add mingw32-make

* Sat Dec  6 2008 Levente Farkas <lfarkas@lfarkas.org> - 40-2
- Rewrite mingw32-scripts to run in the current shell
- (Re-add mingw32-make) - Removed by RWMJ.
- Add mingw32-env to mingw32.sh

* Mon Nov 24 2008 Richard W.M. Jones <rjones@redhat.com> - 39-3
- Unify mingw32-filesystem packages from all three branches again, and test.
- Fix mingw32-scripts so it can handle extra parameters correctly.
- Remove mingw32-env & mingw32-make since neither of them actually work.

* Sun Nov 23 2008 Richard Jones <rjones@redhat.com> - 38-1
- Added mingw32(glut32.dll).

* Wed Nov 19 2008 Richard Jones <rjones@redhat.com> - 37-1
- Revert part of the 36-1 patch.  --build option to configure was wrong.

* Wed Nov 19 2008 Richard Jones <rjones@redhat.com> - 36-1
- Greatly improved macros (Levente Farkas).
- Added -mms-bitfields.

* Thu Nov 13 2008 Richard Jones <rjones@redhat.com> - 35-1
- Added mingw32(wldap32.dll) pseudo-provides.

* Wed Oct 29 2008 Richard Jones <rjones@redhat.com> - 34-1
- Set --prefix correctly.

* Wed Oct 29 2008 Richard Jones <rjones@redhat.com> - 33-1
- Remove mingw32.{sh,csh} which are unused.

* Mon Oct 27 2008 Richard Jones <rjones@redhat.com> - 32-1
- Add mingw32-configure script.

* Mon Oct 27 2008 Richard Jones <rjones@redhat.com> - 31-1
- Update the spec file with explanation of the 'Provides: mingw32(...)'
  lines for Windows system DLLs.

* Mon Oct  6 2008 Richard Jones <rjones@redhat.com> - 30-1
- Added _mingw32_cxx.

* Thu Sep 25 2008 Richard Jones <rjones@redhat.com> - 29-1
- Added _mingw32_as, _mingw32_dlltool, _mingw32_windres.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 27-1
- Begin the grand renaming of mingw -> mingw32.
- Added mingw32(mscoree.dll).

* Sun Sep 21 2008 Richard W.M. Jones <rjones@redhat.com> - 25-1
- Add shared aclocal directory.

* Sun Sep 21 2008 Richard W.M. Jones <rjones@redhat.com> - 24-1
- Remove mingw-defs, since no longer used.
- Add _mingw_infodir.

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 23-1
- Add macros for find-provides/requires scripts

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 22-1
- Windows provides OLE32.DLL.

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 21-1
- Allow '.' in dll names for find-requires
- Windows provides GDI32.DLL.

* Fri Sep  5 2008 Richard W.M. Jones <rjones@redhat.com> - 20-1
- On 64 bit install in %_libdir/rpm always.
