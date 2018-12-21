Name: nano
Version: 2.7.0
Release: alt1

Summary: a user-friendly editor, a Pico clone with enhancements
License: %gpl3plus/%fdl v1.2+
Group: Editors
Url: https://nano-editor.org/
Packager: Artem Zolochevskiy <azol@altlinux.org>

# git clone --branch v2.7.0 git://git.savannah.gnu.org/nano.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Sun Oct 09 2016
# optimized out: groff-base libncurses-devel libtinfo-devel perl perl-Encode perl-Text-Unidecode perl-Unicode-EastAsianWidth perl-Unicode-Normalize perl-libintl perl-unicore pkg-config python-base xz
BuildRequires: groff-extra groff-ps libmagic-devel libncursesw-devel makeinfo
# explicitly added
BuildRequires: desktop-file-utils

%description
GNU nano is a small and friendly text editor. It aims to emulate the
Pico text editor while also offering several enhancements.

%prep
%setup

%build
./autogen.sh
%configure
%make_build

%install
%makeinstall_std

# install config file
install -d %buildroot%_sysconfdir
sed 's/^# include "/include "/' doc/nanorc.sample > %buildroot%_sysconfdir/nanorc

#install doc files to package
install -pm644 AUTHORS IMPROVEMENTS NEWS README THANKS TODO %buildroot%_docdir/%name
xz %buildroot%_docdir/%name/NEWS
install -Dpm644 doc/nanorc.sample %buildroot%_docdir/%name/examples/nanorc.sample
mv %buildroot%_docdir/%name %buildroot%_docdir/%name-%version

# install icons
install -Dpm644 %name-16x16.png %buildroot%_miconsdir/%name.png
install -Dpm644 %name-32x32.png %buildroot%_niconsdir/%name.png
install -Dpm644 %name-48x48.png %buildroot%_liconsdir/%name.png

# install .desktop file
desktop-file-install --dir %buildroot%_desktopdir %name.desktop

# list of language specific files
%find_lang --with-man --all-name %name

%files -f %name.lang
%doc %_docdir/%name-%version
%_bindir/*
%_datadir/%name/
%_infodir/*
%_man1dir/*
%_man5dir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_desktopdir/*
%config(noreplace) %_sysconfdir/nanorc

%changelog
* Sun Oct 09 2016 Artem Zolochevskiy <azol@altlinux.ru> 2.7.0-alt1
- New upstream release.
- Removed third-party syntax highlighting (xorg).
- Minimalistic system-wide settings: include color syntaxes only

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1.qa1.1
- NMU: added BR: texinfo

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.2.4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat May 08 2010 Artem Zolochevskiy <azol@altlinux.ru> 2.2.4-alt1
- update to 2.2.4
- don't package COPYING and ChangLog files (according to Docs Policy)

* Wed Feb 24 2010 Artem Zolochevskiy <azol@altlinux.ru> 2.2.3-alt1
- update to 2.2.3

* Mon Jan 18 2010 Artem Zolochevskiy <azol@altlinux.ru> 2.2.2-alt1
- update to 2.2.2
- remove erroneous 'set suspendenable' from nanorc

* Mon Dec 28 2009 Artem Zolochevskiy <azol@altlinux.ru> 2.2.1-alt1
- update to 2.2.1
- spec changes:
  + disable --no-print-directory and --silent make options
  + disable _unpackaged_files_terminate_build
  + use makeinstall_std macro
  + use desktop-file-install to install desktop file

* Sun Jun 14 2009 Artem Zolochevskiy <azol@altlinux.ru> 2.0.9-alt3
- Removed obsolete %%install_info/%%uninstall_info calls

* Wed Nov 19 2008 Artem Zolochevskiy <azol@altlinux.ru> 2.0.9-alt2
- fixed previous changelog entry

* Mon Nov 17 2008 Artem Zolochevskiy <azol@altlinux.ru> 2.0.9-alt1
- Updated to version 2.0.9
- Removed obsolete %%update_menus/%%clean_menus calls

* Fri Aug 29 2008 Artem Zolochevskiy <azol@altlinux.ru> 2.0.8-alt1
- Updated to version 2.0.8

* Sun Dec 23 2007 Artem Zolochevskiy <azol@altlinux.ru> 2.0.7-alt1
- Updated to version 2.0.7
  + nano is now licensed under GNU GPL v3 or later
  + documentation is now dual-licensed:
    GNU GPL v3 or later and the GNU FDL v1.2 or later

* Tue Oct 16 2007 Artem Zolochevskiy <azol@altlinux.ru> 2.0.6-alt3
- added missed Requires(post/preun):
  + install_info and uninstall_info (#13135)

* Mon Oct 01 2007 Artem Zolochevskiy <azol@altlinux.ru> 2.0.6-alt2
- switched to freedesktop menu:
  + replaced Debian menufile with Freedesktop one
- added 16x16, 32x32 and 48x48 icons to comply with
  ALTLinux IconPaths policy
- some spec improvements:
  + used %%url in Source tag
  + used macro from rpm-build-licenses for License tag

* Sat Apr 28 2007 Artem Zolochevskiy <azol@altlinux.ru> 2.0.6-alt1
- Updated to version 2.0.6

* Mon Apr 23 2007 Artem Zolochevskiy <azol@altlinux.ru> 2.0.5-alt1
- Updated to version 2.0.5

* Fri Apr 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 2.0.4-alt1
- Updated to version 2.0.4

* Wed Feb 07 2007 Artem Zolochevskiy <azol@altlinux.ru> 2.0.3-alt1
- Updated to version 2.0.3

* Mon Dec 25 2006 Artem Zolochevskiy <azol@altlinux.ru> 2.0.2-alt1
- Updated to version 2.0.2
- Changed summary and description
- Added COPYING as symlink
- Added ABOUT-NLS, NEWS to package
- Compressed ChangeLog

* Mon Nov 20 2006 Slava Semushin <php-coder@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Fri Nov 17 2006 Slava Semushin <php-coder@altlinux.ru> 2.0.0-alt2
- Added some changes from azol@:
  + enable smarthome in configuration file
  + enable syntax highlighting for POV-Ray
  + remove inutile spaces in configuration file
  + change section in menu file to "Applications/Editors"

* Sun Nov 12 2006 Slava Semushin <php-coder@altlinux.ru> 2.0.0-alt1
- Added global configuration file, which turns on
  (joint work with azol@):
  + autoindent (use auto-indentation)
  + const (constantly display the cursor position in the statusbar)
  + historylog (enable ~/.nano_history for saving and reading
    search/replace strings)
  + morespace (do not displaying empty line after titlebar)
  + mouse (enable mouse support)
  + nonewlines (don't add newlines to the ends of files)
  + nowrap (don't add newlines to the ends of files)
  + smooth (use smooth scrolling)
  + suspend (allow nano to be suspended)
  + enable syntax highlighting for nanorc, C/C++, HTML, TeX, quoted
    emails, patches, man pages, groff, Perl, Python, Ruby, Java,
    Assembler, Bash
- Added syntax highlighting (and enable by default) for PHP, XML, CSS
  and xorg.conf file (picked up from http://gentoo-wiki.com site)
- Added icon from Debian (idea from azol@)
- Change url in Source tag to official site

* Wed Nov 08 2006 Slava Semushin <php-coder@altlinux.ru> 2.0.0-alt0
- Updated to version 2.0.0 (#10246)
- Changed Packager to Artem Zolochevskiy aka azol@
- Added AUTHORS, BUGS, ChangeLog, README, THANKS, TODO, UPGRADE,
  faq.html and nanorc.sample to package
- Updated BuildRequires (build with libncursesw)
- Added full url to Source tag
- Added menu file
- Formatted %%description
- Spec cleanup
- Running make with --no-print-directory and --silent options
- Use %%find_lang for finding nanorc manual pages
- Using %%{un,}install_info for registry info pages (thanx to icesik@)
- Enable _unpackaged_files_terminate_build

* Wed Apr 26 2006 Dmitry Marochko <mothlike@altlinux.ru> 1.3.11-alt1
- New version
- Enabled extra functionality

* Sun Mar 19 2006 Dmitry Marochko <mothlike@altlinux.ru> 1.3.10-alt1
- Initial build for Sisyphus
